import pydantic


class ClimateRemovalsProductsPrice(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    amount_fees: int = pydantic.Field(
        alias="amount_fees",
    )
    """
    Fees for one metric ton of carbon removal in the currency's smallest unit.
    """
    amount_subtotal: int = pydantic.Field(
        alias="amount_subtotal",
    )
    """
    Subtotal for one metric ton of carbon removal (excluding fees) in the currency's smallest unit.
    """
    amount_total: int = pydantic.Field(
        alias="amount_total",
    )
    """
    Total for one metric ton of carbon removal (including fees) in the currency's smallest unit.
    """
