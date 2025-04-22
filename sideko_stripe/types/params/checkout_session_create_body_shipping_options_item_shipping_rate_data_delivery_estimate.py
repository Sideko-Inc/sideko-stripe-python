import pydantic
import typing
import typing_extensions

from .checkout_session_create_body_shipping_options_item_shipping_rate_data_delivery_estimate_maximum import (
    CheckoutSessionCreateBodyShippingOptionsItemShippingRateDataDeliveryEstimateMaximum,
    _SerializerCheckoutSessionCreateBodyShippingOptionsItemShippingRateDataDeliveryEstimateMaximum,
)
from .checkout_session_create_body_shipping_options_item_shipping_rate_data_delivery_estimate_minimum import (
    CheckoutSessionCreateBodyShippingOptionsItemShippingRateDataDeliveryEstimateMinimum,
    _SerializerCheckoutSessionCreateBodyShippingOptionsItemShippingRateDataDeliveryEstimateMinimum,
)


class CheckoutSessionCreateBodyShippingOptionsItemShippingRateDataDeliveryEstimate(
    typing_extensions.TypedDict
):
    """
    CheckoutSessionCreateBodyShippingOptionsItemShippingRateDataDeliveryEstimate
    """

    maximum: typing_extensions.NotRequired[
        CheckoutSessionCreateBodyShippingOptionsItemShippingRateDataDeliveryEstimateMaximum
    ]

    minimum: typing_extensions.NotRequired[
        CheckoutSessionCreateBodyShippingOptionsItemShippingRateDataDeliveryEstimateMinimum
    ]


class _SerializerCheckoutSessionCreateBodyShippingOptionsItemShippingRateDataDeliveryEstimate(
    pydantic.BaseModel
):
    """
    Serializer for CheckoutSessionCreateBodyShippingOptionsItemShippingRateDataDeliveryEstimate handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    maximum: typing.Optional[
        _SerializerCheckoutSessionCreateBodyShippingOptionsItemShippingRateDataDeliveryEstimateMaximum
    ] = pydantic.Field(alias="maximum", default=None)
    minimum: typing.Optional[
        _SerializerCheckoutSessionCreateBodyShippingOptionsItemShippingRateDataDeliveryEstimateMinimum
    ] = pydantic.Field(alias="minimum", default=None)
