# -*- coding: utf-8 -*-
from collections import defaultdict
from copy import copy
from dataclasses import dataclass, field
from enum import Enum
from functools import total_ordering
from itertools import chain
from pathlib import Path
from typing import DefaultDict, Generator, List, Optional, Union

from .empty_klass import EMPTY_KLASS_DEF, EMPTY_KLASS_PROPERTY


class DirOrFileMismatchError(Exception):
    """
    Raised when two TemplateInfo classes have different values for dir_name and
    file_name but should have the same values.
    """


class ImportMapping(defaultdict):
    """Stores imports needed for a single Jinja2 template rendering.

    This is a subclass of ``defaultdict``. The keys of this mapping are the
    module portion of an import statement. The value for a particular key will
    be a ``set()`` with the names to be imported. For example, to include the
    names ``path`` and ``getcwd`` from the ``os`` module, you could do the
    following:

    >>> imports = ImportMapping()
    >>> imports['os'] = {'path', 'getcwd'}

    When this is rendered by the Jinja2 template, it will appear like this:

    >>> from os import getcwd, path

    To import a name without a module (e.g., ``import os``), add it to the
    empty string module, like this:

    >>> imports[''].add('os')

    The ``__add__`` operator makes it easy to combine two instances of this
    class in a way that automatically de-duplicates all imports. For example:

    >>> imports1 = ImportMapping({'os': {'path', 'getcwd'}})
    >>> imports2 = ImportMapping({'os': {'getcwd', 'setuid'}})
    >>> {'os': {'getcwd', 'setuid', 'path'}} == imports1 + imports2  # True
    """

    def __init__(self, *args, **kwargs):
        if "default_factory" in kwargs:
            kwargs.pop("default_factory")
        super().__init__(set, *args, **kwargs)

    def __add__(self, other: "ImportMapping") -> "ImportMapping":
        """Return the union of two or more import sets.

        Does NOT modify the import sets given as parameters.
        """
        if not isinstance(other, self.__class__):
            raise TypeError(f"Cannot merge imports from type {type(other)}")

        merged = ImportMapping()
        for module, set_of_names_to_import in chain(
            self.items(), (other or {}).items()
        ):
            merged[module].update(set_of_names_to_import)

        return merged


class KlassPropertyType(Enum):
    """Indication of how complex the property's type is.

    NATIVE properties have types that are built-in to Python/JSON, like
    str/string, bool/boolean, None/null, float/number.

    COMBINED properties have types where one or more NATIVE types are valid,
    like ``Union[str, None]`` or ``List[str]``.

    SCHEMA properties have types that are references to object definitions
    elsewhere in the JSON schema, such as ``Meta``.

    This enum is ordered from simplest to most complex, which means if you want
    to know if one value is more complex than another, you can do the
    following:

    >>> first = KlassPropertyType.COMBINED
    >>> second = KlassPropertyType.SCHEMA
    >>> first > second  # Is first more complex than second? Returns False
    """

    NATIVE = 1  # Native Python types (str, bool, etc)
    COMBINED = 2  # Types with List or Union
    SCHEMA = 3  # Types that refer to classes defined in the schema


@dataclass
class PropertyTypeInfo:
    """The information about a property from the schema."""

    type: str
    type_class: KlassPropertyType
    type_simplified: str
    imports: ImportMapping
    relative_imports: ImportMapping


