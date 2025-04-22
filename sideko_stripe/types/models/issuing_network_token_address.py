import pydantic


class IssuingNetworkTokenAddress(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    line1: str = pydantic.Field(
        alias="line1",
    )
    """
    The street address of the cardholder tokenizing the card.
    """
    postal_code: str = pydantic.Field(
        alias="postal_code",
    )
    """
    The postal code of the cardholder tokenizing the card.
    """
