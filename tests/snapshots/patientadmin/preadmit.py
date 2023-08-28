# -*- coding: utf-8 -*-
# ----  AUTO-GENERATED BY redox_parser_gen. DO NOT MODIFY MANUALLY!!  ---- #

from typing import List, Union

from pydantic import Field

from ..abstract_base import EventTypeAbstractModel, RedoxAbstractModel
from ..field_types import Number


class PreAdmit(EventTypeAbstractModel):
    Meta: "PreAdmitMeta" = Field(...)
    Patient: "PreAdmitPatient" = Field(...)
    Visit: "PreAdmitVisit" = Field(None)


class PreAdmitMeta(RedoxAbstractModel):
    DataModel: str = Field(...)
    Destinations: List["PreAdmitMetaDestination"] = Field(None)
    EventDateTime: Union[str, None] = Field(None)
    EventType: str = Field(...)
    FacilityCode: Union[str, None] = Field(None)
    Logs: List["PreAdmitMetaLog"] = Field(None)
    Message: "PreAdmitMetaMessage" = Field(None)
    Source: "PreAdmitMetaSource" = Field(None)
    Test: Union[bool, None] = Field(None)
    Transmission: "PreAdmitMetaTransmission" = Field(None)


class PreAdmitMetaDestination(RedoxAbstractModel):
    ID: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)


class PreAdmitMetaLog(RedoxAbstractModel):
    AttemptID: Union[str, None] = Field(None)
    ID: Union[str, None] = Field(None)


class PreAdmitMetaMessage(RedoxAbstractModel):
    ID: Union[Number, None] = Field(None)


class PreAdmitMetaSource(RedoxAbstractModel):
    ID: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)


class PreAdmitMetaTransmission(RedoxAbstractModel):
    ID: Union[Number, None] = Field(None)


class PreAdmitPatient(RedoxAbstractModel):
    Allergies: List["PreAdmitPatientAllergy"] = Field(None)
    Contacts: List["PreAdmitPatientContact"] = Field(None)
    Demographics: "PreAdmitPatientDemographics" = Field(None)
    Diagnoses: List["PreAdmitPatientDiagnosis"] = Field(None)
    Identifiers: List["PreAdmitPatientIdentifier"] = Field(...)
    Notes: List[str] = Field(None)
    PCP: "PreAdmitPatientPCP" = Field(None)


class PreAdmitPatientAllergy(RedoxAbstractModel):
    Code: Union[str, None] = Field(None)
    Codeset: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)
    OnsetDateTime: Union[str, None] = Field(None)
    Reaction: List["PreAdmitPatientAllergyReaction"] = Field(None)
    Severity: "PreAdmitPatientAllergySeverity" = Field(None)
    Status: Union[str, None] = Field(None)
    Type: "PreAdmitPatientAllergyType" = Field(None)


class PreAdmitPatientAllergyReaction(RedoxAbstractModel):
    Code: Union[str, None] = Field(None)
    Codeset: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)


class PreAdmitPatientAllergySeverity(RedoxAbstractModel):
    Code: Union[str, None] = Field(None)
    Codeset: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)


class PreAdmitPatientAllergyType(RedoxAbstractModel):
    Code: Union[str, None] = Field(None)
    Codeset: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)


class PreAdmitPatientContact(RedoxAbstractModel):
    Address: "PreAdmitPatientContactAddress" = Field(None)
    EmailAddresses: List[str] = Field(None)
    FirstName: Union[str, None] = Field(None)
    LastName: Union[str, None] = Field(None)
    MiddleName: Union[str, None] = Field(None)
    PhoneNumber: "PreAdmitPatientContactPhoneNumber" = Field(None)
    RelationToPatient: Union[str, None] = Field(None)
    Roles: List[str] = Field(None)


class PreAdmitPatientContactAddress(RedoxAbstractModel):
    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class PreAdmitPatientContactPhoneNumber(RedoxAbstractModel):
    Home: Union[str, None] = Field(None)
    Mobile: Union[str, None] = Field(None)
    Office: Union[str, None] = Field(None)


class PreAdmitPatientDemographics(RedoxAbstractModel):
    Address: "PreAdmitPatientDemographicsAddress" = Field(None)
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
    PhoneNumber: "PreAdmitPatientDemographicsPhoneNumber" = Field(None)
    Race: Union[str, None] = Field(None)
    Religion: Union[str, None] = Field(None)
    SSN: Union[str, None] = Field(None)
    Sex: Union[str, None] = Field(None)


