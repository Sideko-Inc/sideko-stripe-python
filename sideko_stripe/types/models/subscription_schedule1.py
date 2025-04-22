import pydantic
import typing
import typing_extensions

from .application import Application
from .deleted_application import DeletedApplication
from .deleted_customer import DeletedCustomer
from .subscription_schedule_current_phase import SubscriptionScheduleCurrentPhase
from .subscription_schedule_metadata import SubscriptionScheduleMetadata
from .test_helpers_test_clock import TestHelpersTestClock

if typing_extensions.TYPE_CHECKING:
    from .customer import Customer
    from .subscription import Subscription
    from .subscription_schedule_phase_configuration import (
        SubscriptionSchedulePhaseConfiguration,
    )
    from .subscription_schedules_resource_default_settings import (
        SubscriptionSchedulesResourceDefaultSettings,
    )


class SubscriptionSchedule1(pydantic.BaseModel):
    """
    A subscription schedule allows you to create and manage the lifecycle of a subscription by predefining expected changes.

    Related guide: [Subscription schedules](https://stripe.com/docs/billing/subscriptions/subscription-schedules)
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    application: typing.Optional[typing.Union[str, Application, DeletedApplication]] = (
        pydantic.Field(alias="application", default=None)
    )
    """
    ID of the Connect Application that created the schedule.
    """
    canceled_at: typing.Optional[int] = pydantic.Field(
        alias="canceled_at", default=None
    )
    """
    Time at which the subscription schedule was canceled. Measured in seconds since the Unix epoch.
    """
    completed_at: typing.Optional[int] = pydantic.Field(
        alias="completed_at", default=None
    )
    """
    Time at which the subscription schedule was completed. Measured in seconds since the Unix epoch.
    """
    created: int = pydantic.Field(
        alias="created",
    )
    """
    Time at which the object was created. Measured in seconds since the Unix epoch.
    """
    current_phase: typing.Optional[SubscriptionScheduleCurrentPhase] = pydantic.Field(
        alias="current_phase", default=None
    )
    customer: typing.Union[str, "Customer", DeletedCustomer] = pydantic.Field(
        alias="customer",
    )
    """
    ID of the customer who owns the subscription schedule.
    """
    default_settings: "SubscriptionSchedulesResourceDefaultSettings" = pydantic.Field(
        alias="default_settings",
    )
    end_behavior: typing_extensions.Literal["cancel", "none", "release", "renew"] = (
        pydantic.Field(
            alias="end_behavior",
        )
    )
    """
    Behavior of the subscription schedule and underlying subscription when it ends. Possible values are `release` or `cancel` with the default being `release`. `release` will end the subscription schedule and keep the underlying subscription running. `cancel` will end the subscription schedule and cancel the underlying subscription.
    """
    id: str = pydantic.Field(
        alias="id",
    )
    """
    Unique identifier for the object.
    """
    livemode: bool = pydantic.Field(
        alias="livemode",
    )
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    metadata: typing.Optional[SubscriptionScheduleMetadata] = pydantic.Field(
        alias="metadata", default=None
    )
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    object: typing_extensions.Literal["subscription_schedule"] = pydantic.Field(
        alias="object",
    )
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    phases: typing.List["SubscriptionSchedulePhaseConfiguration"] = pydantic.Field(
        alias="phases",
    )
    """
    Configuration for the subscription schedule's phases.
    """
    released_at: typing.Optional[int] = pydantic.Field(
        alias="released_at", default=None
    )
    """
    Time at which the subscription schedule was released. Measured in seconds since the Unix epoch.
    """
    released_subscription: typing.Optional[str] = pydantic.Field(
        alias="released_subscription", default=None
    )
    """
    ID of the subscription once managed by the subscription schedule (if it is released).
    """
    status: typing_extensions.Literal[
        "active", "canceled", "completed", "not_started", "released"
    ] = pydantic.Field(
        alias="status",
    )
    """
    The present status of the subscription schedule. Possible values are `not_started`, `active`, `completed`, `released`, and `canceled`. You can read more about the different states in our [behavior guide](https://stripe.com/docs/billing/subscriptions/subscription-schedules).
    """
    subscription: typing.Optional[typing.Union[str, "Subscription"]] = pydantic.Field(
        alias="subscription", default=None
    )
    """
    ID of the subscription managed by the subscription schedule.
    """
    test_clock: typing.Optional[typing.Union[str, TestHelpersTestClock]] = (
        pydantic.Field(alias="test_clock", default=None)
    )
    """
    ID of the test clock this subscription schedule belongs to.
    """
