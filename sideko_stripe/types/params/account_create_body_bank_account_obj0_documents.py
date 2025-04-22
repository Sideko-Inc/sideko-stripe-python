import pydantic
import typing
import typing_extensions

from .account_create_body_bank_account_obj0_documents_bank_account_ownership_verification import (
    AccountCreateBodyBankAccountObj0DocumentsBankAccountOwnershipVerification,
    _SerializerAccountCreateBodyBankAccountObj0DocumentsBankAccountOwnershipVerification,
)


class AccountCreateBodyBankAccountObj0Documents(typing_extensions.TypedDict):
    """
    AccountCreateBodyBankAccountObj0Documents
    """

    bank_account_ownership_verification: typing_extensions.NotRequired[
        AccountCreateBodyBankAccountObj0DocumentsBankAccountOwnershipVerification
    ]


class _SerializerAccountCreateBodyBankAccountObj0Documents(pydantic.BaseModel):
    """
    Serializer for AccountCreateBodyBankAccountObj0Documents handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    bank_account_ownership_verification: typing.Optional[
        _SerializerAccountCreateBodyBankAccountObj0DocumentsBankAccountOwnershipVerification
    ] = pydantic.Field(alias="bank_account_ownership_verification", default=None)
