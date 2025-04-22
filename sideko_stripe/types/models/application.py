import pydantic
import typing
import typing_extensions


class Application(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    id: str = pydantic.Field(
        alias="id",
    )
    """
    Unique identifier for the object.
    """
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    """
    The name of the application.
    """
    object: typing_extensions.Literal["application"] = pydantic.Field(
        alias="object",
    )
    """
    String representing the object's type. Objects of the same type share the same value.
    """
