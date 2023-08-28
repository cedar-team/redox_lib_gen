# -*- coding: utf-8 -*-
from typing import Optional


REDOX_DEV_DOCS_URL_BASE = "https://developer.redoxengine.com/data-models/"


class NameTranslationNotFoundError(ValueError):
    pass


def get_name_trans(name_stem: str, dir_stem: Optional[str] = None) -> str:
    try:
        return NAME_TRANSLATIONS[name_stem]
    except KeyError as err:
        page = ""
        if dir_trans := NAME_TRANSLATIONS.get(dir_stem):
            page = f"{dir_trans}.html"

        raise NameTranslationNotFoundError(
            f'Missing name translation for "{name_stem}"\nMost likely, an entry needs '
            f"to be added to the NAME_TRANSLATIONS dict.\nYou may find helpful "
            f"information here: {REDOX_DEV_DOCS_URL_BASE}{page}"
        ) from err


GENERIC_DIR_NAME = "generic"

# NAME_TRANSLATIONS is a mapping of the file names from the extracted specification
# archive to valid Python class names.

NAME_TRANSLATIONS = {
    "accountupdate": "AccountUpdate",
    "activate": "Activate",
    "administration": "Administration",
    "arrival": "Arrival",
    "authresponse": "AuthResponse",
    "authreview": "AuthReview",
    "availableslots": "AvailableSlots",
    "availableslotsresponse": "AvailableSlotsResponse",
    "booked": "Booked",
    "bookedresponse": "BookedResponse",
    "cancel": "Cancel",
    "censusquery": "CensusQuery",
    "censusqueryresponse": "CensusQueryResponse",
    "claim": "Claim",
    "clinicaldecisions": "ClinicalDecisions",
    "clinicalsummary": "ClinicalSummary",
    "deactivate": "Deactivate",
    "delete": "Delete",
    "deplete": "Deplete",
    "device": "Device",
    "discharge": "Discharge",
    "documentget": "DocumentGet",
    "documentgetresponse": "DocumentGetResponse",
    "documentquery": "DocumentQuery",
    "documentqueryresponse": "DocumentQueryResponse",
    "enrichment": "Enrichment",
    "financial": "Financial",
    "flowsheet": "Flowsheet",
    "groupedorders": "GroupedOrders",
    "inventory": "Inventory",
    "locationquery": "LocationQuery",
    "locationqueryresponse": "LocationQueryResponse",
    "media": "Media",
    "medications": "Medications",
    "modification": "Modification",
    "modify": "Modify",
    "naturallanguageprocessingquery": "NaturalLanguageProcessingQuery",
    "naturallanguageprocessingqueryresponse": "NaturalLanguageProcessingQueryResponse",
    "new": "New",
    "newpatient": "NewPatient",
    "newunsolicited": "NewUnsolicited",
    "normalizationquery": "NormalizationQuery",
    "normalizationqueryresponse": "NormalizationQueryResponse",
    "noshow": "NoShow",
    "notes": "Notes",
    "order": "Order",
    "organization": "Organization",
    "patientadmin": "PatientAdmin",
    "patienteducation": "PatientEducation",
    "patientmerge": "PatientMerge",
    "patientpush": "PatientPush",
    "patientquery": "PatientQuery",
    "patientqueryresponse": "PatientQueryResponse",
    "patientsearch": "PatientSearch",
    "patientupdate": "PatientUpdate",
    "payment": "Payment",
    "paymentbatch": "PaymentBatch",
    "preadmit": "PreAdmit",
    "provider": "Provider",
    "providerquery": "ProviderQuery",
    "providerqueryresponse": "ProviderQueryResponse",
    "pushslots": "PushSlots",
    "query": "Query",
    "queryresponse": "QueryResponse",
    "referral": "Referral",
    "registration": "Registration",
    "replace": "Replace",
    "request": "Request",
    "reschedule": "Reschedule",
    "research": "Research",
    "response": "Response",
    "results": "Results",
    "scheduling": "Scheduling",
    "sign-on": "SignOn",
    "sso": "SSO",
    "study": "Study",
    "subjectupdate": "SubjectUpdate",
    "submission": "Submission",
    "submissionbatch": "SubmissionBatch",
    "surgicalscheduling": "SurgicalScheduling",
    "transaction": "Transaction",
    "transfer": "Transfer",
    "update": "Update",
    "vaccination": "Vaccination",
    "visitmerge": "VisitMerge",
    "visitpush": "VisitPush",
    "visitquery": "VisitQuery",
    "visitqueryresponse": "VisitQueryResponse",
    "visitupdate": "VisitUpdate",
}
