import pydantic
import typing
import typing_extensions

from .shipping_rate_create_body_delivery_estimate_maximum import (
    ShippingRateCreateBodyDeliveryEstimateMaximum,
    _SerializerShippingRateCreateBodyDeliveryEstimateMaximum,
)
from .shipping_rate_create_body_delivery_estimate_minimum import (
    ShippingRateCreateBodyDeliveryEstimateMinimum,
    _SerializerShippingRateCreateBodyDeliveryEstimateMinimum,
)


class ShippingRateCreateBodyDeliveryEstimate(typing_extensions.TypedDict):
    """
    The estimated range for how long shipping will take, meant to be displayable to the customer. This will appear on CheckoutSessions.
    """

    maximum: typing_extensions.NotRequired[
        ShippingRateCreateBodyDeliveryEstimateMaximum
    ]

    minimum: typing_extensions.NotRequired[
        ShippingRateCreateBodyDeliveryEstimateMinimum
    ]


class _SerializerShippingRateCreateBodyDeliveryEstimate(pydantic.BaseModel):
    """
    Serializer for ShippingRateCreateBodyDeliveryEstimate handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    maximum: typing.Optional[
        _SerializerShippingRateCreateBodyDeliveryEstimateMaximum
    ] = pydantic.Field(alias="maximum", default=None)
    minimum: typing.Optional[
        _SerializerShippingRateCreateBodyDeliveryEstimateMinimum
    ] = pydantic.Field(alias="minimum", default=None)
