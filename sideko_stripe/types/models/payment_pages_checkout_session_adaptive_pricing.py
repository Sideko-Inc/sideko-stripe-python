import pydantic


class PaymentPagesCheckoutSessionAdaptivePricing(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    enabled: bool = pydantic.Field(
        alias="enabled",
    )
    """
    Whether Adaptive Pricing is enabled.
    """
