# -*- coding: utf-8 -*-
from copy import copy

from redox_parser_gen.gen_helpers.sub_types import DeconstructedType
from redox_parser_gen.gen_helpers.types import (
    ImportMapping,
    KlassDefinition,
    KlassPropertySignatureInfo,
    KlassPropertyType,
    PropertyTypeInfo,
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
        type_info=PropertyTypeInfo(
            _raw_type=DeconstructedType(
                property_type=KlassPropertyType.NATIVE, types={"str"}
            )
        ),
        required=True,
        name="FirstProperty",
        appears_in=set(),
    )
    prop_2 = KlassPropertySignatureInfo(
        type_info=PropertyTypeInfo(
            _raw_type=DeconstructedType(
                KlassPropertyType.UNION,
                {
                    DeconstructedType(KlassPropertyType.NATIVE, {"str"}),
                    DeconstructedType(KlassPropertyType.NATIVE, {"None"}),
                },
            )
        ),
        required=False,
        name="FirstProperty",
        appears_in=set(),
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
        type_info=PropertyTypeInfo(
            _raw_type=DeconstructedType(KlassPropertyType.NATIVE, {"str"})
        ),
        required=True,
        name="FirstProperty",
        appears_in=set(),
    )
    prop_1b = KlassPropertySignatureInfo(
        type_info=PropertyTypeInfo(
            _raw_type=DeconstructedType(
                KlassPropertyType.UNION,
                {
                    DeconstructedType(KlassPropertyType.NATIVE, {"str"}),
                    DeconstructedType(KlassPropertyType.NATIVE, {"None"}),
                },
            )
        ),
        required=False,
        name="FirstProperty",
        appears_in=set(),
    )

    prop_2a = copy(prop_1a)
    prop_2a.name = "SecondProperty"

    prop_2b = copy(prop_2a)
    prop_2b.type_info = PropertyTypeInfo(
        _raw_type=DeconstructedType(
            KlassPropertyType.UNION,
            {
                DeconstructedType(KlassPropertyType.NATIVE, {"str"}),
                DeconstructedType(KlassPropertyType.NATIVE, {"None"}),
            },
        )
    )

    klass_a = KlassDefinition(
        klass_name="Dude",
        properties=[
            prop_1a,
            prop_2a,
        ],
        is_event_type=True,
        dir_name="",
    )

    klass_b = KlassDefinition(
        klass_name="Dude",
        properties=[
            prop_1b,
            prop_2b,
        ],
        is_event_type=True,
        dir_name="",
    )

    ab = klass_a | klass_b
    assert ab == klass_b


def test_deconstructed_merge():
    str1 = DeconstructedType(KlassPropertyType.NATIVE, {"str"})
    bool1 = DeconstructedType(KlassPropertyType.NATIVE, {"bool"})
    list1 = DeconstructedType(KlassPropertyType.LIST, {str1})
    list2 = DeconstructedType(KlassPropertyType.LIST, {bool1})
    blah1 = DeconstructedType(KlassPropertyType.SCHEMA, {"Blah"})
    halb1 = DeconstructedType(KlassPropertyType.SCHEMA, {"Halb"})

    str_bool1 = DeconstructedType(
        KlassPropertyType.UNION,
        {
            DeconstructedType(KlassPropertyType.NATIVE, {"str"}),
            DeconstructedType(KlassPropertyType.NATIVE, {"bool"}),
        },
    )

    str_none1 = DeconstructedType(
        KlassPropertyType.UNION,
        {
            DeconstructedType(KlassPropertyType.NATIVE, {"str"}),
            DeconstructedType(KlassPropertyType.NATIVE, {"None"}),
        },
    )

    #
    # NATIVE
    #

    # Native | Native
    assert str(str1 | str1) == "str"
    assert str(str1 | bool1) == "Union[bool, str]"

    # Native | List
    assert str(str1 | list1) == "Union[List[str], str]"

    # Native | Union
    assert str(str1 | str_none1) == "Union[str, None]"

    # Native | Schema
    assert str(str1 | blah1) == 'Union["Blah", str]'

    #
    # LIST
    #

    # List | Native
    assert str(list1 | str1) == "Union[List[str], str]"

    # List | List
    assert str(list1 | list2) == "Union[List[bool], List[str]]"

    # List | Union
    assert str(list1 | str_none1) == "Union[List[str], str, None]"

    # List | Schema
    assert str(list1 | blah1) == 'Union["Blah", List[str]]'

    #
    # UNION
    #

    # Union | Native
    assert str(str_none1 | str1) == "Union[str, None]"

    # Union | List
    assert str(str_none1 | list1) == "Union[List[str], str, None]"

    # Union | Union
    assert str(str_none1 | str_none1) == "Union[str, None]"
    assert str(str_bool1 | str_none1) == "Union[bool, str, None]"

    # Union | Schema
    assert str(str_bool1 | blah1) == 'Union["Blah", bool, str]'

    #
    # SCHEMA
    #

    # Schema | Native
    assert str(blah1 | str1) == 'Union["Blah", str]'

    # Schema | List
    assert str(blah1 | list1) == 'Union["Blah", List[str]]'

    # Schema | Union
    assert str(blah1 | str_bool1) == 'Union["Blah", bool, str]'

    # Schema | Schema
    assert str(blah1 | blah1) == str(blah1)
    assert str(blah1 | halb1) == 'Union["Blah", "Halb"]'
