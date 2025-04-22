import pydantic


class SubscriptionScheduleCurrentPhase(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    end_date: int = pydantic.Field(
        alias="end_date",
    )
    """
    The end of this phase of the subscription schedule.
    """
    start_date: int = pydantic.Field(
        alias="start_date",
    )
    """
    The start of this phase of the subscription schedule.
    """
