# -*- coding: utf-8 -*-
from functools import reduce
from itertools import repeat
from json import load
from operator import add
from pathlib import Path
from typing import Generator

from inflection import singularize

from .name_map import NAME_TRANSLATIONS
from .types import (
    KlassDefinition,
    KlassPropertySignatureInfo,
    KlassPropertyType,
    TemplateInfo,
)
from .utils import get_property_type


def parse_and_build_models(spec_dir: Path) -> Generator[TemplateInfo, None, None]:
    """Parse the schemas and produce the corresponding definitions.

    This function is intended to work on a single directory of JSON schemas.

    IMPORTANT: Because this function is a generator, it **will not** ``yield``
    any of the ``TemplateInfo`` objects until you iterate over the object
    returned from initially invoking the function.

    :param spec_dir: A directory in the extracted specification archive. The
        parser expects this dir to only contain JSON files specifying different
        event types. In other words, this function expects to only operate on a
        single directory within the extracted spec archive.
    """

    for spec_file_path in spec_dir.iterdir():
        with open(spec_file_path) as spec_file:
            schema_def = load(spec_file)

        dir_stem = spec_dir.stem  # Remove any parent dirs from the Path obj
        file_stem = spec_file_path.stem  # Remove parents & extension

        try:
            klass_name = NAME_TRANSLATIONS[file_stem]
        except KeyError as err:
            raise ValueError(
                f"Missing class name translation for found spec file: {file_stem}"
            ) from err

        yield create_template_info(
            KlassDefinition(
                parent_klass_name="RedoxAbstractModel",
                klass_name=klass_name,
                schema_def=schema_def,
                is_event_type=True,
            ),
            dir_name=dir_stem,
            file_name=f"{file_stem}.py",
        )


def create_template_info(
    klass_def: KlassDefinition, dir_name: str, file_name: str
) -> TemplateInfo:
    """Collect and return info for the Jinja2 template.

    Recursively iterates through the definitions of the given class and its
    sub-classes, transforming the KlassDefinition objects into a single
    TemplateInfo instance. This function calls itself on any properties with
    a JSON schema type of either "object" or "array". In the case of the
    latter, this function is only concerned with arrays of types other than
    str.

    :param klass_def: The KlassDefinition instance for an object in the JSON
        schema.
    :param dir_name: The string name of the directory where the JSON schema
        file is that's currently being processed. Will also be the directory
        where the generated Python file will go.
    :param file_name: The string of the filename where the template will be
        rendered after this function completes its work.
    :returns: An TemplateInfo instance that has the combined information for
        the provided object type and any contained object types.
    """

    t_info = TemplateInfo(dir_name=dir_name, file_name=file_name)
    t_info.add_import("pydantic", "Field")

    subklasses_to_define = []
    prop_name: str
    prop_info: dict
    for prop_name, prop_info in klass_def.schema_def["properties"].items():
        if prop_info["type"] == "object":
            # These properties need their own class/model
            subklass = KlassDefinition(
                parent_klass_name=klass_def.full_name,
                klass_name=prop_name,
                schema_def=prop_info,
            )
            subklasses_to_define.append(subklass)
            prop_type = f'"{subklass.full_name}"'
            prop_type_class = KlassPropertyType.SCHEMA
            prop_type_simp = f'"{subklass.klass_name}"'
            klass_def.has_forward_refs = True

        elif (
            prop_info["type"] == "array" and prop_info["items"].get("type") == "object"
        ):
            singular_name = singularize(prop_name)

            subklass = KlassDefinition(
                parent_klass_name=klass_def.full_name,
                klass_name=singular_name,
                schema_def=prop_info["items"],
            )
            subklasses_to_define.append(subklass)
            t_info.imports["typing"].add("List")
            prop_type = f'List["{subklass.full_name}"]'
            prop_type_class = KlassPropertyType.COMBINED
            prop_type_simp = f'List["{subklass.klass_name}"]'
            klass_def.has_forward_refs = True

        else:
            prop_type_info = get_property_type(prop_info["type"])
            prop_type = prop_type_info.type
            prop_type_class = prop_type_info.type_class
            prop_type_simp = prop_type_info.type_simplified
            t_info.add_imports(prop_type_info.imports)
            t_info.add_relative_imports(prop_type_info.relative_imports)

        klass_def.properties.append(
            KlassPropertySignatureInfo(
                type=prop_type,
                type_class=prop_type_class,
                type_simplified=prop_type_simp,
                required=prop_name in klass_def.schema_def.get("required", []),
                name=prop_name,
            )
        )
    t_info.add_klass_def(klass_def)

    sub_t_infos = map(
        create_template_info,
        subklasses_to_define,
        repeat(dir_name),
        repeat(file_name),
    )
    return reduce(add, sub_t_infos, t_info)
