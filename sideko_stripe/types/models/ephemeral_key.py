import pydantic
import typing
import typing_extensions


class EphemeralKey(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    created: int = pydantic.Field(
        alias="created",
    )
    """
    Time at which the object was created. Measured in seconds since the Unix epoch.
    """
    expires: int = pydantic.Field(
        alias="expires",
    )
    """
    Time at which the key will expire. Measured in seconds since the Unix epoch.
    """
    id: str = pydantic.Field(
        alias="id",
    )
    """
    Unique identifier for the object.
    """
    livemode: bool = pydantic.Field(
        alias="livemode",
    )
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    object: typing_extensions.Literal["ephemeral_key"] = pydantic.Field(
        alias="object",
    )
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    secret: typing.Optional[str] = pydantic.Field(alias="secret", default=None)
    """
    The key's secret. You can use this value to make authorized requests to the Stripe API.
    """
