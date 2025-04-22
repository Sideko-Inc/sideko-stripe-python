import pydantic
import typing
import typing_extensions

from .invoice_update_body_shipping_cost_obj0_shipping_rate_data_delivery_estimate_maximum import (
    InvoiceUpdateBodyShippingCostObj0ShippingRateDataDeliveryEstimateMaximum,
    _SerializerInvoiceUpdateBodyShippingCostObj0ShippingRateDataDeliveryEstimateMaximum,
)
from .invoice_update_body_shipping_cost_obj0_shipping_rate_data_delivery_estimate_minimum import (
    InvoiceUpdateBodyShippingCostObj0ShippingRateDataDeliveryEstimateMinimum,
    _SerializerInvoiceUpdateBodyShippingCostObj0ShippingRateDataDeliveryEstimateMinimum,
)


class InvoiceUpdateBodyShippingCostObj0ShippingRateDataDeliveryEstimate(
    typing_extensions.TypedDict
):
    """
    InvoiceUpdateBodyShippingCostObj0ShippingRateDataDeliveryEstimate
    """

    maximum: typing_extensions.NotRequired[
        InvoiceUpdateBodyShippingCostObj0ShippingRateDataDeliveryEstimateMaximum
    ]

    minimum: typing_extensions.NotRequired[
        InvoiceUpdateBodyShippingCostObj0ShippingRateDataDeliveryEstimateMinimum
    ]


class _SerializerInvoiceUpdateBodyShippingCostObj0ShippingRateDataDeliveryEstimate(
    pydantic.BaseModel
):
    """
    Serializer for InvoiceUpdateBodyShippingCostObj0ShippingRateDataDeliveryEstimate handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    maximum: typing.Optional[
        _SerializerInvoiceUpdateBodyShippingCostObj0ShippingRateDataDeliveryEstimateMaximum
    ] = pydantic.Field(alias="maximum", default=None)
    minimum: typing.Optional[
        _SerializerInvoiceUpdateBodyShippingCostObj0ShippingRateDataDeliveryEstimateMinimum
    ] = pydantic.Field(alias="minimum", default=None)
