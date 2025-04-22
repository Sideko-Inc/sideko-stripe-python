import pydantic
import typing
import typing_extensions

from .invoice_update_body_shipping_cost_obj0_shipping_rate_data_delivery_estimate import (
    InvoiceUpdateBodyShippingCostObj0ShippingRateDataDeliveryEstimate,
    _SerializerInvoiceUpdateBodyShippingCostObj0ShippingRateDataDeliveryEstimate,
)
from .invoice_update_body_shipping_cost_obj0_shipping_rate_data_fixed_amount import (
    InvoiceUpdateBodyShippingCostObj0ShippingRateDataFixedAmount,
    _SerializerInvoiceUpdateBodyShippingCostObj0ShippingRateDataFixedAmount,
)
from .invoice_update_body_shipping_cost_obj0_shipping_rate_data_metadata import (
    InvoiceUpdateBodyShippingCostObj0ShippingRateDataMetadata,
    _SerializerInvoiceUpdateBodyShippingCostObj0ShippingRateDataMetadata,
)


class InvoiceUpdateBodyShippingCostObj0ShippingRateData(typing_extensions.TypedDict):
    """
    InvoiceUpdateBodyShippingCostObj0ShippingRateData
    """

    delivery_estimate: typing_extensions.NotRequired[
        InvoiceUpdateBodyShippingCostObj0ShippingRateDataDeliveryEstimate
    ]

    display_name: typing_extensions.Required[str]

    fixed_amount: typing_extensions.NotRequired[
        InvoiceUpdateBodyShippingCostObj0ShippingRateDataFixedAmount
    ]

    metadata: typing_extensions.NotRequired[
        InvoiceUpdateBodyShippingCostObj0ShippingRateDataMetadata
    ]

    tax_behavior: typing_extensions.NotRequired[
        typing_extensions.Literal["exclusive", "inclusive", "unspecified"]
    ]

    tax_code: typing_extensions.NotRequired[str]

    type_: typing_extensions.NotRequired[typing_extensions.Literal["fixed_amount"]]


class _SerializerInvoiceUpdateBodyShippingCostObj0ShippingRateData(pydantic.BaseModel):
    """
    Serializer for InvoiceUpdateBodyShippingCostObj0ShippingRateData handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    delivery_estimate: typing.Optional[
        _SerializerInvoiceUpdateBodyShippingCostObj0ShippingRateDataDeliveryEstimate
    ] = pydantic.Field(alias="delivery_estimate", default=None)
    display_name: str = pydantic.Field(
        alias="display_name",
    )
    fixed_amount: typing.Optional[
        _SerializerInvoiceUpdateBodyShippingCostObj0ShippingRateDataFixedAmount
    ] = pydantic.Field(alias="fixed_amount", default=None)
    metadata: typing.Optional[
        _SerializerInvoiceUpdateBodyShippingCostObj0ShippingRateDataMetadata
    ] = pydantic.Field(alias="metadata", default=None)
    tax_behavior: typing.Optional[
        typing_extensions.Literal["exclusive", "inclusive", "unspecified"]
    ] = pydantic.Field(alias="tax_behavior", default=None)
    tax_code: typing.Optional[str] = pydantic.Field(alias="tax_code", default=None)
    type_: typing.Optional[typing_extensions.Literal["fixed_amount"]] = pydantic.Field(
        alias="type", default=None
    )
