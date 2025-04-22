import pydantic
import typing
import typing_extensions

from .billing_meter_create_body_customer_mapping import (
    BillingMeterCreateBodyCustomerMapping,
    _SerializerBillingMeterCreateBodyCustomerMapping,
)
from .billing_meter_create_body_default_aggregation import (
    BillingMeterCreateBodyDefaultAggregation,
    _SerializerBillingMeterCreateBodyDefaultAggregation,
)
from .billing_meter_create_body_value_settings import (
    BillingMeterCreateBodyValueSettings,
    _SerializerBillingMeterCreateBodyValueSettings,
)


class BillingMeterCreateBody(typing_extensions.TypedDict, total=False):
    """
    BillingMeterCreateBody
    """

    customer_mapping: typing_extensions.NotRequired[
        BillingMeterCreateBodyCustomerMapping
    ]
    """
    Fields that specify how to map a meter event to a customer.
    """

    default_aggregation: typing_extensions.Required[
        BillingMeterCreateBodyDefaultAggregation
    ]
    """
    The default settings to aggregate a meter's events with.
    """

    display_name: typing_extensions.Required[str]
    """
    The meter’s name. Not visible to the customer.
    """

    event_name: typing_extensions.Required[str]
    """
    The name of the meter event to record usage for. Corresponds with the `event_name` field on meter events.
    """

    event_time_window: typing_extensions.NotRequired[
        typing_extensions.Literal["day", "hour"]
    ]
    """
    The time window to pre-aggregate meter events for, if any.
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """

    value_settings: typing_extensions.NotRequired[BillingMeterCreateBodyValueSettings]
    """
    Fields that specify how to calculate a meter event's value.
    """


class _SerializerBillingMeterCreateBody(pydantic.BaseModel):
    """
    Serializer for BillingMeterCreateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    customer_mapping: typing.Optional[
        _SerializerBillingMeterCreateBodyCustomerMapping
    ] = pydantic.Field(alias="customer_mapping", default=None)
    default_aggregation: _SerializerBillingMeterCreateBodyDefaultAggregation = (
        pydantic.Field(
            alias="default_aggregation",
        )
    )
    display_name: str = pydantic.Field(
        alias="display_name",
    )
    event_name: str = pydantic.Field(
        alias="event_name",
    )
    event_time_window: typing.Optional[typing_extensions.Literal["day", "hour"]] = (
        pydantic.Field(alias="event_time_window", default=None)
    )
    expand: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="expand", default=None
    )
    value_settings: typing.Optional[_SerializerBillingMeterCreateBodyValueSettings] = (
        pydantic.Field(alias="value_settings", default=None)
    )
