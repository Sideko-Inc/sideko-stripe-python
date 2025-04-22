import pydantic
import typing
import typing_extensions

from .customer_subscription_create_body_add_invoice_items_item import (
    CustomerSubscriptionCreateBodyAddInvoiceItemsItem,
    _SerializerCustomerSubscriptionCreateBodyAddInvoiceItemsItem,
)
from .customer_subscription_create_body_automatic_tax import (
    CustomerSubscriptionCreateBodyAutomaticTax,
    _SerializerCustomerSubscriptionCreateBodyAutomaticTax,
)
from .customer_subscription_create_body_discounts_arr0_item import (
    CustomerSubscriptionCreateBodyDiscountsArr0Item,
    _SerializerCustomerSubscriptionCreateBodyDiscountsArr0Item,
)
from .customer_subscription_create_body_invoice_settings import (
    CustomerSubscriptionCreateBodyInvoiceSettings,
    _SerializerCustomerSubscriptionCreateBodyInvoiceSettings,
)
from .customer_subscription_create_body_items_item import (
    CustomerSubscriptionCreateBodyItemsItem,
    _SerializerCustomerSubscriptionCreateBodyItemsItem,
)
from .customer_subscription_create_body_metadata_obj0 import (
    CustomerSubscriptionCreateBodyMetadataObj0,
    _SerializerCustomerSubscriptionCreateBodyMetadataObj0,
)
from .customer_subscription_create_body_payment_settings import (
    CustomerSubscriptionCreateBodyPaymentSettings,
    _SerializerCustomerSubscriptionCreateBodyPaymentSettings,
)
from .customer_subscription_create_body_pending_invoice_item_interval_obj0 import (
    CustomerSubscriptionCreateBodyPendingInvoiceItemIntervalObj0,
    _SerializerCustomerSubscriptionCreateBodyPendingInvoiceItemIntervalObj0,
)
from .customer_subscription_create_body_transfer_data import (
    CustomerSubscriptionCreateBodyTransferData,
    _SerializerCustomerSubscriptionCreateBodyTransferData,
)
from .customer_subscription_create_body_trial_settings import (
    CustomerSubscriptionCreateBodyTrialSettings,
    _SerializerCustomerSubscriptionCreateBodyTrialSettings,
)


