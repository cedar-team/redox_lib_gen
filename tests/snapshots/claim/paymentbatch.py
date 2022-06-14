# -*- coding: utf-8 -*-
# ----  AUTO-GENERATED BY redox_lib_gen. DO NOT MODIFY MANUALLY!!  ---- #

from typing import List, Union

from pydantic import Field

from ..abstract_base import EventTypeAbstractModel, RedoxAbstractModel
from ..field_types import Number


class PaymentBatch(EventTypeAbstractModel):

    Meta: "PaymentBatchMeta" = Field(...)
    Transactions: List["PaymentBatchTransaction"] = Field(None)


class PaymentBatchMeta(RedoxAbstractModel):

    DataModel: str = Field(...)
    Destinations: List["PaymentBatchMetaDestination"] = Field(None)
    EventDateTime: Union[str, None] = Field(None)
    EventType: str = Field(...)
    FacilityCode: Union[str, None] = Field(None)
    Logs: List["PaymentBatchMetaLog"] = Field(None)
    Message: "PaymentBatchMetaMessage" = Field(None)
    Source: "PaymentBatchMetaSource" = Field(None)
    Test: Union[bool, None] = Field(None)
    Transmission: "PaymentBatchMetaTransmission" = Field(None)


class PaymentBatchMetaDestination(RedoxAbstractModel):

    ID: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)


class PaymentBatchMetaLog(RedoxAbstractModel):

    AttemptID: Union[str, None] = Field(None)
    ID: Union[str, None] = Field(None)


class PaymentBatchMetaMessage(RedoxAbstractModel):

    ID: Union[Number, None] = Field(None)


class PaymentBatchMetaSource(RedoxAbstractModel):

    ID: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)


class PaymentBatchMetaTransmission(RedoxAbstractModel):

    ID: Union[Number, None] = Field(None)


class PaymentBatchTransaction(RedoxAbstractModel):

    CreditOrDebit: Union[str, None] = Field(None)
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)
    PaymentDateTime: Union[str, None] = Field(None)
    PaymentMethod: Union[str, None] = Field(None)
    Payments: List["PaymentBatchTransactionPayment"] = Field(None)
    Receiver: "PaymentBatchTransactionReceiver" = Field(None)
    Submitter: "PaymentBatchTransactionSubmitter" = Field(None)
    TotalPaymentAmount: Union[str, None] = Field(None)
    TrackingNumber: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


class PaymentBatchTransactionPayment(RedoxAbstractModel):

    Claims: List["PaymentBatchTransactionPaymentClaim"] = Field(None)
    DateTime: Union[str, None] = Field(None)
    Patient: "PaymentBatchTransactionPaymentPatient" = Field(None)


class PaymentBatchTransactionPaymentClaim(RedoxAbstractModel):

    Adjustments: List["PaymentBatchTransactionPaymentClaimAdjustment"] = Field(None)
    ChargedAmount: Union[str, None] = Field(None)
    ControlNumber: Union[str, None] = Field(None)
    EndDateTime: Union[str, None] = Field(None)
    PatientResponsibilityAmount: Union[str, None] = Field(None)
    PaymentAmount: Union[str, None] = Field(None)
    ReceivedDate: Union[str, None] = Field(None)
    ReferenceNumbers: List[
        "PaymentBatchTransactionPaymentClaimReferenceNumber"
    ] = Field(None)
    Services: List["PaymentBatchTransactionPaymentClaimService"] = Field(None)
    StartDateTime: Union[str, None] = Field(None)
    Status: Union[str, None] = Field(None)
    SubmissionNumber: Union[str, None] = Field(None)


class PaymentBatchTransactionPaymentClaimAdjustment(RedoxAbstractModel):

    Amount: Union[str, None] = Field(None)
    Quantity: Union[str, None] = Field(None)
    Reason: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


class PaymentBatchTransactionPaymentClaimReferenceNumber(RedoxAbstractModel):

    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)


class PaymentBatchTransactionPaymentClaimService(RedoxAbstractModel):

    AdjudicatedService: "PaymentBatchTransactionPaymentClaimServiceAdjudicatedService" = Field(
        None
    )
    Adjustments: List["PaymentBatchTransactionPaymentClaimServiceAdjustment"] = Field(
        None
    )
    AllowedAmount: Union[str, None] = Field(None)
    ChargedAmount: Union[str, None] = Field(None)
    ChargedUnits: Union[str, None] = Field(None)
    EndDateTime: Union[str, None] = Field(None)
    PaymentAmount: Union[str, None] = Field(None)
    PaymentUnits: Union[str, None] = Field(None)
    ReferenceNumbers: List[
        "PaymentBatchTransactionPaymentClaimServiceReferenceNumber"
    ] = Field(None)
    StartDateTime: Union[str, None] = Field(None)
    SubmittedService: "PaymentBatchTransactionPaymentClaimServiceSubmittedService" = (
        Field(None)
    )


