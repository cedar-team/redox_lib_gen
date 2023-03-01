# -*- coding: utf-8 -*-
# ----  AUTO-GENERATED BY redox_lib_gen. DO NOT MODIFY MANUALLY!!  ---- #

from typing import List, Union

from pydantic import Field

from ..abstract_base import EventTypeAbstractModel, RedoxAbstractModel
from ..field_types import Number


class PatientUpdate(EventTypeAbstractModel):
    Meta: "PatientUpdateMeta" = Field(...)
    Patient: "PatientUpdatePatient" = Field(...)


class PatientUpdateMeta(RedoxAbstractModel):
    DataModel: str = Field(...)
    Destinations: List["PatientUpdateMetaDestination"] = Field(None)
    EventDateTime: Union[str, None] = Field(None)
    EventType: str = Field(...)
    FacilityCode: Union[str, None] = Field(None)
    Logs: List["PatientUpdateMetaLog"] = Field(None)
    Message: "PatientUpdateMetaMessage" = Field(None)
    Source: "PatientUpdateMetaSource" = Field(None)
    Test: Union[bool, None] = Field(None)
    Transmission: "PatientUpdateMetaTransmission" = Field(None)


class PatientUpdateMetaDestination(RedoxAbstractModel):
    ID: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)


class PatientUpdateMetaLog(RedoxAbstractModel):
    AttemptID: Union[str, None] = Field(None)
    ID: Union[str, None] = Field(None)


class PatientUpdateMetaMessage(RedoxAbstractModel):
    ID: Union[Number, None] = Field(None)


class PatientUpdateMetaSource(RedoxAbstractModel):
    ID: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)


class PatientUpdateMetaTransmission(RedoxAbstractModel):
    ID: Union[Number, None] = Field(None)


class PatientUpdatePatient(RedoxAbstractModel):
    Allergies: List["PatientUpdatePatientAllergy"] = Field(None)
    Contacts: List["PatientUpdatePatientContact"] = Field(None)
    Demographics: "PatientUpdatePatientDemographics" = Field(None)
    Diagnoses: List["PatientUpdatePatientDiagnosis"] = Field(None)
    Guarantor: "PatientUpdatePatientGuarantor" = Field(None)
    Identifiers: List["PatientUpdatePatientIdentifier"] = Field(...)
    Insurances: List["PatientUpdatePatientInsurance"] = Field(None)
    Notes: List[str] = Field(None)
    PCP: "PatientUpdatePatientPCP" = Field(None)


class PatientUpdatePatientAllergy(RedoxAbstractModel):
    Code: Union[str, None] = Field(None)
    Codeset: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)
    OnsetDateTime: Union[str, None] = Field(None)
    Reaction: List["PatientUpdatePatientAllergyReaction"] = Field(None)
    Severity: "PatientUpdatePatientAllergySeverity" = Field(None)
    Status: Union[str, None] = Field(None)
    Type: "PatientUpdatePatientAllergyType" = Field(None)


class PatientUpdatePatientAllergyReaction(RedoxAbstractModel):
    Code: Union[str, None] = Field(None)
    Codeset: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)


class PatientUpdatePatientAllergySeverity(RedoxAbstractModel):
    Code: Union[str, None] = Field(None)
    Codeset: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)


class PatientUpdatePatientAllergyType(RedoxAbstractModel):
    Code: Union[str, None] = Field(None)
    Codeset: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)


class PatientUpdatePatientContact(RedoxAbstractModel):
    Address: "PatientUpdatePatientContactAddress" = Field(None)
    EmailAddresses: List[str] = Field(None)
    FirstName: Union[str, None] = Field(None)
    LastName: Union[str, None] = Field(None)
    MiddleName: Union[str, None] = Field(None)
    PhoneNumber: "PatientUpdatePatientContactPhoneNumber" = Field(None)
    RelationToPatient: Union[str, None] = Field(None)
    Roles: List[str] = Field(None)


class PatientUpdatePatientContactAddress(RedoxAbstractModel):
    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class PatientUpdatePatientContactPhoneNumber(RedoxAbstractModel):
    Home: Union[str, None] = Field(None)
    Mobile: Union[str, None] = Field(None)
    Office: Union[str, None] = Field(None)


class PatientUpdatePatientDemographics(RedoxAbstractModel):
    Address: "PatientUpdatePatientDemographicsAddress" = Field(None)
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
    PhoneNumber: "PatientUpdatePatientDemographicsPhoneNumber" = Field(None)
    Race: Union[str, None] = Field(None)
    Religion: Union[str, None] = Field(None)
    SSN: Union[str, None] = Field(None)
    Sex: Union[str, None] = Field(None)


class PatientUpdatePatientDemographicsAddress(RedoxAbstractModel):
    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class PatientUpdatePatientDemographicsPhoneNumber(RedoxAbstractModel):
    Home: Union[str, None] = Field(None)
    Mobile: Union[str, None] = Field(None)
    Office: Union[str, None] = Field(None)


class PatientUpdatePatientDiagnosis(RedoxAbstractModel):
    Code: Union[str, None] = Field(None)
    Codeset: Union[str, None] = Field(None)
    DocumentedDateTime: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


class PatientUpdatePatientGuarantor(RedoxAbstractModel):
    Address: "PatientUpdatePatientGuarantorAddress" = Field(None)
    DOB: Union[str, None] = Field(None)
    EmailAddresses: List[str] = Field(None)
    Employer: "PatientUpdatePatientGuarantorEmployer" = Field(None)
    FirstName: Union[str, None] = Field(None)
    LastName: Union[str, None] = Field(None)
    MiddleName: Union[str, None] = Field(None)
    Number: Union[str, None] = Field(None)
    PhoneNumber: "PatientUpdatePatientGuarantorPhoneNumber" = Field(None)
    RelationToPatient: Union[str, None] = Field(None)
    SSN: Union[str, None] = Field(None)
    Sex: Union[str, None] = Field(None)
    Spouse: "PatientUpdatePatientGuarantorSpouse" = Field(None)
    Type: Union[str, None] = Field(None)


