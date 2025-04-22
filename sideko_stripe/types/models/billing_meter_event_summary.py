import pydantic
import typing_extensions


class BillingMeterEventSummary(pydantic.BaseModel):
    """
    A billing meter event summary represents an aggregated view of a customer's billing meter events within a specified timeframe. It indicates how much
    usage was accrued by a customer for that period.

    Note: Meters events are aggregated asynchronously so the meter event summaries provide an eventually consistent view of the reported usage.
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    aggregated_value: float = pydantic.Field(
        alias="aggregated_value",
    )
    """
    Aggregated value of all the events within `start_time` (inclusive) and `end_time` (inclusive). The aggregation strategy is defined on meter via `default_aggregation`.
    """
    end_time: int = pydantic.Field(
        alias="end_time",
    )
    """
    End timestamp for this event summary (exclusive). Must be aligned with minute boundaries.
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
    meter: str = pydantic.Field(
        alias="meter",
    )
    """
    The meter associated with this event summary.
    """
    object: typing_extensions.Literal["billing.meter_event_summary"] = pydantic.Field(
        alias="object",
    )
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    start_time: int = pydantic.Field(
        alias="start_time",
    )
    """
    Start timestamp for this event summary (inclusive). Must be aligned with minute boundaries.
    """
