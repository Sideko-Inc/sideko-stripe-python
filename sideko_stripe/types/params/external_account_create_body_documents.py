import pydantic
import typing
import typing_extensions

from .external_account_create_body_documents_bank_account_ownership_verification import (
    ExternalAccountCreateBodyDocumentsBankAccountOwnershipVerification,
    _SerializerExternalAccountCreateBodyDocumentsBankAccountOwnershipVerification,
)


class ExternalAccountCreateBodyDocuments(typing_extensions.TypedDict):
    """
    Documents that may be submitted to satisfy various informational requests.
    """

    bank_account_ownership_verification: typing_extensions.NotRequired[
        ExternalAccountCreateBodyDocumentsBankAccountOwnershipVerification
    ]


class _SerializerExternalAccountCreateBodyDocuments(pydantic.BaseModel):
    """
    Serializer for ExternalAccountCreateBodyDocuments handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    bank_account_ownership_verification: typing.Optional[
        _SerializerExternalAccountCreateBodyDocumentsBankAccountOwnershipVerification
    ] = pydantic.Field(alias="bank_account_ownership_verification", default=None)
