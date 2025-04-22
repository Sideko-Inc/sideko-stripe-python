import pydantic
import typing_extensions


class PortalResourceScheduleUpdateAtPeriodEndCondition(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    type_: typing_extensions.Literal[
        "decreasing_item_amount", "shortening_interval"
    ] = pydantic.Field(
        alias="type",
    )
    """
    The type of condition.
    """
