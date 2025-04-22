import pydantic
import typing
import typing_extensions

from .customer_balance_transaction_create_body_metadata_obj0 import (
    CustomerBalanceTransactionCreateBodyMetadataObj0,
    _SerializerCustomerBalanceTransactionCreateBodyMetadataObj0,
)


class CustomerBalanceTransactionCreateBody(typing_extensions.TypedDict, total=False):
    """
    CustomerBalanceTransactionCreateBody
    """

    amount: typing_extensions.Required[int]
    """
    The integer amount in **cents (or local equivalent)** to apply to the customer's credit balance.
    """

    currency: typing_extensions.Required[str]
    """
    Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies). Specifies the [`invoice_credit_balance`](https://stripe.com/docs/api/customers/object#customer_object-invoice_credit_balance) that this transaction will apply to. If the customer's `currency` is not set, it will be updated to this value.
    """

    description: typing_extensions.NotRequired[str]
    """
    An arbitrary string attached to the object. Often useful for displaying to users.
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """

    metadata: typing_extensions.NotRequired[
        typing.Union[CustomerBalanceTransactionCreateBodyMetadataObj0, str]
    ]
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    """


class _SerializerCustomerBalanceTransactionCreateBody(pydantic.BaseModel):
    """
    Serializer for CustomerBalanceTransactionCreateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    amount: int = pydantic.Field(
        alias="amount",
    )
    currency: str = pydantic.Field(
        alias="currency",
    )
    description: typing.Optional[str] = pydantic.Field(
        alias="description", default=None
    )
    expand: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="expand", default=None
    )
    metadata: typing.Optional[
        typing.Union[_SerializerCustomerBalanceTransactionCreateBodyMetadataObj0, str]
    ] = pydantic.Field(alias="metadata", default=None)
