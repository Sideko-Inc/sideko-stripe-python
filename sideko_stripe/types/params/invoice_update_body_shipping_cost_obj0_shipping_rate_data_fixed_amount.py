import pydantic
import typing
import typing_extensions

from .invoice_update_body_shipping_cost_obj0_shipping_rate_data_fixed_amount_currency_options import (
    InvoiceUpdateBodyShippingCostObj0ShippingRateDataFixedAmountCurrencyOptions,
    _SerializerInvoiceUpdateBodyShippingCostObj0ShippingRateDataFixedAmountCurrencyOptions,
)


class InvoiceUpdateBodyShippingCostObj0ShippingRateDataFixedAmount(
    typing_extensions.TypedDict
):
    """
    InvoiceUpdateBodyShippingCostObj0ShippingRateDataFixedAmount
    """

    amount: typing_extensions.Required[int]

    currency: typing_extensions.Required[str]

    currency_options: typing_extensions.NotRequired[
        InvoiceUpdateBodyShippingCostObj0ShippingRateDataFixedAmountCurrencyOptions
    ]


class _SerializerInvoiceUpdateBodyShippingCostObj0ShippingRateDataFixedAmount(
    pydantic.BaseModel
):
    """
    Serializer for InvoiceUpdateBodyShippingCostObj0ShippingRateDataFixedAmount handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    amount: int = pydantic.Field(
        alias="amount",
    )
    currency: str = pydantic.Field(
        alias="currency",
    )
    currency_options: typing.Optional[
        _SerializerInvoiceUpdateBodyShippingCostObj0ShippingRateDataFixedAmountCurrencyOptions
    ] = pydantic.Field(alias="currency_options", default=None)
