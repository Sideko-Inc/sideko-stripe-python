import pydantic
import typing
import typing_extensions

from .customer_source_create_body_bank_account_obj0 import (
    CustomerSourceCreateBodyBankAccountObj0,
    _SerializerCustomerSourceCreateBodyBankAccountObj0,
)
from .customer_source_create_body_card_obj0 import (
    CustomerSourceCreateBodyCardObj0,
    _SerializerCustomerSourceCreateBodyCardObj0,
)
from .customer_source_create_body_metadata import (
    CustomerSourceCreateBodyMetadata,
    _SerializerCustomerSourceCreateBodyMetadata,
)


class CustomerSourceCreateBody(typing_extensions.TypedDict, total=False):
    """
    CustomerSourceCreateBody
    """

    alipay_account: typing_extensions.NotRequired[str]
    """
    A token returned by [Stripe.js](https://stripe.com/docs/js) representing the user’s Alipay account details.
    """

    bank_account: typing_extensions.NotRequired[
        typing.Union[CustomerSourceCreateBodyBankAccountObj0, str]
    ]
    """
    Either a token, like the ones returned by [Stripe.js](https://stripe.com/docs/js), or a dictionary containing a user's bank account details.
    """

    card: typing_extensions.NotRequired[
        typing.Union[CustomerSourceCreateBodyCardObj0, str]
    ]
    """
    A token, like the ones returned by [Stripe.js](https://stripe.com/docs/js).
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """

    metadata: typing_extensions.NotRequired[CustomerSourceCreateBodyMetadata]
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    """

    source: typing_extensions.NotRequired[str]
    """
    Please refer to full [documentation](https://stripe.com/docs/api) instead.
    """


class _SerializerCustomerSourceCreateBody(pydantic.BaseModel):
    """
    Serializer for CustomerSourceCreateBody handling case conversions
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
        typing.Union[_SerializerCustomerSourceCreateBodyBankAccountObj0, str]
    ] = pydantic.Field(alias="bank_account", default=None)
    card: typing.Optional[
        typing.Union[_SerializerCustomerSourceCreateBodyCardObj0, str]
    ] = pydantic.Field(alias="card", default=None)
    expand: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="expand", default=None
    )
    metadata: typing.Optional[_SerializerCustomerSourceCreateBodyMetadata] = (
        pydantic.Field(alias="metadata", default=None)
    )
    source: typing.Optional[str] = pydantic.Field(alias="source", default=None)
