import pydantic
import typing
import typing_extensions

from .application import Application
from .cancellation_details import CancellationDetails
from .deleted_application import DeletedApplication
from .deleted_customer import DeletedCustomer
from .source import Source
from .subscription_metadata import SubscriptionMetadata
from .subscription_pending_invoice_item_interval import (
    SubscriptionPendingInvoiceItemInterval,
)
from .subscriptions_resource_billing_cycle_anchor_config import (
    SubscriptionsResourceBillingCycleAnchorConfig,
)
from .subscriptions_resource_pause_collection import (
    SubscriptionsResourcePauseCollection,
)
from .subscriptions_resource_payment_settings import (
    SubscriptionsResourcePaymentSettings,
)
from .subscriptions_trials_resource_trial_settings import (
    SubscriptionsTrialsResourceTrialSettings,
)
from .tax_rate import TaxRate
from .test_helpers_test_clock import TestHelpersTestClock

if typing_extensions.TYPE_CHECKING:
    from .account import Account
    from .bank_account import BankAccount
    from .card import Card
    from .customer import Customer
    from .discount import Discount
    from .invoice import Invoice
    from .payment_method import PaymentMethod
    from .setup_intent import SetupIntent
    from .subscription_automatic_tax import SubscriptionAutomaticTax
    from .subscription_items import SubscriptionItems
    from .subscription_schedule1 import SubscriptionSchedule1
    from .subscription_transfer_data import SubscriptionTransferData
    from .subscriptions_resource_pending_update import (
        SubscriptionsResourcePendingUpdate,
    )
    from .subscriptions_resource_subscription_invoice_settings import (
        SubscriptionsResourceSubscriptionInvoiceSettings,
    )