class PreAdmitPatientDemographicsAddress(RedoxAbstractModel):
    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class PreAdmitPatientDemographicsPhoneNumber(RedoxAbstractModel):
    Home: Union[str, None] = Field(None)
    Mobile: Union[str, None] = Field(None)
    Office: Union[str, None] = Field(None)


class PreAdmitPatientDiagnosis(RedoxAbstractModel):
    Code: Union[str, None] = Field(None)
    Codeset: Union[str, None] = Field(None)
    DocumentedDateTime: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


class PreAdmitPatientIdentifier(RedoxAbstractModel):
    ID: str = Field(...)
    IDType: str = Field(...)


class PreAdmitPatientPCP(RedoxAbstractModel):
    Address: "PreAdmitPatientPCPAddress" = Field(None)
    Credentials: List[str] = Field(None)
    EmailAddresses: List[str] = Field(None)
    FirstName: Union[str, None] = Field(None)
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)
    LastName: Union[str, None] = Field(None)
    Location: "PreAdmitPatientPCPLocation" = Field(None)
    NPI: Union[str, None] = Field(None)
    PhoneNumber: "PreAdmitPatientPCPPhoneNumber" = Field(None)


class PreAdmitPatientPCPAddress(RedoxAbstractModel):
    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class PreAdmitPatientPCPLocation(RedoxAbstractModel):
    Department: Union[str, None] = Field(None)
    DepartmentIdentifiers: List[
        "PreAdmitPatientPCPLocationDepartmentIdentifier"
    ] = Field(None)
    Facility: Union[str, None] = Field(None)
    FacilityIdentifiers: List["PreAdmitPatientPCPLocationFacilityIdentifier"] = Field(
        None
    )
    Room: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


class PreAdmitPatientPCPLocationDepartmentIdentifier(RedoxAbstractModel):
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)


class PreAdmitPatientPCPLocationFacilityIdentifier(RedoxAbstractModel):
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)


class PreAdmitPatientPCPPhoneNumber(RedoxAbstractModel):
    Office: Union[str, None] = Field(None)


class PreAdmitVisit(RedoxAbstractModel):
    AccountNumber: Union[str, None] = Field(None)
    AdditionalStaff: List["PreAdmitVisitAdditionalStaff"] = Field(None)
    AdmittingProvider: "PreAdmitVisitAdmittingProvider" = Field(None)
    AttendingProvider: "PreAdmitVisitAttendingProvider" = Field(None)
    Balance: Union[Number, None] = Field(None)
    ConsultingProvider: "PreAdmitVisitConsultingProvider" = Field(None)
    DiagnosisRelatedGroup: Union[Number, None] = Field(None)
    DiagnosisRelatedGroupType: Union[Number, None] = Field(None)
    Duration: Union[Number, None] = Field(None)
    Guarantor: "PreAdmitVisitGuarantor" = Field(None)
    Instructions: List[str] = Field(None)
    Insurances: List["PreAdmitVisitInsurance"] = Field(None)
    Location: "PreAdmitVisitLocation" = Field(None)
    PatientClass: Union[str, None] = Field(None)
    Reason: Union[str, None] = Field(None)
    ReferringProvider: "PreAdmitVisitReferringProvider" = Field(None)
    VisitDateTime: Union[str, None] = Field(None)
    VisitNumber: Union[str, None] = Field(None)


class PreAdmitVisitAdditionalStaff(RedoxAbstractModel):
    Address: "PreAdmitVisitAdditionalStaffAddress" = Field(None)
    Credentials: List[str] = Field(None)
    EmailAddresses: List[str] = Field(None)
    FirstName: Union[str, None] = Field(None)
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)
    LastName: Union[str, None] = Field(None)
    Location: "PreAdmitVisitAdditionalStaffLocation" = Field(None)
    PhoneNumber: "PreAdmitVisitAdditionalStaffPhoneNumber" = Field(None)
    Role: "PreAdmitVisitAdditionalStaffRole" = Field(None)


