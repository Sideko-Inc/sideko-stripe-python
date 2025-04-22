import pydantic
import typing
import typing_extensions

from .account_external_account_create_body_bank_account_obj0_documents_bank_account_ownership_verification import (
    AccountExternalAccountCreateBodyBankAccountObj0DocumentsBankAccountOwnershipVerification,
    _SerializerAccountExternalAccountCreateBodyBankAccountObj0DocumentsBankAccountOwnershipVerification,
)


class AccountExternalAccountCreateBodyBankAccountObj0Documents(
    typing_extensions.TypedDict
):
    """
    AccountExternalAccountCreateBodyBankAccountObj0Documents
    """

    bank_account_ownership_verification: typing_extensions.NotRequired[
        AccountExternalAccountCreateBodyBankAccountObj0DocumentsBankAccountOwnershipVerification
    ]


class _SerializerAccountExternalAccountCreateBodyBankAccountObj0Documents(
    pydantic.BaseModel
):
    """
    Serializer for AccountExternalAccountCreateBodyBankAccountObj0Documents handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    bank_account_ownership_verification: typing.Optional[
        _SerializerAccountExternalAccountCreateBodyBankAccountObj0DocumentsBankAccountOwnershipVerification
    ] = pydantic.Field(alias="bank_account_ownership_verification", default=None)
