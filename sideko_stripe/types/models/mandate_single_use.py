import pydantic


class MandateSingleUse(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    amount: int = pydantic.Field(
        alias="amount",
    )
    """
    The amount of the payment on a single use mandate.
    """
    currency: str = pydantic.Field(
        alias="currency",
    )
    """
    The currency of the payment on a single use mandate.
    """
