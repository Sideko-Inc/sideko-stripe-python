import pydantic


class PaymentLinksResourceCustomTextPosition(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    message: str = pydantic.Field(
        alias="message",
    )
    """
    Text may be up to 1200 characters in length.
    """
