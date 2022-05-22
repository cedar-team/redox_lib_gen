# -*- coding: utf-8 -*-
# ----  AUTO-GENERATED BY redox_lib_gen. DO NOT MODIFY MANUALLY!!  ---- #

from typing import List, Union

from pydantic import Field

from ..abstract_base import EventTypeAbstractModel, RedoxAbstractModel
from ..field_types import Number


class Cancel(EventTypeAbstractModel):

    Meta: "CancelMeta" = Field(...)
    Patient: "CancelPatient" = Field(...)
    Visit: "CancelVisit" = Field(None)


class CancelMeta(RedoxAbstractModel):

    CanceledEvent: Union[str, None] = Field(None)
    DataModel: str = Field(...)
    Destinations: List["CancelMetaDestination"] = Field(None)
    EventDateTime: Union[str, None] = Field(None)
    EventType: str = Field(...)
    FacilityCode: Union[str, None] = Field(None)
    Logs: List["CancelMetaLog"] = Field(None)
    Message: "CancelMetaMessage" = Field(None)
    Source: "CancelMetaSource" = Field(None)
    Test: Union[bool, None] = Field(None)
    Transmission: "CancelMetaTransmission" = Field(None)


class CancelMetaDestination(RedoxAbstractModel):

    ID: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)


class CancelMetaLog(RedoxAbstractModel):

    AttemptID: Union[str, None] = Field(None)
    ID: Union[str, None] = Field(None)


class CancelMetaMessage(RedoxAbstractModel):

    ID: Union[Number, None] = Field(None)


class CancelMetaSource(RedoxAbstractModel):

    ID: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)


class CancelMetaTransmission(RedoxAbstractModel):

    ID: Union[Number, None] = Field(None)


class CancelPatient(RedoxAbstractModel):

    Allergies: List["CancelPatientAllergy"] = Field(None)
    Contacts: List["CancelPatientContact"] = Field(None)
    Demographics: "CancelPatientDemographics" = Field(None)
    Diagnoses: List["CancelPatientDiagnosis"] = Field(None)
    Identifiers: List["CancelPatientIdentifier"] = Field(...)
    Notes: List[str] = Field(None)
    PCP: "CancelPatientPCP" = Field(None)


class CancelPatientAllergy(RedoxAbstractModel):

    Code: Union[str, None] = Field(None)
    Codeset: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)
    OnsetDateTime: Union[str, None] = Field(None)
    Reaction: List["CancelPatientAllergyReaction"] = Field(None)
    Severity: "CancelPatientAllergySeverity" = Field(None)
    Status: Union[str, None] = Field(None)
    Type: "CancelPatientAllergyType" = Field(None)


class CancelPatientAllergyReaction(RedoxAbstractModel):

    Code: Union[str, None] = Field(None)
    Codeset: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)


class CancelPatientAllergySeverity(RedoxAbstractModel):

    Code: Union[str, None] = Field(None)
    Codeset: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)


class CancelPatientAllergyType(RedoxAbstractModel):

    Code: Union[str, None] = Field(None)
    Codeset: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)


class CancelPatientContact(RedoxAbstractModel):

    Address: "CancelPatientContactAddress" = Field(None)
    EmailAddresses: List[str] = Field(None)
    FirstName: Union[str, None] = Field(None)
    LastName: Union[str, None] = Field(None)
    MiddleName: Union[str, None] = Field(None)
    PhoneNumber: "CancelPatientContactPhoneNumber" = Field(None)
    RelationToPatient: Union[str, None] = Field(None)
    Roles: List[str] = Field(None)


class CancelPatientContactAddress(RedoxAbstractModel):

    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class CancelPatientContactPhoneNumber(RedoxAbstractModel):

    Home: Union[str, None] = Field(None)
    Mobile: Union[str, None] = Field(None)
    Office: Union[str, None] = Field(None)


class CancelPatientDemographics(RedoxAbstractModel):

    Address: "CancelPatientDemographicsAddress" = Field(None)
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
    PhoneNumber: "CancelPatientDemographicsPhoneNumber" = Field(None)
    Race: Union[str, None] = Field(None)
    Religion: Union[str, None] = Field(None)
    Sex: Union[str, None] = Field(None)
    SSN: Union[str, None] = Field(None)


