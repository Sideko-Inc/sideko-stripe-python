import pydantic
import typing
import typing_extensions

from .treasury_inbound_transfer_create_body_metadata import (
    TreasuryInboundTransferCreateBodyMetadata,
    _SerializerTreasuryInboundTransferCreateBodyMetadata,
)


class TreasuryInboundTransferCreateBody(typing_extensions.TypedDict, total=False):
    """
    TreasuryInboundTransferCreateBody
    """

    amount: typing_extensions.Required[int]
    """
    Amount (in cents) to be transferred.
    """

    currency: typing_extensions.Required[str]
    """
    Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    """

    description: typing_extensions.NotRequired[str]
    """
    An arbitrary string attached to the object. Often useful for displaying to users.
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """

    financial_account: typing_extensions.Required[str]
    """
    The FinancialAccount to send funds to.
    """

    metadata: typing_extensions.NotRequired[TreasuryInboundTransferCreateBodyMetadata]
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    """

    origin_payment_method: typing_extensions.Required[str]
    """
    The origin payment method to be debited for the InboundTransfer.
    """

    statement_descriptor: typing_extensions.NotRequired[str]
    """
    The complete description that appears on your customers' statements. Maximum 10 characters.
    """


class _SerializerTreasuryInboundTransferCreateBody(pydantic.BaseModel):
    """
    Serializer for TreasuryInboundTransferCreateBody handling case conversions
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
    financial_account: str = pydantic.Field(
        alias="financial_account",
    )
    metadata: typing.Optional[_SerializerTreasuryInboundTransferCreateBodyMetadata] = (
        pydantic.Field(alias="metadata", default=None)
    )
    origin_payment_method: str = pydantic.Field(
        alias="origin_payment_method",
    )
    statement_descriptor: typing.Optional[str] = pydantic.Field(
        alias="statement_descriptor", default=None
    )
