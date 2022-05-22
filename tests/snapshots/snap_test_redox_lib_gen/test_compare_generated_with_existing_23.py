# -*- coding: utf-8 -*-
# ----  AUTO-GENERATED BY redox_lib_gen. DO NOT MODIFY MANUALLY!!  ---- #

from typing import List, Union

from pydantic import Field

from ..abstract_base import EventTypeAbstractModel, RedoxAbstractModel
from ..field_types import Number


class New(EventTypeAbstractModel):

    Device: "NewDevice" = Field(...)
    Meta: "NewMeta" = Field(...)
    Observations: List["NewObservation"] = Field(...)
    Patient: "NewPatient" = Field(None)
    Visit: "NewVisit" = Field(None)


class NewDevice(RedoxAbstractModel):

    ID: str = Field(...)


class NewMeta(RedoxAbstractModel):

    DataModel: str = Field(...)
    Destinations: List["NewMetaDestination"] = Field(None)
    EventDateTime: Union[str, None] = Field(None)
    EventType: str = Field(...)
    FacilityCode: Union[str, None] = Field(None)
    Logs: List["NewMetaLog"] = Field(None)
    Message: "NewMetaMessage" = Field(None)
    Source: "NewMetaSource" = Field(None)
    Test: Union[bool, None] = Field(None)
    Transmission: "NewMetaTransmission" = Field(None)


class NewMetaDestination(RedoxAbstractModel):

    ID: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)


class NewMetaLog(RedoxAbstractModel):

    AttemptID: Union[str, None] = Field(None)
    ID: Union[str, None] = Field(None)


class NewMetaMessage(RedoxAbstractModel):

    ID: Union[Number, None] = Field(None)


class NewMetaSource(RedoxAbstractModel):

    ID: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)


class NewMetaTransmission(RedoxAbstractModel):

    ID: Union[Number, None] = Field(None)


class NewObservation(RedoxAbstractModel):

    Code: str = Field(...)
    DateTime: str = Field(...)
    Units: Union[str, None] = Field(None)
    Value: str = Field(...)
    ValueType: str = Field(...)


class NewPatient(RedoxAbstractModel):

    Contacts: List["NewPatientContact"] = Field(None)
    Demographics: "NewPatientDemographics" = Field(None)
    Identifiers: List["NewPatientIdentifier"] = Field(None)
    Notes: List[str] = Field(None)


class NewPatientContact(RedoxAbstractModel):

    Address: "NewPatientContactAddress" = Field(None)
    EmailAddresses: List[str] = Field(None)
    FirstName: Union[str, None] = Field(None)
    LastName: Union[str, None] = Field(None)
    MiddleName: Union[str, None] = Field(None)
    PhoneNumber: "NewPatientContactPhoneNumber" = Field(None)
    RelationToPatient: Union[str, None] = Field(None)
    Roles: List[str] = Field(None)


class NewPatientContactAddress(RedoxAbstractModel):

    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class NewPatientContactPhoneNumber(RedoxAbstractModel):

    Home: Union[str, None] = Field(None)
    Mobile: Union[str, None] = Field(None)
    Office: Union[str, None] = Field(None)


class NewPatientDemographics(RedoxAbstractModel):

    Address: "NewPatientDemographicsAddress" = Field(None)
    Citizenship: List[str] = Field(None)
    DeathDateTime: Union[str, None] = Field(None)
    DOB: Union[str, None] = Field(None)
    EmailAddresses: List[str] = Field(None)
    FirstName: Union[str, None] = Field(None)
    IsDeceased: Union[bool, None] = Field(None)
    IsHispanic: Union[bool, None] = Field(None)
    Language: Union[str, None] = Field(None)
    LastName: Union[str, None] = Field(None)
    MaritalStatus: Union[str, None] = Field(None)
    MiddleName: Union[str, None] = Field(None)
    PhoneNumber: "NewPatientDemographicsPhoneNumber" = Field(None)
    Race: Union[str, None] = Field(None)
    Religion: Union[str, None] = Field(None)
    Sex: Union[str, None] = Field(None)
    SSN: Union[str, None] = Field(None)


class NewPatientDemographicsAddress(RedoxAbstractModel):

    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class NewPatientDemographicsPhoneNumber(RedoxAbstractModel):

    Home: Union[str, None] = Field(None)
    Mobile: Union[str, None] = Field(None)
    Office: Union[str, None] = Field(None)


class NewPatientIdentifier(RedoxAbstractModel):

    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)


class NewVisit(RedoxAbstractModel):

    Location: "NewVisitLocation" = Field(None)
    VisitNumber: Union[str, None] = Field(None)


class NewVisitLocation(RedoxAbstractModel):

    Bed: Union[str, None] = Field(None)
    Department: Union[str, None] = Field(None)
    Facility: Union[str, None] = Field(None)
    Room: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


New.update_forward_refs()
NewMeta.update_forward_refs()
NewPatient.update_forward_refs()
NewPatientContact.update_forward_refs()
NewPatientDemographics.update_forward_refs()
NewVisit.update_forward_refs()
