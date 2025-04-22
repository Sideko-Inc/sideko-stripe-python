import pydantic
import typing
import typing_extensions

from .treasury_outbound_transfer_create_body_destination_payment_method_options_us_bank_account_obj0 import (
    TreasuryOutboundTransferCreateBodyDestinationPaymentMethodOptionsUsBankAccountObj0,
    _SerializerTreasuryOutboundTransferCreateBodyDestinationPaymentMethodOptionsUsBankAccountObj0,
)


class TreasuryOutboundTransferCreateBodyDestinationPaymentMethodOptions(
    typing_extensions.TypedDict
):
    """
    Hash describing payment method configuration details.
    """

    us_bank_account: typing_extensions.NotRequired[
        typing.Union[
            TreasuryOutboundTransferCreateBodyDestinationPaymentMethodOptionsUsBankAccountObj0,
            str,
        ]
    ]


class _SerializerTreasuryOutboundTransferCreateBodyDestinationPaymentMethodOptions(
    pydantic.BaseModel
):
    """
    Serializer for TreasuryOutboundTransferCreateBodyDestinationPaymentMethodOptions handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    us_bank_account: typing.Optional[
        typing.Union[
            _SerializerTreasuryOutboundTransferCreateBodyDestinationPaymentMethodOptionsUsBankAccountObj0,
            str,
        ]
    ] = pydantic.Field(alias="us_bank_account", default=None)
