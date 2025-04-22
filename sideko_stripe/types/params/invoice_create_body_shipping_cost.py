import pydantic
import typing
import typing_extensions

from .invoice_create_body_shipping_cost_shipping_rate_data import (
    InvoiceCreateBodyShippingCostShippingRateData,
    _SerializerInvoiceCreateBodyShippingCostShippingRateData,
)


class InvoiceCreateBodyShippingCost(typing_extensions.TypedDict):
    """
    Settings for the cost of shipping for this invoice.
    """

    shipping_rate: typing_extensions.NotRequired[str]

    shipping_rate_data: typing_extensions.NotRequired[
        InvoiceCreateBodyShippingCostShippingRateData
    ]


class _SerializerInvoiceCreateBodyShippingCost(pydantic.BaseModel):
    """
    Serializer for InvoiceCreateBodyShippingCost handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    shipping_rate: typing.Optional[str] = pydantic.Field(
        alias="shipping_rate", default=None
    )
    shipping_rate_data: typing.Optional[
        _SerializerInvoiceCreateBodyShippingCostShippingRateData
    ] = pydantic.Field(alias="shipping_rate_data", default=None)
