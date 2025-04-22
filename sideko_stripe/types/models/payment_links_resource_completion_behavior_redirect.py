import pydantic


class PaymentLinksResourceCompletionBehaviorRedirect(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    url: str = pydantic.Field(
        alias="url",
    )
    """
    The URL the customer will be redirected to after the purchase is complete.
    """
