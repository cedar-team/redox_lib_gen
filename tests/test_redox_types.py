# -*- coding: utf-8 -*-
from copy import copy

from redox_lib_gen.gen_helpers.types import (
    ImportMapping,
    KlassDefinition,
    KlassPropertySignatureInfo,
    KlassPropertyType,
)


def test_import_mapping_adding():
    # Creating an import mapping is the same whether you pass values to the constructor
    # or do it afterwards.
    imports_a = ImportMapping()
    imports_a[""].add("cool_module")

    imports_b = ImportMapping({"": {"cool_module"}})
    assert imports_a == imports_b
    assert imports_a == (imports_a + imports_b)

    imports_a[""].add("cool_mod2")
    imports_a[""].add("cool_mod2")
    imports_a[""].add("cool_mod2")
    assert len(imports_a[""]) == 2
    assert len(imports_a["nope"]) == 0  # Default value is an empty set


def test_property_merging_sorting():
    # Merging checks
    prop_1 = KlassPropertySignatureInfo(
        type="str",
        type_class=KlassPropertyType.NATIVE,
        type_simplified="str",
        required=True,
        name="FirstProperty",
    )
    prop_2 = KlassPropertySignatureInfo(
        type="Union[str, None]",
        type_class=KlassPropertyType.COMBINED,
        type_simplified="Union[str, None]",
        required=False,
        name="FirstProperty",
    )

    combined = prop_1 | prop_2
    # combined should take the values of prop_2
    assert combined.type == prop_2.type
    assert combined.type_class == prop_2.type_class
    assert combined.type_simplified == prop_2.type_simplified
    assert not combined.required
    assert combined.name == prop_1.name

    # Sorting checks
    prop_a = copy(prop_1)
    prop_a.name = "abracadabra"

    prop_b = copy(prop_1)
    prop_b.name = "baboon"

    prop_c = copy(prop_1)
    prop_c.name = "cowboy"

    mixed_props = [prop_c, prop_a, prop_b]
    sorted_props = sorted(mixed_props)
    assert sorted_props[0] is not prop_1  # Copy isn't the same as original
    assert sorted_props[0] is prop_a
    assert sorted_props[1] is prop_b
    assert sorted_props[2] is prop_c


def test_klass_merge_sorting():
    prop_1a = KlassPropertySignatureInfo(
        type="str",
        type_class=KlassPropertyType.NATIVE,
        type_simplified="str",
        required=True,
        name="FirstProperty",
    )
    prop_1b = KlassPropertySignatureInfo(
        type="Union[str, None]",
        type_class=KlassPropertyType.COMBINED,
        type_simplified="Union[str, None]",
        required=False,
        name="FirstProperty",
    )

    prop_2a = copy(prop_1a)
    prop_2a.name = "SecondProperty"

    prop_2b = copy(prop_2a)
    prop_2b.type = "Union[str, None]"
    prop_2b.type_simplified = "Union[str, None]"
    prop_2b.type_class = KlassPropertyType.COMBINED

    klass_a = KlassDefinition(
        klass_name="Dude",
        properties=[
            prop_1a,
            prop_2a,
        ],
        is_event_type=True,
    )

    klass_b = KlassDefinition(
        klass_name="Dude",
        properties=[
            prop_1b,
            prop_2b,
        ],
        is_event_type=True,
    )

    ab = klass_a | klass_b
    assert ab == klass_b
