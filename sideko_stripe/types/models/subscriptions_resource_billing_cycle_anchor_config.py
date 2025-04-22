import pydantic
import typing


class SubscriptionsResourceBillingCycleAnchorConfig(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    day_of_month: int = pydantic.Field(
        alias="day_of_month",
    )
    """
    The day of the month of the billing_cycle_anchor.
    """
    hour: typing.Optional[int] = pydantic.Field(alias="hour", default=None)
    """
    The hour of the day of the billing_cycle_anchor.
    """
    minute: typing.Optional[int] = pydantic.Field(alias="minute", default=None)
    """
    The minute of the hour of the billing_cycle_anchor.
    """
    month: typing.Optional[int] = pydantic.Field(alias="month", default=None)
    """
    The month to start full cycle billing periods.
    """
    second: typing.Optional[int] = pydantic.Field(alias="second", default=None)
    """
    The second of the minute of the billing_cycle_anchor.
    """
