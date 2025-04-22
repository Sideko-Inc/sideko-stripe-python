import pydantic
import typing_extensions


class VerificationSessionRedaction(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    status: typing_extensions.Literal["processing", "redacted"] = pydantic.Field(
        alias="status",
    )
    """
    Indicates whether this object and its related objects have been redacted or not.
    """
