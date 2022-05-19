# -*- coding: utf-8 -*-
# ----  AUTO-GENERATED BY redox_lib_gen. DO NOT MODIFY MANUALLY!!  ---- #

from typing import List, Union

from pydantic import Field

from ..abstract_base import EventTypeAbstractModel, RedoxAbstractModel
from ..field_types import Number


class AvailableSlots(EventTypeAbstractModel):

    EndDateTime: Union[str, None] = Field(None)
    Meta: "AvailableSlotsMeta" = Field(...)
    Patient: "AvailableSlotsPatient" = Field(None)
    StartDateTime: str = Field(...)
    Visit: "AvailableSlotsVisit" = Field(None)


class AvailableSlotsMeta(RedoxAbstractModel):

    DataModel: str = Field(...)
    Destinations: List["AvailableSlotsMetaDestination"] = Field(None)
    EventDateTime: Union[str, None] = Field(None)
    EventType: str = Field(...)
    FacilityCode: Union[str, None] = Field(None)
    Logs: List["AvailableSlotsMetaLog"] = Field(None)
    Message: "AvailableSlotsMetaMessage" = Field(None)
    Source: "AvailableSlotsMetaSource" = Field(None)
    Test: Union[bool, None] = Field(None)
    Transmission: "AvailableSlotsMetaTransmission" = Field(None)


class AvailableSlotsMetaDestination(RedoxAbstractModel):

    ID: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)


class AvailableSlotsMetaLog(RedoxAbstractModel):

    AttemptID: Union[str, None] = Field(None)
    ID: Union[str, None] = Field(None)


class AvailableSlotsMetaMessage(RedoxAbstractModel):

    ID: Union[Number, None] = Field(None)


class AvailableSlotsMetaSource(RedoxAbstractModel):

    ID: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)


class AvailableSlotsMetaTransmission(RedoxAbstractModel):

    ID: Union[Number, None] = Field(None)


class AvailableSlotsPatient(RedoxAbstractModel):

    Identifiers: List["AvailableSlotsPatientIdentifier"] = Field(None)


class AvailableSlotsPatientIdentifier(RedoxAbstractModel):

    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)


class AvailableSlotsVisit(RedoxAbstractModel):

    AttendingProviders: List["AvailableSlotsVisitAttendingProvider"] = Field(None)
    Locations: List["AvailableSlotsVisitLocation"] = Field(None)
    Reasons: List[str] = Field(None)


class AvailableSlotsVisitAttendingProvider(RedoxAbstractModel):

    Address: "AvailableSlotsVisitAttendingProviderAddress" = Field(None)
    Credentials: List[str] = Field(None)
    EmailAddresses: List[str] = Field(None)
    FirstName: Union[str, None] = Field(None)
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)
    LastName: Union[str, None] = Field(None)
    Location: "AvailableSlotsVisitAttendingProviderLocation" = Field(None)
    PhoneNumber: "AvailableSlotsVisitAttendingProviderPhoneNumber" = Field(None)


class AvailableSlotsVisitAttendingProviderAddress(RedoxAbstractModel):

    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class AvailableSlotsVisitAttendingProviderLocation(RedoxAbstractModel):

    Department: Union[str, None] = Field(None)
    Facility: Union[str, None] = Field(None)
    Room: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


class AvailableSlotsVisitAttendingProviderPhoneNumber(RedoxAbstractModel):

    Office: Union[str, None] = Field(None)


class AvailableSlotsVisitLocation(RedoxAbstractModel):

    Department: Union[str, None] = Field(None)
    Facility: Union[str, None] = Field(None)
    Room: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


AvailableSlots.update_forward_refs()
AvailableSlotsMeta.update_forward_refs()
AvailableSlotsPatient.update_forward_refs()
AvailableSlotsVisit.update_forward_refs()
AvailableSlotsVisitAttendingProvider.update_forward_refs()