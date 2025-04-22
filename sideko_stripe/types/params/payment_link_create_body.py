import pydantic
import typing
import typing_extensions

from .payment_link_create_body_after_completion import (
    PaymentLinkCreateBodyAfterCompletion,
    _SerializerPaymentLinkCreateBodyAfterCompletion,
)
from .payment_link_create_body_automatic_tax import (
    PaymentLinkCreateBodyAutomaticTax,
    _SerializerPaymentLinkCreateBodyAutomaticTax,
)
from .payment_link_create_body_consent_collection import (
    PaymentLinkCreateBodyConsentCollection,
    _SerializerPaymentLinkCreateBodyConsentCollection,
)
from .payment_link_create_body_custom_fields_item import (
    PaymentLinkCreateBodyCustomFieldsItem,
    _SerializerPaymentLinkCreateBodyCustomFieldsItem,
)
from .payment_link_create_body_custom_text import (
    PaymentLinkCreateBodyCustomText,
    _SerializerPaymentLinkCreateBodyCustomText,
)
from .payment_link_create_body_invoice_creation import (
    PaymentLinkCreateBodyInvoiceCreation,
    _SerializerPaymentLinkCreateBodyInvoiceCreation,
)
from .payment_link_create_body_line_items_item import (
    PaymentLinkCreateBodyLineItemsItem,
    _SerializerPaymentLinkCreateBodyLineItemsItem,
)
from .payment_link_create_body_metadata import (
    PaymentLinkCreateBodyMetadata,
    _SerializerPaymentLinkCreateBodyMetadata,
)
from .payment_link_create_body_optional_items_item import (
    PaymentLinkCreateBodyOptionalItemsItem,
    _SerializerPaymentLinkCreateBodyOptionalItemsItem,
)
from .payment_link_create_body_payment_intent_data import (
    PaymentLinkCreateBodyPaymentIntentData,
    _SerializerPaymentLinkCreateBodyPaymentIntentData,
)
from .payment_link_create_body_phone_number_collection import (
    PaymentLinkCreateBodyPhoneNumberCollection,
    _SerializerPaymentLinkCreateBodyPhoneNumberCollection,
)
from .payment_link_create_body_restrictions import (
    PaymentLinkCreateBodyRestrictions,
    _SerializerPaymentLinkCreateBodyRestrictions,
)
from .payment_link_create_body_shipping_address_collection import (
    PaymentLinkCreateBodyShippingAddressCollection,
    _SerializerPaymentLinkCreateBodyShippingAddressCollection,
)
from .payment_link_create_body_shipping_options_item import (
    PaymentLinkCreateBodyShippingOptionsItem,
    _SerializerPaymentLinkCreateBodyShippingOptionsItem,
)
from .payment_link_create_body_subscription_data import (
    PaymentLinkCreateBodySubscriptionData,
    _SerializerPaymentLinkCreateBodySubscriptionData,
)
from .payment_link_create_body_tax_id_collection import (
    PaymentLinkCreateBodyTaxIdCollection,
    _SerializerPaymentLinkCreateBodyTaxIdCollection,
)
from .payment_link_create_body_transfer_data import (
    PaymentLinkCreateBodyTransferData,
    _SerializerPaymentLinkCreateBodyTransferData,
)


