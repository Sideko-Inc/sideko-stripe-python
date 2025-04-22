import pydantic


class CouponCurrencyOption(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    amount_off: int = pydantic.Field(
        alias="amount_off",
    )
    """
    Amount (in the `currency` specified) that will be taken off the subtotal of any invoices for this customer.
    """
