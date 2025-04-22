import pydantic
import typing
import typing_extensions

from .account_external_account_update_body_documents_bank_account_ownership_verification import (
    AccountExternalAccountUpdateBodyDocumentsBankAccountOwnershipVerification,
    _SerializerAccountExternalAccountUpdateBodyDocumentsBankAccountOwnershipVerification,
)


class AccountExternalAccountUpdateBodyDocuments(typing_extensions.TypedDict):
    """
    Documents that may be submitted to satisfy various informational requests.
    """

    bank_account_ownership_verification: typing_extensions.NotRequired[
        AccountExternalAccountUpdateBodyDocumentsBankAccountOwnershipVerification
    ]


class _SerializerAccountExternalAccountUpdateBodyDocuments(pydantic.BaseModel):
    """
    Serializer for AccountExternalAccountUpdateBodyDocuments handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    bank_account_ownership_verification: typing.Optional[
        _SerializerAccountExternalAccountUpdateBodyDocumentsBankAccountOwnershipVerification
    ] = pydantic.Field(alias="bank_account_ownership_verification", default=None)
