# -*- coding: utf-8 -*-
# ----  AUTO-GENERATED BY redox_parser_gen. DO NOT MODIFY MANUALLY!!  ---- #

from typing import List, Union

from pydantic import Field

from ..abstract_base import EventTypeAbstractModel, RedoxAbstractModel


class SignOn(EventTypeAbstractModel):
    EmailAddress: Union[str, None] = Field(None)
    Expiration: str = Field(...)
    FirstName: Union[str, None] = Field(None)
    IssuedAt: str = Field(...)
    LastName: Union[str, None] = Field(None)
    Locale: Union[str, None] = Field(None)
    Meta: "SignOnMeta" = Field(...)
    MiddleName: Union[str, None] = Field(None)
    NPI: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)
    Order: "SignOnOrder" = Field(None)
    Patient: "SignOnPatient" = Field(None)
    PhoneNumber: "SignOnPhoneNumber" = Field(None)
    ProviderSpecialty: Union[str, None] = Field(None)
    Subject: str = Field(...)
    TimeZone: Union[str, None] = Field(None)
    UserId: Union[str, None] = Field(None)
    Visit: "SignOnVisit" = Field(None)


class SignOnMeta(RedoxAbstractModel):
    DataModel: str = Field(...)
    Destinations: List["SignOnMetaDestination"] = Field(None)
    EventDateTime: Union[str, None] = Field(None)
    EventType: str = Field(...)
    FacilityCode: Union[str, None] = Field(None)
    SessionBaseURL: Union[str, None] = Field(None)
    SessionID: Union[str, None] = Field(None)
    Source: "SignOnMetaSource" = Field(None)
    Test: Union[bool, None] = Field(None)


class SignOnMetaDestination(RedoxAbstractModel):
    ID: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)


class SignOnMetaSource(RedoxAbstractModel):
    ID: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)


class SignOnOrder(RedoxAbstractModel):
    ID: Union[str, None] = Field(None)


class SignOnPatient(RedoxAbstractModel):
    Demographics: "SignOnPatientDemographics" = Field(None)
    Identifiers: List["SignOnPatientIdentifier"] = Field(None)


class SignOnPatientDemographics(RedoxAbstractModel):
    Address: "SignOnPatientDemographicsAddress" = Field(None)
    DOB: Union[str, None] = Field(None)
    FirstName: Union[str, None] = Field(None)
    LastName: Union[str, None] = Field(None)
    MiddleName: Union[str, None] = Field(None)
    PhoneNumber: "SignOnPatientDemographicsPhoneNumber" = Field(None)
    Sex: Union[str, None] = Field(None)


class SignOnPatientDemographicsAddress(RedoxAbstractModel):
    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class SignOnPatientDemographicsPhoneNumber(RedoxAbstractModel):
    Home: Union[str, None] = Field(None)
    Mobile: Union[str, None] = Field(None)
    Office: Union[str, None] = Field(None)


class SignOnPatientIdentifier(RedoxAbstractModel):
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)


class SignOnPhoneNumber(RedoxAbstractModel):
    Office: Union[str, None] = Field(None)


class SignOnVisit(RedoxAbstractModel):
    Location: "SignOnVisitLocation" = Field(None)
    VisitNumber: Union[str, None] = Field(None)


class SignOnVisitLocation(RedoxAbstractModel):
    Department: Union[str, None] = Field(None)
    DepartmentIdentifiers: List["SignOnVisitLocationDepartmentIdentifier"] = Field(None)
    Facility: Union[str, None] = Field(None)
    FacilityIdentifiers: List["SignOnVisitLocationFacilityIdentifier"] = Field(None)
    Room: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


class SignOnVisitLocationDepartmentIdentifier(RedoxAbstractModel):
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)


class SignOnVisitLocationFacilityIdentifier(RedoxAbstractModel):
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)


SignOn.update_forward_refs()
SignOnMeta.update_forward_refs()
SignOnPatient.update_forward_refs()
SignOnPatientDemographics.update_forward_refs()
SignOnVisit.update_forward_refs()
SignOnVisitLocation.update_forward_refs()
