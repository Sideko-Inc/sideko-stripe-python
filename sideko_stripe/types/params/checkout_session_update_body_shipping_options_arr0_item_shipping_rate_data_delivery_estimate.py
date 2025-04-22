import pydantic
import typing
import typing_extensions

from .checkout_session_update_body_shipping_options_arr0_item_shipping_rate_data_delivery_estimate_maximum import (
    CheckoutSessionUpdateBodyShippingOptionsArr0ItemShippingRateDataDeliveryEstimateMaximum,
    _SerializerCheckoutSessionUpdateBodyShippingOptionsArr0ItemShippingRateDataDeliveryEstimateMaximum,
)
from .checkout_session_update_body_shipping_options_arr0_item_shipping_rate_data_delivery_estimate_minimum import (
    CheckoutSessionUpdateBodyShippingOptionsArr0ItemShippingRateDataDeliveryEstimateMinimum,
    _SerializerCheckoutSessionUpdateBodyShippingOptionsArr0ItemShippingRateDataDeliveryEstimateMinimum,
)


class CheckoutSessionUpdateBodyShippingOptionsArr0ItemShippingRateDataDeliveryEstimate(
    typing_extensions.TypedDict
):
    """
    CheckoutSessionUpdateBodyShippingOptionsArr0ItemShippingRateDataDeliveryEstimate
    """

    maximum: typing_extensions.NotRequired[
        CheckoutSessionUpdateBodyShippingOptionsArr0ItemShippingRateDataDeliveryEstimateMaximum
    ]

    minimum: typing_extensions.NotRequired[
        CheckoutSessionUpdateBodyShippingOptionsArr0ItemShippingRateDataDeliveryEstimateMinimum
    ]


class _SerializerCheckoutSessionUpdateBodyShippingOptionsArr0ItemShippingRateDataDeliveryEstimate(
    pydantic.BaseModel
):
    """
    Serializer for CheckoutSessionUpdateBodyShippingOptionsArr0ItemShippingRateDataDeliveryEstimate handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    maximum: typing.Optional[
        _SerializerCheckoutSessionUpdateBodyShippingOptionsArr0ItemShippingRateDataDeliveryEstimateMaximum
    ] = pydantic.Field(alias="maximum", default=None)
    minimum: typing.Optional[
        _SerializerCheckoutSessionUpdateBodyShippingOptionsArr0ItemShippingRateDataDeliveryEstimateMinimum
    ] = pydantic.Field(alias="minimum", default=None)
