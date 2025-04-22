import pydantic
import typing
import typing_extensions

from .checkout_session_create_body_adaptive_pricing import (
    CheckoutSessionCreateBodyAdaptivePricing,
    _SerializerCheckoutSessionCreateBodyAdaptivePricing,
)
from .checkout_session_create_body_after_expiration import (
    CheckoutSessionCreateBodyAfterExpiration,
    _SerializerCheckoutSessionCreateBodyAfterExpiration,
)
from .checkout_session_create_body_automatic_tax import (
    CheckoutSessionCreateBodyAutomaticTax,
    _SerializerCheckoutSessionCreateBodyAutomaticTax,
)
from .checkout_session_create_body_consent_collection import (
    CheckoutSessionCreateBodyConsentCollection,
    _SerializerCheckoutSessionCreateBodyConsentCollection,
)
from .checkout_session_create_body_custom_fields_item import (
    CheckoutSessionCreateBodyCustomFieldsItem,
    _SerializerCheckoutSessionCreateBodyCustomFieldsItem,
)
from .checkout_session_create_body_custom_text import (
    CheckoutSessionCreateBodyCustomText,
    _SerializerCheckoutSessionCreateBodyCustomText,
)
from .checkout_session_create_body_customer_update import (
    CheckoutSessionCreateBodyCustomerUpdate,
    _SerializerCheckoutSessionCreateBodyCustomerUpdate,
)
from .checkout_session_create_body_discounts_item import (
    CheckoutSessionCreateBodyDiscountsItem,
    _SerializerCheckoutSessionCreateBodyDiscountsItem,
)
from .checkout_session_create_body_invoice_creation import (
    CheckoutSessionCreateBodyInvoiceCreation,
    _SerializerCheckoutSessionCreateBodyInvoiceCreation,
)
from .checkout_session_create_body_line_items_item import (
    CheckoutSessionCreateBodyLineItemsItem,
    _SerializerCheckoutSessionCreateBodyLineItemsItem,
)
from .checkout_session_create_body_metadata import (
    CheckoutSessionCreateBodyMetadata,
    _SerializerCheckoutSessionCreateBodyMetadata,
)
from .checkout_session_create_body_optional_items_item import (
    CheckoutSessionCreateBodyOptionalItemsItem,
    _SerializerCheckoutSessionCreateBodyOptionalItemsItem,
)
from .checkout_session_create_body_payment_intent_data import (
    CheckoutSessionCreateBodyPaymentIntentData,
    _SerializerCheckoutSessionCreateBodyPaymentIntentData,
)
from .checkout_session_create_body_payment_method_data import (
    CheckoutSessionCreateBodyPaymentMethodData,
    _SerializerCheckoutSessionCreateBodyPaymentMethodData,
)
from .checkout_session_create_body_payment_method_options import (
    CheckoutSessionCreateBodyPaymentMethodOptions,
    _SerializerCheckoutSessionCreateBodyPaymentMethodOptions,
)
from .checkout_session_create_body_permissions import (
    CheckoutSessionCreateBodyPermissions,
    _SerializerCheckoutSessionCreateBodyPermissions,
)
from .checkout_session_create_body_phone_number_collection import (
    CheckoutSessionCreateBodyPhoneNumberCollection,
    _SerializerCheckoutSessionCreateBodyPhoneNumberCollection,
)
from .checkout_session_create_body_saved_payment_method_options import (
    CheckoutSessionCreateBodySavedPaymentMethodOptions,
    _SerializerCheckoutSessionCreateBodySavedPaymentMethodOptions,
)
from .checkout_session_create_body_setup_intent_data import (
    CheckoutSessionCreateBodySetupIntentData,
    _SerializerCheckoutSessionCreateBodySetupIntentData,
)
from .checkout_session_create_body_shipping_address_collection import (
    CheckoutSessionCreateBodyShippingAddressCollection,
    _SerializerCheckoutSessionCreateBodyShippingAddressCollection,
)
from .checkout_session_create_body_shipping_options_item import (
    CheckoutSessionCreateBodyShippingOptionsItem,
    _SerializerCheckoutSessionCreateBodyShippingOptionsItem,
)
from .checkout_session_create_body_subscription_data import (
    CheckoutSessionCreateBodySubscriptionData,
    _SerializerCheckoutSessionCreateBodySubscriptionData,
)
from .checkout_session_create_body_tax_id_collection import (
    CheckoutSessionCreateBodyTaxIdCollection,
    _SerializerCheckoutSessionCreateBodyTaxIdCollection,
)


