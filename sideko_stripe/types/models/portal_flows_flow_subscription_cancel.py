import pydantic
import typing

from .portal_flows_retention import PortalFlowsRetention


class PortalFlowsFlowSubscriptionCancel(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    retention: typing.Optional[PortalFlowsRetention] = pydantic.Field(
        alias="retention", default=None
    )
    subscription: str = pydantic.Field(
        alias="subscription",
    )
    """
    The ID of the subscription to be canceled.
    """
