import pydantic
import typing
import typing_extensions


if typing_extensions.TYPE_CHECKING:
    from .subscription_item import SubscriptionItem


class SubscriptionsResourcePendingUpdate(pydantic.BaseModel):
    """
    Pending Updates store the changes pending from a previous update that will be applied
    to the Subscription upon successful payment.
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    billing_cycle_anchor: typing.Optional[int] = pydantic.Field(
        alias="billing_cycle_anchor", default=None
    )
    """
    If the update is applied, determines the date of the first full invoice, and, for plans with `month` or `year` intervals, the day of the month for subsequent invoices. The timestamp is in UTC format.
    """
    expires_at: int = pydantic.Field(
        alias="expires_at",
    )
    """
    The point after which the changes reflected by this update will be discarded and no longer applied.
    """
    subscription_items: typing.Optional[typing.List["SubscriptionItem"]] = (
        pydantic.Field(alias="subscription_items", default=None)
    )
    """
    List of subscription items, each with an attached plan, that will be set if the update is applied.
    """
    trial_end: typing.Optional[int] = pydantic.Field(alias="trial_end", default=None)
    """
    Unix timestamp representing the end of the trial period the customer will get before being charged for the first time, if the update is applied.
    """
    trial_from_plan: typing.Optional[bool] = pydantic.Field(
        alias="trial_from_plan", default=None
    )
    """
    Indicates if a plan's `trial_period_days` should be applied to the subscription. Setting `trial_end` per subscription is preferred, and this defaults to `false`. Setting this flag to `true` together with `trial_end` is not allowed. See [Using trial periods on subscriptions](https://stripe.com/docs/billing/subscriptions/trials) to learn more.
    """
