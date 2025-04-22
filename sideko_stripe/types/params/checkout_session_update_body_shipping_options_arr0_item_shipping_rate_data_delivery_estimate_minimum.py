import pydantic
import typing_extensions


class CheckoutSessionUpdateBodyShippingOptionsArr0ItemShippingRateDataDeliveryEstimateMinimum(
    typing_extensions.TypedDict
):
    """
    CheckoutSessionUpdateBodyShippingOptionsArr0ItemShippingRateDataDeliveryEstimateMinimum
    """

    unit: typing_extensions.Required[
        typing_extensions.Literal["business_day", "day", "hour", "month", "week"]
    ]

    value: typing_extensions.Required[int]


class _SerializerCheckoutSessionUpdateBodyShippingOptionsArr0ItemShippingRateDataDeliveryEstimateMinimum(
    pydantic.BaseModel
):
    """
    Serializer for CheckoutSessionUpdateBodyShippingOptionsArr0ItemShippingRateDataDeliveryEstimateMinimum handling case conversions
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
