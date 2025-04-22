import pydantic
import typing
import typing_extensions


class DeletedCard(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    currency: typing.Optional[str] = pydantic.Field(alias="currency", default=None)
    """
    Three-letter [ISO code for the currency](https://stripe.com/docs/payouts) paid out to the bank account.
    """
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
    object: typing_extensions.Literal["card"] = pydantic.Field(
        alias="object",
    )
    """
    String representing the object's type. Objects of the same type share the same value.
    """
