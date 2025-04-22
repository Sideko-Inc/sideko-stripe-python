import pydantic
import typing
import typing_extensions


if typing_extensions.TYPE_CHECKING:
    from .account import Account


class ConnectAccountReference(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    account: typing.Optional[typing.Union[str, "Account"]] = pydantic.Field(
        alias="account", default=None
    )
    """
    The connected account being referenced when `type` is `account`.
    """
    type_: typing_extensions.Literal["account", "self"] = pydantic.Field(
        alias="type",
    )
    """
    Type of the account referenced.
    """