@dataclass
@total_ordering
class KlassPropertySignatureInfo:
    """The information about a property suitable for rendering the template."""

    type: str
    type_class: KlassPropertyType
    type_simplified: str
    required: bool
    name: str

    def __copy__(self):
        """Create a duplicate of the current instance."""
        return KlassPropertySignatureInfo(
            type=self.type
            if self.type_class.value < KlassPropertyType.SCHEMA.value
            else self.name,
            type_class=self.type_class,
            type_simplified=self.type_simplified,
            required=self.required,
            name=self.name,
        )

    def __or__(self, other: "KlassPropertySignatureInfo"):
        """Return an instance that combines two properties.

        For the two properties to successfully combine, they must have the same
        ``name`` value. Also, a property of type ``SCHEMA`` cannot be combined
        with any other property type.

        During the combination, if one property is required and the other is
        not, the resulting property will NOT be required.

        Finally, if one ``KlassDefinition`` includes a property and the other
        does not, the result will be a copy of the property from the first
        ``KlassDefinition``.
        """
        if other is EMPTY_KLASS_PROPERTY:
            new_prop = copy(self)
            # If the field wasn't present in `other` it can't be required
            new_prop.required = False
            return new_prop

        elif not isinstance(other, self.__class__):
            raise TypeError(
                f"Cannot combine KlassPropertySignatureInfo with {type(other)} object"
            )

        if self.name != other.name:
            raise ValueError(
                "Name must be the same to combine KlassPropertySignatureInfo objects: "
                f"{self.name} vs {other.name}"
            )

        if self.type_class is not other.type_class and KlassPropertyType.SCHEMA in {
            self.type_class,
            other.type_class,
        }:
            raise ValueError(
                "Cannot combine a SCHEMA type property with a non-SCHEMA type "
                "property"
            )

        # If there's a difference in the type class value, upgrade to the more complex
        if self.type_class.value >= other.type_class.value:
            new_type = self.type
            new_type_class = self.type_class
            new_type_simplified = self.type_simplified
        else:
            new_type = other.type
            new_type_class = other.type_class
            new_type_simplified = other.type_simplified

        return KlassPropertySignatureInfo(
            type=new_type,
            type_class=new_type_class,
            type_simplified=new_type_simplified,
            name=self.name,
            required=self.required and other.required,
        )

    def __hash__(self):
        return hash(
            (
                self.name.lower(),
                self.type,
                self.type_class,
                self.type_simplified,
                self.required,
            )
        )

    def __eq__(self, other: "KlassPropertySignatureInfo"):
        """Compare the property with another.

        :param other: Another instance of ``KlassPropertySignatureInfo``.
        :returns: ``True`` if ``name``, ``type``, ``type_class``,
            ``type_simplified``, and ``required`` are all the same for both
            objects.
        """
        return (
            (
                self.name.lower() == other.name.lower()
                and self.type == other.type
                and self.type_class is other.type_class
                and self.type_simplified == other.type_simplified
                and self.required == other.required
            )
            if isinstance(other, self.__class__)
            else NotImplemented
        )

    def __lt__(self, other: "KlassPropertySignatureInfo"):
        """Compare the property with another.

        :param other: Another instance of ``KlassPropertySignatureInfo``.
        :returns: ``True`` if ``name``, ``type_class``, ``type``, or
            ``type_simplified`` are less than the other (checked in that
            order). The values for ``required`` are also compared, with
            ``False`` being less than ``True``. Returns ``False`` if all these
            checks fail.
        """
        if not isinstance(other, self.__class__):
            return NotImplemented

        if self.name.lower() < other.name.lower():
            return True
        if self.name.lower() > other.name.lower():
            return False

        # Only case left is where the names are equal
        if (
            self.type_class < other.type_class
            or self.type < other.type
            or self.type_simplified < other.type_simplified
            or int(self.required) < int(other.required)
        ):
            return True
        return False


