import pydantic
import typing_extensions


class TransformUsage(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    divide_by: int = pydantic.Field(
        alias="divide_by",
    )
    """
    Divide usage by this number.
    """
    round: typing_extensions.Literal["down", "up"] = pydantic.Field(
        alias="round",
    )
    """
    After division, either round the result `up` or `down`.
    """
