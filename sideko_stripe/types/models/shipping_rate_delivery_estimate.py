import pydantic
import typing

from .shipping_rate_delivery_estimate_bound import ShippingRateDeliveryEstimateBound


class ShippingRateDeliveryEstimate(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    maximum: typing.Optional[ShippingRateDeliveryEstimateBound] = pydantic.Field(
        alias="maximum", default=None
    )
    minimum: typing.Optional[ShippingRateDeliveryEstimateBound] = pydantic.Field(
        alias="minimum", default=None
    )
