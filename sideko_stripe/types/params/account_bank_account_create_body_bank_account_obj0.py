import pydantic
import typing
import typing_extensions

from .account_bank_account_create_body_bank_account_obj0_documents import (
    AccountBankAccountCreateBodyBankAccountObj0Documents,
    _SerializerAccountBankAccountCreateBodyBankAccountObj0Documents,
)


class AccountBankAccountCreateBodyBankAccountObj0(typing_extensions.TypedDict):
    """
    AccountBankAccountCreateBodyBankAccountObj0
    """

    account_holder_name: typing_extensions.NotRequired[str]

    account_holder_type: typing_extensions.NotRequired[
        typing_extensions.Literal["company", "individual"]
    ]

    account_number: typing_extensions.Required[str]

    account_type: typing_extensions.NotRequired[
        typing_extensions.Literal["checking", "futsu", "savings", "toza"]
    ]

    country: typing_extensions.Required[str]

    currency: typing_extensions.NotRequired[str]

    documents: typing_extensions.NotRequired[
        AccountBankAccountCreateBodyBankAccountObj0Documents
    ]

    object: typing_extensions.NotRequired[typing_extensions.Literal["bank_account"]]

    routing_number: typing_extensions.NotRequired[str]


class _SerializerAccountBankAccountCreateBodyBankAccountObj0(pydantic.BaseModel):
    """
    Serializer for AccountBankAccountCreateBodyBankAccountObj0 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    account_holder_name: typing.Optional[str] = pydantic.Field(
        alias="account_holder_name", default=None
    )
    account_holder_type: typing.Optional[
        typing_extensions.Literal["company", "individual"]
    ] = pydantic.Field(alias="account_holder_type", default=None)
    account_number: str = pydantic.Field(
        alias="account_number",
    )
    account_type: typing.Optional[
        typing_extensions.Literal["checking", "futsu", "savings", "toza"]
    ] = pydantic.Field(alias="account_type", default=None)
    country: str = pydantic.Field(
        alias="country",
    )
    currency: typing.Optional[str] = pydantic.Field(alias="currency", default=None)
    documents: typing.Optional[
        _SerializerAccountBankAccountCreateBodyBankAccountObj0Documents
    ] = pydantic.Field(alias="documents", default=None)
    object: typing.Optional[typing_extensions.Literal["bank_account"]] = pydantic.Field(
        alias="object", default=None
    )
    routing_number: typing.Optional[str] = pydantic.Field(
        alias="routing_number", default=None
    )
