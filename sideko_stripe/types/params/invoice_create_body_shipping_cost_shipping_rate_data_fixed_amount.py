import pydantic
import typing
import typing_extensions

from .invoice_create_body_shipping_cost_shipping_rate_data_fixed_amount_currency_options import (
    InvoiceCreateBodyShippingCostShippingRateDataFixedAmountCurrencyOptions,
    _SerializerInvoiceCreateBodyShippingCostShippingRateDataFixedAmountCurrencyOptions,
)


class InvoiceCreateBodyShippingCostShippingRateDataFixedAmount(
    typing_extensions.TypedDict
):
    """
    InvoiceCreateBodyShippingCostShippingRateDataFixedAmount
    """

    amount: typing_extensions.Required[int]

    currency: typing_extensions.Required[str]

    currency_options: typing_extensions.NotRequired[
        InvoiceCreateBodyShippingCostShippingRateDataFixedAmountCurrencyOptions
    ]


class _SerializerInvoiceCreateBodyShippingCostShippingRateDataFixedAmount(
    pydantic.BaseModel
):
    """
    Serializer for InvoiceCreateBodyShippingCostShippingRateDataFixedAmount handling case conversions
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
        _SerializerInvoiceCreateBodyShippingCostShippingRateDataFixedAmountCurrencyOptions
    ] = pydantic.Field(alias="currency_options", default=None)
