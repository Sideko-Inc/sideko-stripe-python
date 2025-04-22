import pydantic
import typing
import typing_extensions

from .treasury_outbound_payment_create_body_destination_payment_method_data import (
    TreasuryOutboundPaymentCreateBodyDestinationPaymentMethodData,
    _SerializerTreasuryOutboundPaymentCreateBodyDestinationPaymentMethodData,
)
from .treasury_outbound_payment_create_body_destination_payment_method_options import (
    TreasuryOutboundPaymentCreateBodyDestinationPaymentMethodOptions,
    _SerializerTreasuryOutboundPaymentCreateBodyDestinationPaymentMethodOptions,
)
from .treasury_outbound_payment_create_body_end_user_details import (
    TreasuryOutboundPaymentCreateBodyEndUserDetails,
    _SerializerTreasuryOutboundPaymentCreateBodyEndUserDetails,
)
from .treasury_outbound_payment_create_body_metadata import (
    TreasuryOutboundPaymentCreateBodyMetadata,
    _SerializerTreasuryOutboundPaymentCreateBodyMetadata,
)


class TreasuryOutboundPaymentCreateBody(typing_extensions.TypedDict, total=False):
    """
    TreasuryOutboundPaymentCreateBody
    """

    amount: typing_extensions.Required[int]
    """
    Amount (in cents) to be transferred.
    """

    currency: typing_extensions.Required[str]
    """
    Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    """

    customer: typing_extensions.NotRequired[str]
    """
    ID of the customer to whom the OutboundPayment is sent. Must match the Customer attached to the `destination_payment_method` passed in.
    """

    description: typing_extensions.NotRequired[str]
    """
    An arbitrary string attached to the object. Often useful for displaying to users.
    """

    destination_payment_method: typing_extensions.NotRequired[str]
    """
    The PaymentMethod to use as the payment instrument for the OutboundPayment. Exclusive with `destination_payment_method_data`.
    """

    destination_payment_method_data: typing_extensions.NotRequired[
        TreasuryOutboundPaymentCreateBodyDestinationPaymentMethodData
    ]
    """
    Hash used to generate the PaymentMethod to be used for this OutboundPayment. Exclusive with `destination_payment_method`.
    """

    destination_payment_method_options: typing_extensions.NotRequired[
        TreasuryOutboundPaymentCreateBodyDestinationPaymentMethodOptions
    ]
    """
    Payment method-specific configuration for this OutboundPayment.
    """

    end_user_details: typing_extensions.NotRequired[
        TreasuryOutboundPaymentCreateBodyEndUserDetails
    ]
    """
    End user details.
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """

    financial_account: typing_extensions.Required[str]
    """
    The FinancialAccount to pull funds from.
    """

    metadata: typing_extensions.NotRequired[TreasuryOutboundPaymentCreateBodyMetadata]
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    """

    statement_descriptor: typing_extensions.NotRequired[str]
    """
    The description that appears on the receiving end for this OutboundPayment (for example, bank statement for external bank transfer). Maximum 10 characters for `ach` payments, 140 characters for `us_domestic_wire` payments, or 500 characters for `stripe` network transfers. The default value is "payment".
    """


class _SerializerTreasuryOutboundPaymentCreateBody(pydantic.BaseModel):
    """
    Serializer for TreasuryOutboundPaymentCreateBody handling case conversions
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
    customer: typing.Optional[str] = pydantic.Field(alias="customer", default=None)
    description: typing.Optional[str] = pydantic.Field(
        alias="description", default=None
    )
    destination_payment_method: typing.Optional[str] = pydantic.Field(
        alias="destination_payment_method", default=None
    )
    destination_payment_method_data: typing.Optional[
        _SerializerTreasuryOutboundPaymentCreateBodyDestinationPaymentMethodData
    ] = pydantic.Field(alias="destination_payment_method_data", default=None)
    destination_payment_method_options: typing.Optional[
        _SerializerTreasuryOutboundPaymentCreateBodyDestinationPaymentMethodOptions
    ] = pydantic.Field(alias="destination_payment_method_options", default=None)
    end_user_details: typing.Optional[
        _SerializerTreasuryOutboundPaymentCreateBodyEndUserDetails
    ] = pydantic.Field(alias="end_user_details", default=None)
    expand: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="expand", default=None
    )
    financial_account: str = pydantic.Field(
        alias="financial_account",
    )
    metadata: typing.Optional[_SerializerTreasuryOutboundPaymentCreateBodyMetadata] = (
        pydantic.Field(alias="metadata", default=None)
    )
    statement_descriptor: typing.Optional[str] = pydantic.Field(
        alias="statement_descriptor", default=None
    )
