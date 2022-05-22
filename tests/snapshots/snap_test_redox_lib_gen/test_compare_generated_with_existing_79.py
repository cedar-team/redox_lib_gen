# -*- coding: utf-8 -*-
# ----  AUTO-GENERATED BY redox_lib_gen. DO NOT MODIFY MANUALLY!!  ---- #

from typing import List, Union

from pydantic import Field

from ..abstract_base import EventTypeAbstractModel, RedoxAbstractModel
from ..field_types import Number


class New(EventTypeAbstractModel):

    Education: List["NewEducation"] = Field(...)
    Meta: "NewMeta" = Field(...)
    Patient: "NewPatient" = Field(...)
    Visit: "NewVisit" = Field(None)


class NewEducation(RedoxAbstractModel):

    ActionDateTime: Union[str, None] = Field(None)
    ActionStatus: Union[str, None] = Field(None)
    Assignments: List["NewEducationAssignment"] = Field(None)
    CreatedDateTime: Union[str, None] = Field(None)
    InstanceID: Union[str, None] = Field(None)
    Status: Union[str, None] = Field(None)
    Subject: "NewEducationSubject" = Field(...)


class NewEducationAssignment(RedoxAbstractModel):

    ActionDateTime: Union[str, None] = Field(None)
    ActionStatus: Union[str, None] = Field(None)
    Assignees: List["NewEducationAssignmentAssignee"] = Field(None)
    Code: Union[str, None] = Field(None)
    Codeset: Union[str, None] = Field(None)
    CreatedDateTime: Union[str, None] = Field(None)
    Description: Union[str, None] = Field(None)
    InstanceID: Union[str, None] = Field(None)
    Status: Union[str, None] = Field(None)
    Topic: "NewEducationAssignmentTopic" = Field(None)


class NewEducationAssignmentAssignee(RedoxAbstractModel):

    ContentType: Union[str, None] = Field(None)
    Learner: Union[str, None] = Field(None)
    Notes: List[str] = Field(None)
    Readiness: Union[str, None] = Field(None)
    Response: Union[str, None] = Field(None)


class NewEducationAssignmentTopic(RedoxAbstractModel):

    Code: Union[str, None] = Field(None)
    Codeset: Union[str, None] = Field(None)
    Description: Union[str, None] = Field(None)


class NewEducationSubject(RedoxAbstractModel):

    Code: str = Field(...)
    Codeset: Union[str, None] = Field(None)
    Description: Union[str, None] = Field(None)


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


class NewPatient(RedoxAbstractModel):

    Demographics: "NewPatientDemographics" = Field(None)
    Identifiers: List["NewPatientIdentifier"] = Field(...)
    Notes: List[str] = Field(None)


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

    ID: str = Field(...)
    IDType: str = Field(...)


class NewVisit(RedoxAbstractModel):

    AccountNumber: Union[str, None] = Field(None)
    AttendingProvider: "NewVisitAttendingProvider" = Field(None)
    ConsultingProvider: "NewVisitConsultingProvider" = Field(None)
    Location: "NewVisitLocation" = Field(None)
    PatientClass: Union[str, None] = Field(None)
    ReferringProvider: "NewVisitReferringProvider" = Field(None)
    VisitDateTime: Union[str, None] = Field(None)
    VisitNumber: Union[str, None] = Field(None)


class NewVisitAttendingProvider(RedoxAbstractModel):

    Address: "NewVisitAttendingProviderAddress" = Field(None)
    Credentials: List[str] = Field(None)
    EmailAddresses: List[str] = Field(None)
    FirstName: Union[str, None] = Field(None)
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)
    LastName: Union[str, None] = Field(None)
    Location: "NewVisitAttendingProviderLocation" = Field(None)
    NPI: Union[str, None] = Field(None)
    PhoneNumber: "NewVisitAttendingProviderPhoneNumber" = Field(None)


class NewVisitAttendingProviderAddress(RedoxAbstractModel):

    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class NewVisitAttendingProviderLocation(RedoxAbstractModel):

    Department: Union[str, None] = Field(None)
    Facility: Union[str, None] = Field(None)
    Room: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


class NewVisitAttendingProviderPhoneNumber(RedoxAbstractModel):

    Office: Union[str, None] = Field(None)


class NewVisitConsultingProvider(RedoxAbstractModel):

    Address: "NewVisitConsultingProviderAddress" = Field(None)
    Credentials: List[str] = Field(None)
    EmailAddresses: List[str] = Field(None)
    FirstName: Union[str, None] = Field(None)
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)
    LastName: Union[str, None] = Field(None)
    Location: "NewVisitConsultingProviderLocation" = Field(None)
    NPI: Union[str, None] = Field(None)
    PhoneNumber: "NewVisitConsultingProviderPhoneNumber" = Field(None)


class NewVisitConsultingProviderAddress(RedoxAbstractModel):

    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class NewVisitConsultingProviderLocation(RedoxAbstractModel):

    Department: Union[str, None] = Field(None)
    Facility: Union[str, None] = Field(None)
    Room: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


class NewVisitConsultingProviderPhoneNumber(RedoxAbstractModel):

    Office: Union[str, None] = Field(None)


class NewVisitLocation(RedoxAbstractModel):

    Bed: Union[str, None] = Field(None)
    Department: Union[str, None] = Field(None)
    Facility: Union[str, None] = Field(None)
    Room: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


class NewVisitReferringProvider(RedoxAbstractModel):

    Address: "NewVisitReferringProviderAddress" = Field(None)
    Credentials: List[str] = Field(None)
    EmailAddresses: List[str] = Field(None)
    FirstName: Union[str, None] = Field(None)
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)
    LastName: Union[str, None] = Field(None)
    Location: "NewVisitReferringProviderLocation" = Field(None)
    NPI: Union[str, None] = Field(None)
    PhoneNumber: "NewVisitReferringProviderPhoneNumber" = Field(None)


class NewVisitReferringProviderAddress(RedoxAbstractModel):

    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class NewVisitReferringProviderLocation(RedoxAbstractModel):

    Department: Union[str, None] = Field(None)
    Facility: Union[str, None] = Field(None)
    Room: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


class NewVisitReferringProviderPhoneNumber(RedoxAbstractModel):

    Office: Union[str, None] = Field(None)


New.update_forward_refs()
NewEducation.update_forward_refs()
NewEducationAssignment.update_forward_refs()
NewMeta.update_forward_refs()
NewPatient.update_forward_refs()
NewPatientDemographics.update_forward_refs()
NewVisit.update_forward_refs()
NewVisitAttendingProvider.update_forward_refs()
NewVisitConsultingProvider.update_forward_refs()
NewVisitReferringProvider.update_forward_refs()
