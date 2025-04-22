import pydantic
import typing
import typing_extensions

from .account_update_body_documents_bank_account_ownership_verification import (
    AccountUpdateBodyDocumentsBankAccountOwnershipVerification,
    _SerializerAccountUpdateBodyDocumentsBankAccountOwnershipVerification,
)
from .account_update_body_documents_company_license import (
    AccountUpdateBodyDocumentsCompanyLicense,
    _SerializerAccountUpdateBodyDocumentsCompanyLicense,
)
from .account_update_body_documents_company_memorandum_of_association import (
    AccountUpdateBodyDocumentsCompanyMemorandumOfAssociation,
    _SerializerAccountUpdateBodyDocumentsCompanyMemorandumOfAssociation,
)
from .account_update_body_documents_company_ministerial_decree import (
    AccountUpdateBodyDocumentsCompanyMinisterialDecree,
    _SerializerAccountUpdateBodyDocumentsCompanyMinisterialDecree,
)
from .account_update_body_documents_company_registration_verification import (
    AccountUpdateBodyDocumentsCompanyRegistrationVerification,
    _SerializerAccountUpdateBodyDocumentsCompanyRegistrationVerification,
)
from .account_update_body_documents_company_tax_id_verification import (
    AccountUpdateBodyDocumentsCompanyTaxIdVerification,
    _SerializerAccountUpdateBodyDocumentsCompanyTaxIdVerification,
)
from .account_update_body_documents_proof_of_registration import (
    AccountUpdateBodyDocumentsProofOfRegistration,
    _SerializerAccountUpdateBodyDocumentsProofOfRegistration,
)
from .account_update_body_documents_proof_of_ultimate_beneficial_ownership import (
    AccountUpdateBodyDocumentsProofOfUltimateBeneficialOwnership,
    _SerializerAccountUpdateBodyDocumentsProofOfUltimateBeneficialOwnership,
)


class AccountUpdateBodyDocuments(typing_extensions.TypedDict):
    """
    Documents that may be submitted to satisfy various informational requests.
    """

    bank_account_ownership_verification: typing_extensions.NotRequired[
        AccountUpdateBodyDocumentsBankAccountOwnershipVerification
    ]

    company_license: typing_extensions.NotRequired[
        AccountUpdateBodyDocumentsCompanyLicense
    ]

    company_memorandum_of_association: typing_extensions.NotRequired[
        AccountUpdateBodyDocumentsCompanyMemorandumOfAssociation
    ]

    company_ministerial_decree: typing_extensions.NotRequired[
        AccountUpdateBodyDocumentsCompanyMinisterialDecree
    ]

    company_registration_verification: typing_extensions.NotRequired[
        AccountUpdateBodyDocumentsCompanyRegistrationVerification
    ]

    company_tax_id_verification: typing_extensions.NotRequired[
        AccountUpdateBodyDocumentsCompanyTaxIdVerification
    ]

    proof_of_registration: typing_extensions.NotRequired[
        AccountUpdateBodyDocumentsProofOfRegistration
    ]

    proof_of_ultimate_beneficial_ownership: typing_extensions.NotRequired[
        AccountUpdateBodyDocumentsProofOfUltimateBeneficialOwnership
    ]


class _SerializerAccountUpdateBodyDocuments(pydantic.BaseModel):
    """
    Serializer for AccountUpdateBodyDocuments handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    bank_account_ownership_verification: typing.Optional[
        _SerializerAccountUpdateBodyDocumentsBankAccountOwnershipVerification
    ] = pydantic.Field(alias="bank_account_ownership_verification", default=None)
    company_license: typing.Optional[
        _SerializerAccountUpdateBodyDocumentsCompanyLicense
    ] = pydantic.Field(alias="company_license", default=None)
    company_memorandum_of_association: typing.Optional[
        _SerializerAccountUpdateBodyDocumentsCompanyMemorandumOfAssociation
    ] = pydantic.Field(alias="company_memorandum_of_association", default=None)
    company_ministerial_decree: typing.Optional[
        _SerializerAccountUpdateBodyDocumentsCompanyMinisterialDecree
    ] = pydantic.Field(alias="company_ministerial_decree", default=None)
    company_registration_verification: typing.Optional[
        _SerializerAccountUpdateBodyDocumentsCompanyRegistrationVerification
    ] = pydantic.Field(alias="company_registration_verification", default=None)
    company_tax_id_verification: typing.Optional[
        _SerializerAccountUpdateBodyDocumentsCompanyTaxIdVerification
    ] = pydantic.Field(alias="company_tax_id_verification", default=None)
    proof_of_registration: typing.Optional[
        _SerializerAccountUpdateBodyDocumentsProofOfRegistration
    ] = pydantic.Field(alias="proof_of_registration", default=None)
    proof_of_ultimate_beneficial_ownership: typing.Optional[
        _SerializerAccountUpdateBodyDocumentsProofOfUltimateBeneficialOwnership
    ] = pydantic.Field(alias="proof_of_ultimate_beneficial_ownership", default=None)
