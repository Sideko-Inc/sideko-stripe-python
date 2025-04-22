import pydantic
import typing
import typing_extensions

from .invoice_create_body_shipping_cost_shipping_rate_data_delivery_estimate_maximum import (
    InvoiceCreateBodyShippingCostShippingRateDataDeliveryEstimateMaximum,
    _SerializerInvoiceCreateBodyShippingCostShippingRateDataDeliveryEstimateMaximum,
)
from .invoice_create_body_shipping_cost_shipping_rate_data_delivery_estimate_minimum import (
    InvoiceCreateBodyShippingCostShippingRateDataDeliveryEstimateMinimum,
    _SerializerInvoiceCreateBodyShippingCostShippingRateDataDeliveryEstimateMinimum,
)


class InvoiceCreateBodyShippingCostShippingRateDataDeliveryEstimate(
    typing_extensions.TypedDict
):
    """
    InvoiceCreateBodyShippingCostShippingRateDataDeliveryEstimate
    """

    maximum: typing_extensions.NotRequired[
        InvoiceCreateBodyShippingCostShippingRateDataDeliveryEstimateMaximum
    ]

    minimum: typing_extensions.NotRequired[
        InvoiceCreateBodyShippingCostShippingRateDataDeliveryEstimateMinimum
    ]


class _SerializerInvoiceCreateBodyShippingCostShippingRateDataDeliveryEstimate(
    pydantic.BaseModel
):
    """
    Serializer for InvoiceCreateBodyShippingCostShippingRateDataDeliveryEstimate handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    maximum: typing.Optional[
        _SerializerInvoiceCreateBodyShippingCostShippingRateDataDeliveryEstimateMaximum
    ] = pydantic.Field(alias="maximum", default=None)
    minimum: typing.Optional[
        _SerializerInvoiceCreateBodyShippingCostShippingRateDataDeliveryEstimateMinimum
    ] = pydantic.Field(alias="minimum", default=None)
