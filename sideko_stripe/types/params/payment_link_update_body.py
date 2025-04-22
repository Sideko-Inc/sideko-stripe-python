import pydantic
import typing
import typing_extensions

from .payment_link_update_body_after_completion import (
    PaymentLinkUpdateBodyAfterCompletion,
    _SerializerPaymentLinkUpdateBodyAfterCompletion,
)
from .payment_link_update_body_automatic_tax import (
    PaymentLinkUpdateBodyAutomaticTax,
    _SerializerPaymentLinkUpdateBodyAutomaticTax,
)
from .payment_link_update_body_custom_fields_arr0_item import (
    PaymentLinkUpdateBodyCustomFieldsArr0Item,
    _SerializerPaymentLinkUpdateBodyCustomFieldsArr0Item,
)
from .payment_link_update_body_custom_text import (
    PaymentLinkUpdateBodyCustomText,
    _SerializerPaymentLinkUpdateBodyCustomText,
)
from .payment_link_update_body_invoice_creation import (
    PaymentLinkUpdateBodyInvoiceCreation,
    _SerializerPaymentLinkUpdateBodyInvoiceCreation,
)
from .payment_link_update_body_line_items_item import (
    PaymentLinkUpdateBodyLineItemsItem,
    _SerializerPaymentLinkUpdateBodyLineItemsItem,
)
from .payment_link_update_body_metadata import (
    PaymentLinkUpdateBodyMetadata,
    _SerializerPaymentLinkUpdateBodyMetadata,
)
from .payment_link_update_body_payment_intent_data import (
    PaymentLinkUpdateBodyPaymentIntentData,
    _SerializerPaymentLinkUpdateBodyPaymentIntentData,
)
from .payment_link_update_body_phone_number_collection import (
    PaymentLinkUpdateBodyPhoneNumberCollection,
    _SerializerPaymentLinkUpdateBodyPhoneNumberCollection,
)
from .payment_link_update_body_restrictions_obj0 import (
    PaymentLinkUpdateBodyRestrictionsObj0,
    _SerializerPaymentLinkUpdateBodyRestrictionsObj0,
)
from .payment_link_update_body_shipping_address_collection_obj0 import (
    PaymentLinkUpdateBodyShippingAddressCollectionObj0,
    _SerializerPaymentLinkUpdateBodyShippingAddressCollectionObj0,
)
from .payment_link_update_body_subscription_data import (
    PaymentLinkUpdateBodySubscriptionData,
    _SerializerPaymentLinkUpdateBodySubscriptionData,
)
from .payment_link_update_body_tax_id_collection import (
    PaymentLinkUpdateBodyTaxIdCollection,
    _SerializerPaymentLinkUpdateBodyTaxIdCollection,
)


