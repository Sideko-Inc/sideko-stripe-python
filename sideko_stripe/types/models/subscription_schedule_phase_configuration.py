import pydantic
import typing
import typing_extensions

from .subscription_schedule_phase_configuration_metadata import (
    SubscriptionSchedulePhaseConfigurationMetadata,
)
from .tax_rate import TaxRate

if typing_extensions.TYPE_CHECKING:
    from .account import Account
    from .discounts_resource_stackable_discount import (
        DiscountsResourceStackableDiscount,
    )
    from .invoice_setting_subscription_schedule_phase_setting import (
        InvoiceSettingSubscriptionSchedulePhaseSetting,
    )
    from .payment_method import PaymentMethod
    from .schedules_phase_automatic_tax import SchedulesPhaseAutomaticTax
    from .subscription_schedule_add_invoice_item import (
        SubscriptionScheduleAddInvoiceItem,
    )
    from .subscription_schedule_configuration_item import (
        SubscriptionScheduleConfigurationItem,
    )
    from .subscription_transfer_data import SubscriptionTransferData


class SubscriptionSchedulePhaseConfiguration(pydantic.BaseModel):
    """
    A phase describes the plans, coupon, and trialing status of a subscription for a predefined time period.
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    add_invoice_items: typing.List["SubscriptionScheduleAddInvoiceItem"] = (
        pydantic.Field(
            alias="add_invoice_items",
        )
    )
    """
    A list of prices and quantities that will generate invoice items appended to the next invoice for this phase.
    """
    application_fee_percent: typing.Optional[float] = pydantic.Field(
        alias="application_fee_percent", default=None
    )
    """
    A non-negative decimal between 0 and 100, with at most two decimal places. This represents the percentage of the subscription invoice total that will be transferred to the application owner's Stripe account during this phase of the schedule.
    """
    automatic_tax: typing.Optional["SchedulesPhaseAutomaticTax"] = pydantic.Field(
        alias="automatic_tax", default=None
    )
    billing_cycle_anchor: typing.Optional[
        typing_extensions.Literal["automatic", "phase_start"]
    ] = pydantic.Field(alias="billing_cycle_anchor", default=None)
    """
    Possible values are `phase_start` or `automatic`. If `phase_start` then billing cycle anchor of the subscription is set to the start of the phase when entering the phase. If `automatic` then the billing cycle anchor is automatically modified as needed when entering the phase. For more information, see the billing cycle [documentation](https://stripe.com/docs/billing/subscriptions/billing-cycle).
    """
    collection_method: typing.Optional[
        typing_extensions.Literal["charge_automatically", "send_invoice"]
    ] = pydantic.Field(alias="collection_method", default=None)
    """
    Either `charge_automatically`, or `send_invoice`. When charging automatically, Stripe will attempt to pay the underlying subscription at the end of each billing cycle using the default source attached to the customer. When sending an invoice, Stripe will email your customer an invoice with payment instructions and mark the subscription as `active`.
    """
    currency: str = pydantic.Field(
        alias="currency",
    )
    """
    Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    """
    default_payment_method: typing.Optional[typing.Union[str, "PaymentMethod"]] = (
        pydantic.Field(alias="default_payment_method", default=None)
    )
    """
    ID of the default payment method for the subscription schedule. It must belong to the customer associated with the subscription schedule. If not set, invoices will use the default payment method in the customer's invoice settings.
    """
    default_tax_rates: typing.Optional[typing.List[TaxRate]] = pydantic.Field(
        alias="default_tax_rates", default=None
    )
    """
    The default tax rates to apply to the subscription during this phase of the subscription schedule.
    """
    description: typing.Optional[str] = pydantic.Field(
        alias="description", default=None
    )
    """
    Subscription description, meant to be displayable to the customer. Use this field to optionally store an explanation of the subscription for rendering in Stripe surfaces and certain local payment methods UIs.
    """
    discounts: typing.List["DiscountsResourceStackableDiscount"] = pydantic.Field(
        alias="discounts",
    )
    """
    The stackable discounts that will be applied to the subscription on this phase. Subscription item discounts are applied before subscription discounts.
    """
    end_date: int = pydantic.Field(
        alias="end_date",
    )
    """
    The end of this phase of the subscription schedule.
    """
    invoice_settings: typing.Optional[
        "InvoiceSettingSubscriptionSchedulePhaseSetting"
    ] = pydantic.Field(alias="invoice_settings", default=None)
    items: typing.List["SubscriptionScheduleConfigurationItem"] = pydantic.Field(
        alias="items",
    )
    """
    Subscription items to configure the subscription to during this phase of the subscription schedule.
    """
    metadata: typing.Optional[SubscriptionSchedulePhaseConfigurationMetadata] = (
        pydantic.Field(alias="metadata", default=None)
    )
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to a phase. Metadata on a schedule's phase will update the underlying subscription's `metadata` when the phase is entered. Updating the underlying subscription's `metadata` directly will not affect the current phase's `metadata`.
    """
    on_behalf_of: typing.Optional[typing.Union[str, "Account"]] = pydantic.Field(
        alias="on_behalf_of", default=None
    )
    """
    The account (if any) the charge was made on behalf of for charges associated with the schedule's subscription. See the Connect documentation for details.
    """
    proration_behavior: typing_extensions.Literal[
        "always_invoice", "create_prorations", "none"
    ] = pydantic.Field(
        alias="proration_behavior",
    )
    """
    If the subscription schedule will prorate when transitioning to this phase. Possible values are `create_prorations` and `none`.
    """
    start_date: int = pydantic.Field(
        alias="start_date",
    )
    """
    The start of this phase of the subscription schedule.
    """
    transfer_data: typing.Optional["SubscriptionTransferData"] = pydantic.Field(
        alias="transfer_data", default=None
    )
    trial_end: typing.Optional[int] = pydantic.Field(alias="trial_end", default=None)
    """
    When the trial ends within the phase.
    """
