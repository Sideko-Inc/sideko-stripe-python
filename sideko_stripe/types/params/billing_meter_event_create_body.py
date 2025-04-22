import pydantic
import typing
import typing_extensions

from .billing_meter_event_create_body_payload import (
    BillingMeterEventCreateBodyPayload,
    _SerializerBillingMeterEventCreateBodyPayload,
)


class BillingMeterEventCreateBody(typing_extensions.TypedDict, total=False):
    """
    BillingMeterEventCreateBody
    """

    event_name: typing_extensions.Required[str]
    """
    The name of the meter event. Corresponds with the `event_name` field on a meter.
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """

    identifier: typing_extensions.NotRequired[str]
    """
    A unique identifier for the event. If not provided, one is generated. We recommend using UUID-like identifiers. We will enforce uniqueness within a rolling period of at least 24 hours. The enforcement of uniqueness primarily addresses issues arising from accidental retries or other problems occurring within extremely brief time intervals. This approach helps prevent duplicate entries and ensures data integrity in high-frequency operations.
    """

    payload: typing_extensions.Required[BillingMeterEventCreateBodyPayload]
    """
    The payload of the event. This must contain the fields corresponding to a meter's `customer_mapping.event_payload_key` (default is `stripe_customer_id`) and `value_settings.event_payload_key` (default is `value`). Read more about the [payload](https://docs.stripe.com/billing/subscriptions/usage-based/recording-usage#payload-key-overrides).
    """

    timestamp: typing_extensions.NotRequired[int]
    """
    The time of the event. Measured in seconds since the Unix epoch. Must be within the past 35 calendar days or up to 5 minutes in the future. Defaults to current timestamp if not specified.
    """


class _SerializerBillingMeterEventCreateBody(pydantic.BaseModel):
    """
    Serializer for BillingMeterEventCreateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    event_name: str = pydantic.Field(
        alias="event_name",
    )
    expand: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="expand", default=None
    )
    identifier: typing.Optional[str] = pydantic.Field(alias="identifier", default=None)
    payload: _SerializerBillingMeterEventCreateBodyPayload = pydantic.Field(
        alias="payload",
    )
    timestamp: typing.Optional[int] = pydantic.Field(alias="timestamp", default=None)
