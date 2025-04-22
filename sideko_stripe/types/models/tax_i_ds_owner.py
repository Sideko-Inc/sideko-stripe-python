import pydantic
import typing
import typing_extensions

from .application import Application

if typing_extensions.TYPE_CHECKING:
    from .account import Account
    from .customer import Customer


class TaxIDsOwner(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    account: typing.Optional[typing.Union[str, "Account"]] = pydantic.Field(
        alias="account", default=None
    )
    """
    The account being referenced when `type` is `account`.
    """
    application: typing.Optional[typing.Union[str, Application]] = pydantic.Field(
        alias="application", default=None
    )
    """
    The Connect Application being referenced when `type` is `application`.
    """
    customer: typing.Optional[typing.Union[str, "Customer"]] = pydantic.Field(
        alias="customer", default=None
    )
    """
    The customer being referenced when `type` is `customer`.
    """
    type_: typing_extensions.Literal["account", "application", "customer", "self"] = (
        pydantic.Field(
            alias="type",
        )
    )
    """
    Type of owner referenced.
    """
