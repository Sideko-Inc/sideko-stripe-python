import pydantic
import typing_extensions


class InvoiceUpdateBodyShippingCostObj0ShippingRateDataDeliveryEstimateMinimum(
    typing_extensions.TypedDict
):
    """
    InvoiceUpdateBodyShippingCostObj0ShippingRateDataDeliveryEstimateMinimum
    """

    unit: typing_extensions.Required[
        typing_extensions.Literal["business_day", "day", "hour", "month", "week"]
    ]

    value: typing_extensions.Required[int]


class _SerializerInvoiceUpdateBodyShippingCostObj0ShippingRateDataDeliveryEstimateMinimum(
    pydantic.BaseModel
):
    """
    Serializer for InvoiceUpdateBodyShippingCostObj0ShippingRateDataDeliveryEstimateMinimum handling case conversions
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
