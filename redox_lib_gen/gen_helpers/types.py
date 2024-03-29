# -*- coding: utf-8 -*-
from collections import defaultdict
from copy import copy
from dataclasses import dataclass, field
from functools import total_ordering
from itertools import chain
from pathlib import Path
from typing import DefaultDict, Generator, List, Optional, Union

from .constants import GENERIC_DIR_NAME
from .empty_klass import EMPTY_KLASS_DEF, EMPTY_KLASS_PROPERTY
from .sub_types import DeconstructedType, KlassPropertyType


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
            return NotImplemented

        merged = ImportMapping()
        for module, set_of_names_to_import in chain(
            self.items(), (other or {}).items()
        ):
            merged[module].update(set_of_names_to_import)

        return merged

    def __repr__(self):
        return (
            "ImportMapping({"
            f"{', '.join([f'{repr(k)}: {repr(v)}' for k, v in self.items()])}"
            "})"
        )


@dataclass
class PropertyTypeInfo:
    """The information about a property from the schema."""

    _raw_type: DeconstructedType
    _raw_type_simplified: Optional[DeconstructedType] = None
    imports: ImportMapping = field(default_factory=ImportMapping)
    relative_imports: ImportMapping = field(default_factory=ImportMapping)

    @property
    def type(self) -> str:
        return str(self._raw_type)

    @property
    def type_simplified(self) -> str:
        if self._raw_type_simplified is None:
            return self.type
        return str(self._raw_type_simplified)

    @property
    def type_class(self) -> KlassPropertyType:
        return self._raw_type.property_type

    def prefix_schema_types(self, prefix: str):
        self._raw_type.schema_prefix = prefix
        if self._raw_type_simplified is not None:
            self._raw_type_simplified.schema_prefix = prefix

    def __or__(self, other: "PropertyTypeInfo"):
        if None in (self._raw_type_simplified, other._raw_type_simplified):
            simplified = self._raw_type_simplified or other._raw_type_simplified
        else:
            simplified = self._raw_type_simplified | other._raw_type_simplified

        return (
            PropertyTypeInfo(
                _raw_type=self._raw_type | other._raw_type,
                _raw_type_simplified=simplified,
                imports=self.imports + other.imports,
                relative_imports=self.relative_imports + other.imports,
            )
            if isinstance(other, self.__class__)
            else NotImplemented
        )


@dataclass
@total_ordering
class KlassPropertySignatureInfo:
    """The information about a property suitable for rendering the template."""

    type_info: PropertyTypeInfo
    required: bool
    name: str
    appears_in: set  # This is largely for debugging purposes, but it is VERY useful

    @property
    def type(self):
        return self.type_info.type

    @property
    def type_simplified(self):
        return self.type_info.type_simplified

    @property
    def type_class(self):
        return self.type_info.type_class

    def prefix_schema_types(self, prefix: str):
        self.type_info.prefix_schema_types(prefix)

    def __copy__(self):
        """Create a duplicate of the current instance."""
        return KlassPropertySignatureInfo(
            type_info=copy(self.type_info),
            required=self.required,
            name=self.name,
            appears_in=copy(self.appears_in),
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
            return NotImplemented

        if self.name != other.name:
            raise ValueError(
                "Name must be the same to combine KlassPropertySignatureInfo objects: "
                f"{self.name} vs {other.name}"
            )

        return KlassPropertySignatureInfo(
            type_info=self.type_info | other.type_info,
            name=self.name,
            required=self.required and other.required,
            appears_in=self.appears_in.union(other.appears_in),
        )

    def __hash__(self):
        return hash(
            (
                self.name,
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
                self.name == other.name
                and self.type_info == other.type_info
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

        if self.name < other.name:
            return True
        if self.name > other.name:
            return False

        # Only case left is where the names are equal
        if (
            self.type_class.value < other.type_class.value
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

    # dir_name is the string name of the directory where the JSON schema file is that
    # defines this object. Will also be the directory where the generated Python file
    # will go (assuming it's a valid dir name).
    dir_name: str

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
                EMPTY_KLASS_PROPERTY,
                {p.name: p for p in self.properties if p is not EMPTY_KLASS_PROPERTY},
            )
        return self._prop_map

    def prefix_schema_types(self, prefix: str):
        for p in self.properties:
            p.prefix_schema_types(prefix)

    def __copy__(self):
        """Create a duplicate of the current instance."""
        return KlassDefinition(
            klass_name=self.klass_name,
            properties=[copy(p) for p in self.properties],
            has_forward_refs=self.has_forward_refs,
            is_event_type=self.is_event_type,
            dir_name=self.dir_name,
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
            return NotImplemented

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
            dir_name=self.dir_name,
        )

    def __hash__(self):
        return hash((self.full_name, self.is_event_type, set(self.properties)))

    def __eq__(self, other: "KlassDefinition"):
        """Compare the klass with another klass.

        :param other: Another instance of ``KlassDefinition``.
        :returns: ``True`` if ``full_name``, ``is_event_type``, and
            ``properties`` are equal for both objects.
        """
        return (
            (
                self.full_name == other.full_name
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

        if self.full_name < other.full_name:
            return True
        if self.full_name > other.full_name:
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

    file_name: str
    dir_name: str

    # Keeping track of the imports needed for all the classes in a dict of sets allows
    # for super simple deduplication of entries, and using a defaultdict instead of a
    # standard dict eliminates the need to check if we've already collected an import
    # from a particular module already.
    imports: ImportMapping = field(
        default_factory=lambda: ImportMapping({"pydantic": {"Field"}})
    )
    relative_imports: ImportMapping = field(default_factory=ImportMapping)
    klass_definitions: List[KlassDefinition] = field(default_factory=list)
    use_simple_types: bool = False
    jinja_template_file_name: str = "template-resource.jinja2"
    add_event_types_to_init: bool = True

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

    def prefix_schema_types(self, prefix: str):
        for k in self.klass_definitions:
            k.prefix_schema_types(prefix)

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


@dataclass
class GenericsTemplateInfo(TemplateInfo):
    dir_name: str = GENERIC_DIR_NAME
    use_simple_types: bool = True
    jinja_template_file_name: str = "generics.jinja2"
    model_name: str = ""
    add_event_types_to_init: bool = False

    def as_dict(self):
        return {
            **super().as_dict(),
            "model_name": self.model_name,
        }
