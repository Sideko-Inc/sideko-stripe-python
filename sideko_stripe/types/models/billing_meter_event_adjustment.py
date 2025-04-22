import pydantic
import typing
import typing_extensions

from .billing_meter_resource_billing_meter_event_adjustment_cancel import (
    BillingMeterResourceBillingMeterEventAdjustmentCancel,
)


class BillingMeterEventAdjustment(pydantic.BaseModel):
    """
    A billing meter event adjustment is a resource that allows you to cancel a meter event. For example, you might create a billing meter event adjustment to cancel a meter event that was created in error or attached to the wrong customer.
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    cancel: typing.Optional[BillingMeterResourceBillingMeterEventAdjustmentCancel] = (
        pydantic.Field(alias="cancel", default=None)
    )
    event_name: str = pydantic.Field(
        alias="event_name",
    )
    """
    The name of the meter event. Corresponds with the `event_name` field on a meter.
    """
    livemode: bool = pydantic.Field(
        alias="livemode",
    )
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    object: typing_extensions.Literal["billing.meter_event_adjustment"] = (
        pydantic.Field(
            alias="object",
        )
    )
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    status: typing_extensions.Literal["complete", "pending"] = pydantic.Field(
        alias="status",
    )
    """
    The meter event adjustment's status.
    """
    type_: typing_extensions.Literal["cancel"] = pydantic.Field(
        alias="type",
    )
    """
    Specifies whether to cancel a single event or a range of events for a time period. Time period cancellation is not supported yet.
    """
