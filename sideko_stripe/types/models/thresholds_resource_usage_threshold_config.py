import pydantic
import typing
import typing_extensions

from .billing_meter import BillingMeter

if typing_extensions.TYPE_CHECKING:
    from .thresholds_resource_usage_alert_filter import (
        ThresholdsResourceUsageAlertFilter,
    )


class ThresholdsResourceUsageThresholdConfig(pydantic.BaseModel):
    """
    The usage threshold alert configuration enables setting up alerts for when a certain usage threshold on a specific meter is crossed.
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    filters: typing.Optional[typing.List["ThresholdsResourceUsageAlertFilter"]] = (
        pydantic.Field(alias="filters", default=None)
    )
    """
    The filters allow limiting the scope of this usage alert. You can only specify up to one filter at this time.
    """
    gte: int = pydantic.Field(
        alias="gte",
    )
    """
    The value at which this alert will trigger.
    """
    meter: typing.Union[str, BillingMeter] = pydantic.Field(
        alias="meter",
    )
    """
    The [Billing Meter](/api/billing/meter) ID whose usage is monitored.
    """
    recurrence: typing_extensions.Literal["one_time"] = pydantic.Field(
        alias="recurrence",
    )
    """
    Defines how the alert will behave.
    """
