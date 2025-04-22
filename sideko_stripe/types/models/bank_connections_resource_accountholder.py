import pydantic
import typing
import typing_extensions


if typing_extensions.TYPE_CHECKING:
    from .account import Account
    from .customer import Customer


class BankConnectionsResourceAccountholder(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    account: typing.Optional[typing.Union[str, "Account"]] = pydantic.Field(
        alias="account", default=None
    )
    """
    The ID of the Stripe account this account belongs to. Should only be present if `account_holder.type` is `account`.
    """
    customer: typing.Optional[typing.Union[str, "Customer"]] = pydantic.Field(
        alias="customer", default=None
    )
    """
    ID of the Stripe customer this account belongs to. Present if and only if `account_holder.type` is `customer`.
    """
    type_: typing_extensions.Literal["account", "customer"] = pydantic.Field(
        alias="type",
    )
    """
    Type of account holder that this account belongs to.
    """
