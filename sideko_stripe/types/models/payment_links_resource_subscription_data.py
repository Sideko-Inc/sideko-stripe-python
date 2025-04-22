import pydantic
import typing
import typing_extensions

from .payment_links_resource_subscription_data_metadata import (
    PaymentLinksResourceSubscriptionDataMetadata,
)
from .subscriptions_trials_resource_trial_settings import (
    SubscriptionsTrialsResourceTrialSettings,
)

if typing_extensions.TYPE_CHECKING:
    from .payment_links_resource_subscription_data_invoice_settings import (
        PaymentLinksResourceSubscriptionDataInvoiceSettings,
    )


class PaymentLinksResourceSubscriptionData(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    description: typing.Optional[str] = pydantic.Field(
        alias="description", default=None
    )
    """
    The subscription's description, meant to be displayable to the customer. Use this field to optionally store an explanation of the subscription for rendering in Stripe surfaces and certain local payment methods UIs.
    """
    invoice_settings: "PaymentLinksResourceSubscriptionDataInvoiceSettings" = (
        pydantic.Field(
            alias="invoice_settings",
        )
    )
    metadata: PaymentLinksResourceSubscriptionDataMetadata = pydantic.Field(
        alias="metadata",
    )
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that will set metadata on [Subscriptions](https://stripe.com/docs/api/subscriptions) generated from this payment link.
    """
    trial_period_days: typing.Optional[int] = pydantic.Field(
        alias="trial_period_days", default=None
    )
    """
    Integer representing the number of trial period days before the customer is charged for the first time.
    """
    trial_settings: typing.Optional[SubscriptionsTrialsResourceTrialSettings] = (
        pydantic.Field(alias="trial_settings", default=None)
    )
    """
    Configures how this subscription behaves during the trial period.
    """
