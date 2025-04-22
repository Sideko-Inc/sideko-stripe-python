import pydantic
import typing
import typing_extensions

from .account_capability_future_requirements import AccountCapabilityFutureRequirements
from .account_capability_requirements import AccountCapabilityRequirements

if typing_extensions.TYPE_CHECKING:
    from .account import Account


class Capability(pydantic.BaseModel):
    """
    This is an object representing a capability for a Stripe account.

    Related guide: [Account capabilities](https://stripe.com/docs/connect/account-capabilities)
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    account: typing.Union[str, "Account"] = pydantic.Field(
        alias="account",
    )
    """
    The account for which the capability enables functionality.
    """
    future_requirements: typing.Optional[AccountCapabilityFutureRequirements] = (
        pydantic.Field(alias="future_requirements", default=None)
    )
    id: str = pydantic.Field(
        alias="id",
    )
    """
    The identifier for the capability.
    """
    object: typing_extensions.Literal["capability"] = pydantic.Field(
        alias="object",
    )
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    requested: bool = pydantic.Field(
        alias="requested",
    )
    """
    Whether the capability has been requested.
    """
    requested_at: typing.Optional[int] = pydantic.Field(
        alias="requested_at", default=None
    )
    """
    Time at which the capability was requested. Measured in seconds since the Unix epoch.
    """
    requirements: typing.Optional[AccountCapabilityRequirements] = pydantic.Field(
        alias="requirements", default=None
    )
    status: typing_extensions.Literal[
        "active", "disabled", "inactive", "pending", "unrequested"
    ] = pydantic.Field(
        alias="status",
    )
    """
    The status of the capability.
    """
