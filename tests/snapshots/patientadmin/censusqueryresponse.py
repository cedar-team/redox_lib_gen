# -*- coding: utf-8 -*-
# ----  AUTO-GENERATED BY redox_lib_gen. DO NOT MODIFY MANUALLY!!  ---- #

from typing import List, Union

from pydantic import Field

from ..abstract_base import EventTypeAbstractModel, RedoxAbstractModel
from ..field_types import Number


class CensusQueryResponse(EventTypeAbstractModel):

    Meta: "CensusQueryResponseMeta" = Field(...)
    Patients: List["CensusQueryResponsePatient"] = Field(None)


class CensusQueryResponseMeta(RedoxAbstractModel):

    DataModel: str = Field(...)
    Destinations: List["CensusQueryResponseMetaDestination"] = Field(None)
    EventDateTime: Union[str, None] = Field(None)
    EventType: str = Field(...)
    FacilityCode: Union[str, None] = Field(None)
    Logs: List["CensusQueryResponseMetaLog"] = Field(None)
    Message: "CensusQueryResponseMetaMessage" = Field(None)
    Source: "CensusQueryResponseMetaSource" = Field(None)
    Test: Union[bool, None] = Field(None)
    Transmission: "CensusQueryResponseMetaTransmission" = Field(None)


class CensusQueryResponseMetaDestination(RedoxAbstractModel):

    ID: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)


class CensusQueryResponseMetaLog(RedoxAbstractModel):

    AttemptID: Union[str, None] = Field(None)
    ID: Union[str, None] = Field(None)


class CensusQueryResponseMetaMessage(RedoxAbstractModel):

    ID: Union[Number, None] = Field(None)


class CensusQueryResponseMetaSource(RedoxAbstractModel):

    ID: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)


class CensusQueryResponseMetaTransmission(RedoxAbstractModel):

    ID: Union[Number, None] = Field(None)


class CensusQueryResponsePatient(RedoxAbstractModel):

    Demographics: "CensusQueryResponsePatientDemographics" = Field(None)
    Identifiers: List["CensusQueryResponsePatientIdentifier"] = Field(None)
    Visits: List["CensusQueryResponsePatientVisit"] = Field(None)


class CensusQueryResponsePatientDemographics(RedoxAbstractModel):

    Address: "CensusQueryResponsePatientDemographicsAddress" = Field(None)
    Citizenship: List[str] = Field(None)
    DOB: Union[str, None] = Field(None)
    DeathDateTime: Union[str, None] = Field(None)
    EmailAddresses: List[str] = Field(None)
    FirstName: Union[str, None] = Field(None)
    IsDeceased: Union[bool, None] = Field(None)
    IsHispanic: Union[bool, None] = Field(None)
    Language: Union[str, None] = Field(None)
    LastName: Union[str, None] = Field(None)
    MaritalStatus: Union[str, None] = Field(None)
    MiddleName: Union[str, None] = Field(None)
    PhoneNumber: "CensusQueryResponsePatientDemographicsPhoneNumber" = Field(None)
    Race: Union[str, None] = Field(None)
    Religion: Union[str, None] = Field(None)
    SSN: Union[str, None] = Field(None)
    Sex: Union[str, None] = Field(None)


class CensusQueryResponsePatientDemographicsAddress(RedoxAbstractModel):

    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class CensusQueryResponsePatientDemographicsPhoneNumber(RedoxAbstractModel):

    Home: Union[str, None] = Field(None)
    Mobile: Union[str, None] = Field(None)
    Office: Union[str, None] = Field(None)


class CensusQueryResponsePatientIdentifier(RedoxAbstractModel):

    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)


class CensusQueryResponsePatientVisit(RedoxAbstractModel):

    Location: "CensusQueryResponsePatientVisitLocation" = Field(None)
    PatientClass: Union[str, None] = Field(None)
    VisitDateTime: Union[str, None] = Field(None)
    VisitNumber: Union[str, None] = Field(None)


class CensusQueryResponsePatientVisitLocation(RedoxAbstractModel):

    Bed: Union[str, None] = Field(None)
    Department: Union[str, None] = Field(None)
    Facility: Union[str, None] = Field(None)
    Room: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


CensusQueryResponse.update_forward_refs()
CensusQueryResponseMeta.update_forward_refs()
CensusQueryResponsePatient.update_forward_refs()
CensusQueryResponsePatientDemographics.update_forward_refs()
CensusQueryResponsePatientVisit.update_forward_refs()
