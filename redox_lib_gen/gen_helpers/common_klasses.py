# -*- coding: utf-8 -*-
from collections import defaultdict
from pathlib import Path
from typing import DefaultDict, Generator, List

from .empty_klass import EMPTY_KLASS_DEF
from .types import ImportMapping, KlassDefinition, TemplateInfo


class CommonKlassKeeper:
    def __init__(self, output_filename: str | Path | None = None):
        self.template_filename = output_filename or "common_types.py"
        self._klass_defs: DefaultDict[str, KlassDefinition] = defaultdict(
            EMPTY_KLASS_DEF
        )
        self._imports = ImportMapping({"pydantic": {"Field"}})
        self._relative_imports = ImportMapping()

    @property
    def template(self):
        # Common classes only have non-event-type models, so remove the import for that
        self._relative_imports["abstract_base"].discard("EventTypeAbstractModel")
        yield TemplateInfo(
            dir_name="",
            file_name=self.template_filename,
            imports=self._imports,
            relative_imports=self._relative_imports,
            klass_definitions=list(self._klass_defs.values()),
            use_simple_types=True,
        )

    def add_klass_defs_to_template(self, klass_defs: List[KlassDefinition]):
        for klass_def in klass_defs:
            if not klass_def.is_event_type:
                self._klass_defs[klass_def.klass_name] |= klass_def

    def store_and_yield_templates(
        self, template_info_generator: Generator[TemplateInfo, None, None]
    ) -> Generator[TemplateInfo, None, None]:

        for template_info in template_info_generator:
            # Store template and imports info in this object
            self.add_klass_defs_to_template(template_info.klass_definitions)
            self._imports += template_info.imports
            self._relative_imports += template_info.relative_imports

            # Let the other iterator work on the template info
            yield template_info
