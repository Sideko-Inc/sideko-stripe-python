import pydantic
import typing
import typing_extensions

from .treasury_outbound_payment_create_body_destination_payment_method_options_us_bank_account_obj0 import (
    TreasuryOutboundPaymentCreateBodyDestinationPaymentMethodOptionsUsBankAccountObj0,
    _SerializerTreasuryOutboundPaymentCreateBodyDestinationPaymentMethodOptionsUsBankAccountObj0,
)


class TreasuryOutboundPaymentCreateBodyDestinationPaymentMethodOptions(
    typing_extensions.TypedDict
):
    """
    Payment method-specific configuration for this OutboundPayment.
    """

    us_bank_account: typing_extensions.NotRequired[
        typing.Union[
            TreasuryOutboundPaymentCreateBodyDestinationPaymentMethodOptionsUsBankAccountObj0,
            str,
        ]
    ]


class _SerializerTreasuryOutboundPaymentCreateBodyDestinationPaymentMethodOptions(
    pydantic.BaseModel
):
    """
    Serializer for TreasuryOutboundPaymentCreateBodyDestinationPaymentMethodOptions handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    us_bank_account: typing.Optional[
        typing.Union[
            _SerializerTreasuryOutboundPaymentCreateBodyDestinationPaymentMethodOptionsUsBankAccountObj0,
            str,
        ]
    ] = pydantic.Field(alias="us_bank_account", default=None)
