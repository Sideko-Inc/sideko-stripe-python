import pydantic
import typing
import typing_extensions

from .invoice_create_body_shipping_cost_shipping_rate_data_fixed_amount_currency_options_additional_props import (
    InvoiceCreateBodyShippingCostShippingRateDataFixedAmountCurrencyOptionsAdditionalProps,
    _SerializerInvoiceCreateBodyShippingCostShippingRateDataFixedAmountCurrencyOptionsAdditionalProps,
)


class InvoiceCreateBodyShippingCostShippingRateDataFixedAmountCurrencyOptions(
    typing_extensions.TypedDict, total=False
):
    """
    InvoiceCreateBodyShippingCostShippingRateDataFixedAmountCurrencyOptions
    """


class _SerializerInvoiceCreateBodyShippingCostShippingRateDataFixedAmountCurrencyOptions(
    pydantic.BaseModel
):
    """
    Serializer for InvoiceCreateBodyShippingCostShippingRateDataFixedAmountCurrencyOptions handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[
        str,
        _SerializerInvoiceCreateBodyShippingCostShippingRateDataFixedAmountCurrencyOptionsAdditionalProps,
    ]
