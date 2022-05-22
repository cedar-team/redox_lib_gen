# -*- coding: utf-8 -*-
from copy import copy
from dataclasses import dataclass, field
from enum import Enum
from typing import Iterable, List, Set, Union


class KlassPropertyType(Enum):
    """Indication of how complex the property's type is.

    NATIVE properties have types that are built-in to Python/JSON, like
    str/string, bool/boolean, None/null, float/number.

    SCHEMA properties have types that are references to object definitions
    elsewhere in the JSON schema, such as ``Meta``.

    LIST and UNION properties have types that contain other types, including
    other LIST or UNION types as well as NATIVE and SCHEMA types.
    """

    NATIVE = 1  # Native Python types (str, bool, etc)
    LIST = 2
    UNION = 3
    SCHEMA = 4  # Types that refer to classes defined in the schema


@dataclass
class DeconstructedType:
    """The components of a type declaration.

    This dataclass is what makes it possible to combine all kinds of data types
    from the JSON schema into a single, unified type for the common types. The
    ``property_type`` indicates what kind of container this particular instance
    is, and ``types`` is a ``set`` of the components within the container.

    For ``property_type`` values NATIVE and SCHEMA, ``types`` should only have
    a single value (which is why the ``_validate_length()`` method exists). But
    there is still value in this level of granularity (e.g., versus just having
    any containing ``LIST`` or ``UNION`` types include the values directly).
    For example, consider the following:

    >>> tmp_type1 = DeconstructedType(KlassPropertyType.LIST, {"MySchemaType"})

    If ``tmp_type`` were to be converted to a string, the code would be forced
    to assume that ``"MySchemaType"`` refers to a native type (which it clearly
    isn't) which will lead to an incorrect rendering of the type::

    >>> str(tmp_type1)
    "List[MySchemaType]"

    The correct way to do this is instead:

    >>> tmp_type2 = DeconstructedType(
    ...     KlassPropertyType.LIST,
    ...     {DeconstructedType(KlassPropertyType.SCHEMA, {"MySchemaType"})}
    ... )
    >>> str(tmp_type2)
    'List["MySchemaType"]'
    """

    property_type: KlassPropertyType
    types: Set[Union[str, "DeconstructedType"]] = field(default_factory=set)

    def _validate_length(self):
        """Verify that ``NATIVE`` and ``SCHEMA`` types only have one element."""
        if (
            self.property_type in (KlassPropertyType.NATIVE, KlassPropertyType.SCHEMA)
            and len(self.types) != 1
        ):
            raise IndexError(
                f"Unexpected length for property type {self.property_type.name}: "
                f"{len(self.types)} (should be 1)"
            )

    def __str__(self):
        """Properly converts the object to a string.

        The two key features of this method are that it (1) recursively calls
        ``__str__()`` for any embedded ``DeconstructedType`` objects and (2) it
        correctly quotes any ``SCHEMA`` values. The latter is critical for
        handling forward references (references to types that are defined later
        in a Python file), especially for Python 3.6 which doesn't have as
        robust support for type hints and dataclasses.
        """
        self._validate_length()
        if self.property_type is KlassPropertyType.NATIVE:
            return str(list(self.types)[0])

        elif self.property_type is KlassPropertyType.LIST:
            return f"List[{', '.join(_sort_type_names([str(t) for t in self.types]))}]"

        elif self.property_type is KlassPropertyType.UNION:
            return f"Union[{', '.join(_sort_type_names([str(t) for t in self.types]))}]"

        elif self.property_type is KlassPropertyType.SCHEMA:
            return f'"{list(self.types)[0]}"'

        raise ValueError(f"Unexpected property type: {self.property_type}")

    def __copy__(self):
        return DeconstructedType(self.property_type, copy(self.types))

    def __eq__(self, other: "DeconstructedType"):
        """Allows a ``set`` to determine if it's already present (de-dupe)."""
        if other is None:
            return False
        return self.property_type == other.property_type and self.types == other.types

    def __hash__(self):
        """Allows the class to be added to a ``set``."""
        return hash(
            (
                self.property_type,
                tuple(_sort_type_names(self.types)),
            )
        )

    def __or__(self, other: "DeconstructedType") -> "DeconstructedType":
        """Return the union of two ``DeconstructedType`` objects."""
        # The implementation is split among four methods to simplify the logic for
        # performing the union. Methods are written for each possibility for the value
        # of ``self.property_type``, then within each of those methods, all
        # possibilities for ``other.property_type`` are considered.

        if other is None:
            return copy(self)
        elif not isinstance(other, self.__class__):
            return NotImplemented

        # Cases where self is a native type
        if self.property_type is KlassPropertyType.NATIVE:
            return self.__or_native(other)

        # Cases where self is a List
        elif self.property_type is KlassPropertyType.LIST:
            return self.__or_list(other)

        # Cases where self is a Union
        elif self.property_type is KlassPropertyType.UNION:
            return self.__or_union(other)

        elif self.property_type is KlassPropertyType.SCHEMA:
            return self.__or_schema(other)

        return NotImplemented

    def __or_native(self, other: "DeconstructedType") -> "DeconstructedType":
        if other.property_type is KlassPropertyType.NATIVE:
            if self.types == other.types:
                # The types are the same native type
                return copy(self)
            else:
                # Union[type1, type2]
                return DeconstructedType(
                    KlassPropertyType.UNION, self.types | other.types
                )

        elif other.property_type is KlassPropertyType.LIST:
            if self.types.issubset(other.types):
                # self is already in the other's List of types
                return copy(other)
            else:
                # Union[type1, List[...]]
                return DeconstructedType(KlassPropertyType.UNION, self.types | {other})

        elif other.property_type is KlassPropertyType.UNION:
            # Just try to add self (which is already a native type) to the set of types
            # already in other's types.
            return DeconstructedType(KlassPropertyType.UNION, {self} | other.types)

        elif other.property_type is KlassPropertyType.SCHEMA:
            # Union[type1, SchemaType2]
            return DeconstructedType(KlassPropertyType.UNION, {self} | {other})

    def __or_list(self, other: "DeconstructedType") -> "DeconstructedType":
        if other.property_type is KlassPropertyType.NATIVE:
            # This is an operation defined earlier, just reversed. Reuse it.
            return other | self

        elif other.property_type is KlassPropertyType.LIST:
            if self.types == other.types:
                # The types are the same
                return copy(self)
            else:
                # Union[List1, List2]
                return DeconstructedType(KlassPropertyType.UNION, {self, other})

        elif other.property_type is KlassPropertyType.UNION:
            if self in other.types:
                # self is already one of the types in the Union
                return copy(other)
            else:
                # Union[..., type1]
                return DeconstructedType(KlassPropertyType.UNION, other.types | {self})

        elif other.property_type is KlassPropertyType.SCHEMA:
            # Union[List1, SchemaType2]
            return DeconstructedType(KlassPropertyType.UNION, {self, other})

    def __or_union(self, other: "DeconstructedType") -> "DeconstructedType":
        if other.property_type in (
            KlassPropertyType.NATIVE,
            KlassPropertyType.LIST,
        ):
            # This is an operation defined earlier, just reversed. Reuse it.
            return other | self

        elif other.property_type is KlassPropertyType.UNION:
            # Merging the Unions
            return DeconstructedType(KlassPropertyType.UNION, self.types | other.types)

        elif other.property_type is KlassPropertyType.SCHEMA:
            # Union[..., SchemaType2]
            return DeconstructedType(KlassPropertyType.UNION, self.types | {other})

    def __or_schema(self, other: "DeconstructedType") -> "DeconstructedType":
        if other.property_type in (
            KlassPropertyType.NATIVE,
            KlassPropertyType.LIST,
            KlassPropertyType.UNION,
        ):
            # This is an operation defined earlier, just reversed. Reuse it.
            return other | self

        elif other.property_type is KlassPropertyType.SCHEMA:
            if self.types.issubset(other.types):
                # self is already in the other's List of types
                return copy(other)
            else:
                # Union[SchemaType1, SchemaType2]
                return DeconstructedType(KlassPropertyType.UNION, {self, other})


def _sort_type_names(types: Iterable[str]) -> List[str]:
    """Sort type names, but put None at the end."""
    if isinstance(types, str):
        raise TypeError
    if "None" not in types:
        return sorted(types)
    types = list(types)
    types.remove("None")
    return sorted(types) + ["None"]