@dataclass
@total_ordering
class KlassDefinition:
    """The information about a class suitable for rendering the template."""

    klass_name: str
    parent_klass_name: str = ""
    schema_def: Optional[dict] = None
    properties: List[KlassPropertySignatureInfo] = field(default_factory=list)
    has_forward_refs: bool = False  # Is True if any properties are of type SCHEMA
    is_event_type: bool = False
    _prop_map: DefaultDict[
        str, Union[KlassPropertySignatureInfo, EMPTY_KLASS_PROPERTY]
    ] = None

    @property
    def full_name(self):
        """Combination of the class's parent name and this class's name."""
        if self.parent_klass_name == "RedoxAbstractModel":
            return self.klass_name
        return f"{self.parent_klass_name}{self.klass_name}"

    @property
    def prop_map(self):
        """Map of property names to property objects."""
        if self._prop_map is None:
            self._prop_map = defaultdict(
                EMPTY_KLASS_PROPERTY, {p.name: p for p in self.properties}
            )
        return self._prop_map

    def __copy__(self):
        """Create a duplicate of the current instance."""
        return KlassDefinition(
            klass_name=self.klass_name,
            properties=[copy(p) for p in self.properties],
            has_forward_refs=self.has_forward_refs,
            is_event_type=self.is_event_type,
        )

    def __or__(self, other: "KlassDefinition"):
        """Return the combination of two ``KlassDefinition`` objects.

        For the two klasses to successfully combine, they must have the same
        ``klass_name`` value. The returned instance will have a set of
        properties that is the combination of the properties from both
        instances using the logical or operator (``__or__`` method).

        The essence of a KlassDefinition does not depend on the parent class
        name or the schema def, so those are not included in the combined
        object that is returned.
        """
        if other is EMPTY_KLASS_DEF:
            return copy(self)
        elif not isinstance(other, self.__class__):
            raise TypeError(f"Cannot combine KlassDefinition with {type(other)} object")

        if self.klass_name != other.klass_name:
            raise ValueError(
                "KlassDefinition objects' klass_name must match to combine them"
            )

        combined_properties = {
            k: self.prop_map[k] | other.prop_map[k]
            for k in chain(self.prop_map.keys(), other.prop_map.keys())
        }

        return KlassDefinition(
            klass_name=self.klass_name,
            properties=list(combined_properties.values()),
            has_forward_refs=self.has_forward_refs or other.has_forward_refs,
            is_event_type=self.is_event_type or other.is_event_type,
        )

    def __hash__(self):
        return hash((self.full_name.lower(), self.is_event_type, set(self.properties)))

    def __eq__(self, other: "KlassDefinition"):
        """Compare the klass with another klass.

        :param other: Another instance of ``KlassDefinition``.
        :returns: ``True`` if ``full_name``, ``is_event_type``, and
            ``properties`` are equal for both objects.
        """
        return (
            (
                self.full_name.lower() == other.full_name.lower()
                and self.is_event_type == self.is_event_type
                and set(self.properties) == set(other.properties)
            )
            if isinstance(other, self.__class__)
            else NotImplemented
        )

    def __lt__(self, other: "KlassDefinition"):
        """Compare the klass with another klass.

        :param other: Another instance of ``KlassDefinition``.
        :returns: ``True`` if ``full_name`` is less than the other. Otherwise,
            a series of other checks are performed. The values for
            ``is_event_type`` are compared, with ``False`` being less than
            ``True``. Then the properties are compared by first being converted
            to ``set`` objects. If the first object has a set of properties
            that is a proper subset of the properties in ``other``, returns
            ``True``. Finally, if the set difference of the first's properties
            minus the other's is smaller than the other's minus the first's
            properties, will return ``True``. Returns ``False`` if all these
            checks fail.
        """
        if not isinstance(other, self.__class__):
            return NotImplemented

        if self.full_name.lower() < other.full_name.lower():
            return True
        if self.full_name.lower() > other.full_name.lower():
            return False

        # Only case left is where the names are equal
        self_props_set = set(self.properties)
        other_props_set = set(other.properties)
        if (
            int(self.is_event_type) < int(other.is_event_type)
            or self_props_set < other_props_set  # Is it a proper subset
            or (
                len(self_props_set - other_props_set)
                < len(other_props_set - self_props_set)
            )
        ):
            return True
        return False


