import pydantic


class ThreeDSecureUsage(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    supported: bool = pydantic.Field(
        alias="supported",
    )
    """
    Whether 3D Secure is supported on this card.
    """