class CustomerSubscriptionCreateBody(typing_extensions.TypedDict, total=False):
    """
    CustomerSubscriptionCreateBody
    """

    add_invoice_items: typing_extensions.NotRequired[
        typing.List[CustomerSubscriptionCreateBodyAddInvoiceItemsItem]
    ]
    """
    A list of prices and quantities that will generate invoice items appended to the next invoice for this subscription. You may pass up to 20 items.
    """

    application_fee_percent: typing_extensions.NotRequired[typing.Union[float, str]]
    """
    A non-negative decimal between 0 and 100, with at most two decimal places. This represents the percentage of the subscription invoice total that will be transferred to the application owner's Stripe account. The request must be made by a platform account on a connected account in order to set an application fee percentage. For more information, see the application fees [documentation](https://stripe.com/docs/connect/subscriptions#collecting-fees-on-subscriptions).
    """

    automatic_tax: typing_extensions.NotRequired[
        CustomerSubscriptionCreateBodyAutomaticTax
    ]
    """
    Automatic tax settings for this subscription. We recommend you only include this parameter when the existing value is being changed.
    """

    backdate_start_date: typing_extensions.NotRequired[int]
    """
    For new subscriptions, a past timestamp to backdate the subscription's start date to. If set, the first invoice will contain a proration for the timespan between the start date and the current time. Can be combined with trials and the billing cycle anchor.
    """

    billing_cycle_anchor: typing_extensions.NotRequired[int]
    """
    A future timestamp in UTC format to anchor the subscription's [billing cycle](https://stripe.com/docs/subscriptions/billing-cycle). The anchor is the reference point that aligns future billing cycle dates. It sets the day of week for `week` intervals, the day of month for `month` and `year` intervals, and the month of year for `year` intervals.
    """

    cancel_at: typing_extensions.NotRequired[int]
    """
    A timestamp at which the subscription should cancel. If set to a date before the current period ends, this will cause a proration if prorations have been enabled using `proration_behavior`. If set during a future period, this will always cause a proration for that period.
    """

    cancel_at_period_end: typing_extensions.NotRequired[bool]
    """
    Indicate whether this subscription should cancel at the end of the current period (`current_period_end`). Defaults to `false`.
    """

    collection_method: typing_extensions.NotRequired[
        typing_extensions.Literal["charge_automatically", "send_invoice"]
    ]
    """
    Either `charge_automatically`, or `send_invoice`. When charging automatically, Stripe will attempt to pay this subscription at the end of the cycle using the default source attached to the customer. When sending an invoice, Stripe will email your customer an invoice with payment instructions and mark the subscription as `active`. Defaults to `charge_automatically`.
    """

    currency: typing_extensions.NotRequired[str]
    """
    Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    """

    days_until_due: typing_extensions.NotRequired[int]
    """
    Number of days a customer has to pay invoices generated by this subscription. Valid only for subscriptions where `collection_method` is set to `send_invoice`.
    """

    default_payment_method: typing_extensions.NotRequired[str]
    """
    ID of the default payment method for the subscription. It must belong to the customer associated with the subscription. This takes precedence over `default_source`. If neither are set, invoices will use the customer's [invoice_settings.default_payment_method](https://stripe.com/docs/api/customers/object#customer_object-invoice_settings-default_payment_method) or [default_source](https://stripe.com/docs/api/customers/object#customer_object-default_source).
    """

    default_source: typing_extensions.NotRequired[str]
    """
    ID of the default payment source for the subscription. It must belong to the customer associated with the subscription and be in a chargeable state. If `default_payment_method` is also set, `default_payment_method` will take precedence. If neither are set, invoices will use the customer's [invoice_settings.default_payment_method](https://stripe.com/docs/api/customers/object#customer_object-invoice_settings-default_payment_method) or [default_source](https://stripe.com/docs/api/customers/object#customer_object-default_source).
    """

    default_tax_rates: typing_extensions.NotRequired[
        typing.Union[typing.List[str], str]
    ]
    """
    The tax rates that will apply to any subscription item that does not have `tax_rates` set. Invoices created will have their `default_tax_rates` populated from the subscription.
    """

    discounts: typing_extensions.NotRequired[
        typing.Union[typing.List[CustomerSubscriptionCreateBodyDiscountsArr0Item], str]
    ]
    """
    The coupons to redeem into discounts for the subscription. If not specified or empty, inherits the discount from the subscription's customer.
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """

    invoice_settings: typing_extensions.NotRequired[
        CustomerSubscriptionCreateBodyInvoiceSettings
    ]
    """
    All invoices will be billed using the specified settings.
    """

    items: typing_extensions.NotRequired[
        typing.List[CustomerSubscriptionCreateBodyItemsItem]
    ]
    """
    A list of up to 20 subscription items, each with an attached price.
    """

    metadata: typing_extensions.NotRequired[
        typing.Union[CustomerSubscriptionCreateBodyMetadataObj0, str]
    ]
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    """

    off_session: typing_extensions.NotRequired[bool]
    """
    Indicates if a customer is on or off-session while an invoice payment is attempted. Defaults to `false` (on-session).
    """

    payment_behavior: typing_extensions.NotRequired[
        typing_extensions.Literal[
            "allow_incomplete",
            "default_incomplete",
            "error_if_incomplete",
            "pending_if_incomplete",
        ]
    ]
    """
    Only applies to subscriptions with `collection_method=charge_automatically`.
    
    Use `allow_incomplete` to create Subscriptions with `status=incomplete` if the first invoice can't be paid. Creating Subscriptions with this status allows you to manage scenarios where additional customer actions are needed to pay a subscription's invoice. For example, SCA regulation may require 3DS authentication to complete payment. See the [SCA Migration Guide](https://stripe.com/docs/billing/migration/strong-customer-authentication) for Billing to learn more. This is the default behavior.
    
    Use `default_incomplete` to create Subscriptions with `status=incomplete` when the first invoice requires payment, otherwise start as active. Subscriptions transition to `status=active` when successfully confirming the PaymentIntent on the first invoice. This allows simpler management of scenarios where additional customer actions are needed to pay a subscription’s invoice, such as failed payments, [SCA regulation](https://stripe.com/docs/billing/migration/strong-customer-authentication), or collecting a mandate for a bank debit payment method. If the PaymentIntent is not confirmed within 23 hours Subscriptions transition to `status=incomplete_expired`, which is a terminal state.
    
    Use `error_if_incomplete` if you want Stripe to return an HTTP 402 status code if a subscription's first invoice can't be paid. For example, if a payment method requires 3DS authentication due to SCA regulation and further customer action is needed, this parameter doesn't create a Subscription and returns an error instead. This was the default behavior for API versions prior to 2019-03-14. See the [changelog](https://stripe.com/docs/upgrades#2019-03-14) to learn more.
    
    `pending_if_incomplete` is only used with updates and cannot be passed when creating a Subscription.
    
    Subscriptions with `collection_method=send_invoice` are automatically activated regardless of the first Invoice status.
    """

    payment_settings: typing_extensions.NotRequired[
        CustomerSubscriptionCreateBodyPaymentSettings
    ]
    """
    Payment settings to pass to invoices created by the subscription.
    """

    pending_invoice_item_interval: typing_extensions.NotRequired[
        typing.Union[CustomerSubscriptionCreateBodyPendingInvoiceItemIntervalObj0, str]
    ]
    """
    Specifies an interval for how often to bill for any pending invoice items. It is analogous to calling [Create an invoice](https://stripe.com/docs/api#create_invoice) for the given subscription at the specified interval.
    """

    proration_behavior: typing_extensions.NotRequired[
        typing_extensions.Literal["always_invoice", "create_prorations", "none"]
    ]
    """
    Determines how to handle [prorations](https://stripe.com/docs/billing/subscriptions/prorations) resulting from the `billing_cycle_anchor`. If no value is passed, the default is `create_prorations`.
    """

    transfer_data: typing_extensions.NotRequired[
        CustomerSubscriptionCreateBodyTransferData
    ]
    """
    If specified, the funds from the subscription's invoices will be transferred to the destination and the ID of the resulting transfers will be found on the resulting charges.
    """

    trial_end: typing_extensions.NotRequired[
        typing.Union[typing_extensions.Literal["now"], int]
    ]
    """
    Unix timestamp representing the end of the trial period the customer will get before being charged for the first time. If set, trial_end will override the default trial period of the plan the customer is being subscribed to. The special value `now` can be provided to end the customer's trial immediately. Can be at most two years from `billing_cycle_anchor`. See [Using trial periods on subscriptions](https://stripe.com/docs/billing/subscriptions/trials) to learn more.
    """

    trial_from_plan: typing_extensions.NotRequired[bool]
    """
    Indicates if a plan's `trial_period_days` should be applied to the subscription. Setting `trial_end` per subscription is preferred, and this defaults to `false`. Setting this flag to `true` together with `trial_end` is not allowed. See [Using trial periods on subscriptions](https://stripe.com/docs/billing/subscriptions/trials) to learn more.
    """

    trial_period_days: typing_extensions.NotRequired[int]
    """
    Integer representing the number of trial period days before the customer is charged for the first time. This will always overwrite any trials that might apply via a subscribed plan. See [Using trial periods on subscriptions](https://stripe.com/docs/billing/subscriptions/trials) to learn more.
    """

    trial_settings: typing_extensions.NotRequired[
        CustomerSubscriptionCreateBodyTrialSettings
    ]
    """
    Settings related to subscription trials.
    """


class _SerializerCustomerSubscriptionCreateBody(pydantic.BaseModel):
    """
    Serializer for CustomerSubscriptionCreateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    add_invoice_items: typing.Optional[
        typing.List[_SerializerCustomerSubscriptionCreateBodyAddInvoiceItemsItem]
    ] = pydantic.Field(alias="add_invoice_items", default=None)
    application_fee_percent: typing.Optional[typing.Union[float, str]] = pydantic.Field(
        alias="application_fee_percent", default=None
    )
    automatic_tax: typing.Optional[
        _SerializerCustomerSubscriptionCreateBodyAutomaticTax
    ] = pydantic.Field(alias="automatic_tax", default=None)
    backdate_start_date: typing.Optional[int] = pydantic.Field(
        alias="backdate_start_date", default=None
    )
    billing_cycle_anchor: typing.Optional[int] = pydantic.Field(
        alias="billing_cycle_anchor", default=None
    )
    cancel_at: typing.Optional[int] = pydantic.Field(alias="cancel_at", default=None)
    cancel_at_period_end: typing.Optional[bool] = pydantic.Field(
        alias="cancel_at_period_end", default=None
    )
    collection_method: typing.Optional[
        typing_extensions.Literal["charge_automatically", "send_invoice"]
    ] = pydantic.Field(alias="collection_method", default=None)
    currency: typing.Optional[str] = pydantic.Field(alias="currency", default=None)
    days_until_due: typing.Optional[int] = pydantic.Field(
        alias="days_until_due", default=None
    )
    default_payment_method: typing.Optional[str] = pydantic.Field(
        alias="default_payment_method", default=None
    )
    default_source: typing.Optional[str] = pydantic.Field(
        alias="default_source", default=None
    )
    default_tax_rates: typing.Optional[typing.Union[typing.List[str], str]] = (
        pydantic.Field(alias="default_tax_rates", default=None)
    )
    discounts: typing.Optional[
        typing.Union[
            typing.List[_SerializerCustomerSubscriptionCreateBodyDiscountsArr0Item], str
        ]
    ] = pydantic.Field(alias="discounts", default=None)
    expand: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="expand", default=None
    )
    invoice_settings: typing.Optional[
        _SerializerCustomerSubscriptionCreateBodyInvoiceSettings
    ] = pydantic.Field(alias="invoice_settings", default=None)
    items: typing.Optional[
        typing.List[_SerializerCustomerSubscriptionCreateBodyItemsItem]
    ] = pydantic.Field(alias="items", default=None)
    metadata: typing.Optional[
        typing.Union[_SerializerCustomerSubscriptionCreateBodyMetadataObj0, str]
    ] = pydantic.Field(alias="metadata", default=None)
    off_session: typing.Optional[bool] = pydantic.Field(
        alias="off_session", default=None
    )
    payment_behavior: typing.Optional[
        typing_extensions.Literal[
            "allow_incomplete",
            "default_incomplete",
            "error_if_incomplete",
            "pending_if_incomplete",
        ]
    ] = pydantic.Field(alias="payment_behavior", default=None)
    payment_settings: typing.Optional[
        _SerializerCustomerSubscriptionCreateBodyPaymentSettings
    ] = pydantic.Field(alias="payment_settings", default=None)
    pending_invoice_item_interval: typing.Optional[
        typing.Union[
            _SerializerCustomerSubscriptionCreateBodyPendingInvoiceItemIntervalObj0, str
        ]
    ] = pydantic.Field(alias="pending_invoice_item_interval", default=None)
    proration_behavior: typing.Optional[
        typing_extensions.Literal["always_invoice", "create_prorations", "none"]
    ] = pydantic.Field(alias="proration_behavior", default=None)
    transfer_data: typing.Optional[
        _SerializerCustomerSubscriptionCreateBodyTransferData
    ] = pydantic.Field(alias="transfer_data", default=None)
    trial_end: typing.Optional[typing.Union[typing_extensions.Literal["now"], int]] = (
        pydantic.Field(alias="trial_end", default=None)
    )
    trial_from_plan: typing.Optional[bool] = pydantic.Field(
        alias="trial_from_plan", default=None
    )
    trial_period_days: typing.Optional[int] = pydantic.Field(
        alias="trial_period_days", default=None
    )
    trial_settings: typing.Optional[
        _SerializerCustomerSubscriptionCreateBodyTrialSettings
    ] = pydantic.Field(alias="trial_settings", default=None)
