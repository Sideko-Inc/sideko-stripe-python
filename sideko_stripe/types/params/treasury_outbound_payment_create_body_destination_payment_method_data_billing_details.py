import pydantic
import typing
import typing_extensions

from .treasury_outbound_payment_create_body_destination_payment_method_data_billing_details_address_obj0 import (
    TreasuryOutboundPaymentCreateBodyDestinationPaymentMethodDataBillingDetailsAddressObj0,
    _SerializerTreasuryOutboundPaymentCreateBodyDestinationPaymentMethodDataBillingDetailsAddressObj0,
)


class TreasuryOutboundPaymentCreateBodyDestinationPaymentMethodDataBillingDetails(
    typing_extensions.TypedDict
):
    """
    TreasuryOutboundPaymentCreateBodyDestinationPaymentMethodDataBillingDetails
    """

    address: typing_extensions.NotRequired[
        typing.Union[
            TreasuryOutboundPaymentCreateBodyDestinationPaymentMethodDataBillingDetailsAddressObj0,
            str,
        ]
    ]

    email: typing_extensions.NotRequired[typing.Union[str, str]]

    name: typing_extensions.NotRequired[typing.Union[str, str]]

    phone: typing_extensions.NotRequired[typing.Union[str, str]]


class _SerializerTreasuryOutboundPaymentCreateBodyDestinationPaymentMethodDataBillingDetails(
    pydantic.BaseModel
):
    """
    Serializer for TreasuryOutboundPaymentCreateBodyDestinationPaymentMethodDataBillingDetails handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    address: typing.Optional[
        typing.Union[
            _SerializerTreasuryOutboundPaymentCreateBodyDestinationPaymentMethodDataBillingDetailsAddressObj0,
            str,
        ]
    ] = pydantic.Field(alias="address", default=None)
    email: typing.Optional[typing.Union[str, str]] = pydantic.Field(
        alias="email", default=None
    )
    name: typing.Optional[typing.Union[str, str]] = pydantic.Field(
        alias="name", default=None
    )
    phone: typing.Optional[typing.Union[str, str]] = pydantic.Field(
        alias="phone", default=None
    )