@dataclass
class TemplateInfo:
    """Stores all info needed for populating the Jinja2 template."""

    dir_name: str
    file_name: str

    # Keeping track of the imports needed for all the classes in a dict of sets allows
    # for super simple deduplication of entries, and using a defaultdict instead of a
    # standard dict eliminates the need to check if we've already collected an import
    # from a particular module already.
    imports: ImportMapping = field(default_factory=ImportMapping)
    relative_imports: ImportMapping = field(default_factory=ImportMapping)
    klass_definitions: List[KlassDefinition] = field(default_factory=list)
    use_simple_types: bool = False

    @property
    def forward_refs(self):
        # TODO: Capturing the forward refs isn't necessary for Python 3.7+. See
        #  https://pydantic-docs.helpmanual.io/usage/postponed_annotations/
        #  for more info.
        for klass in self.klass_definitions:
            if klass.has_forward_refs:
                yield klass.full_name

    @property
    def dir_distance_from_abstract(self):
        """Return number of directories up the abstract model is.

        E.g., if the abstract model definition is in the same directory as the
        destination of this template, this property will be zero.
        """
        return len(Path(self.dir_name).parts)

    @property
    def event_type_classes(self) -> Generator[KlassDefinition, None, None]:
        for k in self.klass_definitions:
            if k.is_event_type:
                yield k

    def add_klass_def(self, klass_definition: KlassDefinition):
        if klass_definition.is_event_type:
            self.add_relative_import("abstract_base", "EventTypeAbstractModel")
        else:
            self.add_relative_import("abstract_base", "RedoxAbstractModel")
        self.klass_definitions.append(klass_definition)

    def as_dict(self):
        """Return a dict with the values the Jinja2 template needs.

        This is *NOT* a replacement for ``dataclasses.asdict()`` since the two
        *DO NOT* have the same output.
        """
        return dict(
            imports=self.imports,
            relative_imports=self.relative_imports,
            klass_definitions=self.klass_definitions,
            forward_refs=self.forward_refs,
            dir_dist_from_abstract=self.dir_distance_from_abstract,
            use_simple_types=self.use_simple_types,
        )

    def __add__(self, other: "TemplateInfo") -> "TemplateInfo":
        """Combine the values of two TemplateInfo classes.

        :returns: A *new* instance and leaves this instance (self) and the other
            instance unchanged.
        :raises DirOrFileMismatchError: If the two instances aren't intended
            for the same destination file.
        """
        if self.dir_name != other.dir_name:
            raise DirOrFileMismatchError(
                "TemplateInfo instances can only be combined if they have the same "
                f"dir_name. Got {self.dir_name} vs {other.dir_name}. "
            )
        if self.file_name != other.file_name:
            raise DirOrFileMismatchError(
                "TemplateInfo instances can only be combined if they have the same "
                f"file_name. Got {self.file_name} vs {other.file_name}."
            )

        return TemplateInfo(
            dir_name=self.dir_name,
            file_name=self.file_name,
            imports=self.imports + other.imports,
            relative_imports=self.relative_imports + other.relative_imports,
            klass_definitions=self.klass_definitions + other.klass_definitions,
        )

    def add_imports(self, more_imports: ImportMapping):
        """Merge an import mapping into this instance's import set."""
        self.imports += more_imports

    def add_relative_imports(self, more_imports: ImportMapping):
        """Merge an import mapping into this instance's relative import set."""
        self.relative_imports += more_imports

    def add_import(self, *import_names: str):
        """Include the given import names to the set of stored imports.

        Can be called in one of three ways:

        1. For direct imports, just include the module's name. For example, to
           import the ``json`` module, call ``add_import`` like this:
           ``add_import("json")``
           which will result in the following import when given to the Jinja
           template:
           ``import json``
        2. Specify the module path as separated strings. A call like this:
           ``add_import("os", "path", "join")``
           will result in the following:
           ``from os.path import join``
        3. Give the module path as a single string, like this:
           ``add_import("os.path", "join")``
           which will result in the following:
           ``from os.path import join``
        """
        if len(import_names) == 1:
            self.imports[""].add(import_names[0])
        else:
            module = ".".join(import_names[:-1])
            self.imports[module].add(import_names[-1])

    def add_relative_import(self, *import_names: str):
        """Include the given import names to the set of stored relative imports.

        Can be called in one of three ways:

        1. For direct imports, just include the module's name. For example, to
           import the ``json`` module, call ``add_relative_import`` like this:
           ``add_relative_import("json")``
           which will result in the following import when given to the Jinja
           template:
           ``import json``
        2. Specify the module path as separated strings. A call like this:
           ``add_relative_import("os", "path", "join")``
           will result in the following:
           ``from os.path import join``
        3. Give the module path as a single string, like this:
           ``add_relative_import("os.path", "join")``
           which will result in the following:
           ``from os.path import join``
        """
        if len(import_names) == 1:
            self.relative_imports[""].add(import_names[0])
        else:
            module = ".".join(import_names[:-1])
            self.relative_imports[module].add(import_names[-1])
