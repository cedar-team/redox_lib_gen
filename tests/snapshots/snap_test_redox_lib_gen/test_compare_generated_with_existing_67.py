# -*- coding: utf-8 -*-
# ----  AUTO-GENERATED BY redox_lib_gen. DO NOT MODIFY MANUALLY!!  ---- #

from typing import List, Union

from pydantic import Field

from ..abstract_base import EventTypeAbstractModel, RedoxAbstractModel
from ..field_types import Number


class NewPatient(EventTypeAbstractModel):

    Meta: "NewPatientMeta" = Field(...)
    Patient: "NewPatientPatient" = Field(...)


class NewPatientMeta(RedoxAbstractModel):

    DataModel: str = Field(...)
    Destinations: List["NewPatientMetaDestination"] = Field(None)
    EventDateTime: Union[str, None] = Field(None)
    EventType: str = Field(...)
    FacilityCode: Union[str, None] = Field(None)
    Logs: List["NewPatientMetaLog"] = Field(None)
    Message: "NewPatientMetaMessage" = Field(None)
    Source: "NewPatientMetaSource" = Field(None)
    Test: Union[bool, None] = Field(None)
    Transmission: "NewPatientMetaTransmission" = Field(None)


class NewPatientMetaDestination(RedoxAbstractModel):

    ID: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)


class NewPatientMetaLog(RedoxAbstractModel):

    AttemptID: Union[str, None] = Field(None)
    ID: Union[str, None] = Field(None)


class NewPatientMetaMessage(RedoxAbstractModel):

    ID: Union[Number, None] = Field(None)


class NewPatientMetaSource(RedoxAbstractModel):

    ID: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)


class NewPatientMetaTransmission(RedoxAbstractModel):

    ID: Union[Number, None] = Field(None)


class NewPatientPatient(RedoxAbstractModel):

    Allergies: List["NewPatientPatientAllergy"] = Field(None)
    Contacts: List["NewPatientPatientContact"] = Field(None)
    Demographics: "NewPatientPatientDemographics" = Field(None)
    Guarantor: "NewPatientPatientGuarantor" = Field(None)
    Identifiers: List["NewPatientPatientIdentifier"] = Field(...)
    Insurances: List["NewPatientPatientInsurance"] = Field(None)
    Notes: List[str] = Field(None)
    PCP: "NewPatientPatientPCP" = Field(None)


class NewPatientPatientAllergy(RedoxAbstractModel):

    Code: Union[str, None] = Field(None)
    Codeset: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)
    OnsetDateTime: Union[str, None] = Field(None)
    Reaction: List["NewPatientPatientAllergyReaction"] = Field(None)
    Severity: "NewPatientPatientAllergySeverity" = Field(None)
    Status: Union[str, None] = Field(None)
    Type: "NewPatientPatientAllergyType" = Field(None)


class NewPatientPatientAllergyReaction(RedoxAbstractModel):

    Code: Union[str, None] = Field(None)
    Codeset: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)


class NewPatientPatientAllergySeverity(RedoxAbstractModel):

    Code: Union[str, None] = Field(None)
    Codeset: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)


class NewPatientPatientAllergyType(RedoxAbstractModel):

    Code: Union[str, None] = Field(None)
    Codeset: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)


class NewPatientPatientContact(RedoxAbstractModel):

    Address: "NewPatientPatientContactAddress" = Field(None)
    EmailAddresses: List[str] = Field(None)
    FirstName: Union[str, None] = Field(None)
    LastName: Union[str, None] = Field(None)
    MiddleName: Union[str, None] = Field(None)
    PhoneNumber: "NewPatientPatientContactPhoneNumber" = Field(None)
    RelationToPatient: Union[str, None] = Field(None)
    Roles: List[str] = Field(None)


class NewPatientPatientContactAddress(RedoxAbstractModel):

    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class NewPatientPatientContactPhoneNumber(RedoxAbstractModel):

    Home: Union[str, None] = Field(None)
    Mobile: Union[str, None] = Field(None)
    Office: Union[str, None] = Field(None)


class NewPatientPatientDemographics(RedoxAbstractModel):

    Address: "NewPatientPatientDemographicsAddress" = Field(None)
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
    PhoneNumber: "NewPatientPatientDemographicsPhoneNumber" = Field(None)
    Race: Union[str, None] = Field(None)
    Religion: Union[str, None] = Field(None)
    Sex: Union[str, None] = Field(None)
    SSN: Union[str, None] = Field(None)


class NewPatientPatientDemographicsAddress(RedoxAbstractModel):

    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class NewPatientPatientDemographicsPhoneNumber(RedoxAbstractModel):

    Home: Union[str, None] = Field(None)
    Mobile: Union[str, None] = Field(None)
    Office: Union[str, None] = Field(None)


