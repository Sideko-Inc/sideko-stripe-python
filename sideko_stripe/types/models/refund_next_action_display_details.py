import pydantic

from .email_sent import EmailSent


class RefundNextActionDisplayDetails(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    email_sent: EmailSent = pydantic.Field(
        alias="email_sent",
    )
    expires_at: int = pydantic.Field(
        alias="expires_at",
    )
    """
    The expiry timestamp.
    """
