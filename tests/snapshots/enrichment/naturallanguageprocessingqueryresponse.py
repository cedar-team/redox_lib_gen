# -*- coding: utf-8 -*-
# ----  AUTO-GENERATED BY redox_parser_gen. DO NOT MODIFY MANUALLY!!  ---- #

from typing import List, Union

from pydantic import Field

from ..abstract_base import EventTypeAbstractModel, RedoxAbstractModel
from ..field_types import Number


class NaturalLanguageProcessingQueryResponse(EventTypeAbstractModel):
    Entries: List["NaturalLanguageProcessingQueryResponseEntry"] = Field(...)
    Meta: "NaturalLanguageProcessingQueryResponseMeta" = Field(...)
    Transaction: "NaturalLanguageProcessingQueryResponseTransaction" = Field(...)


class NaturalLanguageProcessingQueryResponseEntry(RedoxAbstractModel):
    Category: "NaturalLanguageProcessingQueryResponseEntryCategory" = Field(...)
    Concept: "NaturalLanguageProcessingQueryResponseEntryConcept" = Field(...)
    Text: "NaturalLanguageProcessingQueryResponseEntryText" = Field(...)


class NaturalLanguageProcessingQueryResponseEntryCategory(RedoxAbstractModel):
    CertaintyScore: Number = Field(...)
    Name: str = Field(...)


class NaturalLanguageProcessingQueryResponseEntryConcept(RedoxAbstractModel):
    CertaintyScore: Number = Field(...)
    Code: Union[str, None] = Field(None)
    Codeset: Union[str, None] = Field(None)
    Description: Union[str, None] = Field(None)


class NaturalLanguageProcessingQueryResponseEntryText(RedoxAbstractModel):
    Contents: str = Field(...)
    Position: "NaturalLanguageProcessingQueryResponseEntryTextPosition" = Field(...)


class NaturalLanguageProcessingQueryResponseEntryTextPosition(RedoxAbstractModel):
    BeginOffset: Number = Field(...)
    EndOffset: Number = Field(...)


class NaturalLanguageProcessingQueryResponseMeta(RedoxAbstractModel):
    DataModel: str = Field(...)
    Destinations: List["NaturalLanguageProcessingQueryResponseMetaDestination"] = Field(
        None
    )
    EventDateTime: Union[str, None] = Field(None)
    EventType: str = Field(...)
    FacilityCode: Union[str, None] = Field(None)
    Logs: List["NaturalLanguageProcessingQueryResponseMetaLog"] = Field(None)
    Message: "NaturalLanguageProcessingQueryResponseMetaMessage" = Field(None)
    Source: "NaturalLanguageProcessingQueryResponseMetaSource" = Field(None)
    Test: Union[bool, None] = Field(None)
    Transmission: "NaturalLanguageProcessingQueryResponseMetaTransmission" = Field(None)


class NaturalLanguageProcessingQueryResponseMetaDestination(RedoxAbstractModel):
    ID: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)


class NaturalLanguageProcessingQueryResponseMetaLog(RedoxAbstractModel):
    AttemptID: Union[str, None] = Field(None)
    ID: Union[str, None] = Field(None)


class NaturalLanguageProcessingQueryResponseMetaMessage(RedoxAbstractModel):
    ID: Union[Number, None] = Field(None)


class NaturalLanguageProcessingQueryResponseMetaSource(RedoxAbstractModel):
    ID: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)


class NaturalLanguageProcessingQueryResponseMetaTransmission(RedoxAbstractModel):
    ID: Union[Number, None] = Field(None)


class NaturalLanguageProcessingQueryResponseTransaction(RedoxAbstractModel):
    ID: str = Field(...)
    Task: "NaturalLanguageProcessingQueryResponseTransactionTask" = Field(...)
    VendorID: str = Field(...)


class NaturalLanguageProcessingQueryResponseTransactionTask(RedoxAbstractModel):
    ID: str = Field(...)
    Message: Union[str, None] = Field(None)
    Status: str = Field(...)


NaturalLanguageProcessingQueryResponse.update_forward_refs()
NaturalLanguageProcessingQueryResponseEntry.update_forward_refs()
NaturalLanguageProcessingQueryResponseEntryText.update_forward_refs()
NaturalLanguageProcessingQueryResponseMeta.update_forward_refs()
NaturalLanguageProcessingQueryResponseTransaction.update_forward_refs()
