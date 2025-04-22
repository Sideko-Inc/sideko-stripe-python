import pydantic


class PaymentPagesCheckoutSessionCurrencyConversion(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    amount_subtotal: int = pydantic.Field(
        alias="amount_subtotal",
    )
    """
    Total of all items in source currency before discounts or taxes are applied.
    """
    amount_total: int = pydantic.Field(
        alias="amount_total",
    )
    """
    Total of all items in source currency after discounts and taxes are applied.
    """
    fx_rate: str = pydantic.Field(
        alias="fx_rate",
    )
    """
    Exchange rate used to convert source currency amounts to customer currency amounts
    """
    source_currency: str = pydantic.Field(
        alias="source_currency",
    )
    """
    Creation currency of the CheckoutSession before localization
    """
