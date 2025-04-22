import pydantic
import typing

from .portal_flows_subscription_update_confirm_discount import (
    PortalFlowsSubscriptionUpdateConfirmDiscount,
)
from .portal_flows_subscription_update_confirm_item import (
    PortalFlowsSubscriptionUpdateConfirmItem,
)


class PortalFlowsFlowSubscriptionUpdateConfirm(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    discounts: typing.Optional[
        typing.List[PortalFlowsSubscriptionUpdateConfirmDiscount]
    ] = pydantic.Field(alias="discounts", default=None)
    """
    The coupon or promotion code to apply to this subscription update. Currently, only up to one may be specified.
    """
    items: typing.List[PortalFlowsSubscriptionUpdateConfirmItem] = pydantic.Field(
        alias="items",
    )
    """
    The [subscription item](https://stripe.com/docs/api/subscription_items) to be updated through this flow. Currently, only up to one may be specified and subscriptions with multiple items are not updatable.
    """
    subscription: str = pydantic.Field(
        alias="subscription",
    )
    """
    The ID of the subscription to be updated.
    """
