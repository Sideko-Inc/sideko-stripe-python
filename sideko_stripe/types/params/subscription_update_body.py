import pydantic
import typing
import typing_extensions

from .subscription_update_body_add_invoice_items_item import (
    SubscriptionUpdateBodyAddInvoiceItemsItem,
    _SerializerSubscriptionUpdateBodyAddInvoiceItemsItem,
)
from .subscription_update_body_automatic_tax import (
    SubscriptionUpdateBodyAutomaticTax,
    _SerializerSubscriptionUpdateBodyAutomaticTax,
)
from .subscription_update_body_cancellation_details import (
    SubscriptionUpdateBodyCancellationDetails,
    _SerializerSubscriptionUpdateBodyCancellationDetails,
)
from .subscription_update_body_discounts_arr0_item import (
    SubscriptionUpdateBodyDiscountsArr0Item,
    _SerializerSubscriptionUpdateBodyDiscountsArr0Item,
)
from .subscription_update_body_invoice_settings import (
    SubscriptionUpdateBodyInvoiceSettings,
    _SerializerSubscriptionUpdateBodyInvoiceSettings,
)
from .subscription_update_body_items_item import (
    SubscriptionUpdateBodyItemsItem,
    _SerializerSubscriptionUpdateBodyItemsItem,
)
from .subscription_update_body_metadata_obj0 import (
    SubscriptionUpdateBodyMetadataObj0,
    _SerializerSubscriptionUpdateBodyMetadataObj0,
)
from .subscription_update_body_pause_collection_obj0 import (
    SubscriptionUpdateBodyPauseCollectionObj0,
    _SerializerSubscriptionUpdateBodyPauseCollectionObj0,
)
from .subscription_update_body_payment_settings import (
    SubscriptionUpdateBodyPaymentSettings,
    _SerializerSubscriptionUpdateBodyPaymentSettings,
)
from .subscription_update_body_pending_invoice_item_interval_obj0 import (
    SubscriptionUpdateBodyPendingInvoiceItemIntervalObj0,
    _SerializerSubscriptionUpdateBodyPendingInvoiceItemIntervalObj0,
)
from .subscription_update_body_transfer_data_obj0 import (
    SubscriptionUpdateBodyTransferDataObj0,
    _SerializerSubscriptionUpdateBodyTransferDataObj0,
)
from .subscription_update_body_trial_settings import (
    SubscriptionUpdateBodyTrialSettings,
    _SerializerSubscriptionUpdateBodyTrialSettings,
)


