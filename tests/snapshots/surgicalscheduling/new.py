# -*- coding: utf-8 -*-
# ----  AUTO-GENERATED BY redox_lib_gen. DO NOT MODIFY MANUALLY!!  ---- #

from typing import List, Union

from pydantic import Field

from ..abstract_base import EventTypeAbstractModel, RedoxAbstractModel
from ..field_types import Number


class New(EventTypeAbstractModel):
    Meta: "NewMeta" = Field(...)
    Patient: "NewPatient" = Field(...)
    Procedures: List["NewProcedure"] = Field(...)
    SurgeryStaff: List["NewSurgeryStaff"] = Field(None)
    SurgicalCase: "NewSurgicalCase" = Field(None)
    SurgicalInfo: List["NewSurgicalInfo"] = Field(None)
    Visit: "NewVisit" = Field(...)


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
    PhoneNumber: "NewPatientDemographicsPhoneNumber" = Field(None)
    Race: Union[str, None] = Field(None)
    Religion: Union[str, None] = Field(None)
    SSN: Union[str, None] = Field(None)
    Sex: Union[str, None] = Field(None)


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


class NewProcedure(RedoxAbstractModel):
    Code: Union[str, None] = Field(None)
    Codeset: Union[str, None] = Field(None)
    DateTime: str = Field(...)
    Description: Union[str, None] = Field(None)
    Duration: Number = Field(...)
    ProcedureInfo: List["NewProcedureProcedureInfo"] = Field(None)


class NewProcedureProcedureInfo(RedoxAbstractModel):
    Description: Union[str, None] = Field(None)
    Value: Union[str, None] = Field(None)


class NewSurgeryStaff(RedoxAbstractModel):
    Address: "NewSurgeryStaffAddress" = Field(None)
    Credentials: List[str] = Field(None)
    Duration: Union[Number, None] = Field(None)
    EmailAddresses: List[str] = Field(None)
    FirstName: Union[str, None] = Field(None)
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)
    LastName: Union[str, None] = Field(None)
    Location: "NewSurgeryStaffLocation" = Field(None)
    PhoneNumber: "NewSurgeryStaffPhoneNumber" = Field(None)
    Role: "NewSurgeryStaffRole" = Field(None)
    StartDateTime: Union[str, None] = Field(None)


class NewSurgeryStaffAddress(RedoxAbstractModel):
    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class NewSurgeryStaffLocation(RedoxAbstractModel):
    Department: Union[str, None] = Field(None)
    DepartmentIdentifiers: List["NewSurgeryStaffLocationDepartmentIdentifier"] = Field(
        None
    )
    Facility: Union[str, None] = Field(None)
    FacilityIdentifiers: List["NewSurgeryStaffLocationFacilityIdentifier"] = Field(None)
    Room: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


class NewSurgeryStaffLocationDepartmentIdentifier(RedoxAbstractModel):
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)


class NewSurgeryStaffLocationFacilityIdentifier(RedoxAbstractModel):
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)


class NewSurgeryStaffPhoneNumber(RedoxAbstractModel):
    Office: Union[str, None] = Field(None)


class NewSurgeryStaffRole(RedoxAbstractModel):
    Code: Union[str, None] = Field(None)
    Codeset: Union[str, None] = Field(None)
    Description: Union[str, None] = Field(None)


class NewSurgicalCase(RedoxAbstractModel):
    Number: Union[str, None] = Field(None)
    Status: Union[str, None] = Field(None)


class NewSurgicalInfo(RedoxAbstractModel):
    Code: Union[str, None] = Field(None)
    Codeset: Union[str, None] = Field(None)
    Description: Union[str, None] = Field(None)
    Value: Union[str, None] = Field(None)


class NewVisit(RedoxAbstractModel):
    AccountNumber: Union[str, None] = Field(None)
    AttendingProvider: "NewVisitAttendingProvider" = Field(None)
    Diagnoses: List["NewVisitDiagnosis"] = Field(None)
    Duration: Union[Number, None] = Field(None)
    Equipment: List["NewVisitEquipment"] = Field(None)
    Location: "NewVisitLocation" = Field(...)
    Notes: List[str] = Field(None)
    PatientClass: Union[str, None] = Field(None)
    Status: Union[str, None] = Field(None)
    VisitDateTime: Union[str, None] = Field(None)
    VisitNumber: str = Field(...)


class NewVisitAttendingProvider(RedoxAbstractModel):
    Address: "NewVisitAttendingProviderAddress" = Field(None)
    Credentials: List[str] = Field(None)
    EmailAddresses: List[str] = Field(None)
    FirstName: Union[str, None] = Field(None)
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)
    LastName: Union[str, None] = Field(None)
    Location: "NewVisitAttendingProviderLocation" = Field(None)
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
    DepartmentIdentifiers: List[
        "NewVisitAttendingProviderLocationDepartmentIdentifier"
    ] = Field(None)
    Facility: Union[str, None] = Field(None)
    FacilityIdentifiers: List[
        "NewVisitAttendingProviderLocationFacilityIdentifier"
    ] = Field(None)
    Room: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


class NewVisitAttendingProviderLocationDepartmentIdentifier(RedoxAbstractModel):
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)


class NewVisitAttendingProviderLocationFacilityIdentifier(RedoxAbstractModel):
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)


class NewVisitAttendingProviderPhoneNumber(RedoxAbstractModel):
    Office: Union[str, None] = Field(None)


class NewVisitDiagnosis(RedoxAbstractModel):
    Code: Union[str, None] = Field(None)
    Codeset: Union[str, None] = Field(None)
    DocumentedDateTime: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


class NewVisitEquipment(RedoxAbstractModel):
    Code: Union[str, None] = Field(None)
    Codeset: Union[str, None] = Field(None)
    Description: Union[str, None] = Field(None)
    Duration: Union[Number, None] = Field(None)
    StartDateTime: Union[str, None] = Field(None)


class NewVisitLocation(RedoxAbstractModel):
    Bed: Union[str, None] = Field(None)
    Department: str = Field(...)
    DepartmentIdentifiers: List["NewVisitLocationDepartmentIdentifier"] = Field(None)
    Facility: Union[str, None] = Field(None)
    FacilityIdentifiers: List["NewVisitLocationFacilityIdentifier"] = Field(None)
    Room: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


class NewVisitLocationDepartmentIdentifier(RedoxAbstractModel):
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)


class NewVisitLocationFacilityIdentifier(RedoxAbstractModel):
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)


New.update_forward_refs()
NewMeta.update_forward_refs()
NewPatient.update_forward_refs()
NewPatientDemographics.update_forward_refs()
NewProcedure.update_forward_refs()
NewSurgeryStaff.update_forward_refs()
NewSurgeryStaffLocation.update_forward_refs()
NewVisit.update_forward_refs()
NewVisitAttendingProvider.update_forward_refs()
NewVisitAttendingProviderLocation.update_forward_refs()
NewVisitLocation.update_forward_refs()