class PreAdmitVisitAdditionalStaffAddress(RedoxAbstractModel):
    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class PreAdmitVisitAdditionalStaffLocation(RedoxAbstractModel):
    Department: Union[str, None] = Field(None)
    DepartmentIdentifiers: List[
        "PreAdmitVisitAdditionalStaffLocationDepartmentIdentifier"
    ] = Field(None)
    Facility: Union[str, None] = Field(None)
    FacilityIdentifiers: List[
        "PreAdmitVisitAdditionalStaffLocationFacilityIdentifier"
    ] = Field(None)
    Room: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


class PreAdmitVisitAdditionalStaffLocationDepartmentIdentifier(RedoxAbstractModel):
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)


class PreAdmitVisitAdditionalStaffLocationFacilityIdentifier(RedoxAbstractModel):
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)


class PreAdmitVisitAdditionalStaffPhoneNumber(RedoxAbstractModel):
    Office: Union[str, None] = Field(None)


class PreAdmitVisitAdditionalStaffRole(RedoxAbstractModel):
    Code: Union[str, None] = Field(None)
    Codeset: Union[str, None] = Field(None)
    Description: Union[str, None] = Field(None)


class PreAdmitVisitAdmittingProvider(RedoxAbstractModel):
    Address: "PreAdmitVisitAdmittingProviderAddress" = Field(None)
    Credentials: List[str] = Field(None)
    EmailAddresses: List[str] = Field(None)
    FirstName: Union[str, None] = Field(None)
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)
    LastName: Union[str, None] = Field(None)
    Location: "PreAdmitVisitAdmittingProviderLocation" = Field(None)
    PhoneNumber: "PreAdmitVisitAdmittingProviderPhoneNumber" = Field(None)


class PreAdmitVisitAdmittingProviderAddress(RedoxAbstractModel):
    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class PreAdmitVisitAdmittingProviderLocation(RedoxAbstractModel):
    Department: Union[str, None] = Field(None)
    DepartmentIdentifiers: List[
        "PreAdmitVisitAdmittingProviderLocationDepartmentIdentifier"
    ] = Field(None)
    Facility: Union[str, None] = Field(None)
    FacilityIdentifiers: List[
        "PreAdmitVisitAdmittingProviderLocationFacilityIdentifier"
    ] = Field(None)
    Room: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


class PreAdmitVisitAdmittingProviderLocationDepartmentIdentifier(RedoxAbstractModel):
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)


class PreAdmitVisitAdmittingProviderLocationFacilityIdentifier(RedoxAbstractModel):
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)


class PreAdmitVisitAdmittingProviderPhoneNumber(RedoxAbstractModel):
    Office: Union[str, None] = Field(None)


class PreAdmitVisitAttendingProvider(RedoxAbstractModel):
    Address: "PreAdmitVisitAttendingProviderAddress" = Field(None)
    Credentials: List[str] = Field(None)
    EmailAddresses: List[str] = Field(None)
    FirstName: Union[str, None] = Field(None)
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)
    LastName: Union[str, None] = Field(None)
    Location: "PreAdmitVisitAttendingProviderLocation" = Field(None)
    PhoneNumber: "PreAdmitVisitAttendingProviderPhoneNumber" = Field(None)


class PreAdmitVisitAttendingProviderAddress(RedoxAbstractModel):
    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class PreAdmitVisitAttendingProviderLocation(RedoxAbstractModel):
    Department: Union[str, None] = Field(None)
    DepartmentIdentifiers: List[
        "PreAdmitVisitAttendingProviderLocationDepartmentIdentifier"
    ] = Field(None)
    Facility: Union[str, None] = Field(None)
    FacilityIdentifiers: List[
        "PreAdmitVisitAttendingProviderLocationFacilityIdentifier"
    ] = Field(None)
    Room: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


class PreAdmitVisitAttendingProviderLocationDepartmentIdentifier(RedoxAbstractModel):
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)


class PreAdmitVisitAttendingProviderLocationFacilityIdentifier(RedoxAbstractModel):
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)


class PreAdmitVisitAttendingProviderPhoneNumber(RedoxAbstractModel):
    Office: Union[str, None] = Field(None)


class PreAdmitVisitConsultingProvider(RedoxAbstractModel):
    Address: "PreAdmitVisitConsultingProviderAddress" = Field(None)
    Credentials: List[str] = Field(None)
    EmailAddresses: List[str] = Field(None)
    FirstName: Union[str, None] = Field(None)
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)
    LastName: Union[str, None] = Field(None)
    Location: "PreAdmitVisitConsultingProviderLocation" = Field(None)
    PhoneNumber: "PreAdmitVisitConsultingProviderPhoneNumber" = Field(None)