class CancelPatientDemographicsAddress(RedoxAbstractModel):

    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class CancelPatientDemographicsPhoneNumber(RedoxAbstractModel):

    Home: Union[str, None] = Field(None)
    Mobile: Union[str, None] = Field(None)
    Office: Union[str, None] = Field(None)


class CancelPatientDiagnosis(RedoxAbstractModel):

    Code: Union[str, None] = Field(None)
    Codeset: Union[str, None] = Field(None)
    DocumentedDateTime: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


class CancelPatientIdentifier(RedoxAbstractModel):

    ID: str = Field(...)
    IDType: str = Field(...)


class CancelPatientPCP(RedoxAbstractModel):

    Address: "CancelPatientPCPAddress" = Field(None)
    Credentials: List[str] = Field(None)
    EmailAddresses: List[str] = Field(None)
    FirstName: Union[str, None] = Field(None)
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)
    LastName: Union[str, None] = Field(None)
    Location: "CancelPatientPCPLocation" = Field(None)
    NPI: Union[str, None] = Field(None)
    PhoneNumber: "CancelPatientPCPPhoneNumber" = Field(None)


class CancelPatientPCPAddress(RedoxAbstractModel):

    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class CancelPatientPCPLocation(RedoxAbstractModel):

    Department: Union[str, None] = Field(None)
    Facility: Union[str, None] = Field(None)
    Room: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


class CancelPatientPCPPhoneNumber(RedoxAbstractModel):

    Office: Union[str, None] = Field(None)


class CancelVisit(RedoxAbstractModel):

    AccountNumber: Union[str, None] = Field(None)
    AdditionalStaff: List["CancelVisitAdditionalStaff"] = Field(None)
    AdmittingProvider: "CancelVisitAdmittingProvider" = Field(None)
    AttendingProvider: "CancelVisitAttendingProvider" = Field(None)
    Balance: Union[Number, None] = Field(None)
    ConsultingProvider: "CancelVisitConsultingProvider" = Field(None)
    DiagnosisRelatedGroup: Union[Number, None] = Field(None)
    DiagnosisRelatedGroupType: Union[Number, None] = Field(None)
    Duration: Union[Number, None] = Field(None)
    Guarantor: "CancelVisitGuarantor" = Field(None)
    Instructions: List[str] = Field(None)
    Insurances: List["CancelVisitInsurance"] = Field(None)
    Location: "CancelVisitLocation" = Field(None)
    PatientClass: Union[str, None] = Field(None)
    Reason: Union[str, None] = Field(None)
    ReferringProvider: "CancelVisitReferringProvider" = Field(None)
    VisitDateTime: Union[str, None] = Field(None)
    VisitNumber: Union[str, None] = Field(None)


class CancelVisitAdditionalStaff(RedoxAbstractModel):

    Address: "CancelVisitAdditionalStaffAddress" = Field(None)
    Credentials: List[str] = Field(None)
    EmailAddresses: List[str] = Field(None)
    FirstName: Union[str, None] = Field(None)
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)
    LastName: Union[str, None] = Field(None)
    Location: "CancelVisitAdditionalStaffLocation" = Field(None)
    PhoneNumber: "CancelVisitAdditionalStaffPhoneNumber" = Field(None)
    Role: "CancelVisitAdditionalStaffRole" = Field(None)


class CancelVisitAdditionalStaffAddress(RedoxAbstractModel):

    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class CancelVisitAdditionalStaffLocation(RedoxAbstractModel):

    Department: Union[str, None] = Field(None)
    Facility: Union[str, None] = Field(None)
    Room: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


class CancelVisitAdditionalStaffPhoneNumber(RedoxAbstractModel):

    Office: Union[str, None] = Field(None)


class CancelVisitAdditionalStaffRole(RedoxAbstractModel):

    Code: Union[str, None] = Field(None)
    Codeset: Union[str, None] = Field(None)
    Description: Union[str, None] = Field(None)


