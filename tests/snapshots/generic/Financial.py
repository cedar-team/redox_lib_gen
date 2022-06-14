# -*- coding: utf-8 -*-
# ----  AUTO-GENERATED BY redox_lib_gen. DO NOT MODIFY MANUALLY!!  ---- #

from typing import List, Union

from pydantic import Field

from pyredox import financial
from ..abstract_base import GenericRedoxAbstractModel
from . import types as generic


class _Financial(GenericRedoxAbstractModel):
    _redox_module = financial


class AccountUpdate(_Financial):

    Meta: generic.Meta = Field(...)
    Patient: generic.Patient = Field(...)
    Visit: generic.Visit = Field(None)


class Transaction(_Financial):

    Meta: generic.Meta = Field(...)
    Patient: generic.Patient = Field(...)
    Transactions: List[generic.Transaction] = Field(...)
    Visit: generic.Visit = Field(None)
