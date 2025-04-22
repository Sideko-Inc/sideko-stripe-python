import pydantic


class PromotionCodeCurrencyOption(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    minimum_amount: int = pydantic.Field(
        alias="minimum_amount",
    )
    """
    Minimum amount required to redeem this Promotion Code into a Coupon (e.g., a purchase must be $100 or more to work).
    """
