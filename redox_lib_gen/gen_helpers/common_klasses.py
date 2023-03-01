# -*- coding: utf-8 -*-
from collections import defaultdict
from copy import copy
from typing import DefaultDict, Dict, Iterator, List

from .constants import GENERIC_DIR_NAME, get_name_trans
from .empty_klass import EMPTY_KLASS_DEF
from .types import GenericsTemplateInfo, ImportMapping, KlassDefinition, TemplateInfo

# Typing helpers
KlassName = str
KlassNameToKlassDef = DefaultDict[KlassName, KlassDefinition]
ModelName = str
ModelNameToTemplate = Dict[ModelName, GenericsTemplateInfo]


class CommonKlassKeeper:
    def __init__(self):
        self.template_filename = "types.py"
        self._klass_defs: KlassNameToKlassDef = defaultdict(EMPTY_KLASS_DEF)
        self._imports = ImportMapping({"pydantic": {"Field"}})
        self._relative_imports = ImportMapping()
        self._generics = _Generics()

    @property
    def template(self):
        # Common classes only have non-event-type models, so remove the import for that
        self._relative_imports["abstract_base"].discard("EventTypeAbstractModel")
        yield TemplateInfo(
            dir_name=GENERIC_DIR_NAME,
            file_name=self.template_filename,
            imports=self._imports,
            relative_imports=self._relative_imports,
            klass_definitions=list(self._klass_defs.values()),
            use_simple_types=True,
        )

    @property
    def templates(self):
        # Generics + common types templates
        yield from self._generics.templates
        yield from self.template

    def add_klass_defs_to_template(self, klass_defs: List[KlassDefinition]):
        for klass_def in klass_defs:
            if not klass_def.is_event_type:
                self._klass_defs[klass_def.klass_name] |= klass_def

    def store_and_yield_templates(
        self, template_info_generator: Iterator[TemplateInfo]
    ) -> Iterator[TemplateInfo]:

        for template_info in template_info_generator:
            # Store template and imports info in this object
            self.add_klass_defs_to_template(template_info.klass_definitions)
            self._imports += template_info.imports
            self._relative_imports += template_info.relative_imports

            # Store template in generics
            self._generics.store(template_info)

            # Let the other iterator work on the template info
            yield template_info


class _Generics:
    def __init__(self):
        self._templates: ModelNameToTemplate = {}

    @property
    def templates(self):
        prefix = "generic"
        for template in self._templates.values():
            template.prefix_schema_types(f"{prefix}.")
            template.add_import(".", f"types as {prefix}")
            template.add_import("pyredox", template.model_name.lower())
            template.add_relative_import("abstract_base", "GenericRedoxAbstractModel")
            yield template

    @property
    def keys(self):
        yield from self._templates.keys()

    def store(self, t_info: TemplateInfo):
        model_name = get_name_trans(t_info.dir_name)
        if model_name not in self._templates:
            self._templates[model_name] = GenericsTemplateInfo(
                file_name=f"{model_name}.py",
                model_name=model_name,
            )

        for klass_def in t_info.klass_definitions:
            if klass_def.is_event_type:
                self._templates[model_name].klass_definitions.append(copy(klass_def))

        self._templates[model_name].add_imports(t_info.imports)
        # Purposefully not adding relative imports since we handle that differently
