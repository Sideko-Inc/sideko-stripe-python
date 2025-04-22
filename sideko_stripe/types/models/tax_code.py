import pydantic
import typing_extensions


class TaxCode(pydantic.BaseModel):
    """
    [Tax codes](https://stripe.com/docs/tax/tax-categories) classify goods and services for tax purposes.
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    description: str = pydantic.Field(
        alias="description",
    )
    """
    A detailed description of which types of products the tax code represents.
    """
    id: str = pydantic.Field(
        alias="id",
    )
    """
    Unique identifier for the object.
    """
    name: str = pydantic.Field(
        alias="name",
    )
    """
    A short name for the tax code.
    """
    object: typing_extensions.Literal["tax_code"] = pydantic.Field(
        alias="object",
    )
    """
    String representing the object's type. Objects of the same type share the same value.
    """