class Subscription(pydantic.BaseModel):
    """
    Subscriptions allow you to charge a customer on a recurring basis.

    Related guide: [Creating subscriptions](https://stripe.com/docs/billing/subscriptions/creating)
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    application: typing.Optional[typing.Union[str, Application, DeletedApplication]] = (
        pydantic.Field(alias="application", default=None)
    )
    """
    ID of the Connect Application that created the subscription.
    """
    application_fee_percent: typing.Optional[float] = pydantic.Field(
        alias="application_fee_percent", default=None
    )
    """
    A non-negative decimal between 0 and 100, with at most two decimal places. This represents the percentage of the subscription invoice total that will be transferred to the application owner's Stripe account.
    """
    automatic_tax: "SubscriptionAutomaticTax" = pydantic.Field(
        alias="automatic_tax",
    )
    billing_cycle_anchor: int = pydantic.Field(
        alias="billing_cycle_anchor",
    )
    """
    The reference point that aligns future [billing cycle](https://stripe.com/docs/subscriptions/billing-cycle) dates. It sets the day of week for `week` intervals, the day of month for `month` and `year` intervals, and the month of year for `year` intervals. The timestamp is in UTC format.
    """
    billing_cycle_anchor_config: typing.Optional[
        SubscriptionsResourceBillingCycleAnchorConfig
    ] = pydantic.Field(alias="billing_cycle_anchor_config", default=None)
    cancel_at: typing.Optional[int] = pydantic.Field(alias="cancel_at", default=None)
    """
    A date in the future at which the subscription will automatically get canceled
    """
    cancel_at_period_end: typing.Optional[bool] = pydantic.Field(
        alias="cancel_at_period_end", default=None
    )
    """
    Whether this subscription will (if `status=active`) or did (if `status=canceled`) cancel at the end of the current billing period.
    """
    canceled_at: typing.Optional[int] = pydantic.Field(
        alias="canceled_at", default=None
    )
    """
    If the subscription has been canceled, the date of that cancellation. If the subscription was canceled with `cancel_at_period_end`, `canceled_at` will reflect the time of the most recent update request, not the end of the subscription period when the subscription is automatically moved to a canceled state.
    """
    cancellation_details: typing.Optional[CancellationDetails] = pydantic.Field(
        alias="cancellation_details", default=None
    )
    collection_method: typing_extensions.Literal[
        "charge_automatically", "send_invoice"
    ] = pydantic.Field(
        alias="collection_method",
    )
    """
    Either `charge_automatically`, or `send_invoice`. When charging automatically, Stripe will attempt to pay this subscription at the end of the cycle using the default source attached to the customer. When sending an invoice, Stripe will email your customer an invoice with payment instructions and mark the subscription as `active`.
    """
    created: int = pydantic.Field(
        alias="created",
    )
    """
    Time at which the object was created. Measured in seconds since the Unix epoch.
    """
    currency: str = pydantic.Field(
        alias="currency",
    )
    """
    Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    """
    customer: typing.Union[str, "Customer", DeletedCustomer] = pydantic.Field(
        alias="customer",
    )
    """
    ID of the customer who owns the subscription.
    """
    days_until_due: typing.Optional[int] = pydantic.Field(
        alias="days_until_due", default=None
    )
    """
    Number of days a customer has to pay invoices generated by this subscription. This value will be `null` for subscriptions where `collection_method=charge_automatically`.
    """
    default_payment_method: typing.Optional[typing.Union[str, "PaymentMethod"]] = (
        pydantic.Field(alias="default_payment_method", default=None)
    )
    """
    ID of the default payment method for the subscription. It must belong to the customer associated with the subscription. This takes precedence over `default_source`. If neither are set, invoices will use the customer's [invoice_settings.default_payment_method](https://stripe.com/docs/api/customers/object#customer_object-invoice_settings-default_payment_method) or [default_source](https://stripe.com/docs/api/customers/object#customer_object-default_source).
    """
    default_source: typing.Optional[
        typing.Union[str, "BankAccount", "Card", Source]
    ] = pydantic.Field(alias="default_source", default=None)
    """
    ID of the default payment source for the subscription. It must belong to the customer associated with the subscription and be in a chargeable state. If `default_payment_method` is also set, `default_payment_method` will take precedence. If neither are set, invoices will use the customer's [invoice_settings.default_payment_method](https://stripe.com/docs/api/customers/object#customer_object-invoice_settings-default_payment_method) or [default_source](https://stripe.com/docs/api/customers/object#customer_object-default_source).
    """
    default_tax_rates: typing.Optional[typing.List[TaxRate]] = pydantic.Field(
        alias="default_tax_rates", default=None
    )
    """
    The tax rates that will apply to any subscription item that does not have `tax_rates` set. Invoices created will have their `default_tax_rates` populated from the subscription.
    """
    description: typing.Optional[str] = pydantic.Field(
        alias="description", default=None
    )
    """
    The subscription's description, meant to be displayable to the customer. Use this field to optionally store an explanation of the subscription for rendering in Stripe surfaces and certain local payment methods UIs.
    """
    discounts: typing.List[typing.Union[str, "Discount"]] = pydantic.Field(
        alias="discounts",
    )
    """
    The discounts applied to the subscription. Subscription item discounts are applied before subscription discounts. Use `expand[]=discounts` to expand each discount.
    """
    ended_at: typing.Optional[int] = pydantic.Field(alias="ended_at", default=None)
    """
    If the subscription has ended, the date the subscription ended.
    """
    id: str = pydantic.Field(
        alias="id",
    )
    """
    Unique identifier for the object.
    """
    invoice_settings: "SubscriptionsResourceSubscriptionInvoiceSettings" = (
        pydantic.Field(
            alias="invoice_settings",
        )
    )
    items: "SubscriptionItems" = pydantic.Field(
        alias="items",
    )
    """
    List of subscription items, each with an attached price.
    """
    latest_invoice: typing.Optional[typing.Union[str, "Invoice"]] = pydantic.Field(
        alias="latest_invoice", default=None
    )
    """
    The most recent invoice this subscription has generated.
    """
    livemode: bool = pydantic.Field(
        alias="livemode",
    )
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    metadata: SubscriptionMetadata = pydantic.Field(
        alias="metadata",
    )
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    next_pending_invoice_item_invoice: typing.Optional[int] = pydantic.Field(
        alias="next_pending_invoice_item_invoice", default=None
    )
    """
    Specifies the approximate timestamp on which any pending invoice items will be billed according to the schedule provided at `pending_invoice_item_interval`.
    """
    object: typing_extensions.Literal["subscription"] = pydantic.Field(
        alias="object",
    )
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    on_behalf_of: typing.Optional[typing.Union[str, "Account"]] = pydantic.Field(
        alias="on_behalf_of", default=None
    )
    """
    The account (if any) the charge was made on behalf of for charges associated with this subscription. See the [Connect documentation](https://stripe.com/docs/connect/subscriptions#on-behalf-of) for details.
    """
    pause_collection: typing.Optional[SubscriptionsResourcePauseCollection] = (
        pydantic.Field(alias="pause_collection", default=None)
    )
    """
    The Pause Collection settings determine how we will pause collection for this subscription and for how long the subscription
    should be paused.
    """
    payment_settings: typing.Optional[SubscriptionsResourcePaymentSettings] = (
        pydantic.Field(alias="payment_settings", default=None)
    )
    pending_invoice_item_interval: typing.Optional[
        SubscriptionPendingInvoiceItemInterval
    ] = pydantic.Field(alias="pending_invoice_item_interval", default=None)
    pending_setup_intent: typing.Optional[typing.Union[str, "SetupIntent"]] = (
        pydantic.Field(alias="pending_setup_intent", default=None)
    )
    """
    You can use this [SetupIntent](https://stripe.com/docs/api/setup_intents) to collect user authentication when creating a subscription without immediate payment or updating a subscription's payment method, allowing you to optimize for off-session payments. Learn more in the [SCA Migration Guide](https://stripe.com/docs/billing/migration/strong-customer-authentication#scenario-2).
    """
    pending_update: typing.Optional["SubscriptionsResourcePendingUpdate"] = (
        pydantic.Field(alias="pending_update", default=None)
    )
    """
    Pending Updates store the changes pending from a previous update that will be applied
    to the Subscription upon successful payment.
    """
    schedule: typing.Optional[typing.Union[str, "SubscriptionSchedule1"]] = (
        pydantic.Field(alias="schedule", default=None)
    )
    """
    The schedule attached to the subscription
    """
    start_date: int = pydantic.Field(
        alias="start_date",
    )
    """
    Date when the subscription was first created. The date might differ from the `created` date due to backdating.
    """
    status: typing_extensions.Literal[
        "active",
        "canceled",
        "incomplete",
        "incomplete_expired",
        "past_due",
        "paused",
        "trialing",
        "unpaid",
    ] = pydantic.Field(
        alias="status",
    )
    """
    Possible values are `incomplete`, `incomplete_expired`, `trialing`, `active`, `past_due`, `canceled`, `unpaid`, or `paused`. 
    
    For `collection_method=charge_automatically` a subscription moves into `incomplete` if the initial payment attempt fails. A subscription in this status can only have metadata and default_source updated. Once the first invoice is paid, the subscription moves into an `active` status. If the first invoice is not paid within 23 hours, the subscription transitions to `incomplete_expired`. This is a terminal status, the open invoice will be voided and no further invoices will be generated. 
    
    A subscription that is currently in a trial period is `trialing` and moves to `active` when the trial period is over. 
    
    A subscription can only enter a `paused` status [when a trial ends without a payment method](https://stripe.com/docs/billing/subscriptions/trials#create-free-trials-without-payment). A `paused` subscription doesn't generate invoices and can be resumed after your customer adds their payment method. The `paused` status is different from [pausing collection](https://stripe.com/docs/billing/subscriptions/pause-payment), which still generates invoices and leaves the subscription's status unchanged. 
    
    If subscription `collection_method=charge_automatically`, it becomes `past_due` when payment is required but cannot be paid (due to failed payment or awaiting additional user actions). Once Stripe has exhausted all payment retry attempts, the subscription will become `canceled` or `unpaid` (depending on your subscriptions settings). 
    
    If subscription `collection_method=send_invoice` it becomes `past_due` when its invoice is not paid by the due date, and `canceled` or `unpaid` if it is still not paid by an additional deadline after that. Note that when a subscription has a status of `unpaid`, no subsequent invoices will be attempted (invoices will be created, but then immediately automatically closed). After receiving updated payment information from a customer, you may choose to reopen and pay their closed invoices.
    """
    test_clock: typing.Optional[typing.Union[str, TestHelpersTestClock]] = (
        pydantic.Field(alias="test_clock", default=None)
    )
    """
    ID of the test clock this subscription belongs to.
    """
    transfer_data: typing.Optional["SubscriptionTransferData"] = pydantic.Field(
        alias="transfer_data", default=None
    )
    trial_end: typing.Optional[int] = pydantic.Field(alias="trial_end", default=None)
    """
    If the subscription has a trial, the end of that trial.
    """
    trial_settings: typing.Optional[SubscriptionsTrialsResourceTrialSettings] = (
        pydantic.Field(alias="trial_settings", default=None)
    )
    """
    Configures how this subscription behaves during the trial period.
    """
    trial_start: typing.Optional[int] = pydantic.Field(
        alias="trial_start", default=None
    )
    """
    If the subscription has a trial, the beginning of that trial.
    """
