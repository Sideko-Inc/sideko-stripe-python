import pydantic
import typing_extensions


class CheckoutSessionCreateBodyShippingOptionsItemShippingRateDataDeliveryEstimateMaximum(
    typing_extensions.TypedDict
):
    """
    CheckoutSessionCreateBodyShippingOptionsItemShippingRateDataDeliveryEstimateMaximum
    """

    unit: typing_extensions.Required[
        typing_extensions.Literal["business_day", "day", "hour", "month", "week"]
    ]

    value: typing_extensions.Required[int]


class _SerializerCheckoutSessionCreateBodyShippingOptionsItemShippingRateDataDeliveryEstimateMaximum(
    pydantic.BaseModel
):
    """
    Serializer for CheckoutSessionCreateBodyShippingOptionsItemShippingRateDataDeliveryEstimateMaximum handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    unit: typing_extensions.Literal["business_day", "day", "hour", "month", "week"] = (
        pydantic.Field(
            alias="unit",
        )
    )
    value: int = pydantic.Field(
        alias="value",
    )
