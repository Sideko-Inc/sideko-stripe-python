import pydantic
import typing
import typing_extensions


if typing_extensions.TYPE_CHECKING:
    from .account import Account
    from .invoice_setting_subscription_schedule_setting import (
        InvoiceSettingSubscriptionScheduleSetting,
    )
    from .payment_method import PaymentMethod
    from .subscription_schedules_resource_default_settings_automatic_tax import (
        SubscriptionSchedulesResourceDefaultSettingsAutomaticTax,
    )
    from .subscription_transfer_data import SubscriptionTransferData


class SubscriptionSchedulesResourceDefaultSettings(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    application_fee_percent: typing.Optional[float] = pydantic.Field(
        alias="application_fee_percent", default=None
    )
    """
    A non-negative decimal between 0 and 100, with at most two decimal places. This represents the percentage of the subscription invoice total that will be transferred to the application owner's Stripe account during this phase of the schedule.
    """
    automatic_tax: typing.Optional[
        "SubscriptionSchedulesResourceDefaultSettingsAutomaticTax"
    ] = pydantic.Field(alias="automatic_tax", default=None)
    billing_cycle_anchor: typing_extensions.Literal["automatic", "phase_start"] = (
        pydantic.Field(
            alias="billing_cycle_anchor",
        )
    )
    """
    Possible values are `phase_start` or `automatic`. If `phase_start` then billing cycle anchor of the subscription is set to the start of the phase when entering the phase. If `automatic` then the billing cycle anchor is automatically modified as needed when entering the phase. For more information, see the billing cycle [documentation](https://stripe.com/docs/billing/subscriptions/billing-cycle).
    """
    collection_method: typing.Optional[
        typing_extensions.Literal["charge_automatically", "send_invoice"]
    ] = pydantic.Field(alias="collection_method", default=None)
    """
    Either `charge_automatically`, or `send_invoice`. When charging automatically, Stripe will attempt to pay the underlying subscription at the end of each billing cycle using the default source attached to the customer. When sending an invoice, Stripe will email your customer an invoice with payment instructions and mark the subscription as `active`.
    """
    default_payment_method: typing.Optional[typing.Union[str, "PaymentMethod"]] = (
        pydantic.Field(alias="default_payment_method", default=None)
    )
    """
    ID of the default payment method for the subscription schedule. If not set, invoices will use the default payment method in the customer's invoice settings.
    """
    description: typing.Optional[str] = pydantic.Field(
        alias="description", default=None
    )
    """
    Subscription description, meant to be displayable to the customer. Use this field to optionally store an explanation of the subscription for rendering in Stripe surfaces and certain local payment methods UIs.
    """
    invoice_settings: "InvoiceSettingSubscriptionScheduleSetting" = pydantic.Field(
        alias="invoice_settings",
    )
    on_behalf_of: typing.Optional[typing.Union[str, "Account"]] = pydantic.Field(
        alias="on_behalf_of", default=None
    )
    """
    The account (if any) the charge was made on behalf of for charges associated with the schedule's subscription. See the Connect documentation for details.
    """
    transfer_data: typing.Optional["SubscriptionTransferData"] = pydantic.Field(
        alias="transfer_data", default=None
    )
