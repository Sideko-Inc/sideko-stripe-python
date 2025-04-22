import pydantic
import typing
import typing_extensions

from .account_unification_account_controller_fees import (
    AccountUnificationAccountControllerFees,
)
from .account_unification_account_controller_losses import (
    AccountUnificationAccountControllerLosses,
)
from .account_unification_account_controller_stripe_dashboard import (
    AccountUnificationAccountControllerStripeDashboard,
)


class AccountUnificationAccountController(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    fees: typing.Optional[AccountUnificationAccountControllerFees] = pydantic.Field(
        alias="fees", default=None
    )
    is_controller: typing.Optional[bool] = pydantic.Field(
        alias="is_controller", default=None
    )
    """
    `true` if the Connect application retrieving the resource controls the account and can therefore exercise [platform controls](https://stripe.com/docs/connect/platform-controls-for-standard-accounts). Otherwise, this field is null.
    """
    losses: typing.Optional[AccountUnificationAccountControllerLosses] = pydantic.Field(
        alias="losses", default=None
    )
    requirement_collection: typing.Optional[
        typing_extensions.Literal["application", "stripe"]
    ] = pydantic.Field(alias="requirement_collection", default=None)
    """
    A value indicating responsibility for collecting requirements on this account. Only returned when the Connect application retrieving the resource controls the account.
    """
    stripe_dashboard: typing.Optional[
        AccountUnificationAccountControllerStripeDashboard
    ] = pydantic.Field(alias="stripe_dashboard", default=None)
    type_: typing_extensions.Literal["account", "application"] = pydantic.Field(
        alias="type",
    )
    """
    The controller type. Can be `application`, if a Connect application controls the account, or `account`, if the account controls itself.
    """
