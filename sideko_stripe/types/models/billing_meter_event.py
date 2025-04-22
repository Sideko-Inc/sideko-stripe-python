import pydantic
import typing_extensions

from .billing_meter_event_payload import BillingMeterEventPayload


class BillingMeterEvent(pydantic.BaseModel):
    """
    Meter events represent actions that customers take in your system. You can use meter events to bill a customer based on their usage. Meter events are associated with billing meters, which define both the contents of the event’s payload and how to aggregate those events.
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    created: int = pydantic.Field(
        alias="created",
    )
    """
    Time at which the object was created. Measured in seconds since the Unix epoch.
    """
    event_name: str = pydantic.Field(
        alias="event_name",
    )
    """
    The name of the meter event. Corresponds with the `event_name` field on a meter.
    """
    identifier: str = pydantic.Field(
        alias="identifier",
    )
    """
    A unique identifier for the event.
    """
    livemode: bool = pydantic.Field(
        alias="livemode",
    )
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    object: typing_extensions.Literal["billing.meter_event"] = pydantic.Field(
        alias="object",
    )
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    payload: BillingMeterEventPayload = pydantic.Field(
        alias="payload",
    )
    """
    The payload of the event. This contains the fields corresponding to a meter's `customer_mapping.event_payload_key` (default is `stripe_customer_id`) and `value_settings.event_payload_key` (default is `value`). Read more about the [payload](https://stripe.com/docs/billing/subscriptions/usage-based/recording-usage#payload-key-overrides).
    """
    timestamp: int = pydantic.Field(
        alias="timestamp",
    )
    """
    The timestamp passed in when creating the event. Measured in seconds since the Unix epoch.
    """