class SubscriptionUpdateBody(typing_extensions.TypedDict, total=False):
    """
    SubscriptionUpdateBody
    """

    add_invoice_items: typing_extensions.NotRequired[
        typing.List[SubscriptionUpdateBodyAddInvoiceItemsItem]
    ]
    """
    A list of prices and quantities that will generate invoice items appended to the next invoice for this subscription. You may pass up to 20 items.
    """

    application_fee_percent: typing_extensions.NotRequired[typing.Union[float, str]]
    """
    A non-negative decimal between 0 and 100, with at most two decimal places. This represents the percentage of the subscription invoice total that will be transferred to the application owner's Stripe account. The request must be made by a platform account on a connected account in order to set an application fee percentage. For more information, see the application fees [documentation](https://stripe.com/docs/connect/subscriptions#collecting-fees-on-subscriptions).
    """

    automatic_tax: typing_extensions.NotRequired[SubscriptionUpdateBodyAutomaticTax]
    """
    Automatic tax settings for this subscription. We recommend you only include this parameter when the existing value is being changed.
    """

    billing_cycle_anchor: typing_extensions.NotRequired[
        typing_extensions.Literal["now", "unchanged"]
    ]
    """
    Either `now` or `unchanged`. Setting the value to `now` resets the subscription's billing cycle anchor to the current time (in UTC). For more information, see the billing cycle [documentation](https://stripe.com/docs/billing/subscriptions/billing-cycle).
    """

    cancel_at: typing_extensions.NotRequired[typing.Union[int, str]]
    """
    A timestamp at which the subscription should cancel. If set to a date before the current period ends, this will cause a proration if prorations have been enabled using `proration_behavior`. If set during a future period, this will always cause a proration for that period.
    """

    cancel_at_period_end: typing_extensions.NotRequired[bool]
    """
    Indicate whether this subscription should cancel at the end of the current period (`current_period_end`). Defaults to `false`.
    """

    cancellation_details: typing_extensions.NotRequired[
        SubscriptionUpdateBodyCancellationDetails
    ]
    """
    Details about why this subscription was cancelled
    """

    collection_method: typing_extensions.NotRequired[
        typing_extensions.Literal["charge_automatically", "send_invoice"]
    ]
    """
    Either `charge_automatically`, or `send_invoice`. When charging automatically, Stripe will attempt to pay this subscription at the end of the cycle using the default source attached to the customer. When sending an invoice, Stripe will email your customer an invoice with payment instructions and mark the subscription as `active`. Defaults to `charge_automatically`.
    """

    days_until_due: typing_extensions.NotRequired[int]
    """
    Number of days a customer has to pay invoices generated by this subscription. Valid only for subscriptions where `collection_method` is set to `send_invoice`.
    """

    default_payment_method: typing_extensions.NotRequired[str]
    """
    ID of the default payment method for the subscription. It must belong to the customer associated with the subscription. This takes precedence over `default_source`. If neither are set, invoices will use the customer's [invoice_settings.default_payment_method](https://stripe.com/docs/api/customers/object#customer_object-invoice_settings-default_payment_method) or [default_source](https://stripe.com/docs/api/customers/object#customer_object-default_source).
    """

    default_source: typing_extensions.NotRequired[typing.Union[str, str]]
    """
    ID of the default payment source for the subscription. It must belong to the customer associated with the subscription and be in a chargeable state. If `default_payment_method` is also set, `default_payment_method` will take precedence. If neither are set, invoices will use the customer's [invoice_settings.default_payment_method](https://stripe.com/docs/api/customers/object#customer_object-invoice_settings-default_payment_method) or [default_source](https://stripe.com/docs/api/customers/object#customer_object-default_source).
    """

    default_tax_rates: typing_extensions.NotRequired[
        typing.Union[typing.List[str], str]
    ]
    """
    The tax rates that will apply to any subscription item that does not have `tax_rates` set. Invoices created will have their `default_tax_rates` populated from the subscription. Pass an empty string to remove previously-defined tax rates.
    """

    description: typing_extensions.NotRequired[typing.Union[str, str]]
    """
    The subscription's description, meant to be displayable to the customer. Use this field to optionally store an explanation of the subscription for rendering in Stripe surfaces and certain local payment methods UIs.
    """

    discounts: typing_extensions.NotRequired[
        typing.Union[typing.List[SubscriptionUpdateBodyDiscountsArr0Item], str]
    ]
    """
    The coupons to redeem into discounts for the subscription. If not specified or empty, inherits the discount from the subscription's customer.
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """

    invoice_settings: typing_extensions.NotRequired[
        SubscriptionUpdateBodyInvoiceSettings
    ]
    """
    All invoices will be billed using the specified settings.
    """

    items: typing_extensions.NotRequired[typing.List[SubscriptionUpdateBodyItemsItem]]
    """
    A list of up to 20 subscription items, each with an attached price.
    """

    metadata: typing_extensions.NotRequired[
        typing.Union[SubscriptionUpdateBodyMetadataObj0, str]
    ]
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    """

    off_session: typing_extensions.NotRequired[bool]
    """
    Indicates if a customer is on or off-session while an invoice payment is attempted. Defaults to `false` (on-session).
    """

    on_behalf_of: typing_extensions.NotRequired[typing.Union[str, str]]
    """
    The account on behalf of which to charge, for each of the subscription's invoices.
    """

    pause_collection: typing_extensions.NotRequired[
        typing.Union[SubscriptionUpdateBodyPauseCollectionObj0, str]
    ]
    """
    If specified, payment collection for this subscription will be paused. Note that the subscription status will be unchanged and will not be updated to `paused`. Learn more about [pausing collection](https://stripe.com/docs/billing/subscriptions/pause-payment).
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
    Use `allow_incomplete` to transition the subscription to `status=past_due` if a payment is required but cannot be paid. This allows you to manage scenarios where additional user actions are needed to pay a subscription's invoice. For example, SCA regulation may require 3DS authentication to complete payment. See the [SCA Migration Guide](https://stripe.com/docs/billing/migration/strong-customer-authentication) for Billing to learn more. This is the default behavior.
    
    Use `default_incomplete` to transition the subscription to `status=past_due` when payment is required and await explicit confirmation of the invoice's payment intent. This allows simpler management of scenarios where additional user actions are needed to pay a subscription’s invoice. Such as failed payments, [SCA regulation](https://stripe.com/docs/billing/migration/strong-customer-authentication), or collecting a mandate for a bank debit payment method.
    
    Use `pending_if_incomplete` to update the subscription using [pending updates](https://stripe.com/docs/billing/subscriptions/pending-updates). When you use `pending_if_incomplete` you can only pass the parameters [supported by pending updates](https://stripe.com/docs/billing/pending-updates-reference#supported-attributes).
    
    Use `error_if_incomplete` if you want Stripe to return an HTTP 402 status code if a subscription's invoice cannot be paid. For example, if a payment method requires 3DS authentication due to SCA regulation and further user action is needed, this parameter does not update the subscription and returns an error instead. This was the default behavior for API versions prior to 2019-03-14. See the [changelog](https://stripe.com/docs/upgrades#2019-03-14) to learn more.
    """

    payment_settings: typing_extensions.NotRequired[
        SubscriptionUpdateBodyPaymentSettings
    ]
    """
    Payment settings to pass to invoices created by the subscription.
    """

    pending_invoice_item_interval: typing_extensions.NotRequired[
        typing.Union[SubscriptionUpdateBodyPendingInvoiceItemIntervalObj0, str]
    ]
    """
    Specifies an interval for how often to bill for any pending invoice items. It is analogous to calling [Create an invoice](https://stripe.com/docs/api#create_invoice) for the given subscription at the specified interval.
    """

    proration_behavior: typing_extensions.NotRequired[
        typing_extensions.Literal["always_invoice", "create_prorations", "none"]
    ]
    """
    Determines how to handle [prorations](https://stripe.com/docs/billing/subscriptions/prorations) when the billing cycle changes (e.g., when switching plans, resetting `billing_cycle_anchor=now`, or starting a trial), or if an item's `quantity` changes. The default value is `create_prorations`.
    """

    proration_date: typing_extensions.NotRequired[int]
    """
    If set, the proration will be calculated as though the subscription was updated at the given time. This can be used to apply exactly the same proration that was previewed with [upcoming invoice](https://stripe.com/docs/api#upcoming_invoice) endpoint. It can also be used to implement custom proration logic, such as prorating by day instead of by second, by providing the time that you wish to use for proration calculations.
    """

    transfer_data: typing_extensions.NotRequired[
        typing.Union[SubscriptionUpdateBodyTransferDataObj0, str]
    ]
    """
    If specified, the funds from the subscription's invoices will be transferred to the destination and the ID of the resulting transfers will be found on the resulting charges. This will be unset if you POST an empty value.
    """

    trial_end: typing_extensions.NotRequired[
        typing.Union[typing_extensions.Literal["now"], int]
    ]
    """
    Unix timestamp representing the end of the trial period the customer will get before being charged for the first time. This will always overwrite any trials that might apply via a subscribed plan. If set, trial_end will override the default trial period of the plan the customer is being subscribed to. The special value `now` can be provided to end the customer's trial immediately. Can be at most two years from `billing_cycle_anchor`.
    """

    trial_from_plan: typing_extensions.NotRequired[bool]
    """
    Indicates if a plan's `trial_period_days` should be applied to the subscription. Setting `trial_end` per subscription is preferred, and this defaults to `false`. Setting this flag to `true` together with `trial_end` is not allowed. See [Using trial periods on subscriptions](https://stripe.com/docs/billing/subscriptions/trials) to learn more.
    """

    trial_settings: typing_extensions.NotRequired[SubscriptionUpdateBodyTrialSettings]
    """
    Settings related to subscription trials.
    """


class _SerializerSubscriptionUpdateBody(pydantic.BaseModel):
    """
    Serializer for SubscriptionUpdateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    add_invoice_items: typing.Optional[
        typing.List[_SerializerSubscriptionUpdateBodyAddInvoiceItemsItem]
    ] = pydantic.Field(alias="add_invoice_items", default=None)
    application_fee_percent: typing.Optional[typing.Union[float, str]] = pydantic.Field(
        alias="application_fee_percent", default=None
    )
    automatic_tax: typing.Optional[_SerializerSubscriptionUpdateBodyAutomaticTax] = (
        pydantic.Field(alias="automatic_tax", default=None)
    )
    billing_cycle_anchor: typing.Optional[
        typing_extensions.Literal["now", "unchanged"]
    ] = pydantic.Field(alias="billing_cycle_anchor", default=None)
    cancel_at: typing.Optional[typing.Union[int, str]] = pydantic.Field(
        alias="cancel_at", default=None
    )
    cancel_at_period_end: typing.Optional[bool] = pydantic.Field(
        alias="cancel_at_period_end", default=None
    )
    cancellation_details: typing.Optional[
        _SerializerSubscriptionUpdateBodyCancellationDetails
    ] = pydantic.Field(alias="cancellation_details", default=None)
    collection_method: typing.Optional[
        typing_extensions.Literal["charge_automatically", "send_invoice"]
    ] = pydantic.Field(alias="collection_method", default=None)
    days_until_due: typing.Optional[int] = pydantic.Field(
        alias="days_until_due", default=None
    )
    default_payment_method: typing.Optional[str] = pydantic.Field(
        alias="default_payment_method", default=None
    )
    default_source: typing.Optional[typing.Union[str, str]] = pydantic.Field(
        alias="default_source", default=None
    )
    default_tax_rates: typing.Optional[typing.Union[typing.List[str], str]] = (
        pydantic.Field(alias="default_tax_rates", default=None)
    )
    description: typing.Optional[typing.Union[str, str]] = pydantic.Field(
        alias="description", default=None
    )
    discounts: typing.Optional[
        typing.Union[
            typing.List[_SerializerSubscriptionUpdateBodyDiscountsArr0Item], str
        ]
    ] = pydantic.Field(alias="discounts", default=None)
    expand: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="expand", default=None
    )
    invoice_settings: typing.Optional[
        _SerializerSubscriptionUpdateBodyInvoiceSettings
    ] = pydantic.Field(alias="invoice_settings", default=None)
    items: typing.Optional[typing.List[_SerializerSubscriptionUpdateBodyItemsItem]] = (
        pydantic.Field(alias="items", default=None)
    )
    metadata: typing.Optional[
        typing.Union[_SerializerSubscriptionUpdateBodyMetadataObj0, str]
    ] = pydantic.Field(alias="metadata", default=None)
    off_session: typing.Optional[bool] = pydantic.Field(
        alias="off_session", default=None
    )
    on_behalf_of: typing.Optional[typing.Union[str, str]] = pydantic.Field(
        alias="on_behalf_of", default=None
    )
    pause_collection: typing.Optional[
        typing.Union[_SerializerSubscriptionUpdateBodyPauseCollectionObj0, str]
    ] = pydantic.Field(alias="pause_collection", default=None)
    payment_behavior: typing.Optional[
        typing_extensions.Literal[
            "allow_incomplete",
            "default_incomplete",
            "error_if_incomplete",
            "pending_if_incomplete",
        ]
    ] = pydantic.Field(alias="payment_behavior", default=None)
    payment_settings: typing.Optional[
        _SerializerSubscriptionUpdateBodyPaymentSettings
    ] = pydantic.Field(alias="payment_settings", default=None)
    pending_invoice_item_interval: typing.Optional[
        typing.Union[
            _SerializerSubscriptionUpdateBodyPendingInvoiceItemIntervalObj0, str
        ]
    ] = pydantic.Field(alias="pending_invoice_item_interval", default=None)
    proration_behavior: typing.Optional[
        typing_extensions.Literal["always_invoice", "create_prorations", "none"]
    ] = pydantic.Field(alias="proration_behavior", default=None)
    proration_date: typing.Optional[int] = pydantic.Field(
        alias="proration_date", default=None
    )
    transfer_data: typing.Optional[
        typing.Union[_SerializerSubscriptionUpdateBodyTransferDataObj0, str]
    ] = pydantic.Field(alias="transfer_data", default=None)
    trial_end: typing.Optional[typing.Union[typing_extensions.Literal["now"], int]] = (
        pydantic.Field(alias="trial_end", default=None)
    )
    trial_from_plan: typing.Optional[bool] = pydantic.Field(
        alias="trial_from_plan", default=None
    )
    trial_settings: typing.Optional[_SerializerSubscriptionUpdateBodyTrialSettings] = (
        pydantic.Field(alias="trial_settings", default=None)
    )