class PreAdmitVisitConsultingProviderAddress(RedoxAbstractModel):
    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class PreAdmitVisitConsultingProviderLocation(RedoxAbstractModel):
    Department: Union[str, None] = Field(None)
    DepartmentIdentifiers: List[
        "PreAdmitVisitConsultingProviderLocationDepartmentIdentifier"
    ] = Field(None)
    Facility: Union[str, None] = Field(None)
    FacilityIdentifiers: List[
        "PreAdmitVisitConsultingProviderLocationFacilityIdentifier"
    ] = Field(None)
    Room: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


class PreAdmitVisitConsultingProviderLocationDepartmentIdentifier(RedoxAbstractModel):
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)


class PreAdmitVisitConsultingProviderLocationFacilityIdentifier(RedoxAbstractModel):
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)


class PreAdmitVisitConsultingProviderPhoneNumber(RedoxAbstractModel):
    Office: Union[str, None] = Field(None)


class PreAdmitVisitGuarantor(RedoxAbstractModel):
    Address: "PreAdmitVisitGuarantorAddress" = Field(None)
    DOB: Union[str, None] = Field(None)
    EmailAddresses: List[str] = Field(None)
    Employer: "PreAdmitVisitGuarantorEmployer" = Field(None)
    FirstName: Union[str, None] = Field(None)
    LastName: Union[str, None] = Field(None)
    MiddleName: Union[str, None] = Field(None)
    Number: Union[str, None] = Field(None)
    PhoneNumber: "PreAdmitVisitGuarantorPhoneNumber" = Field(None)
    RelationToPatient: Union[str, None] = Field(None)
    SSN: Union[str, None] = Field(None)
    Sex: Union[str, None] = Field(None)
    Spouse: "PreAdmitVisitGuarantorSpouse" = Field(None)
    Type: Union[str, None] = Field(None)


class PreAdmitVisitGuarantorAddress(RedoxAbstractModel):
    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class PreAdmitVisitGuarantorEmployer(RedoxAbstractModel):
    Address: "PreAdmitVisitGuarantorEmployerAddress" = Field(None)
    Name: Union[str, None] = Field(None)
    PhoneNumber: Union[str, None] = Field(None)


class PreAdmitVisitGuarantorEmployerAddress(RedoxAbstractModel):
    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class PreAdmitVisitGuarantorPhoneNumber(RedoxAbstractModel):
    Business: Union[str, None] = Field(None)
    Home: Union[str, None] = Field(None)
    Mobile: Union[str, None] = Field(None)


class PreAdmitVisitGuarantorSpouse(RedoxAbstractModel):
    FirstName: Union[str, None] = Field(None)
    LastName: Union[str, None] = Field(None)


class PreAdmitVisitInsurance(RedoxAbstractModel):
    AgreementType: Union[str, None] = Field(None)
    Company: "PreAdmitVisitInsuranceCompany" = Field(None)
    CoverageType: Union[str, None] = Field(None)
    EffectiveDate: Union[str, None] = Field(None)
    ExpirationDate: Union[str, None] = Field(None)
    GroupName: Union[str, None] = Field(None)
    GroupNumber: Union[str, None] = Field(None)
    Insured: "PreAdmitVisitInsuranceInsured" = Field(None)
    MemberNumber: Union[str, None] = Field(None)
    Plan: "PreAdmitVisitInsurancePlan" = Field(None)
    PolicyNumber: Union[str, None] = Field(None)
    Priority: Union[str, None] = Field(None)


class PreAdmitVisitInsuranceCompany(RedoxAbstractModel):
    Address: "PreAdmitVisitInsuranceCompanyAddress" = Field(None)
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)
    PhoneNumber: Union[str, None] = Field(None)


class PreAdmitVisitInsuranceCompanyAddress(RedoxAbstractModel):
    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class PreAdmitVisitInsuranceInsured(RedoxAbstractModel):
    Address: "PreAdmitVisitInsuranceInsuredAddress" = Field(None)
    DOB: Union[str, None] = Field(None)
    FirstName: Union[str, None] = Field(None)
    Identifiers: List["PreAdmitVisitInsuranceInsuredIdentifier"] = Field(None)
    LastName: Union[str, None] = Field(None)
    MiddleName: Union[str, None] = Field(None)
    Relationship: Union[str, None] = Field(None)
    SSN: Union[str, None] = Field(None)
    Sex: Union[str, None] = Field(None)


