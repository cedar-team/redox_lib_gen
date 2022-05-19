# -*- coding: utf-8 -*-
from functools import reduce
from operator import add
from pathlib import Path
from subprocess import run
from typing import Collection, List, Optional, Union

from .types import ImportMapping, KlassPropertyType, PropertyTypeInfo


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
        # If the exclude list was non-empty, trying to remove the dir will fail because
        # it isn't empty, which is fine. But if there's nothing in the exclude list,
        # the exception is legitimate and should be re-raised
        if len(exclude) == 0:
            raise


def get_property_type(type_str: Union[str, List[str]]) -> PropertyTypeInfo:
    """Translate the str of a JSON schema type field to a Python typehint."""

    if isinstance(type_str, list):
        type_infos = [get_property_type(p) for p in type_str]
        type_classes = {t.type_class for t in type_infos}

        if KlassPropertyType.SCHEMA in type_classes:
            raise ValueError("Unsure how to deal with combining schema types here")

        imports = reduce(
            add, [t.imports for t in type_infos], ImportMapping({"typing": {"Union"}})
        )
        relative_imports = reduce(add, [t.relative_imports for t in type_infos])
        prop_type = f"Union[{', '.join(t.type for t in type_infos)}]"
        prop_type_simplified = (
            f"Union[{', '.join(t.type_simplified for t in type_infos)}]"
        )
        return PropertyTypeInfo(
            type=prop_type,
            type_class=KlassPropertyType.COMBINED,
            type_simplified=prop_type_simplified,
            imports=imports,
            relative_imports=relative_imports,
        )

    imports = ImportMapping()
    relative_imports = ImportMapping()

    if type_str == "array":
        # This only accounts for the case where the property has an empty `items`
        # TODO: Verify in the future that it's still okay to assume it will always be a
        #  list of strings.
        imports["typing"].add("List")
        return PropertyTypeInfo(
            type="List[str]",
            type_class=KlassPropertyType.COMBINED,
            type_simplified="List[str]",
            imports=imports,
            relative_imports=relative_imports,
        )
    elif type_str == "number":
        relative_imports["field_types"].add("Number")
        return PropertyTypeInfo(
            type="Number",
            type_class=KlassPropertyType.NATIVE,
            type_simplified="Number",
            imports=imports,
            relative_imports=relative_imports,
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

    return PropertyTypeInfo(
        type=prop_type,
        type_class=KlassPropertyType.NATIVE,
        type_simplified=prop_type,  # Native types are already simplified
        imports=imports,
        relative_imports=relative_imports,
    )


def format_python_files(target_dir: Path):
    """Run black and isort on the target directory."""
    target_dir = target_dir.resolve()
    run(["black", target_dir], check=True)
    run(["isort", target_dir], check=True)
