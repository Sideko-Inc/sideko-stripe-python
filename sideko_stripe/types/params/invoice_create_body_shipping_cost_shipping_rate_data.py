import pydantic
import typing
import typing_extensions

from .invoice_create_body_shipping_cost_shipping_rate_data_delivery_estimate import (
    InvoiceCreateBodyShippingCostShippingRateDataDeliveryEstimate,
    _SerializerInvoiceCreateBodyShippingCostShippingRateDataDeliveryEstimate,
)
from .invoice_create_body_shipping_cost_shipping_rate_data_fixed_amount import (
    InvoiceCreateBodyShippingCostShippingRateDataFixedAmount,
    _SerializerInvoiceCreateBodyShippingCostShippingRateDataFixedAmount,
)
from .invoice_create_body_shipping_cost_shipping_rate_data_metadata import (
    InvoiceCreateBodyShippingCostShippingRateDataMetadata,
    _SerializerInvoiceCreateBodyShippingCostShippingRateDataMetadata,
)


class InvoiceCreateBodyShippingCostShippingRateData(typing_extensions.TypedDict):
    """
    InvoiceCreateBodyShippingCostShippingRateData
    """

    delivery_estimate: typing_extensions.NotRequired[
        InvoiceCreateBodyShippingCostShippingRateDataDeliveryEstimate
    ]

    display_name: typing_extensions.Required[str]

    fixed_amount: typing_extensions.NotRequired[
        InvoiceCreateBodyShippingCostShippingRateDataFixedAmount
    ]

    metadata: typing_extensions.NotRequired[
        InvoiceCreateBodyShippingCostShippingRateDataMetadata
    ]

    tax_behavior: typing_extensions.NotRequired[
        typing_extensions.Literal["exclusive", "inclusive", "unspecified"]
    ]

    tax_code: typing_extensions.NotRequired[str]

    type_: typing_extensions.NotRequired[typing_extensions.Literal["fixed_amount"]]


class _SerializerInvoiceCreateBodyShippingCostShippingRateData(pydantic.BaseModel):
    """
    Serializer for InvoiceCreateBodyShippingCostShippingRateData handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    delivery_estimate: typing.Optional[
        _SerializerInvoiceCreateBodyShippingCostShippingRateDataDeliveryEstimate
    ] = pydantic.Field(alias="delivery_estimate", default=None)
    display_name: str = pydantic.Field(
        alias="display_name",
    )
    fixed_amount: typing.Optional[
        _SerializerInvoiceCreateBodyShippingCostShippingRateDataFixedAmount
    ] = pydantic.Field(alias="fixed_amount", default=None)
    metadata: typing.Optional[
        _SerializerInvoiceCreateBodyShippingCostShippingRateDataMetadata
    ] = pydantic.Field(alias="metadata", default=None)
    tax_behavior: typing.Optional[
        typing_extensions.Literal["exclusive", "inclusive", "unspecified"]
    ] = pydantic.Field(alias="tax_behavior", default=None)
    tax_code: typing.Optional[str] = pydantic.Field(alias="tax_code", default=None)
    type_: typing.Optional[typing_extensions.Literal["fixed_amount"]] = pydantic.Field(
        alias="type", default=None
    )
