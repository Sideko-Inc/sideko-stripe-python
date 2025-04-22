import pydantic
import typing
import typing_extensions


class CheckoutSessionCreateBodyAdaptivePricing(typing_extensions.TypedDict):
    """
    Settings for price localization with [Adaptive Pricing](https://docs.stripe.com/payments/checkout/adaptive-pricing).
    """

    enabled: typing_extensions.NotRequired[bool]


class _SerializerCheckoutSessionCreateBodyAdaptivePricing(pydantic.BaseModel):
    """
    Serializer for CheckoutSessionCreateBodyAdaptivePricing handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    enabled: typing.Optional[bool] = pydantic.Field(alias="enabled", default=None)
