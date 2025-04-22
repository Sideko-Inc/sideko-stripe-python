import pydantic
import typing
import typing_extensions

from .treasury_outbound_payment_create_body_destination_payment_method_data_billing_details import (
    TreasuryOutboundPaymentCreateBodyDestinationPaymentMethodDataBillingDetails,
    _SerializerTreasuryOutboundPaymentCreateBodyDestinationPaymentMethodDataBillingDetails,
)
from .treasury_outbound_payment_create_body_destination_payment_method_data_metadata import (
    TreasuryOutboundPaymentCreateBodyDestinationPaymentMethodDataMetadata,
    _SerializerTreasuryOutboundPaymentCreateBodyDestinationPaymentMethodDataMetadata,
)
from .treasury_outbound_payment_create_body_destination_payment_method_data_us_bank_account import (
    TreasuryOutboundPaymentCreateBodyDestinationPaymentMethodDataUsBankAccount,
    _SerializerTreasuryOutboundPaymentCreateBodyDestinationPaymentMethodDataUsBankAccount,
)


class TreasuryOutboundPaymentCreateBodyDestinationPaymentMethodData(
    typing_extensions.TypedDict
):
    """
    Hash used to generate the PaymentMethod to be used for this OutboundPayment. Exclusive with `destination_payment_method`.
    """

    billing_details: typing_extensions.NotRequired[
        TreasuryOutboundPaymentCreateBodyDestinationPaymentMethodDataBillingDetails
    ]

    financial_account: typing_extensions.NotRequired[str]

    metadata: typing_extensions.NotRequired[
        TreasuryOutboundPaymentCreateBodyDestinationPaymentMethodDataMetadata
    ]

    type_: typing_extensions.Required[
        typing_extensions.Literal["financial_account", "us_bank_account"]
    ]

    us_bank_account: typing_extensions.NotRequired[
        TreasuryOutboundPaymentCreateBodyDestinationPaymentMethodDataUsBankAccount
    ]


class _SerializerTreasuryOutboundPaymentCreateBodyDestinationPaymentMethodData(
    pydantic.BaseModel
):
    """
    Serializer for TreasuryOutboundPaymentCreateBodyDestinationPaymentMethodData handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    billing_details: typing.Optional[
        _SerializerTreasuryOutboundPaymentCreateBodyDestinationPaymentMethodDataBillingDetails
    ] = pydantic.Field(alias="billing_details", default=None)
    financial_account: typing.Optional[str] = pydantic.Field(
        alias="financial_account", default=None
    )
    metadata: typing.Optional[
        _SerializerTreasuryOutboundPaymentCreateBodyDestinationPaymentMethodDataMetadata
    ] = pydantic.Field(alias="metadata", default=None)
    type_: typing_extensions.Literal["financial_account", "us_bank_account"] = (
        pydantic.Field(
            alias="type",
        )
    )
    us_bank_account: typing.Optional[
        _SerializerTreasuryOutboundPaymentCreateBodyDestinationPaymentMethodDataUsBankAccount
    ] = pydantic.Field(alias="us_bank_account", default=None)