class CheckoutSessionCreateBody(typing_extensions.TypedDict, total=False):
    """
    CheckoutSessionCreateBody
    """

    adaptive_pricing: typing_extensions.NotRequired[
        CheckoutSessionCreateBodyAdaptivePricing
    ]
    """
    Settings for price localization with [Adaptive Pricing](https://docs.stripe.com/payments/checkout/adaptive-pricing).
    """

    after_expiration: typing_extensions.NotRequired[
        CheckoutSessionCreateBodyAfterExpiration
    ]
    """
    Configure actions after a Checkout Session has expired.
    """

    allow_promotion_codes: typing_extensions.NotRequired[bool]
    """
    Enables user redeemable promotion codes.
    """

    automatic_tax: typing_extensions.NotRequired[CheckoutSessionCreateBodyAutomaticTax]
    """
    Settings for automatic tax lookup for this session and resulting payments, invoices, and subscriptions.
    """

    billing_address_collection: typing_extensions.NotRequired[
        typing_extensions.Literal["auto", "required"]
    ]
    """
    Specify whether Checkout should collect the customer's billing address. Defaults to `auto`.
    """

    cancel_url: typing_extensions.NotRequired[str]
    """
    If set, Checkout displays a back button and customers will be directed to this URL if they decide to cancel payment and return to your website. This parameter is not allowed if ui_mode is `embedded` or `custom`.
    """

    client_reference_id: typing_extensions.NotRequired[str]
    """
    A unique string to reference the Checkout Session. This can be a
    customer ID, a cart ID, or similar, and can be used to reconcile the
    session with your internal systems.
    """

    consent_collection: typing_extensions.NotRequired[
        CheckoutSessionCreateBodyConsentCollection
    ]
    """
    Configure fields for the Checkout Session to gather active consent from customers.
    """

    currency: typing_extensions.NotRequired[str]
    """
    Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies). Required in `setup` mode when `payment_method_types` is not set.
    """

    custom_fields: typing_extensions.NotRequired[
        typing.List[CheckoutSessionCreateBodyCustomFieldsItem]
    ]
    """
    Collect additional information from your customer using custom fields. Up to 3 fields are supported.
    """

    custom_text: typing_extensions.NotRequired[CheckoutSessionCreateBodyCustomText]
    """
    Display additional text for your customers using custom text.
    """

    customer: typing_extensions.NotRequired[str]
    """
    ID of an existing Customer, if one exists. In `payment` mode, the customer’s most recently saved card
    payment method will be used to prefill the email, name, card details, and billing address
    on the Checkout page. In `subscription` mode, the customer’s [default payment method](https://stripe.com/docs/api/customers/update#update_customer-invoice_settings-default_payment_method)
    will be used if it’s a card, otherwise the most recently saved card will be used. A valid billing address, billing name and billing email are required on the payment method for Checkout to prefill the customer's card details.
    
    If the Customer already has a valid [email](https://stripe.com/docs/api/customers/object#customer_object-email) set, the email will be prefilled and not editable in Checkout.
    If the Customer does not have a valid `email`, Checkout will set the email entered during the session on the Customer.
    
    If blank for Checkout Sessions in `subscription` mode or with `customer_creation` set as `always` in `payment` mode, Checkout will create a new Customer object based on information provided during the payment flow.
    
    You can set [`payment_intent_data.setup_future_usage`](https://stripe.com/docs/api/checkout/sessions/create#create_checkout_session-payment_intent_data-setup_future_usage) to have Checkout automatically attach the payment method to the Customer you pass in for future reuse.
    """

    customer_creation: typing_extensions.NotRequired[
        typing_extensions.Literal["always", "if_required"]
    ]
    """
    Configure whether a Checkout Session creates a [Customer](https://stripe.com/docs/api/customers) during Session confirmation.
    
    When a Customer is not created, you can still retrieve email, address, and other customer data entered in Checkout
    with [customer_details](https://stripe.com/docs/api/checkout/sessions/object#checkout_session_object-customer_details).
    
    Sessions that don't create Customers instead are grouped by [guest customers](https://stripe.com/docs/payments/checkout/guest-customers)
    in the Dashboard. Promotion codes limited to first time customers will return invalid for these Sessions.
    
    Can only be set in `payment` and `setup` mode.
    """

    customer_email: typing_extensions.NotRequired[str]
    """
    If provided, this value will be used when the Customer object is created.
    If not provided, customers will be asked to enter their email address.
    Use this parameter to prefill customer data if you already have an email
    on file. To access information about the customer once a session is
    complete, use the `customer` field.
    """

    customer_update: typing_extensions.NotRequired[
        CheckoutSessionCreateBodyCustomerUpdate
    ]
    """
    Controls what fields on Customer can be updated by the Checkout Session. Can only be provided when `customer` is provided.
    """

    discounts: typing_extensions.NotRequired[
        typing.List[CheckoutSessionCreateBodyDiscountsItem]
    ]
    """
    The coupon or promotion code to apply to this Session. Currently, only up to one may be specified.
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """

    expires_at: typing_extensions.NotRequired[int]
    """
    The Epoch time in seconds at which the Checkout Session will expire. It can be anywhere from 30 minutes to 24 hours after Checkout Session creation. By default, this value is 24 hours from creation.
    """

    invoice_creation: typing_extensions.NotRequired[
        CheckoutSessionCreateBodyInvoiceCreation
    ]
    """
    Generate a post-purchase Invoice for one-time payments.
    """

    line_items: typing_extensions.NotRequired[
        typing.List[CheckoutSessionCreateBodyLineItemsItem]
    ]
    """
    A list of items the customer is purchasing. Use this parameter to pass one-time or recurring [Prices](https://stripe.com/docs/api/prices).
    
    For `payment` mode, there is a maximum of 100 line items, however it is recommended to consolidate line items if there are more than a few dozen.
    
    For `subscription` mode, there is a maximum of 20 line items with recurring Prices and 20 line items with one-time Prices. Line items with one-time Prices will be on the initial invoice only.
    """

    locale: typing_extensions.NotRequired[
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
    ]
    """
    The IETF language tag of the locale Checkout is displayed in. If blank or `auto`, the browser's locale is used.
    """

    metadata: typing_extensions.NotRequired[CheckoutSessionCreateBodyMetadata]
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    """

    mode: typing_extensions.NotRequired[
        typing_extensions.Literal["payment", "setup", "subscription"]
    ]
    """
    The mode of the Checkout Session. Pass `subscription` if the Checkout Session includes at least one recurring item.
    """

    optional_items: typing_extensions.NotRequired[
        typing.List[CheckoutSessionCreateBodyOptionalItemsItem]
    ]
    """
    A list of optional items the customer can add to their order at checkout. Use this parameter to pass one-time or recurring [Prices](https://stripe.com/docs/api/prices).
    
    There is a maximum of 10 optional items allowed on a Checkout Session, and the existing limits on the number of line items allowed on a Checkout Session apply to the combined number of line items and optional items.
    
    For `payment` mode, there is a maximum of 100 combined line items and optional items, however it is recommended to consolidate items if there are more than a few dozen.
    
    For `subscription` mode, there is a maximum of 20 line items and optional items with recurring Prices and 20 line items and optional items with one-time Prices.
    """

    payment_intent_data: typing_extensions.NotRequired[
        CheckoutSessionCreateBodyPaymentIntentData
    ]
    """
    A subset of parameters to be passed to PaymentIntent creation for Checkout Sessions in `payment` mode.
    """

    payment_method_collection: typing_extensions.NotRequired[
        typing_extensions.Literal["always", "if_required"]
    ]
    """
    Specify whether Checkout should collect a payment method. When set to `if_required`, Checkout will not collect a payment method when the total due for the session is 0.
    This may occur if the Checkout Session includes a free trial or a discount.
    
    Can only be set in `subscription` mode. Defaults to `always`.
    
    If you'd like information on how to collect a payment method outside of Checkout, read the guide on configuring [subscriptions with a free trial](https://stripe.com/docs/payments/checkout/free-trials).
    """

    payment_method_configuration: typing_extensions.NotRequired[str]
    """
    The ID of the payment method configuration to use with this Checkout session.
    """

    payment_method_data: typing_extensions.NotRequired[
        CheckoutSessionCreateBodyPaymentMethodData
    ]
    """
    This parameter allows you to set some attributes on the payment method created during a Checkout session.
    """

    payment_method_options: typing_extensions.NotRequired[
        CheckoutSessionCreateBodyPaymentMethodOptions
    ]
    """
    Payment-method-specific configuration.
    """

    payment_method_types: typing_extensions.NotRequired[
        typing.List[
            typing_extensions.Literal[
                "acss_debit",
                "affirm",
                "afterpay_clearpay",
                "alipay",
                "alma",
                "amazon_pay",
                "au_becs_debit",
                "bacs_debit",
                "bancontact",
                "billie",
                "blik",
                "boleto",
                "card",
                "cashapp",
                "customer_balance",
                "eps",
                "fpx",
                "giropay",
                "grabpay",
                "ideal",
                "kakao_pay",
                "klarna",
                "konbini",
                "kr_card",
                "link",
                "mobilepay",
                "multibanco",
                "naver_pay",
                "oxxo",
                "p24",
                "pay_by_bank",
                "payco",
                "paynow",
                "paypal",
                "pix",
                "promptpay",
                "revolut_pay",
                "samsung_pay",
                "satispay",
                "sepa_debit",
                "sofort",
                "swish",
                "twint",
                "us_bank_account",
                "wechat_pay",
                "zip",
            ]
        ]
    ]
    """
    A list of the types of payment methods (e.g., `card`) this Checkout Session can accept.
    
    You can omit this attribute to manage your payment methods from the [Stripe Dashboard](https://dashboard.stripe.com/settings/payment_methods).
    See [Dynamic Payment Methods](https://stripe.com/docs/payments/payment-methods/integration-options#using-dynamic-payment-methods) for more details.
    
    Read more about the supported payment methods and their requirements in our [payment
    method details guide](/docs/payments/checkout/payment-methods).
    
    If multiple payment methods are passed, Checkout will dynamically reorder them to
    prioritize the most relevant payment methods based on the customer's location and
    other characteristics.
    """

    permissions: typing_extensions.NotRequired[CheckoutSessionCreateBodyPermissions]
    """
    This property is used to set up permissions for various actions (e.g., update) on the CheckoutSession object.
    
    For specific permissions, please refer to their dedicated subsections, such as `permissions.update.shipping_details`.
    """

    phone_number_collection: typing_extensions.NotRequired[
        CheckoutSessionCreateBodyPhoneNumberCollection
    ]
    """
    Controls phone number collection settings for the session.
    
    We recommend that you review your privacy policy and check with your legal contacts
    before using this feature. Learn more about [collecting phone numbers with Checkout](https://stripe.com/docs/payments/checkout/phone-numbers).
    """

    redirect_on_completion: typing_extensions.NotRequired[
        typing_extensions.Literal["always", "if_required", "never"]
    ]
    """
    This parameter applies to `ui_mode: embedded`. Learn more about the [redirect behavior](https://stripe.com/docs/payments/checkout/custom-success-page?payment-ui=embedded-form) of embedded sessions. Defaults to `always`.
    """

    return_url: typing_extensions.NotRequired[str]
    """
    The URL to redirect your customer back to after they authenticate or cancel their payment on the
    payment method's app or site. This parameter is required if `ui_mode` is `embedded` or `custom`
    and redirect-based payment methods are enabled on the session.
    """

    saved_payment_method_options: typing_extensions.NotRequired[
        CheckoutSessionCreateBodySavedPaymentMethodOptions
    ]
    """
    Controls saved payment method settings for the session. Only available in `payment` and `subscription` mode.
    """

    setup_intent_data: typing_extensions.NotRequired[
        CheckoutSessionCreateBodySetupIntentData
    ]
    """
    A subset of parameters to be passed to SetupIntent creation for Checkout Sessions in `setup` mode.
    """

    shipping_address_collection: typing_extensions.NotRequired[
        CheckoutSessionCreateBodyShippingAddressCollection
    ]
    """
    When set, provides configuration for Checkout to collect a shipping address from a customer.
    """

    shipping_options: typing_extensions.NotRequired[
        typing.List[CheckoutSessionCreateBodyShippingOptionsItem]
    ]
    """
    The shipping rate options to apply to this Session. Up to a maximum of 5.
    """

    submit_type: typing_extensions.NotRequired[
        typing_extensions.Literal["auto", "book", "donate", "pay", "subscribe"]
    ]
    """
    Describes the type of transaction being performed by Checkout in order
    to customize relevant text on the page, such as the submit button.
     `submit_type` can only be specified on Checkout Sessions in
    `payment` or `subscription` mode. If blank or `auto`, `pay` is used.
    """

    subscription_data: typing_extensions.NotRequired[
        CheckoutSessionCreateBodySubscriptionData
    ]
    """
    A subset of parameters to be passed to subscription creation for Checkout Sessions in `subscription` mode.
    """

    success_url: typing_extensions.NotRequired[str]
    """
    The URL to which Stripe should send customers when payment or setup
    is complete.
    This parameter is not allowed if ui_mode is `embedded` or `custom`. If you'd like to use
    information from the successful Checkout Session on your page, read the
    guide on [customizing your success page](https://stripe.com/docs/payments/checkout/custom-success-page).
    """

    tax_id_collection: typing_extensions.NotRequired[
        CheckoutSessionCreateBodyTaxIdCollection
    ]
    """
    Controls tax ID collection during checkout.
    """

    ui_mode: typing_extensions.NotRequired[
        typing_extensions.Literal["custom", "embedded", "hosted"]
    ]
    """
    The UI mode of the Session. Defaults to `hosted`.
    """


class _SerializerCheckoutSessionCreateBody(pydantic.BaseModel):
    """
    Serializer for CheckoutSessionCreateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    adaptive_pricing: typing.Optional[
        _SerializerCheckoutSessionCreateBodyAdaptivePricing
    ] = pydantic.Field(alias="adaptive_pricing", default=None)
    after_expiration: typing.Optional[
        _SerializerCheckoutSessionCreateBodyAfterExpiration
    ] = pydantic.Field(alias="after_expiration", default=None)
    allow_promotion_codes: typing.Optional[bool] = pydantic.Field(
        alias="allow_promotion_codes", default=None
    )
    automatic_tax: typing.Optional[_SerializerCheckoutSessionCreateBodyAutomaticTax] = (
        pydantic.Field(alias="automatic_tax", default=None)
    )
    billing_address_collection: typing.Optional[
        typing_extensions.Literal["auto", "required"]
    ] = pydantic.Field(alias="billing_address_collection", default=None)
    cancel_url: typing.Optional[str] = pydantic.Field(alias="cancel_url", default=None)
    client_reference_id: typing.Optional[str] = pydantic.Field(
        alias="client_reference_id", default=None
    )
    consent_collection: typing.Optional[
        _SerializerCheckoutSessionCreateBodyConsentCollection
    ] = pydantic.Field(alias="consent_collection", default=None)
    currency: typing.Optional[str] = pydantic.Field(alias="currency", default=None)
    custom_fields: typing.Optional[
        typing.List[_SerializerCheckoutSessionCreateBodyCustomFieldsItem]
    ] = pydantic.Field(alias="custom_fields", default=None)
    custom_text: typing.Optional[_SerializerCheckoutSessionCreateBodyCustomText] = (
        pydantic.Field(alias="custom_text", default=None)
    )
    customer: typing.Optional[str] = pydantic.Field(alias="customer", default=None)
    customer_creation: typing.Optional[
        typing_extensions.Literal["always", "if_required"]
    ] = pydantic.Field(alias="customer_creation", default=None)
    customer_email: typing.Optional[str] = pydantic.Field(
        alias="customer_email", default=None
    )
    customer_update: typing.Optional[
        _SerializerCheckoutSessionCreateBodyCustomerUpdate
    ] = pydantic.Field(alias="customer_update", default=None)
    discounts: typing.Optional[
        typing.List[_SerializerCheckoutSessionCreateBodyDiscountsItem]
    ] = pydantic.Field(alias="discounts", default=None)
    expand: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="expand", default=None
    )
    expires_at: typing.Optional[int] = pydantic.Field(alias="expires_at", default=None)
    invoice_creation: typing.Optional[
        _SerializerCheckoutSessionCreateBodyInvoiceCreation
    ] = pydantic.Field(alias="invoice_creation", default=None)
    line_items: typing.Optional[
        typing.List[_SerializerCheckoutSessionCreateBodyLineItemsItem]
    ] = pydantic.Field(alias="line_items", default=None)
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
    metadata: typing.Optional[_SerializerCheckoutSessionCreateBodyMetadata] = (
        pydantic.Field(alias="metadata", default=None)
    )
    mode: typing.Optional[
        typing_extensions.Literal["payment", "setup", "subscription"]
    ] = pydantic.Field(alias="mode", default=None)
    optional_items: typing.Optional[
        typing.List[_SerializerCheckoutSessionCreateBodyOptionalItemsItem]
    ] = pydantic.Field(alias="optional_items", default=None)
    payment_intent_data: typing.Optional[
        _SerializerCheckoutSessionCreateBodyPaymentIntentData
    ] = pydantic.Field(alias="payment_intent_data", default=None)
    payment_method_collection: typing.Optional[
        typing_extensions.Literal["always", "if_required"]
    ] = pydantic.Field(alias="payment_method_collection", default=None)
    payment_method_configuration: typing.Optional[str] = pydantic.Field(
        alias="payment_method_configuration", default=None
    )
    payment_method_data: typing.Optional[
        _SerializerCheckoutSessionCreateBodyPaymentMethodData
    ] = pydantic.Field(alias="payment_method_data", default=None)
    payment_method_options: typing.Optional[
        _SerializerCheckoutSessionCreateBodyPaymentMethodOptions
    ] = pydantic.Field(alias="payment_method_options", default=None)
    payment_method_types: typing.Optional[
        typing.List[
            typing_extensions.Literal[
                "acss_debit",
                "affirm",
                "afterpay_clearpay",
                "alipay",
                "alma",
                "amazon_pay",
                "au_becs_debit",
                "bacs_debit",
                "bancontact",
                "billie",
                "blik",
                "boleto",
                "card",
                "cashapp",
                "customer_balance",
                "eps",
                "fpx",
                "giropay",
                "grabpay",
                "ideal",
                "kakao_pay",
                "klarna",
                "konbini",
                "kr_card",
                "link",
                "mobilepay",
                "multibanco",
                "naver_pay",
                "oxxo",
                "p24",
                "pay_by_bank",
                "payco",
                "paynow",
                "paypal",
                "pix",
                "promptpay",
                "revolut_pay",
                "samsung_pay",
                "satispay",
                "sepa_debit",
                "sofort",
                "swish",
                "twint",
                "us_bank_account",
                "wechat_pay",
                "zip",
            ]
        ]
    ] = pydantic.Field(alias="payment_method_types", default=None)
    permissions: typing.Optional[_SerializerCheckoutSessionCreateBodyPermissions] = (
        pydantic.Field(alias="permissions", default=None)
    )
    phone_number_collection: typing.Optional[
        _SerializerCheckoutSessionCreateBodyPhoneNumberCollection
    ] = pydantic.Field(alias="phone_number_collection", default=None)
    redirect_on_completion: typing.Optional[
        typing_extensions.Literal["always", "if_required", "never"]
    ] = pydantic.Field(alias="redirect_on_completion", default=None)
    return_url: typing.Optional[str] = pydantic.Field(alias="return_url", default=None)
    saved_payment_method_options: typing.Optional[
        _SerializerCheckoutSessionCreateBodySavedPaymentMethodOptions
    ] = pydantic.Field(alias="saved_payment_method_options", default=None)
    setup_intent_data: typing.Optional[
        _SerializerCheckoutSessionCreateBodySetupIntentData
    ] = pydantic.Field(alias="setup_intent_data", default=None)
    shipping_address_collection: typing.Optional[
        _SerializerCheckoutSessionCreateBodyShippingAddressCollection
    ] = pydantic.Field(alias="shipping_address_collection", default=None)
    shipping_options: typing.Optional[
        typing.List[_SerializerCheckoutSessionCreateBodyShippingOptionsItem]
    ] = pydantic.Field(alias="shipping_options", default=None)
    submit_type: typing.Optional[
        typing_extensions.Literal["auto", "book", "donate", "pay", "subscribe"]
    ] = pydantic.Field(alias="submit_type", default=None)
    subscription_data: typing.Optional[
        _SerializerCheckoutSessionCreateBodySubscriptionData
    ] = pydantic.Field(alias="subscription_data", default=None)
    success_url: typing.Optional[str] = pydantic.Field(
        alias="success_url", default=None
    )
    tax_id_collection: typing.Optional[
        _SerializerCheckoutSessionCreateBodyTaxIdCollection
    ] = pydantic.Field(alias="tax_id_collection", default=None)
    ui_mode: typing.Optional[
        typing_extensions.Literal["custom", "embedded", "hosted"]
    ] = pydantic.Field(alias="ui_mode", default=None)
