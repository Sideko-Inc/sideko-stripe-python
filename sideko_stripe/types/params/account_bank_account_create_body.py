import pydantic
import typing
import typing_extensions

from .account_bank_account_create_body_bank_account_obj0 import (
    AccountBankAccountCreateBodyBankAccountObj0,
    _SerializerAccountBankAccountCreateBodyBankAccountObj0,
)
from .account_bank_account_create_body_metadata import (
    AccountBankAccountCreateBodyMetadata,
    _SerializerAccountBankAccountCreateBodyMetadata,
)


class AccountBankAccountCreateBody(typing_extensions.TypedDict, total=False):
    """
    AccountBankAccountCreateBody
    """

    bank_account: typing_extensions.NotRequired[
        typing.Union[AccountBankAccountCreateBodyBankAccountObj0, str]
    ]
    """
    Either a token, like the ones returned by [Stripe.js](https://stripe.com/docs/js), or a dictionary containing a user's bank account details.
    """

    default_for_currency: typing_extensions.NotRequired[bool]
    """
    When set to true, or if this is the first external account added in this currency, this account becomes the default external account for its currency.
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """

    external_account: typing_extensions.NotRequired[str]
    """
    A token, like the ones returned by [Stripe.js](https://stripe.com/docs/js) or a dictionary containing a user's external account details (with the options shown below). Please refer to full [documentation](https://stripe.com/docs/api/external_accounts) instead.
    """

    metadata: typing_extensions.NotRequired[AccountBankAccountCreateBodyMetadata]
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    """


class _SerializerAccountBankAccountCreateBody(pydantic.BaseModel):
    """
    Serializer for AccountBankAccountCreateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    bank_account: typing.Optional[
        typing.Union[_SerializerAccountBankAccountCreateBodyBankAccountObj0, str]
    ] = pydantic.Field(alias="bank_account", default=None)
    default_for_currency: typing.Optional[bool] = pydantic.Field(
        alias="default_for_currency", default=None
    )
    expand: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="expand", default=None
    )
    external_account: typing.Optional[str] = pydantic.Field(
        alias="external_account", default=None
    )
    metadata: typing.Optional[_SerializerAccountBankAccountCreateBodyMetadata] = (
        pydantic.Field(alias="metadata", default=None)
    )
