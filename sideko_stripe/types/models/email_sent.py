import pydantic


class EmailSent(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    email_sent_at: int = pydantic.Field(
        alias="email_sent_at",
    )
    """
    The timestamp when the email was sent.
    """
    email_sent_to: str = pydantic.Field(
        alias="email_sent_to",
    )
    """
    The recipient's email address.
    """
