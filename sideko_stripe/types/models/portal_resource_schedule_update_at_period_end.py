import pydantic
import typing

from .portal_resource_schedule_update_at_period_end_condition import (
    PortalResourceScheduleUpdateAtPeriodEndCondition,
)


class PortalResourceScheduleUpdateAtPeriodEnd(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    conditions: typing.List[PortalResourceScheduleUpdateAtPeriodEndCondition] = (
        pydantic.Field(
            alias="conditions",
        )
    )
    """
    List of conditions. When any condition is true, an update will be scheduled at the end of the current period.
    """
