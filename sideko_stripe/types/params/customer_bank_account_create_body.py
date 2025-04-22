import pydantic
import typing
import typing_extensions

from .customer_bank_account_create_body_bank_account_obj0 import (
    CustomerBankAccountCreateBodyBankAccountObj0,
    _SerializerCustomerBankAccountCreateBodyBankAccountObj0,
)
from .customer_bank_account_create_body_card_obj0 import (
    CustomerBankAccountCreateBodyCardObj0,
    _SerializerCustomerBankAccountCreateBodyCardObj0,
)
from .customer_bank_account_create_body_metadata import (
    CustomerBankAccountCreateBodyMetadata,
    _SerializerCustomerBankAccountCreateBodyMetadata,
)


class CustomerBankAccountCreateBody(typing_extensions.TypedDict, total=False):
    """
    CustomerBankAccountCreateBody
    """

    alipay_account: typing_extensions.NotRequired[str]
    """
    A token returned by [Stripe.js](https://stripe.com/docs/js) representing the user’s Alipay account details.
    """

    bank_account: typing_extensions.NotRequired[
        typing.Union[CustomerBankAccountCreateBodyBankAccountObj0, str]
    ]
    """
    Either a token, like the ones returned by [Stripe.js](https://stripe.com/docs/js), or a dictionary containing a user's bank account details.
    """

    card: typing_extensions.NotRequired[
        typing.Union[CustomerBankAccountCreateBodyCardObj0, str]
    ]
    """
    A token, like the ones returned by [Stripe.js](https://stripe.com/docs/js).
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """

    metadata: typing_extensions.NotRequired[CustomerBankAccountCreateBodyMetadata]
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    """

    source: typing_extensions.NotRequired[str]
    """
    Please refer to full [documentation](https://stripe.com/docs/api) instead.
    """


class _SerializerCustomerBankAccountCreateBody(pydantic.BaseModel):
    """
    Serializer for CustomerBankAccountCreateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    alipay_account: typing.Optional[str] = pydantic.Field(
        alias="alipay_account", default=None
    )
    bank_account: typing.Optional[
        typing.Union[_SerializerCustomerBankAccountCreateBodyBankAccountObj0, str]
    ] = pydantic.Field(alias="bank_account", default=None)
    card: typing.Optional[
        typing.Union[_SerializerCustomerBankAccountCreateBodyCardObj0, str]
    ] = pydantic.Field(alias="card", default=None)
    expand: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="expand", default=None
    )
    metadata: typing.Optional[_SerializerCustomerBankAccountCreateBodyMetadata] = (
        pydantic.Field(alias="metadata", default=None)
    )
    source: typing.Optional[str] = pydantic.Field(alias="source", default=None)