class PaymentBatchTransactionPaymentClaimServiceAdjudicatedService(RedoxAbstractModel):

    Code: Union[str, None] = Field(None)
    Codeset: Union[str, None] = Field(None)
    Description: Union[str, None] = Field(None)
    Modifiers: List[str] = Field(None)


class PaymentBatchTransactionPaymentClaimServiceAdjustment(RedoxAbstractModel):

    Amount: Union[str, None] = Field(None)
    Quantity: Union[str, None] = Field(None)
    Reason: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


class PaymentBatchTransactionPaymentClaimServiceReferenceNumber(RedoxAbstractModel):

    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)


class PaymentBatchTransactionPaymentClaimServiceSubmittedService(RedoxAbstractModel):

    Code: Union[str, None] = Field(None)
    Codeset: Union[str, None] = Field(None)
    Description: Union[str, None] = Field(None)
    Modifiers: List[str] = Field(None)


class PaymentBatchTransactionPaymentPatient(RedoxAbstractModel):

    Demographics: "PaymentBatchTransactionPaymentPatientDemographics" = Field(None)
    Identifiers: List["PaymentBatchTransactionPaymentPatientIdentifier"] = Field(None)
    Notes: List[str] = Field(None)


class PaymentBatchTransactionPaymentPatientDemographics(RedoxAbstractModel):

    Address: "PaymentBatchTransactionPaymentPatientDemographicsAddress" = Field(None)
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
    PhoneNumber: "PaymentBatchTransactionPaymentPatientDemographicsPhoneNumber" = Field(
        None
    )
    Race: Union[str, None] = Field(None)
    Religion: Union[str, None] = Field(None)
    SSN: Union[str, None] = Field(None)
    Sex: Union[str, None] = Field(None)


class PaymentBatchTransactionPaymentPatientDemographicsAddress(RedoxAbstractModel):

    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class PaymentBatchTransactionPaymentPatientDemographicsPhoneNumber(RedoxAbstractModel):

    Home: Union[str, None] = Field(None)
    Mobile: Union[str, None] = Field(None)
    Office: Union[str, None] = Field(None)


class PaymentBatchTransactionPaymentPatientIdentifier(RedoxAbstractModel):

    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)


class PaymentBatchTransactionReceiver(RedoxAbstractModel):

    Address: "PaymentBatchTransactionReceiverAddress" = Field(None)
    EmailAddress: Union[str, None] = Field(None)
    Identifiers: List["PaymentBatchTransactionReceiverIdentifier"] = Field(None)
    Name: Union[str, None] = Field(None)
    PhoneNumber: "PaymentBatchTransactionReceiverPhoneNumber" = Field(None)


class PaymentBatchTransactionReceiverAddress(RedoxAbstractModel):

    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class PaymentBatchTransactionReceiverIdentifier(RedoxAbstractModel):

    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)


class PaymentBatchTransactionReceiverPhoneNumber(RedoxAbstractModel):

    Fax: Union[str, None] = Field(None)
    Office: Union[str, None] = Field(None)


class PaymentBatchTransactionSubmitter(RedoxAbstractModel):

    Address: "PaymentBatchTransactionSubmitterAddress" = Field(None)
    EmailAddress: Union[str, None] = Field(None)
    Identifiers: List["PaymentBatchTransactionSubmitterIdentifier"] = Field(None)
    Name: Union[str, None] = Field(None)
    PhoneNumber: "PaymentBatchTransactionSubmitterPhoneNumber" = Field(None)


class PaymentBatchTransactionSubmitterAddress(RedoxAbstractModel):

    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class PaymentBatchTransactionSubmitterIdentifier(RedoxAbstractModel):

    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)


class PaymentBatchTransactionSubmitterPhoneNumber(RedoxAbstractModel):

    Fax: Union[str, None] = Field(None)
    Office: Union[str, None] = Field(None)


PaymentBatch.update_forward_refs()
PaymentBatchMeta.update_forward_refs()
PaymentBatchTransaction.update_forward_refs()
PaymentBatchTransactionPayment.update_forward_refs()
PaymentBatchTransactionPaymentClaim.update_forward_refs()
PaymentBatchTransactionPaymentClaimService.update_forward_refs()
PaymentBatchTransactionPaymentPatient.update_forward_refs()
PaymentBatchTransactionPaymentPatientDemographics.update_forward_refs()
PaymentBatchTransactionReceiver.update_forward_refs()
PaymentBatchTransactionSubmitter.update_forward_refs()