class PaymentLinkCreateBody(typing_extensions.TypedDict, total=False):
    """
    PaymentLinkCreateBody
    """

    after_completion: typing_extensions.NotRequired[
        PaymentLinkCreateBodyAfterCompletion
    ]
    """
    Behavior after the purchase is complete.
    """

    allow_promotion_codes: typing_extensions.NotRequired[bool]
    """
    Enables user redeemable promotion codes.
    """

    application_fee_amount: typing_extensions.NotRequired[int]
    """
    The amount of the application fee (if any) that will be requested to be applied to the payment and transferred to the application owner's Stripe account. Can only be applied when there are no line items with recurring prices.
    """

    application_fee_percent: typing_extensions.NotRequired[float]
    """
    A non-negative decimal between 0 and 100, with at most two decimal places. This represents the percentage of the subscription invoice total that will be transferred to the application owner's Stripe account. There must be at least 1 line item with a recurring price to use this field.
    """

    automatic_tax: typing_extensions.NotRequired[PaymentLinkCreateBodyAutomaticTax]
    """
    Configuration for automatic tax collection.
    """

    billing_address_collection: typing_extensions.NotRequired[
        typing_extensions.Literal["auto", "required"]
    ]
    """
    Configuration for collecting the customer's billing address. Defaults to `auto`.
    """

    consent_collection: typing_extensions.NotRequired[
        PaymentLinkCreateBodyConsentCollection
    ]
    """
    Configure fields to gather active consent from customers.
    """

    currency: typing_extensions.NotRequired[str]
    """
    Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies) and supported by each line item's price.
    """

    custom_fields: typing_extensions.NotRequired[
        typing.List[PaymentLinkCreateBodyCustomFieldsItem]
    ]
    """
    Collect additional information from your customer using custom fields. Up to 3 fields are supported.
    """

    custom_text: typing_extensions.NotRequired[PaymentLinkCreateBodyCustomText]
    """
    Display additional text for your customers using custom text.
    """

    customer_creation: typing_extensions.NotRequired[
        typing_extensions.Literal["always", "if_required"]
    ]
    """
    Configures whether [checkout sessions](https://stripe.com/docs/api/checkout/sessions) created by this payment link create a [Customer](https://stripe.com/docs/api/customers).
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """

    inactive_message: typing_extensions.NotRequired[str]
    """
    The custom message to be displayed to a customer when a payment link is no longer active.
    """

    invoice_creation: typing_extensions.NotRequired[
        PaymentLinkCreateBodyInvoiceCreation
    ]
    """
    Generate a post-purchase Invoice for one-time payments.
    """

    line_items: typing_extensions.Required[
        typing.List[PaymentLinkCreateBodyLineItemsItem]
    ]
    """
    The line items representing what is being sold. Each line item represents an item being sold. Up to 20 line items are supported.
    """

    metadata: typing_extensions.NotRequired[PaymentLinkCreateBodyMetadata]
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`. Metadata associated with this Payment Link will automatically be copied to [checkout sessions](https://stripe.com/docs/api/checkout/sessions) created by this payment link.
    """

    on_behalf_of: typing_extensions.NotRequired[str]
    """
    The account on behalf of which to charge.
    """

    optional_items: typing_extensions.NotRequired[
        typing.List[PaymentLinkCreateBodyOptionalItemsItem]
    ]
    """
    A list of optional items the customer can add to their order at checkout. Use this parameter to pass one-time or recurring [Prices](https://stripe.com/docs/api/prices).
    There is a maximum of 10 optional items allowed on a payment link, and the existing limits on the number of line items allowed on a payment link apply to the combined number of line items and optional items.
    There is a maximum of 20 combined line items and optional items.
    """

    payment_intent_data: typing_extensions.NotRequired[
        PaymentLinkCreateBodyPaymentIntentData
    ]
    """
    A subset of parameters to be passed to PaymentIntent creation for Checkout Sessions in `payment` mode.
    """

    payment_method_collection: typing_extensions.NotRequired[
        typing_extensions.Literal["always", "if_required"]
    ]
    """
    Specify whether Checkout should collect a payment method. When set to `if_required`, Checkout will not collect a payment method when the total due for the session is 0.This may occur if the Checkout Session includes a free trial or a discount.
    
    Can only be set in `subscription` mode. Defaults to `always`.
    
    If you'd like information on how to collect a payment method outside of Checkout, read the guide on [configuring subscriptions with a free trial](https://stripe.com/docs/payments/checkout/free-trials).
    """

    payment_method_types: typing_extensions.NotRequired[
        typing.List[
            typing_extensions.Literal[
                "affirm",
                "afterpay_clearpay",
                "alipay",
                "alma",
                "au_becs_debit",
                "bacs_debit",
                "bancontact",
                "billie",
                "blik",
                "boleto",
                "card",
                "cashapp",
                "eps",
                "fpx",
                "giropay",
                "grabpay",
                "ideal",
                "klarna",
                "konbini",
                "link",
                "mobilepay",
                "multibanco",
                "oxxo",
                "p24",
                "pay_by_bank",
                "paynow",
                "paypal",
                "pix",
                "promptpay",
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
    The list of payment method types that customers can use. If no value is passed, Stripe will dynamically show relevant payment methods from your [payment method settings](https://dashboard.stripe.com/settings/payment_methods) (20+ payment methods [supported](https://stripe.com/docs/payments/payment-methods/integration-options#payment-method-product-support)).
    """

    phone_number_collection: typing_extensions.NotRequired[
        PaymentLinkCreateBodyPhoneNumberCollection
    ]
    """
    Controls phone number collection settings during checkout.
    
    We recommend that you review your privacy policy and check with your legal contacts.
    """

    restrictions: typing_extensions.NotRequired[PaymentLinkCreateBodyRestrictions]
    """
    Settings that restrict the usage of a payment link.
    """

    shipping_address_collection: typing_extensions.NotRequired[
        PaymentLinkCreateBodyShippingAddressCollection
    ]
    """
    Configuration for collecting the customer's shipping address.
    """

    shipping_options: typing_extensions.NotRequired[
        typing.List[PaymentLinkCreateBodyShippingOptionsItem]
    ]
    """
    The shipping rate options to apply to [checkout sessions](https://stripe.com/docs/api/checkout/sessions) created by this payment link.
    """

    submit_type: typing_extensions.NotRequired[
        typing_extensions.Literal["auto", "book", "donate", "pay", "subscribe"]
    ]
    """
    Describes the type of transaction being performed in order to customize relevant text on the page, such as the submit button. Changing this value will also affect the hostname in the [url](https://stripe.com/docs/api/payment_links/payment_links/object#url) property (example: `donate.stripe.com`).
    """

    subscription_data: typing_extensions.NotRequired[
        PaymentLinkCreateBodySubscriptionData
    ]
    """
    When creating a subscription, the specified configuration data will be used. There must be at least one line item with a recurring price to use `subscription_data`.
    """

    tax_id_collection: typing_extensions.NotRequired[
        PaymentLinkCreateBodyTaxIdCollection
    ]
    """
    Controls tax ID collection during checkout.
    """

    transfer_data: typing_extensions.NotRequired[PaymentLinkCreateBodyTransferData]
    """
    The account (if any) the payments will be attributed to for tax reporting, and where funds from each payment will be transferred to.
    """


class _SerializerPaymentLinkCreateBody(pydantic.BaseModel):
    """
    Serializer for PaymentLinkCreateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    after_completion: typing.Optional[
        _SerializerPaymentLinkCreateBodyAfterCompletion
    ] = pydantic.Field(alias="after_completion", default=None)
    allow_promotion_codes: typing.Optional[bool] = pydantic.Field(
        alias="allow_promotion_codes", default=None
    )
    application_fee_amount: typing.Optional[int] = pydantic.Field(
        alias="application_fee_amount", default=None
    )
    application_fee_percent: typing.Optional[float] = pydantic.Field(
        alias="application_fee_percent", default=None
    )
    automatic_tax: typing.Optional[_SerializerPaymentLinkCreateBodyAutomaticTax] = (
        pydantic.Field(alias="automatic_tax", default=None)
    )
    billing_address_collection: typing.Optional[
        typing_extensions.Literal["auto", "required"]
    ] = pydantic.Field(alias="billing_address_collection", default=None)
    consent_collection: typing.Optional[
        _SerializerPaymentLinkCreateBodyConsentCollection
    ] = pydantic.Field(alias="consent_collection", default=None)
    currency: typing.Optional[str] = pydantic.Field(alias="currency", default=None)
    custom_fields: typing.Optional[
        typing.List[_SerializerPaymentLinkCreateBodyCustomFieldsItem]
    ] = pydantic.Field(alias="custom_fields", default=None)
    custom_text: typing.Optional[_SerializerPaymentLinkCreateBodyCustomText] = (
        pydantic.Field(alias="custom_text", default=None)
    )
    customer_creation: typing.Optional[
        typing_extensions.Literal["always", "if_required"]
    ] = pydantic.Field(alias="customer_creation", default=None)
    expand: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="expand", default=None
    )
    inactive_message: typing.Optional[str] = pydantic.Field(
        alias="inactive_message", default=None
    )
    invoice_creation: typing.Optional[
        _SerializerPaymentLinkCreateBodyInvoiceCreation
    ] = pydantic.Field(alias="invoice_creation", default=None)
    line_items: typing.List[_SerializerPaymentLinkCreateBodyLineItemsItem] = (
        pydantic.Field(
            alias="line_items",
        )
    )
    metadata: typing.Optional[_SerializerPaymentLinkCreateBodyMetadata] = (
        pydantic.Field(alias="metadata", default=None)
    )
    on_behalf_of: typing.Optional[str] = pydantic.Field(
        alias="on_behalf_of", default=None
    )
    optional_items: typing.Optional[
        typing.List[_SerializerPaymentLinkCreateBodyOptionalItemsItem]
    ] = pydantic.Field(alias="optional_items", default=None)
    payment_intent_data: typing.Optional[
        _SerializerPaymentLinkCreateBodyPaymentIntentData
    ] = pydantic.Field(alias="payment_intent_data", default=None)
    payment_method_collection: typing.Optional[
        typing_extensions.Literal["always", "if_required"]
    ] = pydantic.Field(alias="payment_method_collection", default=None)
    payment_method_types: typing.Optional[
        typing.List[
            typing_extensions.Literal[
                "affirm",
                "afterpay_clearpay",
                "alipay",
                "alma",
                "au_becs_debit",
                "bacs_debit",
                "bancontact",
                "billie",
                "blik",
                "boleto",
                "card",
                "cashapp",
                "eps",
                "fpx",
                "giropay",
                "grabpay",
                "ideal",
                "klarna",
                "konbini",
                "link",
                "mobilepay",
                "multibanco",
                "oxxo",
                "p24",
                "pay_by_bank",
                "paynow",
                "paypal",
                "pix",
                "promptpay",
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
    phone_number_collection: typing.Optional[
        _SerializerPaymentLinkCreateBodyPhoneNumberCollection
    ] = pydantic.Field(alias="phone_number_collection", default=None)
    restrictions: typing.Optional[_SerializerPaymentLinkCreateBodyRestrictions] = (
        pydantic.Field(alias="restrictions", default=None)
    )
    shipping_address_collection: typing.Optional[
        _SerializerPaymentLinkCreateBodyShippingAddressCollection
    ] = pydantic.Field(alias="shipping_address_collection", default=None)
    shipping_options: typing.Optional[
        typing.List[_SerializerPaymentLinkCreateBodyShippingOptionsItem]
    ] = pydantic.Field(alias="shipping_options", default=None)
    submit_type: typing.Optional[
        typing_extensions.Literal["auto", "book", "donate", "pay", "subscribe"]
    ] = pydantic.Field(alias="submit_type", default=None)
    subscription_data: typing.Optional[
        _SerializerPaymentLinkCreateBodySubscriptionData
    ] = pydantic.Field(alias="subscription_data", default=None)
    tax_id_collection: typing.Optional[
        _SerializerPaymentLinkCreateBodyTaxIdCollection
    ] = pydantic.Field(alias="tax_id_collection", default=None)
    transfer_data: typing.Optional[_SerializerPaymentLinkCreateBodyTransferData] = (
        pydantic.Field(alias="transfer_data", default=None)
    )
