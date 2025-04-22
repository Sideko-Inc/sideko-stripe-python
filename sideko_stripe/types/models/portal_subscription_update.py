import pydantic
import typing
import typing_extensions

from .portal_resource_schedule_update_at_period_end import (
    PortalResourceScheduleUpdateAtPeriodEnd,
)
from .portal_subscription_update_product import PortalSubscriptionUpdateProduct


class PortalSubscriptionUpdate(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    default_allowed_updates: typing.List[
        typing_extensions.Literal["price", "promotion_code", "quantity"]
    ] = pydantic.Field(
        alias="default_allowed_updates",
    )
    """
    The types of subscription updates that are supported for items listed in the `products` attribute. When empty, subscriptions are not updateable.
    """
    enabled: bool = pydantic.Field(
        alias="enabled",
    )
    """
    Whether the feature is enabled.
    """
    products: typing.Optional[typing.List[PortalSubscriptionUpdateProduct]] = (
        pydantic.Field(alias="products", default=None)
    )
    """
    The list of up to 10 products that support subscription updates.
    """
    proration_behavior: typing_extensions.Literal[
        "always_invoice", "create_prorations", "none"
    ] = pydantic.Field(
        alias="proration_behavior",
    )
    """
    Determines how to handle prorations resulting from subscription updates. Valid values are `none`, `create_prorations`, and `always_invoice`. Defaults to a value of `none` if you don't set it during creation.
    """
    schedule_at_period_end: PortalResourceScheduleUpdateAtPeriodEnd = pydantic.Field(
        alias="schedule_at_period_end",
    )
