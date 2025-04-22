import pydantic
import typing
import typing_extensions

from .account_bank_account_create_body_bank_account_obj0_documents_bank_account_ownership_verification import (
    AccountBankAccountCreateBodyBankAccountObj0DocumentsBankAccountOwnershipVerification,
    _SerializerAccountBankAccountCreateBodyBankAccountObj0DocumentsBankAccountOwnershipVerification,
)


class AccountBankAccountCreateBodyBankAccountObj0Documents(typing_extensions.TypedDict):
    """
    AccountBankAccountCreateBodyBankAccountObj0Documents
    """

    bank_account_ownership_verification: typing_extensions.NotRequired[
        AccountBankAccountCreateBodyBankAccountObj0DocumentsBankAccountOwnershipVerification
    ]


class _SerializerAccountBankAccountCreateBodyBankAccountObj0Documents(
    pydantic.BaseModel
):
    """
    Serializer for AccountBankAccountCreateBodyBankAccountObj0Documents handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    bank_account_ownership_verification: typing.Optional[
        _SerializerAccountBankAccountCreateBodyBankAccountObj0DocumentsBankAccountOwnershipVerification
    ] = pydantic.Field(alias="bank_account_ownership_verification", default=None)