class NewPatientPatientGuarantor(RedoxAbstractModel):

    Address: "NewPatientPatientGuarantorAddress" = Field(None)
    DOB: Union[str, None] = Field(None)
    EmailAddresses: List[str] = Field(None)
    Employer: "NewPatientPatientGuarantorEmployer" = Field(None)
    FirstName: Union[str, None] = Field(None)
    LastName: Union[str, None] = Field(None)
    MiddleName: Union[str, None] = Field(None)
    Number: Union[str, None] = Field(None)
    PhoneNumber: "NewPatientPatientGuarantorPhoneNumber" = Field(None)
    RelationToPatient: Union[str, None] = Field(None)
    Sex: Union[str, None] = Field(None)
    Spouse: "NewPatientPatientGuarantorSpouse" = Field(None)
    SSN: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


class NewPatientPatientGuarantorAddress(RedoxAbstractModel):

    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class NewPatientPatientGuarantorEmployer(RedoxAbstractModel):

    Address: "NewPatientPatientGuarantorEmployerAddress" = Field(None)
    Name: Union[str, None] = Field(None)
    PhoneNumber: Union[str, None] = Field(None)


class NewPatientPatientGuarantorEmployerAddress(RedoxAbstractModel):

    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class NewPatientPatientGuarantorPhoneNumber(RedoxAbstractModel):

    Business: Union[str, None] = Field(None)
    Home: Union[str, None] = Field(None)
    Mobile: Union[str, None] = Field(None)


class NewPatientPatientGuarantorSpouse(RedoxAbstractModel):

    FirstName: Union[str, None] = Field(None)
    LastName: Union[str, None] = Field(None)


class NewPatientPatientIdentifier(RedoxAbstractModel):

    ID: str = Field(...)
    IDType: str = Field(...)


class NewPatientPatientInsurance(RedoxAbstractModel):

    AgreementType: Union[str, None] = Field(None)
    Company: "NewPatientPatientInsuranceCompany" = Field(None)
    CoverageType: Union[str, None] = Field(None)
    EffectiveDate: Union[str, None] = Field(None)
    ExpirationDate: Union[str, None] = Field(None)
    GroupName: Union[str, None] = Field(None)
    GroupNumber: Union[str, None] = Field(None)
    Insured: "NewPatientPatientInsuranceInsured" = Field(None)
    MemberNumber: Union[str, None] = Field(None)
    Plan: "NewPatientPatientInsurancePlan" = Field(None)
    PolicyNumber: Union[str, None] = Field(None)
    Priority: Union[str, None] = Field(None)


class NewPatientPatientInsuranceCompany(RedoxAbstractModel):

    Address: "NewPatientPatientInsuranceCompanyAddress" = Field(None)
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)
    PhoneNumber: Union[str, None] = Field(None)


class NewPatientPatientInsuranceCompanyAddress(RedoxAbstractModel):

    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class NewPatientPatientInsuranceInsured(RedoxAbstractModel):

    Address: "NewPatientPatientInsuranceInsuredAddress" = Field(None)
    DOB: Union[str, None] = Field(None)
    FirstName: Union[str, None] = Field(None)
    Identifiers: List["NewPatientPatientInsuranceInsuredIdentifier"] = Field(None)
    LastName: Union[str, None] = Field(None)
    MiddleName: Union[str, None] = Field(None)
    Relationship: Union[str, None] = Field(None)
    Sex: Union[str, None] = Field(None)
    SSN: Union[str, None] = Field(None)


class NewPatientPatientInsuranceInsuredAddress(RedoxAbstractModel):

    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class NewPatientPatientInsuranceInsuredIdentifier(RedoxAbstractModel):

    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)


class NewPatientPatientInsurancePlan(RedoxAbstractModel):

    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


class NewPatientPatientPCP(RedoxAbstractModel):

    Address: "NewPatientPatientPCPAddress" = Field(None)
    Credentials: List[str] = Field(None)
    EmailAddresses: List[str] = Field(None)
    FirstName: Union[str, None] = Field(None)
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)
    LastName: Union[str, None] = Field(None)
    Location: "NewPatientPatientPCPLocation" = Field(None)
    NPI: Union[str, None] = Field(None)
    PhoneNumber: "NewPatientPatientPCPPhoneNumber" = Field(None)


class NewPatientPatientPCPAddress(RedoxAbstractModel):

    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class NewPatientPatientPCPLocation(RedoxAbstractModel):

    Department: Union[str, None] = Field(None)
    Facility: Union[str, None] = Field(None)
    Room: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


class NewPatientPatientPCPPhoneNumber(RedoxAbstractModel):

    Office: Union[str, None] = Field(None)


NewPatient.update_forward_refs()
NewPatientMeta.update_forward_refs()
NewPatientPatient.update_forward_refs()
NewPatientPatientAllergy.update_forward_refs()
NewPatientPatientContact.update_forward_refs()
NewPatientPatientDemographics.update_forward_refs()
NewPatientPatientGuarantor.update_forward_refs()
NewPatientPatientGuarantorEmployer.update_forward_refs()
NewPatientPatientInsurance.update_forward_refs()
NewPatientPatientInsuranceCompany.update_forward_refs()
NewPatientPatientInsuranceInsured.update_forward_refs()
NewPatientPatientPCP.update_forward_refs()
