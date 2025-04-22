import pydantic


class PaymentLinksResourcePhoneNumberCollection(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    enabled: bool = pydantic.Field(
        alias="enabled",
    )
    """
    If `true`, a phone number will be collected during checkout.
    """
