import pydantic
import typing
import typing_extensions

from .billing_meter_resource_aggregation_settings import (
    BillingMeterResourceAggregationSettings,
)
from .billing_meter_resource_billing_meter_status_transitions import (
    BillingMeterResourceBillingMeterStatusTransitions,
)
from .billing_meter_resource_billing_meter_value import (
    BillingMeterResourceBillingMeterValue,
)
from .billing_meter_resource_customer_mapping_settings import (
    BillingMeterResourceCustomerMappingSettings,
)


class BillingMeter(pydantic.BaseModel):
    """
    Meters specify how to aggregate meter events over a billing period. Meter events represent the actions that customers take in your system. Meters attach to prices and form the basis of the bill.

    Related guide: [Usage based billing](https://docs.stripe.com/billing/subscriptions/usage-based)
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
    customer_mapping: BillingMeterResourceCustomerMappingSettings = pydantic.Field(
        alias="customer_mapping",
    )
    default_aggregation: BillingMeterResourceAggregationSettings = pydantic.Field(
        alias="default_aggregation",
    )
    display_name: str = pydantic.Field(
        alias="display_name",
    )
    """
    The meter's name.
    """
    event_name: str = pydantic.Field(
        alias="event_name",
    )
    """
    The name of the meter event to record usage for. Corresponds with the `event_name` field on meter events.
    """
    event_time_window: typing.Optional[typing_extensions.Literal["day", "hour"]] = (
        pydantic.Field(alias="event_time_window", default=None)
    )
    """
    The time window to pre-aggregate meter events for, if any.
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
    object: typing_extensions.Literal["billing.meter"] = pydantic.Field(
        alias="object",
    )
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    status: typing_extensions.Literal["active", "inactive"] = pydantic.Field(
        alias="status",
    )
    """
    The meter's status.
    """
    status_transitions: BillingMeterResourceBillingMeterStatusTransitions = (
        pydantic.Field(
            alias="status_transitions",
        )
    )
    updated: int = pydantic.Field(
        alias="updated",
    )
    """
    Time at which the object was last updated. Measured in seconds since the Unix epoch.
    """
    value_settings: BillingMeterResourceBillingMeterValue = pydantic.Field(
        alias="value_settings",
    )
