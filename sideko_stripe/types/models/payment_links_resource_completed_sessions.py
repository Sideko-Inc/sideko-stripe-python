import pydantic


class PaymentLinksResourceCompletedSessions(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    count: int = pydantic.Field(
        alias="count",
    )
    """
    The current number of checkout sessions that have been completed on the payment link which count towards the `completed_sessions` restriction to be met.
    """
    limit: int = pydantic.Field(
        alias="limit",
    )
    """
    The maximum number of checkout sessions that can be completed for the `completed_sessions` restriction to be met.
    """