class PreAdmitVisitInsuranceInsuredAddress(RedoxAbstractModel):
    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class PreAdmitVisitInsuranceInsuredIdentifier(RedoxAbstractModel):
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)


class PreAdmitVisitInsurancePlan(RedoxAbstractModel):
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


class PreAdmitVisitLocation(RedoxAbstractModel):
    Address: "PreAdmitVisitLocationAddress" = Field(None)
    Bed: Union[str, None] = Field(None)
    Department: Union[str, None] = Field(None)
    DepartmentIdentifiers: List["PreAdmitVisitLocationDepartmentIdentifier"] = Field(
        None
    )
    Facility: Union[str, None] = Field(None)
    FacilityIdentifiers: List["PreAdmitVisitLocationFacilityIdentifier"] = Field(None)
    Room: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


class PreAdmitVisitLocationAddress(RedoxAbstractModel):
    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class PreAdmitVisitLocationDepartmentIdentifier(RedoxAbstractModel):
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)


class PreAdmitVisitLocationFacilityIdentifier(RedoxAbstractModel):
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)


class PreAdmitVisitReferringProvider(RedoxAbstractModel):
    Address: "PreAdmitVisitReferringProviderAddress" = Field(None)
    Credentials: List[str] = Field(None)
    EmailAddresses: List[str] = Field(None)
    FirstName: Union[str, None] = Field(None)
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)
    LastName: Union[str, None] = Field(None)
    Location: "PreAdmitVisitReferringProviderLocation" = Field(None)
    PhoneNumber: "PreAdmitVisitReferringProviderPhoneNumber" = Field(None)


class PreAdmitVisitReferringProviderAddress(RedoxAbstractModel):
    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class PreAdmitVisitReferringProviderLocation(RedoxAbstractModel):
    Department: Union[str, None] = Field(None)
    DepartmentIdentifiers: List[
        "PreAdmitVisitReferringProviderLocationDepartmentIdentifier"
    ] = Field(None)
    Facility: Union[str, None] = Field(None)
    FacilityIdentifiers: List[
        "PreAdmitVisitReferringProviderLocationFacilityIdentifier"
    ] = Field(None)
    Room: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


class PreAdmitVisitReferringProviderLocationDepartmentIdentifier(RedoxAbstractModel):
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)


class PreAdmitVisitReferringProviderLocationFacilityIdentifier(RedoxAbstractModel):
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)


class PreAdmitVisitReferringProviderPhoneNumber(RedoxAbstractModel):
    Office: Union[str, None] = Field(None)


PreAdmit.update_forward_refs()
PreAdmitMeta.update_forward_refs()
PreAdmitPatient.update_forward_refs()
PreAdmitPatientAllergy.update_forward_refs()
PreAdmitPatientContact.update_forward_refs()
PreAdmitPatientDemographics.update_forward_refs()
PreAdmitPatientPCP.update_forward_refs()
PreAdmitPatientPCPLocation.update_forward_refs()
PreAdmitVisit.update_forward_refs()
PreAdmitVisitAdditionalStaff.update_forward_refs()
PreAdmitVisitAdditionalStaffLocation.update_forward_refs()
PreAdmitVisitAdmittingProvider.update_forward_refs()
PreAdmitVisitAdmittingProviderLocation.update_forward_refs()
PreAdmitVisitAttendingProvider.update_forward_refs()
PreAdmitVisitAttendingProviderLocation.update_forward_refs()
PreAdmitVisitConsultingProvider.update_forward_refs()
PreAdmitVisitConsultingProviderLocation.update_forward_refs()
PreAdmitVisitGuarantor.update_forward_refs()
PreAdmitVisitGuarantorEmployer.update_forward_refs()
PreAdmitVisitInsurance.update_forward_refs()
PreAdmitVisitInsuranceCompany.update_forward_refs()
PreAdmitVisitInsuranceInsured.update_forward_refs()
PreAdmitVisitLocation.update_forward_refs()
PreAdmitVisitReferringProvider.update_forward_refs()
PreAdmitVisitReferringProviderLocation.update_forward_refs()