class CancelVisitAdmittingProvider(RedoxAbstractModel):

    Address: "CancelVisitAdmittingProviderAddress" = Field(None)
    Credentials: List[str] = Field(None)
    EmailAddresses: List[str] = Field(None)
    FirstName: Union[str, None] = Field(None)
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)
    LastName: Union[str, None] = Field(None)
    Location: "CancelVisitAdmittingProviderLocation" = Field(None)
    PhoneNumber: "CancelVisitAdmittingProviderPhoneNumber" = Field(None)


class CancelVisitAdmittingProviderAddress(RedoxAbstractModel):

    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class CancelVisitAdmittingProviderLocation(RedoxAbstractModel):

    Department: Union[str, None] = Field(None)
    Facility: Union[str, None] = Field(None)
    Room: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


class CancelVisitAdmittingProviderPhoneNumber(RedoxAbstractModel):

    Office: Union[str, None] = Field(None)


class CancelVisitAttendingProvider(RedoxAbstractModel):

    Address: "CancelVisitAttendingProviderAddress" = Field(None)
    Credentials: List[str] = Field(None)
    EmailAddresses: List[str] = Field(None)
    FirstName: Union[str, None] = Field(None)
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)
    LastName: Union[str, None] = Field(None)
    Location: "CancelVisitAttendingProviderLocation" = Field(None)
    PhoneNumber: "CancelVisitAttendingProviderPhoneNumber" = Field(None)


class CancelVisitAttendingProviderAddress(RedoxAbstractModel):

    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class CancelVisitAttendingProviderLocation(RedoxAbstractModel):

    Department: Union[str, None] = Field(None)
    Facility: Union[str, None] = Field(None)
    Room: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


class CancelVisitAttendingProviderPhoneNumber(RedoxAbstractModel):

    Office: Union[str, None] = Field(None)


class CancelVisitConsultingProvider(RedoxAbstractModel):

    Address: "CancelVisitConsultingProviderAddress" = Field(None)
    Credentials: List[str] = Field(None)
    EmailAddresses: List[str] = Field(None)
    FirstName: Union[str, None] = Field(None)
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)
    LastName: Union[str, None] = Field(None)
    Location: "CancelVisitConsultingProviderLocation" = Field(None)
    PhoneNumber: "CancelVisitConsultingProviderPhoneNumber" = Field(None)


class CancelVisitConsultingProviderAddress(RedoxAbstractModel):

    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class CancelVisitConsultingProviderLocation(RedoxAbstractModel):

    Department: Union[str, None] = Field(None)
    Facility: Union[str, None] = Field(None)
    Room: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


class CancelVisitConsultingProviderPhoneNumber(RedoxAbstractModel):

    Office: Union[str, None] = Field(None)


class CancelVisitGuarantor(RedoxAbstractModel):

    Address: "CancelVisitGuarantorAddress" = Field(None)
    DOB: Union[str, None] = Field(None)
    EmailAddresses: List[str] = Field(None)
    Employer: "CancelVisitGuarantorEmployer" = Field(None)
    FirstName: Union[str, None] = Field(None)
    LastName: Union[str, None] = Field(None)
    MiddleName: Union[str, None] = Field(None)
    Number: Union[str, None] = Field(None)
    PhoneNumber: "CancelVisitGuarantorPhoneNumber" = Field(None)
    RelationToPatient: Union[str, None] = Field(None)
    Sex: Union[str, None] = Field(None)
    Spouse: "CancelVisitGuarantorSpouse" = Field(None)
    SSN: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


class CancelVisitGuarantorAddress(RedoxAbstractModel):

    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class CancelVisitGuarantorEmployer(RedoxAbstractModel):

    Address: "CancelVisitGuarantorEmployerAddress" = Field(None)
    Name: Union[str, None] = Field(None)
    PhoneNumber: Union[str, None] = Field(None)


class CancelVisitGuarantorEmployerAddress(RedoxAbstractModel):

    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class CancelVisitGuarantorPhoneNumber(RedoxAbstractModel):

    Business: Union[str, None] = Field(None)
    Home: Union[str, None] = Field(None)
    Mobile: Union[str, None] = Field(None)


class CancelVisitGuarantorSpouse(RedoxAbstractModel):

    FirstName: Union[str, None] = Field(None)
    LastName: Union[str, None] = Field(None)


