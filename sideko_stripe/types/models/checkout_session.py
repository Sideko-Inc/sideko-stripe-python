import pydantic
import typing
import typing_extensions

from .checkout_session_metadata import CheckoutSessionMetadata
from .checkout_session_payment_method_options import CheckoutSessionPaymentMethodOptions
from .deleted_customer import DeletedCustomer
from .payment_flows_payment_intent_presentment_details import (
    PaymentFlowsPaymentIntentPresentmentDetails,
)
from .payment_method_config_biz_payment_method_configuration_details import (
    PaymentMethodConfigBizPaymentMethodConfigurationDetails,
)
from .payment_pages_checkout_session_adaptive_pricing import (
    PaymentPagesCheckoutSessionAdaptivePricing,
)
from .payment_pages_checkout_session_after_expiration import (
    PaymentPagesCheckoutSessionAfterExpiration,
)
from .payment_pages_checkout_session_collected_information import (
    PaymentPagesCheckoutSessionCollectedInformation,
)
from .payment_pages_checkout_session_consent import PaymentPagesCheckoutSessionConsent
from .payment_pages_checkout_session_consent_collection import (
    PaymentPagesCheckoutSessionConsentCollection,
)
from .payment_pages_checkout_session_currency_conversion import (
    PaymentPagesCheckoutSessionCurrencyConversion,
)
from .payment_pages_checkout_session_custom_fields import (
    PaymentPagesCheckoutSessionCustomFields,
)
from .payment_pages_checkout_session_custom_text import (
    PaymentPagesCheckoutSessionCustomText,
)
from .payment_pages_checkout_session_customer_details import (
    PaymentPagesCheckoutSessionCustomerDetails,
)
from .payment_pages_checkout_session_optional_item import (
    PaymentPagesCheckoutSessionOptionalItem,
)
from .payment_pages_checkout_session_permissions import (
    PaymentPagesCheckoutSessionPermissions,
)
from .payment_pages_checkout_session_phone_number_collection import (
    PaymentPagesCheckoutSessionPhoneNumberCollection,
)
from .payment_pages_checkout_session_saved_payment_method_options import (
    PaymentPagesCheckoutSessionSavedPaymentMethodOptions,
)
from .payment_pages_checkout_session_shipping_address_collection import (
    PaymentPagesCheckoutSessionShippingAddressCollection,
)
from .payment_pages_checkout_session_shipping_cost import (
    PaymentPagesCheckoutSessionShippingCost,
)
from .payment_pages_checkout_session_shipping_option import (
    PaymentPagesCheckoutSessionShippingOption,
)
from .payment_pages_checkout_session_tax_id_collection import (
    PaymentPagesCheckoutSessionTaxIdCollection,
)

if typing_extensions.TYPE_CHECKING:
    from .checkout_session_line_items import CheckoutSessionLineItems
    from .customer import Customer
    from .invoice import Invoice
    from .payment_intent import PaymentIntent
    from .payment_link import PaymentLink
    from .payment_pages_checkout_session_automatic_tax import (
        PaymentPagesCheckoutSessionAutomaticTax,
    )
    from .payment_pages_checkout_session_discount import (
        PaymentPagesCheckoutSessionDiscount,
    )
    from .payment_pages_checkout_session_invoice_creation import (
        PaymentPagesCheckoutSessionInvoiceCreation,
    )
    from .payment_pages_checkout_session_total_details import (
        PaymentPagesCheckoutSessionTotalDetails,
    )
    from .setup_intent import SetupIntent
    from .subscription import Subscription


