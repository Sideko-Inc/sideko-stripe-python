import pydantic
import typing_extensions

from .portal_subscription_cancellation_reason import (
    PortalSubscriptionCancellationReason,
)


class PortalSubscriptionCancel(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    cancellation_reason: PortalSubscriptionCancellationReason = pydantic.Field(
        alias="cancellation_reason",
    )
    enabled: bool = pydantic.Field(
        alias="enabled",
    )
    """
    Whether the feature is enabled.
    """
    mode: typing_extensions.Literal["at_period_end", "immediately"] = pydantic.Field(
        alias="mode",
    )
    """
    Whether to cancel subscriptions immediately or at the end of the billing period.
    """
    proration_behavior: typing_extensions.Literal[
        "always_invoice", "create_prorations", "none"
    ] = pydantic.Field(
        alias="proration_behavior",
    )
    """
    Whether to create prorations when canceling subscriptions. Possible values are `none` and `create_prorations`.
    """
