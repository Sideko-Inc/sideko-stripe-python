import pydantic
import typing
import typing_extensions

from .account_create_body_documents_bank_account_ownership_verification import (
    AccountCreateBodyDocumentsBankAccountOwnershipVerification,
    _SerializerAccountCreateBodyDocumentsBankAccountOwnershipVerification,
)
from .account_create_body_documents_company_license import (
    AccountCreateBodyDocumentsCompanyLicense,
    _SerializerAccountCreateBodyDocumentsCompanyLicense,
)
from .account_create_body_documents_company_memorandum_of_association import (
    AccountCreateBodyDocumentsCompanyMemorandumOfAssociation,
    _SerializerAccountCreateBodyDocumentsCompanyMemorandumOfAssociation,
)
from .account_create_body_documents_company_ministerial_decree import (
    AccountCreateBodyDocumentsCompanyMinisterialDecree,
    _SerializerAccountCreateBodyDocumentsCompanyMinisterialDecree,
)
from .account_create_body_documents_company_registration_verification import (
    AccountCreateBodyDocumentsCompanyRegistrationVerification,
    _SerializerAccountCreateBodyDocumentsCompanyRegistrationVerification,
)
from .account_create_body_documents_company_tax_id_verification import (
    AccountCreateBodyDocumentsCompanyTaxIdVerification,
    _SerializerAccountCreateBodyDocumentsCompanyTaxIdVerification,
)
from .account_create_body_documents_proof_of_registration import (
    AccountCreateBodyDocumentsProofOfRegistration,
    _SerializerAccountCreateBodyDocumentsProofOfRegistration,
)
from .account_create_body_documents_proof_of_ultimate_beneficial_ownership import (
    AccountCreateBodyDocumentsProofOfUltimateBeneficialOwnership,
    _SerializerAccountCreateBodyDocumentsProofOfUltimateBeneficialOwnership,
)


class AccountCreateBodyDocuments(typing_extensions.TypedDict):
    """
    Documents that may be submitted to satisfy various informational requests.
    """

    bank_account_ownership_verification: typing_extensions.NotRequired[
        AccountCreateBodyDocumentsBankAccountOwnershipVerification
    ]

    company_license: typing_extensions.NotRequired[
        AccountCreateBodyDocumentsCompanyLicense
    ]

    company_memorandum_of_association: typing_extensions.NotRequired[
        AccountCreateBodyDocumentsCompanyMemorandumOfAssociation
    ]

    company_ministerial_decree: typing_extensions.NotRequired[
        AccountCreateBodyDocumentsCompanyMinisterialDecree
    ]

    company_registration_verification: typing_extensions.NotRequired[
        AccountCreateBodyDocumentsCompanyRegistrationVerification
    ]

    company_tax_id_verification: typing_extensions.NotRequired[
        AccountCreateBodyDocumentsCompanyTaxIdVerification
    ]

    proof_of_registration: typing_extensions.NotRequired[
        AccountCreateBodyDocumentsProofOfRegistration
    ]

    proof_of_ultimate_beneficial_ownership: typing_extensions.NotRequired[
        AccountCreateBodyDocumentsProofOfUltimateBeneficialOwnership
    ]


class _SerializerAccountCreateBodyDocuments(pydantic.BaseModel):
    """
    Serializer for AccountCreateBodyDocuments handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    bank_account_ownership_verification: typing.Optional[
        _SerializerAccountCreateBodyDocumentsBankAccountOwnershipVerification
    ] = pydantic.Field(alias="bank_account_ownership_verification", default=None)
    company_license: typing.Optional[
        _SerializerAccountCreateBodyDocumentsCompanyLicense
    ] = pydantic.Field(alias="company_license", default=None)
    company_memorandum_of_association: typing.Optional[
        _SerializerAccountCreateBodyDocumentsCompanyMemorandumOfAssociation
    ] = pydantic.Field(alias="company_memorandum_of_association", default=None)
    company_ministerial_decree: typing.Optional[
        _SerializerAccountCreateBodyDocumentsCompanyMinisterialDecree
    ] = pydantic.Field(alias="company_ministerial_decree", default=None)
    company_registration_verification: typing.Optional[
        _SerializerAccountCreateBodyDocumentsCompanyRegistrationVerification
    ] = pydantic.Field(alias="company_registration_verification", default=None)
    company_tax_id_verification: typing.Optional[
        _SerializerAccountCreateBodyDocumentsCompanyTaxIdVerification
    ] = pydantic.Field(alias="company_tax_id_verification", default=None)
    proof_of_registration: typing.Optional[
        _SerializerAccountCreateBodyDocumentsProofOfRegistration
    ] = pydantic.Field(alias="proof_of_registration", default=None)
    proof_of_ultimate_beneficial_ownership: typing.Optional[
        _SerializerAccountCreateBodyDocumentsProofOfUltimateBeneficialOwnership
    ] = pydantic.Field(alias="proof_of_ultimate_beneficial_ownership", default=None)
