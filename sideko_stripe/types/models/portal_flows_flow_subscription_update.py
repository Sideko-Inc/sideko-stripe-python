import pydantic


class PortalFlowsFlowSubscriptionUpdate(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    subscription: str = pydantic.Field(
        alias="subscription",
    )
    """
    The ID of the subscription to be updated.
    """
