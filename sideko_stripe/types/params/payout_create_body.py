import pydantic
import typing
import typing_extensions

from .payout_create_body_metadata import (
    PayoutCreateBodyMetadata,
    _SerializerPayoutCreateBodyMetadata,
)


class PayoutCreateBody(typing_extensions.TypedDict, total=False):
    """
    PayoutCreateBody
    """

    amount: typing_extensions.Required[int]
    """
    A positive integer in cents representing how much to payout.
    """

    currency: typing_extensions.Required[str]
    """
    Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    """

    description: typing_extensions.NotRequired[str]
    """
    An arbitrary string attached to the object. Often useful for displaying to users.
    """

    destination: typing_extensions.NotRequired[str]
    """
    The ID of a bank account or a card to send the payout to. If you don't provide a destination, we use the default external account for the specified currency.
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """

    metadata: typing_extensions.NotRequired[PayoutCreateBodyMetadata]
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    """

    method: typing_extensions.NotRequired[
        typing_extensions.Literal["instant", "standard"]
    ]
    """
    The method used to send this payout, which is `standard` or `instant`. We support `instant` for payouts to debit cards and bank accounts in certain countries. Learn more about [bank support for Instant Payouts](https://stripe.com/docs/payouts/instant-payouts-banks).
    """

    source_type: typing_extensions.NotRequired[
        typing_extensions.Literal["bank_account", "card", "fpx"]
    ]
    """
    The balance type of your Stripe balance to draw this payout from. Balances for different payment sources are kept separately. You can find the amounts with the Balances API. One of `bank_account`, `card`, or `fpx`.
    """

    statement_descriptor: typing_extensions.NotRequired[str]
    """
    A string that displays on the recipient's bank or card statement (up to 22 characters). A `statement_descriptor` that's longer than 22 characters return an error. Most banks truncate this information and display it inconsistently. Some banks might not display it at all.
    """


class _SerializerPayoutCreateBody(pydantic.BaseModel):
    """
    Serializer for PayoutCreateBody handling case conversions
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
    destination: typing.Optional[str] = pydantic.Field(
        alias="destination", default=None
    )
    expand: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="expand", default=None
    )
    metadata: typing.Optional[_SerializerPayoutCreateBodyMetadata] = pydantic.Field(
        alias="metadata", default=None
    )
    method: typing.Optional[typing_extensions.Literal["instant", "standard"]] = (
        pydantic.Field(alias="method", default=None)
    )
    source_type: typing.Optional[
        typing_extensions.Literal["bank_account", "card", "fpx"]
    ] = pydantic.Field(alias="source_type", default=None)
    statement_descriptor: typing.Optional[str] = pydantic.Field(
        alias="statement_descriptor", default=None
    )
