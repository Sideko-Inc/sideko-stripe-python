import pydantic
import typing
import typing_extensions

from .account_create_body_controller_fees import (
    AccountCreateBodyControllerFees,
    _SerializerAccountCreateBodyControllerFees,
)
from .account_create_body_controller_losses import (
    AccountCreateBodyControllerLosses,
    _SerializerAccountCreateBodyControllerLosses,
)
from .account_create_body_controller_stripe_dashboard import (
    AccountCreateBodyControllerStripeDashboard,
    _SerializerAccountCreateBodyControllerStripeDashboard,
)


class AccountCreateBodyController(typing_extensions.TypedDict):
    """
    A hash of configuration describing the account controller's attributes.
    """

    fees: typing_extensions.NotRequired[AccountCreateBodyControllerFees]

    losses: typing_extensions.NotRequired[AccountCreateBodyControllerLosses]

    requirement_collection: typing_extensions.NotRequired[
        typing_extensions.Literal["application", "stripe"]
    ]

    stripe_dashboard: typing_extensions.NotRequired[
        AccountCreateBodyControllerStripeDashboard
    ]


class _SerializerAccountCreateBodyController(pydantic.BaseModel):
    """
    Serializer for AccountCreateBodyController handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    fees: typing.Optional[_SerializerAccountCreateBodyControllerFees] = pydantic.Field(
        alias="fees", default=None
    )
    losses: typing.Optional[_SerializerAccountCreateBodyControllerLosses] = (
        pydantic.Field(alias="losses", default=None)
    )
    requirement_collection: typing.Optional[
        typing_extensions.Literal["application", "stripe"]
    ] = pydantic.Field(alias="requirement_collection", default=None)
    stripe_dashboard: typing.Optional[
        _SerializerAccountCreateBodyControllerStripeDashboard
    ] = pydantic.Field(alias="stripe_dashboard", default=None)
