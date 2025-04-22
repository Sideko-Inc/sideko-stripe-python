import pydantic
import typing
import typing_extensions

from .source import Source

if typing_extensions.TYPE_CHECKING:
    from .bank_account import BankAccount
    from .card import Card


class CustomerSources(pydantic.BaseModel):
    """
    The customer's payment sources, if any.
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.List[typing.Union["BankAccount", "Card", Source]] = pydantic.Field(
        alias="data",
    )
    """
    Details about each object.
    """
    has_more: bool = pydantic.Field(
        alias="has_more",
    )
    """
    True if this list has another page of items after this one that can be fetched.
    """
    object: typing_extensions.Literal["list"] = pydantic.Field(
        alias="object",
    )
    """
    String representing the object's type. Objects of the same type share the same value. Always has the value `list`.
    """
    url: str = pydantic.Field(
        alias="url",
    )
    """
    The URL where this list can be accessed.
    """
