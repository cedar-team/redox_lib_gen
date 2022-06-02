# -*- coding: utf-8 -*-
from dataclasses import dataclass
from json import load
from pathlib import Path
from typing import Iterator, Union

from inflection import singularize

from .constants import NAME_TRANSLATIONS
from .types import (
    ImportMapping,
    KlassDefinition,
    KlassPropertySignatureInfo,
    TemplateInfo,
)
from .utils import get_property_type


def parse_and_build_models(spec_dir: Path) -> Iterator[TemplateInfo]:
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
                dir_name=dir_stem,
            ),
            # This 👇 is how we support the "sign-on" dir
            file_name=f"{file_stem.replace('-', '')}.py",
        )


def create_template_info(klass_def: KlassDefinition, file_name: str) -> TemplateInfo:
    """Collect and return info for the Jinja2 template.

    Recursively iterates through the definitions of the given class and its
    sub-classes, transforming the KlassDefinition objects into a single
    TemplateInfo instance. This function calls itself on any properties with
    a JSON schema type of either "object" or "array". In the case of the
    latter, this function is only concerned with arrays of types other than
    str.

    :param klass_def: The KlassDefinition instance for an object in the JSON
        schema.
    :param file_name: The string of the filename where the template will be
        rendered after this function completes its work.
    :returns: An TemplateInfo instance that has the combined information for
        the provided object type and any contained object types.
    """

    t_info = TemplateInfo(dir_name=klass_def.dir_name, file_name=file_name)

    for subklass_info in _get_subklasses(klass_def.schema_def["properties"], klass_def):
        if subklass_info.subklass is not None:
            t_info += create_template_info(subklass_info.subklass, file_name)

        t_info.add_imports(subklass_info.imports)
        t_info.add_relative_imports(subklass_info.relative_imports)

    t_info.add_klass_def(klass_def)
    return t_info


def _get_subklasses(
    properties: dict, klass_def: KlassDefinition
) -> Iterator[Union["_SubklassInfo", None]]:
    """Generate info on all properties in the parent ``KlassDefinition``.

    :param properties: The value from the parent JSON object's "properties" key.
    :param klass_def: The ``Klass_definition`` instance for the parent object.
    :returns: The iterator for this function yields a ``_SubklassInfo``
        dataclass instance with the subklass's ``KlassDefinition`` instance and
        the regular and relative imports that need to be added to the template.
        If a property from the parent object does not need to have a subklass
        definition, that part of the yielded value will be ``None``.
    """

    prop_name: str
    prop_info: dict
    for prop_name, prop_info in properties.items():

        # Object JSON type - Will need its own KlassDefinition
        if prop_info["type"] == "object":
            subklass = KlassDefinition(
                parent_klass_name=klass_def.full_name,
                klass_name=prop_name,
                schema_def=prop_info,
                dir_name=klass_def.dir_name,
            )
            klass_def.has_forward_refs = True

        # Array JSON type - Its subtypes will need their own KlassDefinition
        elif (
            prop_info["type"] == "array" and prop_info["items"].get("type") == "object"
        ):
            subklass = KlassDefinition(
                parent_klass_name=klass_def.full_name,
                klass_name=singularize(prop_name),
                schema_def=prop_info["items"],
                dir_name=klass_def.dir_name,
            )
            klass_def.has_forward_refs = True

        else:
            subklass = None

        prop_type_info = get_property_type(prop_info["type"], subklass)
        klass_def.properties.append(
            KlassPropertySignatureInfo(
                type_info=prop_type_info,
                required=prop_name in klass_def.schema_def.get("required", []),
                name=prop_name,
                appears_in={f"{klass_def.dir_name}.{klass_def.full_name}"},
            )
        )

        yield _SubklassInfo(
            subklass=subklass,
            imports=prop_type_info.imports,
            relative_imports=prop_type_info.relative_imports,
        )


@dataclass
class _SubklassInfo:
    subklass: KlassDefinition | None
    imports: ImportMapping
    relative_imports: ImportMapping
