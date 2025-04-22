import pydantic
import typing_extensions


class InvoiceCreateBodyShippingCostShippingRateDataDeliveryEstimateMaximum(
    typing_extensions.TypedDict
):
    """
    InvoiceCreateBodyShippingCostShippingRateDataDeliveryEstimateMaximum
    """

    unit: typing_extensions.Required[
        typing_extensions.Literal["business_day", "day", "hour", "month", "week"]
    ]

    value: typing_extensions.Required[int]


class _SerializerInvoiceCreateBodyShippingCostShippingRateDataDeliveryEstimateMaximum(
    pydantic.BaseModel
):
    """
    Serializer for InvoiceCreateBodyShippingCostShippingRateDataDeliveryEstimateMaximum handling case conversions
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
