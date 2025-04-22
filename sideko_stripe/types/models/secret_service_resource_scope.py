import pydantic
import typing
import typing_extensions


class SecretServiceResourceScope(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    type_: typing_extensions.Literal["account", "user"] = pydantic.Field(
        alias="type",
    )
    """
    The secret scope type.
    """
    user: typing.Optional[str] = pydantic.Field(alias="user", default=None)
    """
    The user ID, if type is set to "user"
    """
