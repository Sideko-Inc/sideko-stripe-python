import pydantic
import typing_extensions


class DeletedApplePayDomain(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    deleted: bool = pydantic.Field(
        alias="deleted",
    )
    """
    Always true for a deleted object
    """
    id: str = pydantic.Field(
        alias="id",
    )
    """
    Unique identifier for the object.
    """
    object: typing_extensions.Literal["apple_pay_domain"] = pydantic.Field(
        alias="object",
    )
    """
    String representing the object's type. Objects of the same type share the same value.
    """