class PatientUpdatePatientGuarantorAddress(RedoxAbstractModel):
    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class PatientUpdatePatientGuarantorEmployer(RedoxAbstractModel):
    Address: "PatientUpdatePatientGuarantorEmployerAddress" = Field(None)
    Name: Union[str, None] = Field(None)
    PhoneNumber: Union[str, None] = Field(None)


class PatientUpdatePatientGuarantorEmployerAddress(RedoxAbstractModel):
    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class PatientUpdatePatientGuarantorPhoneNumber(RedoxAbstractModel):
    Business: Union[str, None] = Field(None)
    Home: Union[str, None] = Field(None)
    Mobile: Union[str, None] = Field(None)


class PatientUpdatePatientGuarantorSpouse(RedoxAbstractModel):
    FirstName: Union[str, None] = Field(None)
    LastName: Union[str, None] = Field(None)


class PatientUpdatePatientIdentifier(RedoxAbstractModel):
    ID: str = Field(...)
    IDType: str = Field(...)


class PatientUpdatePatientInsurance(RedoxAbstractModel):
    AgreementType: Union[str, None] = Field(None)
    Company: "PatientUpdatePatientInsuranceCompany" = Field(None)
    CoverageType: Union[str, None] = Field(None)
    EffectiveDate: Union[str, None] = Field(None)
    ExpirationDate: Union[str, None] = Field(None)
    GroupName: Union[str, None] = Field(None)
    GroupNumber: Union[str, None] = Field(None)
    Insured: "PatientUpdatePatientInsuranceInsured" = Field(None)
    MemberNumber: Union[str, None] = Field(None)
    Plan: "PatientUpdatePatientInsurancePlan" = Field(None)
    PolicyNumber: Union[str, None] = Field(None)
    Priority: Union[str, None] = Field(None)


class PatientUpdatePatientInsuranceCompany(RedoxAbstractModel):
    Address: "PatientUpdatePatientInsuranceCompanyAddress" = Field(None)
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)
    PhoneNumber: Union[str, None] = Field(None)


class PatientUpdatePatientInsuranceCompanyAddress(RedoxAbstractModel):
    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class PatientUpdatePatientInsuranceInsured(RedoxAbstractModel):
    Address: "PatientUpdatePatientInsuranceInsuredAddress" = Field(None)
    DOB: Union[str, None] = Field(None)
    FirstName: Union[str, None] = Field(None)
    Identifiers: List["PatientUpdatePatientInsuranceInsuredIdentifier"] = Field(None)
    LastName: Union[str, None] = Field(None)
    MiddleName: Union[str, None] = Field(None)
    Relationship: Union[str, None] = Field(None)
    SSN: Union[str, None] = Field(None)
    Sex: Union[str, None] = Field(None)


class PatientUpdatePatientInsuranceInsuredAddress(RedoxAbstractModel):
    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class PatientUpdatePatientInsuranceInsuredIdentifier(RedoxAbstractModel):
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)


class PatientUpdatePatientInsurancePlan(RedoxAbstractModel):
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


class PatientUpdatePatientPCP(RedoxAbstractModel):
    Address: "PatientUpdatePatientPCPAddress" = Field(None)
    Credentials: List[str] = Field(None)
    EmailAddresses: List[str] = Field(None)
    FirstName: Union[str, None] = Field(None)
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)
    LastName: Union[str, None] = Field(None)
    Location: "PatientUpdatePatientPCPLocation" = Field(None)
    NPI: Union[str, None] = Field(None)
    PhoneNumber: "PatientUpdatePatientPCPPhoneNumber" = Field(None)


class PatientUpdatePatientPCPAddress(RedoxAbstractModel):
    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class PatientUpdatePatientPCPLocation(RedoxAbstractModel):
    Department: Union[str, None] = Field(None)
    DepartmentIdentifiers: List[
        "PatientUpdatePatientPCPLocationDepartmentIdentifier"
    ] = Field(None)
    Facility: Union[str, None] = Field(None)
    FacilityIdentifiers: List[
        "PatientUpdatePatientPCPLocationFacilityIdentifier"
    ] = Field(None)
    Room: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


class PatientUpdatePatientPCPLocationDepartmentIdentifier(RedoxAbstractModel):
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)


class PatientUpdatePatientPCPLocationFacilityIdentifier(RedoxAbstractModel):
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)


class PatientUpdatePatientPCPPhoneNumber(RedoxAbstractModel):
    Office: Union[str, None] = Field(None)


PatientUpdate.update_forward_refs()
PatientUpdateMeta.update_forward_refs()
PatientUpdatePatient.update_forward_refs()
PatientUpdatePatientAllergy.update_forward_refs()
PatientUpdatePatientContact.update_forward_refs()
PatientUpdatePatientDemographics.update_forward_refs()
PatientUpdatePatientGuarantor.update_forward_refs()
PatientUpdatePatientGuarantorEmployer.update_forward_refs()
PatientUpdatePatientInsurance.update_forward_refs()
PatientUpdatePatientInsuranceCompany.update_forward_refs()
PatientUpdatePatientInsuranceInsured.update_forward_refs()
PatientUpdatePatientPCP.update_forward_refs()
PatientUpdatePatientPCPLocation.update_forward_refs()