class PaymentLinkUpdateBody(typing_extensions.TypedDict, total=False):
    """
    PaymentLinkUpdateBody
    """

    active: typing_extensions.NotRequired[bool]
    """
    Whether the payment link's `url` is active. If `false`, customers visiting the URL will be shown a page saying that the link has been deactivated.
    """

    after_completion: typing_extensions.NotRequired[
        PaymentLinkUpdateBodyAfterCompletion
    ]
    """
    Behavior after the purchase is complete.
    """

    allow_promotion_codes: typing_extensions.NotRequired[bool]
    """
    Enables user redeemable promotion codes.
    """

    automatic_tax: typing_extensions.NotRequired[PaymentLinkUpdateBodyAutomaticTax]
    """
    Configuration for automatic tax collection.
    """

    billing_address_collection: typing_extensions.NotRequired[
        typing_extensions.Literal["auto", "required"]
    ]
    """
    Configuration for collecting the customer's billing address. Defaults to `auto`.
    """

    custom_fields: typing_extensions.NotRequired[
        typing.Union[typing.List[PaymentLinkUpdateBodyCustomFieldsArr0Item], str]
    ]
    """
    Collect additional information from your customer using custom fields. Up to 3 fields are supported.
    """

    custom_text: typing_extensions.NotRequired[PaymentLinkUpdateBodyCustomText]
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

    inactive_message: typing_extensions.NotRequired[typing.Union[str, str]]
    """
    The custom message to be displayed to a customer when a payment link is no longer active.
    """

    invoice_creation: typing_extensions.NotRequired[
        PaymentLinkUpdateBodyInvoiceCreation
    ]
    """
    Generate a post-purchase Invoice for one-time payments.
    """

    line_items: typing_extensions.NotRequired[
        typing.List[PaymentLinkUpdateBodyLineItemsItem]
    ]
    """
    The line items representing what is being sold. Each line item represents an item being sold. Up to 20 line items are supported.
    """

    metadata: typing_extensions.NotRequired[PaymentLinkUpdateBodyMetadata]
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`. Metadata associated with this Payment Link will automatically be copied to [checkout sessions](https://stripe.com/docs/api/checkout/sessions) created by this payment link.
    """

    payment_intent_data: typing_extensions.NotRequired[
        PaymentLinkUpdateBodyPaymentIntentData
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
        typing.Union[
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
            ],
            str,
        ]
    ]
    """
    The list of payment method types that customers can use. Pass an empty string to enable dynamic payment methods that use your [payment method settings](https://dashboard.stripe.com/settings/payment_methods).
    """

    phone_number_collection: typing_extensions.NotRequired[
        PaymentLinkUpdateBodyPhoneNumberCollection
    ]
    """
    Controls phone number collection settings during checkout.
    
    We recommend that you review your privacy policy and check with your legal contacts.
    """

    restrictions: typing_extensions.NotRequired[
        typing.Union[PaymentLinkUpdateBodyRestrictionsObj0, str]
    ]
    """
    Settings that restrict the usage of a payment link.
    """

    shipping_address_collection: typing_extensions.NotRequired[
        typing.Union[PaymentLinkUpdateBodyShippingAddressCollectionObj0, str]
    ]
    """
    Configuration for collecting the customer's shipping address.
    """

    submit_type: typing_extensions.NotRequired[
        typing_extensions.Literal["auto", "book", "donate", "pay", "subscribe"]
    ]
    """
    Describes the type of transaction being performed in order to customize relevant text on the page, such as the submit button. Changing this value will also affect the hostname in the [url](https://stripe.com/docs/api/payment_links/payment_links/object#url) property (example: `donate.stripe.com`).
    """

    subscription_data: typing_extensions.NotRequired[
        PaymentLinkUpdateBodySubscriptionData
    ]
    """
    When creating a subscription, the specified configuration data will be used. There must be at least one line item with a recurring price to use `subscription_data`.
    """

    tax_id_collection: typing_extensions.NotRequired[
        PaymentLinkUpdateBodyTaxIdCollection
    ]
    """
    Controls tax ID collection during checkout.
    """


class _SerializerPaymentLinkUpdateBody(pydantic.BaseModel):
    """
    Serializer for PaymentLinkUpdateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    active: typing.Optional[bool] = pydantic.Field(alias="active", default=None)
    after_completion: typing.Optional[
        _SerializerPaymentLinkUpdateBodyAfterCompletion
    ] = pydantic.Field(alias="after_completion", default=None)
    allow_promotion_codes: typing.Optional[bool] = pydantic.Field(
        alias="allow_promotion_codes", default=None
    )
    automatic_tax: typing.Optional[_SerializerPaymentLinkUpdateBodyAutomaticTax] = (
        pydantic.Field(alias="automatic_tax", default=None)
    )
    billing_address_collection: typing.Optional[
        typing_extensions.Literal["auto", "required"]
    ] = pydantic.Field(alias="billing_address_collection", default=None)
    custom_fields: typing.Optional[
        typing.Union[
            typing.List[_SerializerPaymentLinkUpdateBodyCustomFieldsArr0Item], str
        ]
    ] = pydantic.Field(alias="custom_fields", default=None)
    custom_text: typing.Optional[_SerializerPaymentLinkUpdateBodyCustomText] = (
        pydantic.Field(alias="custom_text", default=None)
    )
    customer_creation: typing.Optional[
        typing_extensions.Literal["always", "if_required"]
    ] = pydantic.Field(alias="customer_creation", default=None)
    expand: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="expand", default=None
    )
    inactive_message: typing.Optional[typing.Union[str, str]] = pydantic.Field(
        alias="inactive_message", default=None
    )
    invoice_creation: typing.Optional[
        _SerializerPaymentLinkUpdateBodyInvoiceCreation
    ] = pydantic.Field(alias="invoice_creation", default=None)
    line_items: typing.Optional[
        typing.List[_SerializerPaymentLinkUpdateBodyLineItemsItem]
    ] = pydantic.Field(alias="line_items", default=None)
    metadata: typing.Optional[_SerializerPaymentLinkUpdateBodyMetadata] = (
        pydantic.Field(alias="metadata", default=None)
    )
    payment_intent_data: typing.Optional[
        _SerializerPaymentLinkUpdateBodyPaymentIntentData
    ] = pydantic.Field(alias="payment_intent_data", default=None)
    payment_method_collection: typing.Optional[
        typing_extensions.Literal["always", "if_required"]
    ] = pydantic.Field(alias="payment_method_collection", default=None)
    payment_method_types: typing.Optional[
        typing.Union[
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
            ],
            str,
        ]
    ] = pydantic.Field(alias="payment_method_types", default=None)
    phone_number_collection: typing.Optional[
        _SerializerPaymentLinkUpdateBodyPhoneNumberCollection
    ] = pydantic.Field(alias="phone_number_collection", default=None)
    restrictions: typing.Optional[
        typing.Union[_SerializerPaymentLinkUpdateBodyRestrictionsObj0, str]
    ] = pydantic.Field(alias="restrictions", default=None)
    shipping_address_collection: typing.Optional[
        typing.Union[_SerializerPaymentLinkUpdateBodyShippingAddressCollectionObj0, str]
    ] = pydantic.Field(alias="shipping_address_collection", default=None)
    submit_type: typing.Optional[
        typing_extensions.Literal["auto", "book", "donate", "pay", "subscribe"]
    ] = pydantic.Field(alias="submit_type", default=None)
    subscription_data: typing.Optional[
        _SerializerPaymentLinkUpdateBodySubscriptionData
    ] = pydantic.Field(alias="subscription_data", default=None)
    tax_id_collection: typing.Optional[
        _SerializerPaymentLinkUpdateBodyTaxIdCollection
    ] = pydantic.Field(alias="tax_id_collection", default=None)
