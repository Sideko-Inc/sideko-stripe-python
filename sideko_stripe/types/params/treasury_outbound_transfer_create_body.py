import pydantic
import typing
import typing_extensions

from .treasury_outbound_transfer_create_body_destination_payment_method_data import (
    TreasuryOutboundTransferCreateBodyDestinationPaymentMethodData,
    _SerializerTreasuryOutboundTransferCreateBodyDestinationPaymentMethodData,
)
from .treasury_outbound_transfer_create_body_destination_payment_method_options import (
    TreasuryOutboundTransferCreateBodyDestinationPaymentMethodOptions,
    _SerializerTreasuryOutboundTransferCreateBodyDestinationPaymentMethodOptions,
)
from .treasury_outbound_transfer_create_body_metadata import (
    TreasuryOutboundTransferCreateBodyMetadata,
    _SerializerTreasuryOutboundTransferCreateBodyMetadata,
)


class TreasuryOutboundTransferCreateBody(typing_extensions.TypedDict, total=False):
    """
    TreasuryOutboundTransferCreateBody
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

    destination_payment_method: typing_extensions.NotRequired[str]
    """
    The PaymentMethod to use as the payment instrument for the OutboundTransfer.
    """

    destination_payment_method_data: typing_extensions.NotRequired[
        TreasuryOutboundTransferCreateBodyDestinationPaymentMethodData
    ]
    """
    Hash used to generate the PaymentMethod to be used for this OutboundTransfer. Exclusive with `destination_payment_method`.
    """

    destination_payment_method_options: typing_extensions.NotRequired[
        TreasuryOutboundTransferCreateBodyDestinationPaymentMethodOptions
    ]
    """
    Hash describing payment method configuration details.
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """

    financial_account: typing_extensions.Required[str]
    """
    The FinancialAccount to pull funds from.
    """

    metadata: typing_extensions.NotRequired[TreasuryOutboundTransferCreateBodyMetadata]
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    """

    statement_descriptor: typing_extensions.NotRequired[str]
    """
    Statement descriptor to be shown on the receiving end of an OutboundTransfer. Maximum 10 characters for `ach` transfers or 140 characters for `us_domestic_wire` transfers. The default value is "transfer".
    """


class _SerializerTreasuryOutboundTransferCreateBody(pydantic.BaseModel):
    """
    Serializer for TreasuryOutboundTransferCreateBody handling case conversions
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
    destination_payment_method: typing.Optional[str] = pydantic.Field(
        alias="destination_payment_method", default=None
    )
    destination_payment_method_data: typing.Optional[
        _SerializerTreasuryOutboundTransferCreateBodyDestinationPaymentMethodData
    ] = pydantic.Field(alias="destination_payment_method_data", default=None)
    destination_payment_method_options: typing.Optional[
        _SerializerTreasuryOutboundTransferCreateBodyDestinationPaymentMethodOptions
    ] = pydantic.Field(alias="destination_payment_method_options", default=None)
    expand: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="expand", default=None
    )
    financial_account: str = pydantic.Field(
        alias="financial_account",
    )
    metadata: typing.Optional[_SerializerTreasuryOutboundTransferCreateBodyMetadata] = (
        pydantic.Field(alias="metadata", default=None)
    )
    statement_descriptor: typing.Optional[str] = pydantic.Field(
        alias="statement_descriptor", default=None
    )