class CheckoutSession(pydantic.BaseModel):
    """
    A Checkout Session represents your customer's session as they pay for
    one-time purchases or subscriptions through [Checkout](https://stripe.com/docs/payments/checkout)
    or [Payment Links](https://stripe.com/docs/payments/payment-links). We recommend creating a
    new Session each time your customer attempts to pay.

    Once payment is successful, the Checkout Session will contain a reference
    to the [Customer](https://stripe.com/docs/api/customers), and either the successful
    [PaymentIntent](https://stripe.com/docs/api/payment_intents) or an active
    [Subscription](https://stripe.com/docs/api/subscriptions).

    You can create a Checkout Session on your server and redirect to its URL
    to begin Checkout.

    Related guide: [Checkout quickstart](https://stripe.com/docs/checkout/quickstart)
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    adaptive_pricing: typing.Optional[PaymentPagesCheckoutSessionAdaptivePricing] = (
        pydantic.Field(alias="adaptive_pricing", default=None)
    )
    after_expiration: typing.Optional[PaymentPagesCheckoutSessionAfterExpiration] = (
        pydantic.Field(alias="after_expiration", default=None)
    )
    allow_promotion_codes: typing.Optional[bool] = pydantic.Field(
        alias="allow_promotion_codes", default=None
    )
    """
    Enables user redeemable promotion codes.
    """
    amount_subtotal: typing.Optional[int] = pydantic.Field(
        alias="amount_subtotal", default=None
    )
    """
    Total of all items before discounts or taxes are applied.
    """
    amount_total: typing.Optional[int] = pydantic.Field(
        alias="amount_total", default=None
    )
    """
    Total of all items after discounts and taxes are applied.
    """
    automatic_tax: "PaymentPagesCheckoutSessionAutomaticTax" = pydantic.Field(
        alias="automatic_tax",
    )
    billing_address_collection: typing.Optional[
        typing_extensions.Literal["auto", "required"]
    ] = pydantic.Field(alias="billing_address_collection", default=None)
    """
    Describes whether Checkout should collect the customer's billing address. Defaults to `auto`.
    """
    cancel_url: typing.Optional[str] = pydantic.Field(alias="cancel_url", default=None)
    """
    If set, Checkout displays a back button and customers will be directed to this URL if they decide to cancel payment and return to your website.
    """
    client_reference_id: typing.Optional[str] = pydantic.Field(
        alias="client_reference_id", default=None
    )
    """
    A unique string to reference the Checkout Session. This can be a
    customer ID, a cart ID, or similar, and can be used to reconcile the
    Session with your internal systems.
    """
    client_secret: typing.Optional[str] = pydantic.Field(
        alias="client_secret", default=None
    )
    """
    The client secret of your Checkout Session. Applies to Checkout Sessions with `ui_mode: embedded`. Client secret to be used when initializing Stripe.js embedded checkout.
    """
    collected_information: typing.Optional[
        PaymentPagesCheckoutSessionCollectedInformation
    ] = pydantic.Field(alias="collected_information", default=None)
    consent: typing.Optional[PaymentPagesCheckoutSessionConsent] = pydantic.Field(
        alias="consent", default=None
    )
    consent_collection: typing.Optional[
        PaymentPagesCheckoutSessionConsentCollection
    ] = pydantic.Field(alias="consent_collection", default=None)
    created: int = pydantic.Field(
        alias="created",
    )
    """
    Time at which the object was created. Measured in seconds since the Unix epoch.
    """
    currency: typing.Optional[str] = pydantic.Field(alias="currency", default=None)
    """
    Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    """
    currency_conversion: typing.Optional[
        PaymentPagesCheckoutSessionCurrencyConversion
    ] = pydantic.Field(alias="currency_conversion", default=None)
    custom_fields: typing.List[PaymentPagesCheckoutSessionCustomFields] = (
        pydantic.Field(
            alias="custom_fields",
        )
    )
    """
    Collect additional information from your customer using custom fields. Up to 3 fields are supported.
    """
    custom_text: PaymentPagesCheckoutSessionCustomText = pydantic.Field(
        alias="custom_text",
    )
    customer: typing.Optional[typing.Union[str, "Customer", DeletedCustomer]] = (
        pydantic.Field(alias="customer", default=None)
    )
    """
    The ID of the customer for this Session.
    For Checkout Sessions in `subscription` mode or Checkout Sessions with `customer_creation` set as `always` in `payment` mode, Checkout
    will create a new customer object based on information provided
    during the payment flow unless an existing customer was provided when
    the Session was created.
    """
    customer_creation: typing.Optional[
        typing_extensions.Literal["always", "if_required"]
    ] = pydantic.Field(alias="customer_creation", default=None)
    """
    Configure whether a Checkout Session creates a Customer when the Checkout Session completes.
    """
    customer_details: typing.Optional[PaymentPagesCheckoutSessionCustomerDetails] = (
        pydantic.Field(alias="customer_details", default=None)
    )
    customer_email: typing.Optional[str] = pydantic.Field(
        alias="customer_email", default=None
    )
    """
    If provided, this value will be used when the Customer object is created.
    If not provided, customers will be asked to enter their email address.
    Use this parameter to prefill customer data if you already have an email
    on file. To access information about the customer once the payment flow is
    complete, use the `customer` attribute.
    """
    discounts: typing.Optional[typing.List["PaymentPagesCheckoutSessionDiscount"]] = (
        pydantic.Field(alias="discounts", default=None)
    )
    """
    List of coupons and promotion codes attached to the Checkout Session.
    """
    expires_at: int = pydantic.Field(
        alias="expires_at",
    )
    """
    The timestamp at which the Checkout Session will expire.
    """
    id: str = pydantic.Field(
        alias="id",
    )
    """
    Unique identifier for the object.
    """
    invoice: typing.Optional[typing.Union[str, "Invoice"]] = pydantic.Field(
        alias="invoice", default=None
    )
    """
    ID of the invoice created by the Checkout Session, if it exists.
    """
    invoice_creation: typing.Optional["PaymentPagesCheckoutSessionInvoiceCreation"] = (
        pydantic.Field(alias="invoice_creation", default=None)
    )
    line_items: typing.Optional["CheckoutSessionLineItems"] = pydantic.Field(
        alias="line_items", default=None
    )
    """
    The line items purchased by the customer.
    """
    livemode: bool = pydantic.Field(
        alias="livemode",
    )
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    locale: typing.Optional[
        typing_extensions.Literal[
            "auto",
            "bg",
            "cs",
            "da",
            "de",
            "el",
            "en",
            "en-GB",
            "es",
            "es-419",
            "et",
            "fi",
            "fil",
            "fr",
            "fr-CA",
            "hr",
            "hu",
            "id",
            "it",
            "ja",
            "ko",
            "lt",
            "lv",
            "ms",
            "mt",
            "nb",
            "nl",
            "pl",
            "pt",
            "pt-BR",
            "ro",
            "ru",
            "sk",
            "sl",
            "sv",
            "th",
            "tr",
            "vi",
            "zh",
            "zh-HK",
            "zh-TW",
        ]
    ] = pydantic.Field(alias="locale", default=None)
    """
    The IETF language tag of the locale Checkout is displayed in. If blank or `auto`, the browser's locale is used.
    """
    metadata: typing.Optional[CheckoutSessionMetadata] = pydantic.Field(
        alias="metadata", default=None
    )
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    mode: typing_extensions.Literal["payment", "setup", "subscription"] = (
        pydantic.Field(
            alias="mode",
        )
    )
    """
    The mode of the Checkout Session.
    """
    object: typing_extensions.Literal["checkout.session"] = pydantic.Field(
        alias="object",
    )
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    optional_items: typing.Optional[
        typing.List[PaymentPagesCheckoutSessionOptionalItem]
    ] = pydantic.Field(alias="optional_items", default=None)
    """
    The optional items presented to the customer at checkout.
    """
    payment_intent: typing.Optional[typing.Union[str, "PaymentIntent"]] = (
        pydantic.Field(alias="payment_intent", default=None)
    )
    """
    The ID of the PaymentIntent for Checkout Sessions in `payment` mode. You can't confirm or cancel the PaymentIntent for a Checkout Session. To cancel, [expire the Checkout Session](https://stripe.com/docs/api/checkout/sessions/expire) instead.
    """
    payment_link: typing.Optional[typing.Union[str, "PaymentLink"]] = pydantic.Field(
        alias="payment_link", default=None
    )
    """
    The ID of the Payment Link that created this Session.
    """
    payment_method_collection: typing.Optional[
        typing_extensions.Literal["always", "if_required"]
    ] = pydantic.Field(alias="payment_method_collection", default=None)
    """
    Configure whether a Checkout Session should collect a payment method. Defaults to `always`.
    """
    payment_method_configuration_details: typing.Optional[
        PaymentMethodConfigBizPaymentMethodConfigurationDetails
    ] = pydantic.Field(alias="payment_method_configuration_details", default=None)
    payment_method_options: typing.Optional[CheckoutSessionPaymentMethodOptions] = (
        pydantic.Field(alias="payment_method_options", default=None)
    )
    payment_method_types: typing.List[str] = pydantic.Field(
        alias="payment_method_types",
    )
    """
    A list of the types of payment methods (e.g. card) this Checkout
    Session is allowed to accept.
    """
    payment_status: typing_extensions.Literal[
        "no_payment_required", "paid", "unpaid"
    ] = pydantic.Field(
        alias="payment_status",
    )
    """
    The payment status of the Checkout Session, one of `paid`, `unpaid`, or `no_payment_required`.
    You can use this value to decide when to fulfill your customer's order.
    """
    permissions: typing.Optional[PaymentPagesCheckoutSessionPermissions] = (
        pydantic.Field(alias="permissions", default=None)
    )
    phone_number_collection: typing.Optional[
        PaymentPagesCheckoutSessionPhoneNumberCollection
    ] = pydantic.Field(alias="phone_number_collection", default=None)
    presentment_details: typing.Optional[
        PaymentFlowsPaymentIntentPresentmentDetails
    ] = pydantic.Field(alias="presentment_details", default=None)
    recovered_from: typing.Optional[str] = pydantic.Field(
        alias="recovered_from", default=None
    )
    """
    The ID of the original expired Checkout Session that triggered the recovery flow.
    """
    redirect_on_completion: typing.Optional[
        typing_extensions.Literal["always", "if_required", "never"]
    ] = pydantic.Field(alias="redirect_on_completion", default=None)
    """
    This parameter applies to `ui_mode: embedded`. Learn more about the [redirect behavior](https://stripe.com/docs/payments/checkout/custom-success-page?payment-ui=embedded-form) of embedded sessions. Defaults to `always`.
    """
    return_url: typing.Optional[str] = pydantic.Field(alias="return_url", default=None)
    """
    Applies to Checkout Sessions with `ui_mode: embedded`. The URL to redirect your customer back to after they authenticate or cancel their payment on the payment method's app or site.
    """
    saved_payment_method_options: typing.Optional[
        PaymentPagesCheckoutSessionSavedPaymentMethodOptions
    ] = pydantic.Field(alias="saved_payment_method_options", default=None)
    setup_intent: typing.Optional[typing.Union[str, "SetupIntent"]] = pydantic.Field(
        alias="setup_intent", default=None
    )
    """
    The ID of the SetupIntent for Checkout Sessions in `setup` mode. You can't confirm or cancel the SetupIntent for a Checkout Session. To cancel, [expire the Checkout Session](https://stripe.com/docs/api/checkout/sessions/expire) instead.
    """
    shipping_address_collection: typing.Optional[
        PaymentPagesCheckoutSessionShippingAddressCollection
    ] = pydantic.Field(alias="shipping_address_collection", default=None)
    shipping_cost: typing.Optional[PaymentPagesCheckoutSessionShippingCost] = (
        pydantic.Field(alias="shipping_cost", default=None)
    )
    shipping_options: typing.List[PaymentPagesCheckoutSessionShippingOption] = (
        pydantic.Field(
            alias="shipping_options",
        )
    )
    """
    The shipping rate options applied to this Session.
    """
    status: typing.Optional[
        typing_extensions.Literal["complete", "expired", "open"]
    ] = pydantic.Field(alias="status", default=None)
    """
    The status of the Checkout Session, one of `open`, `complete`, or `expired`.
    """
    submit_type: typing.Optional[
        typing_extensions.Literal["auto", "book", "donate", "pay", "subscribe"]
    ] = pydantic.Field(alias="submit_type", default=None)
    """
    Describes the type of transaction being performed by Checkout in order to customize
    relevant text on the page, such as the submit button. `submit_type` can only be
    specified on Checkout Sessions in `payment` mode. If blank or `auto`, `pay` is used.
    """
    subscription: typing.Optional[typing.Union[str, "Subscription"]] = pydantic.Field(
        alias="subscription", default=None
    )
    """
    The ID of the subscription for Checkout Sessions in `subscription` mode.
    """
    success_url: typing.Optional[str] = pydantic.Field(
        alias="success_url", default=None
    )
    """
    The URL the customer will be directed to after the payment or
    subscription creation is successful.
    """
    tax_id_collection: typing.Optional[PaymentPagesCheckoutSessionTaxIdCollection] = (
        pydantic.Field(alias="tax_id_collection", default=None)
    )
    total_details: typing.Optional["PaymentPagesCheckoutSessionTotalDetails"] = (
        pydantic.Field(alias="total_details", default=None)
    )
    ui_mode: typing.Optional[
        typing_extensions.Literal["custom", "embedded", "hosted"]
    ] = pydantic.Field(alias="ui_mode", default=None)
    """
    The UI mode of the Session. Defaults to `hosted`.
    """
    url: typing.Optional[str] = pydantic.Field(alias="url", default=None)
    """
    The URL to the Checkout Session. Applies to Checkout Sessions with `ui_mode: hosted`. Redirect customers to this URL to take them to Checkout. If you’re using [Custom Domains](https://stripe.com/docs/payments/checkout/custom-domains), the URL will use your subdomain. Otherwise, it’ll use `checkout.stripe.com.`
    This value is only present when the session is active.
    """