class CancelVisitInsurance(RedoxAbstractModel):

    AgreementType: Union[str, None] = Field(None)
    Company: "CancelVisitInsuranceCompany" = Field(None)
    CoverageType: Union[str, None] = Field(None)
    EffectiveDate: Union[str, None] = Field(None)
    ExpirationDate: Union[str, None] = Field(None)
    GroupName: Union[str, None] = Field(None)
    GroupNumber: Union[str, None] = Field(None)
    Insured: "CancelVisitInsuranceInsured" = Field(None)
    MemberNumber: Union[str, None] = Field(None)
    Plan: "CancelVisitInsurancePlan" = Field(None)
    PolicyNumber: Union[str, None] = Field(None)
    Priority: Union[str, None] = Field(None)


class CancelVisitInsuranceCompany(RedoxAbstractModel):

    Address: "CancelVisitInsuranceCompanyAddress" = Field(None)
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)
    PhoneNumber: Union[str, None] = Field(None)


class CancelVisitInsuranceCompanyAddress(RedoxAbstractModel):

    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class CancelVisitInsuranceInsured(RedoxAbstractModel):

    Address: "CancelVisitInsuranceInsuredAddress" = Field(None)
    DOB: Union[str, None] = Field(None)
    FirstName: Union[str, None] = Field(None)
    Identifiers: List["CancelVisitInsuranceInsuredIdentifier"] = Field(None)
    LastName: Union[str, None] = Field(None)
    MiddleName: Union[str, None] = Field(None)
    Relationship: Union[str, None] = Field(None)
    Sex: Union[str, None] = Field(None)
    SSN: Union[str, None] = Field(None)


class CancelVisitInsuranceInsuredAddress(RedoxAbstractModel):

    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class CancelVisitInsuranceInsuredIdentifier(RedoxAbstractModel):

    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)


class CancelVisitInsurancePlan(RedoxAbstractModel):

    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


class CancelVisitLocation(RedoxAbstractModel):

    Address: "CancelVisitLocationAddress" = Field(None)
    Bed: Union[str, None] = Field(None)
    Department: Union[str, None] = Field(None)
    Facility: Union[str, None] = Field(None)
    Room: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


class CancelVisitLocationAddress(RedoxAbstractModel):

    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class CancelVisitReferringProvider(RedoxAbstractModel):

    Address: "CancelVisitReferringProviderAddress" = Field(None)
    Credentials: List[str] = Field(None)
    EmailAddresses: List[str] = Field(None)
    FirstName: Union[str, None] = Field(None)
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)
    LastName: Union[str, None] = Field(None)
    Location: "CancelVisitReferringProviderLocation" = Field(None)
    PhoneNumber: "CancelVisitReferringProviderPhoneNumber" = Field(None)


class CancelVisitReferringProviderAddress(RedoxAbstractModel):

    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class CancelVisitReferringProviderLocation(RedoxAbstractModel):

    Department: Union[str, None] = Field(None)
    Facility: Union[str, None] = Field(None)
    Room: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


class CancelVisitReferringProviderPhoneNumber(RedoxAbstractModel):

    Office: Union[str, None] = Field(None)


Cancel.update_forward_refs()
CancelMeta.update_forward_refs()
CancelPatient.update_forward_refs()
CancelPatientAllergy.update_forward_refs()
CancelPatientContact.update_forward_refs()
CancelPatientDemographics.update_forward_refs()
CancelPatientPCP.update_forward_refs()
CancelVisit.update_forward_refs()
CancelVisitAdditionalStaff.update_forward_refs()
CancelVisitAdmittingProvider.update_forward_refs()
CancelVisitAttendingProvider.update_forward_refs()
CancelVisitConsultingProvider.update_forward_refs()
CancelVisitGuarantor.update_forward_refs()
CancelVisitGuarantorEmployer.update_forward_refs()
CancelVisitInsurance.update_forward_refs()
CancelVisitInsuranceCompany.update_forward_refs()
CancelVisitInsuranceInsured.update_forward_refs()
CancelVisitLocation.update_forward_refs()
CancelVisitReferringProvider.update_forward_refs()
