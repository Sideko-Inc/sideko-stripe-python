import pydantic
import typing
import typing_extensions

from .invoice_update_body_shipping_cost_obj0_shipping_rate_data_fixed_amount_currency_options_additional_props import (
    InvoiceUpdateBodyShippingCostObj0ShippingRateDataFixedAmountCurrencyOptionsAdditionalProps,
    _SerializerInvoiceUpdateBodyShippingCostObj0ShippingRateDataFixedAmountCurrencyOptionsAdditionalProps,
)


class InvoiceUpdateBodyShippingCostObj0ShippingRateDataFixedAmountCurrencyOptions(
    typing_extensions.TypedDict, total=False
):
    """
    InvoiceUpdateBodyShippingCostObj0ShippingRateDataFixedAmountCurrencyOptions
    """


class _SerializerInvoiceUpdateBodyShippingCostObj0ShippingRateDataFixedAmountCurrencyOptions(
    pydantic.BaseModel
):
    """
    Serializer for InvoiceUpdateBodyShippingCostObj0ShippingRateDataFixedAmountCurrencyOptions handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[
        str,
        _SerializerInvoiceUpdateBodyShippingCostObj0ShippingRateDataFixedAmountCurrencyOptionsAdditionalProps,
    ]
