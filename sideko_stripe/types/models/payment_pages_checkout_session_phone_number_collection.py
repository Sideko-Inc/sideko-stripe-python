import pydantic


class PaymentPagesCheckoutSessionPhoneNumberCollection(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    enabled: bool = pydantic.Field(
        alias="enabled",
    )
    """
    Indicates whether phone number collection is enabled for the session
    """
