# -*- coding: utf-8 -*-
from functools import reduce
from operator import add
from pathlib import Path
from subprocess import run
from typing import Collection, List, Optional

from .sub_types import DeconstructedType, KlassPropertyType
from .types import ImportMapping, KlassDefinition, PropertyTypeInfo

NATIVE = KlassPropertyType.NATIVE
LIST = KlassPropertyType.LIST
UNION = KlassPropertyType.UNION
SCHEMA = KlassPropertyType.SCHEMA


def rmrf(
    dir_path: Path,
    exclude: Optional[Collection[Path]] = None,
    exclude_relative_to: Optional[Path] = None,
):
    """Rim raff that riffraff!"""
    if not dir_path.exists():
        return

    # Capture dir sent to the first call
    if exclude_relative_to is None:
        exclude_relative_to = dir_path

    # Cast exclude list to set of Paths relative to the first dir being removed
    if exclude is None:
        exclude = set()
    elif not isinstance(exclude, (set, list, tuple)):
        raise TypeError(
            f"Exclude param must be a list, tuple, set, or None, not {type(exclude)}"
        )
    else:
        exclude = {exclude_relative_to / d for d in exclude}

    if dir_path in exclude:
        return

    if not dir_path.is_dir():
        return dir_path.unlink()
    for child in dir_path.iterdir():
        rmrf(child, exclude, exclude_relative_to)

    try:
        dir_path.rmdir()
    except OSError:
        # If the exclude-list was non-empty, trying to remove the dir will fail because
        # it isn't empty, which is fine. But if there's nothing in the exclude-list,
        # the exception is legitimate and should be re-raised
        if len(exclude) == 0:
            raise


def get_property_type(
    type_str: str | List[str], klass_def: Optional[KlassDefinition] = None
) -> PropertyTypeInfo:
    """Translate the str of a JSON schema type field to a Python typehint."""

    if isinstance(type_str, list):
        # This is a union of types
        return _get_sub_object_prop_type([get_property_type(p) for p in type_str])

    if type_str == "object":
        return PropertyTypeInfo(
            _raw_type=DeconstructedType(SCHEMA, {klass_def.full_name}),
            _raw_type_simplified=DeconstructedType(SCHEMA, {klass_def.klass_name}),
        )

    elif type_str == "array":
        return _get_array_prop_type(klass_def)

    elif type_str == "number":
        return PropertyTypeInfo(
            _raw_type=DeconstructedType(NATIVE, {"Number"}),
            relative_imports=ImportMapping({"field_types": {"Number"}}),
        )

    type_mapping = {
        "string": "str",
        "boolean": "bool",
        "null": "None",
        "integer": "int",
    }
    try:
        prop_type = type_mapping[type_str]
    except KeyError as err:
        raise ValueError(f"Unknown property type: {type_str}") from err

    return PropertyTypeInfo(_raw_type=DeconstructedType(NATIVE, {prop_type}))


def _get_sub_object_prop_type(type_infos: List[PropertyTypeInfo]) -> PropertyTypeInfo:
    """Get property type infor for each subtype, returned combined."""
    if SCHEMA in (t.type_class for t in type_infos):
        raise ValueError("Unsure how to deal with combining schema types here")

    # Combine all the imports and relative imports
    imports = reduce(
        add, (t.imports for t in type_infos), ImportMapping({"typing": {"Union"}})
    )
    relative_imports = reduce(add, (t.relative_imports for t in type_infos))

    # Create the union of the subtypes
    prop_type = DeconstructedType(UNION, {t.type for t in type_infos})
    prop_type_simplified = DeconstructedType(
        UNION, {t.type_simplified for t in type_infos}
    )
    if len(prop_type_simplified.types) == 0:
        prop_type_simplified = None  # Force simplified type to mirror the regular type

    return PropertyTypeInfo(
        _raw_type=prop_type,
        _raw_type_simplified=prop_type_simplified,
        imports=imports,
        relative_imports=relative_imports,
    )


def _get_array_prop_type(
    klass_def: Optional[KlassDefinition] = None,
) -> PropertyTypeInfo:
    """Get the property type info for an array of types from the klass.

    If the array of types doesn't have any "schema_def" property (and an empty
    array for the "items" property), this has historically indicated an array
    of strings, but the Redox spec isn't explicit on this point, so there's a
    chance this may change in the future.
    """

    schema_def = getattr(klass_def, "schema_def", None)
    if schema_def and schema_def.get("type") == "object":
        return PropertyTypeInfo(
            _raw_type=DeconstructedType(
                LIST, {DeconstructedType(SCHEMA, {klass_def.full_name})}
            ),
            _raw_type_simplified=DeconstructedType(
                LIST, {DeconstructedType(SCHEMA, {klass_def.klass_name})}
            ),
            imports=ImportMapping({"typing": {"List"}}),
        )

    return PropertyTypeInfo(
        _raw_type=DeconstructedType(LIST, {DeconstructedType(NATIVE, {"str"})}),
        imports=ImportMapping({"typing": {"List"}}),
    )


def format_python_files(target_dir: Path):
    """Run black and isort on the target directory."""
    target_dir = target_dir.resolve()
    run(["black", target_dir], check=True)
    run(["isort", target_dir], check=True)
