import pydantic
import typing
import typing_extensions


if typing_extensions.TYPE_CHECKING:
    from .bank_account import BankAccount
    from .card import Card


class AccountExternalAccountListResponse(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.List[typing.Union["BankAccount", "Card"]] = pydantic.Field(
        alias="data",
    )
    """
    The list contains all external accounts that have been attached to the Stripe account. These may be bank accounts or cards.
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
