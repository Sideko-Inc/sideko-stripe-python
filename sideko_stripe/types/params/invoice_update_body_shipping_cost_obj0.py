import pydantic
import typing
import typing_extensions

from .invoice_update_body_shipping_cost_obj0_shipping_rate_data import (
    InvoiceUpdateBodyShippingCostObj0ShippingRateData,
    _SerializerInvoiceUpdateBodyShippingCostObj0ShippingRateData,
)


class InvoiceUpdateBodyShippingCostObj0(typing_extensions.TypedDict):
    """
    InvoiceUpdateBodyShippingCostObj0
    """

    shipping_rate: typing_extensions.NotRequired[str]

    shipping_rate_data: typing_extensions.NotRequired[
        InvoiceUpdateBodyShippingCostObj0ShippingRateData
    ]


class _SerializerInvoiceUpdateBodyShippingCostObj0(pydantic.BaseModel):
    """
    Serializer for InvoiceUpdateBodyShippingCostObj0 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    shipping_rate: typing.Optional[str] = pydantic.Field(
        alias="shipping_rate", default=None
    )
    shipping_rate_data: typing.Optional[
        _SerializerInvoiceUpdateBodyShippingCostObj0ShippingRateData
    ] = pydantic.Field(alias="shipping_rate_data", default=None)
