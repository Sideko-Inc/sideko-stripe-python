import pydantic
import typing
import typing_extensions

from .subscription_schedule_update_body_default_settings import (
    SubscriptionScheduleUpdateBodyDefaultSettings,
    _SerializerSubscriptionScheduleUpdateBodyDefaultSettings,
)
from .subscription_schedule_update_body_metadata_obj0 import (
    SubscriptionScheduleUpdateBodyMetadataObj0,
    _SerializerSubscriptionScheduleUpdateBodyMetadataObj0,
)
from .subscription_schedule_update_body_phases_item import (
    SubscriptionScheduleUpdateBodyPhasesItem,
    _SerializerSubscriptionScheduleUpdateBodyPhasesItem,
)


class SubscriptionScheduleUpdateBody(typing_extensions.TypedDict, total=False):
    """
    SubscriptionScheduleUpdateBody
    """

    default_settings: typing_extensions.NotRequired[
        SubscriptionScheduleUpdateBodyDefaultSettings
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

    metadata: typing_extensions.NotRequired[
        typing.Union[SubscriptionScheduleUpdateBodyMetadataObj0, str]
    ]
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    """

    phases: typing_extensions.NotRequired[
        typing.List[SubscriptionScheduleUpdateBodyPhasesItem]
    ]
    """
    List representing phases of the subscription schedule. Each phase can be customized to have different durations, plans, and coupons. If there are multiple phases, the `end_date` of one phase will always equal the `start_date` of the next phase. Note that past phases can be omitted.
    """

    proration_behavior: typing_extensions.NotRequired[
        typing_extensions.Literal["always_invoice", "create_prorations", "none"]
    ]
    """
    If the update changes the current phase, indicates whether the changes should be prorated. The default value is `create_prorations`.
    """


class _SerializerSubscriptionScheduleUpdateBody(pydantic.BaseModel):
    """
    Serializer for SubscriptionScheduleUpdateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    default_settings: typing.Optional[
        _SerializerSubscriptionScheduleUpdateBodyDefaultSettings
    ] = pydantic.Field(alias="default_settings", default=None)
    end_behavior: typing.Optional[
        typing_extensions.Literal["cancel", "none", "release", "renew"]
    ] = pydantic.Field(alias="end_behavior", default=None)
    expand: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="expand", default=None
    )
    metadata: typing.Optional[
        typing.Union[_SerializerSubscriptionScheduleUpdateBodyMetadataObj0, str]
    ] = pydantic.Field(alias="metadata", default=None)
    phases: typing.Optional[
        typing.List[_SerializerSubscriptionScheduleUpdateBodyPhasesItem]
    ] = pydantic.Field(alias="phases", default=None)
    proration_behavior: typing.Optional[
        typing_extensions.Literal["always_invoice", "create_prorations", "none"]
    ] = pydantic.Field(alias="proration_behavior", default=None)
