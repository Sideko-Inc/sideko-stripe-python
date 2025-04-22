import pydantic
import typing
import typing_extensions

from .portal_flows_flow_after_completion import PortalFlowsFlowAfterCompletion
from .portal_flows_flow_subscription_cancel import PortalFlowsFlowSubscriptionCancel
from .portal_flows_flow_subscription_update import PortalFlowsFlowSubscriptionUpdate
from .portal_flows_flow_subscription_update_confirm import (
    PortalFlowsFlowSubscriptionUpdateConfirm,
)


class PortalFlowsFlow(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    after_completion: PortalFlowsFlowAfterCompletion = pydantic.Field(
        alias="after_completion",
    )
    subscription_cancel: typing.Optional[PortalFlowsFlowSubscriptionCancel] = (
        pydantic.Field(alias="subscription_cancel", default=None)
    )
    subscription_update: typing.Optional[PortalFlowsFlowSubscriptionUpdate] = (
        pydantic.Field(alias="subscription_update", default=None)
    )
    subscription_update_confirm: typing.Optional[
        PortalFlowsFlowSubscriptionUpdateConfirm
    ] = pydantic.Field(alias="subscription_update_confirm", default=None)
    type_: typing_extensions.Literal[
        "payment_method_update",
        "subscription_cancel",
        "subscription_update",
        "subscription_update_confirm",
    ] = pydantic.Field(
        alias="type",
    )
    """
    Type of flow that the customer will go through.
    """
