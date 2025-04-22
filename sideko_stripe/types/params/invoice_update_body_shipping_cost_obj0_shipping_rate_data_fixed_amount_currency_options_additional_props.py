import pydantic
import typing
import typing_extensions


class InvoiceUpdateBodyShippingCostObj0ShippingRateDataFixedAmountCurrencyOptionsAdditionalProps(
    typing_extensions.TypedDict
):
    """
    InvoiceUpdateBodyShippingCostObj0ShippingRateDataFixedAmountCurrencyOptionsAdditionalProps
    """

    amount: typing_extensions.Required[int]

    tax_behavior: typing_extensions.NotRequired[
        typing_extensions.Literal["exclusive", "inclusive", "unspecified"]
    ]


class _SerializerInvoiceUpdateBodyShippingCostObj0ShippingRateDataFixedAmountCurrencyOptionsAdditionalProps(
    pydantic.BaseModel
):
    """
    Serializer for InvoiceUpdateBodyShippingCostObj0ShippingRateDataFixedAmountCurrencyOptionsAdditionalProps handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    amount: int = pydantic.Field(
        alias="amount",
    )
    tax_behavior: typing.Optional[
        typing_extensions.Literal["exclusive", "inclusive", "unspecified"]
    ] = pydantic.Field(alias="tax_behavior", default=None)
