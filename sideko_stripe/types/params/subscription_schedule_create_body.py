import pydantic
import typing
import typing_extensions

from .subscription_schedule_create_body_default_settings import (
    SubscriptionScheduleCreateBodyDefaultSettings,
    _SerializerSubscriptionScheduleCreateBodyDefaultSettings,
)
from .subscription_schedule_create_body_metadata_obj0 import (
    SubscriptionScheduleCreateBodyMetadataObj0,
    _SerializerSubscriptionScheduleCreateBodyMetadataObj0,
)
from .subscription_schedule_create_body_phases_item import (
    SubscriptionScheduleCreateBodyPhasesItem,
    _SerializerSubscriptionScheduleCreateBodyPhasesItem,
)


class SubscriptionScheduleCreateBody(typing_extensions.TypedDict, total=False):
    """
    SubscriptionScheduleCreateBody
    """

    customer: typing_extensions.NotRequired[str]
    """
    The identifier of the customer to create the subscription schedule for.
    """

    default_settings: typing_extensions.NotRequired[
        SubscriptionScheduleCreateBodyDefaultSettings
    ]
    """
    Object representing the subscription schedule's default settings.
    """

    end_behavior: typing_extensions.NotRequired[
        typing_extensions.Literal["cancel", "none", "release", "renew"]
    ]
    """
    Behavior of the subscription schedule and underlying subscription when it ends. Possible values are `release` or `cancel` with the default being `release`. `release` will end the subscription schedule and keep the underlying subscription running. `cancel` will end the subscription schedule and cancel the underlying subscription.
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """

    from_subscription: typing_extensions.NotRequired[str]
    """
    Migrate an existing subscription to be managed by a subscription schedule. If this parameter is set, a subscription schedule will be created using the subscription's item(s), set to auto-renew using the subscription's interval. When using this parameter, other parameters (such as phase values) cannot be set. To create a subscription schedule with other modifications, we recommend making two separate API calls.
    """

    metadata: typing_extensions.NotRequired[
        typing.Union[SubscriptionScheduleCreateBodyMetadataObj0, str]
    ]
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    """

    phases: typing_extensions.NotRequired[
        typing.List[SubscriptionScheduleCreateBodyPhasesItem]
    ]
    """
    List representing phases of the subscription schedule. Each phase can be customized to have different durations, plans, and coupons. If there are multiple phases, the `end_date` of one phase will always equal the `start_date` of the next phase.
    """

    start_date: typing_extensions.NotRequired[
        typing.Union[int, typing_extensions.Literal["now"]]
    ]
    """
    When the subscription schedule starts. We recommend using `now` so that it starts the subscription immediately. You can also use a Unix timestamp to backdate the subscription so that it starts on a past date, or set a future date for the subscription to start on.
    """


class _SerializerSubscriptionScheduleCreateBody(pydantic.BaseModel):
    """
    Serializer for SubscriptionScheduleCreateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    customer: typing.Optional[str] = pydantic.Field(alias="customer", default=None)
    default_settings: typing.Optional[
        _SerializerSubscriptionScheduleCreateBodyDefaultSettings
    ] = pydantic.Field(alias="default_settings", default=None)
    end_behavior: typing.Optional[
        typing_extensions.Literal["cancel", "none", "release", "renew"]
    ] = pydantic.Field(alias="end_behavior", default=None)
    expand: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="expand", default=None
    )
    from_subscription: typing.Optional[str] = pydantic.Field(
        alias="from_subscription", default=None
    )
    metadata: typing.Optional[
        typing.Union[_SerializerSubscriptionScheduleCreateBodyMetadataObj0, str]
    ] = pydantic.Field(alias="metadata", default=None)
    phases: typing.Optional[
        typing.List[_SerializerSubscriptionScheduleCreateBodyPhasesItem]
    ] = pydantic.Field(alias="phases", default=None)
    start_date: typing.Optional[typing.Union[int, typing_extensions.Literal["now"]]] = (
        pydantic.Field(alias="start_date", default=None)
    )
