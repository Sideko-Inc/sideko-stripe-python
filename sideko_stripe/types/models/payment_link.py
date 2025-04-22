import pydantic
import typing
import typing_extensions

from .application import Application
from .deleted_application import DeletedApplication
from .payment_link_metadata import PaymentLinkMetadata
from .payment_links_resource_after_completion import PaymentLinksResourceAfterCompletion
from .payment_links_resource_consent_collection import (
    PaymentLinksResourceConsentCollection,
)
from .payment_links_resource_custom_fields import PaymentLinksResourceCustomFields
from .payment_links_resource_custom_text import PaymentLinksResourceCustomText
from .payment_links_resource_optional_item import PaymentLinksResourceOptionalItem
from .payment_links_resource_payment_intent_data import (
    PaymentLinksResourcePaymentIntentData,
)
from .payment_links_resource_phone_number_collection import (
    PaymentLinksResourcePhoneNumberCollection,
)
from .payment_links_resource_restrictions import PaymentLinksResourceRestrictions
from .payment_links_resource_shipping_address_collection import (
    PaymentLinksResourceShippingAddressCollection,
)
from .payment_links_resource_shipping_option import PaymentLinksResourceShippingOption
from .payment_links_resource_tax_id_collection import (
    PaymentLinksResourceTaxIdCollection,
)

if typing_extensions.TYPE_CHECKING:
    from .account import Account
    from .payment_link_line_items import PaymentLinkLineItems
    from .payment_links_resource_automatic_tax import PaymentLinksResourceAutomaticTax
    from .payment_links_resource_invoice_creation import (
        PaymentLinksResourceInvoiceCreation,
    )
    from .payment_links_resource_subscription_data import (
        PaymentLinksResourceSubscriptionData,
    )
    from .payment_links_resource_transfer_data import PaymentLinksResourceTransferData


class PaymentLink(pydantic.BaseModel):
    """
    A payment link is a shareable URL that will take your customers to a hosted payment page. A payment link can be shared and used multiple times.

    When a customer opens a payment link it will open a new [checkout session](https://stripe.com/docs/api/checkout/sessions) to render the payment page. You can use [checkout session events](https://stripe.com/docs/api/events/types#event_types-checkout.session.completed) to track payments through payment links.

    Related guide: [Payment Links API](https://stripe.com/docs/payment-links)
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    active: bool = pydantic.Field(
        alias="active",
    )
    """
    Whether the payment link's `url` is active. If `false`, customers visiting the URL will be shown a page saying that the link has been deactivated.
    """
    after_completion: PaymentLinksResourceAfterCompletion = pydantic.Field(
        alias="after_completion",
    )
    allow_promotion_codes: bool = pydantic.Field(
        alias="allow_promotion_codes",
    )
    """
    Whether user redeemable promotion codes are enabled.
    """
    application: typing.Optional[typing.Union[str, Application, DeletedApplication]] = (
        pydantic.Field(alias="application", default=None)
    )
    """
    The ID of the Connect application that created the Payment Link.
    """
    application_fee_amount: typing.Optional[int] = pydantic.Field(
        alias="application_fee_amount", default=None
    )
    """
    The amount of the application fee (if any) that will be requested to be applied to the payment and transferred to the application owner's Stripe account.
    """
    application_fee_percent: typing.Optional[float] = pydantic.Field(
        alias="application_fee_percent", default=None
    )
    """
    This represents the percentage of the subscription invoice total that will be transferred to the application owner's Stripe account.
    """
    automatic_tax: "PaymentLinksResourceAutomaticTax" = pydantic.Field(
        alias="automatic_tax",
    )
    billing_address_collection: typing_extensions.Literal["auto", "required"] = (
        pydantic.Field(
            alias="billing_address_collection",
        )
    )
    """
    Configuration for collecting the customer's billing address. Defaults to `auto`.
    """
    consent_collection: typing.Optional[PaymentLinksResourceConsentCollection] = (
        pydantic.Field(alias="consent_collection", default=None)
    )
    currency: str = pydantic.Field(
        alias="currency",
    )
    """
    Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    """
    custom_fields: typing.List[PaymentLinksResourceCustomFields] = pydantic.Field(
        alias="custom_fields",
    )
    """
    Collect additional information from your customer using custom fields. Up to 3 fields are supported.
    """
    custom_text: PaymentLinksResourceCustomText = pydantic.Field(
        alias="custom_text",
    )
    customer_creation: typing_extensions.Literal["always", "if_required"] = (
        pydantic.Field(
            alias="customer_creation",
        )
    )
    """
    Configuration for Customer creation during checkout.
    """
    id: str = pydantic.Field(
        alias="id",
    )
    """
    Unique identifier for the object.
    """
    inactive_message: typing.Optional[str] = pydantic.Field(
        alias="inactive_message", default=None
    )
    """
    The custom message to be displayed to a customer when a payment link is no longer active.
    """
    invoice_creation: typing.Optional["PaymentLinksResourceInvoiceCreation"] = (
        pydantic.Field(alias="invoice_creation", default=None)
    )
    line_items: typing.Optional["PaymentLinkLineItems"] = pydantic.Field(
        alias="line_items", default=None
    )
    """
    The line items representing what is being sold.
    """
    livemode: bool = pydantic.Field(
        alias="livemode",
    )
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    metadata: PaymentLinkMetadata = pydantic.Field(
        alias="metadata",
    )
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    object: typing_extensions.Literal["payment_link"] = pydantic.Field(
        alias="object",
    )
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    on_behalf_of: typing.Optional[typing.Union[str, "Account"]] = pydantic.Field(
        alias="on_behalf_of", default=None
    )
    """
    The account on behalf of which to charge. See the [Connect documentation](https://support.stripe.com/questions/sending-invoices-on-behalf-of-connected-accounts) for details.
    """
    optional_items: typing.Optional[typing.List[PaymentLinksResourceOptionalItem]] = (
        pydantic.Field(alias="optional_items", default=None)
    )
    """
    The optional items presented to the customer at checkout.
    """
    payment_intent_data: typing.Optional[PaymentLinksResourcePaymentIntentData] = (
        pydantic.Field(alias="payment_intent_data", default=None)
    )
    payment_method_collection: typing_extensions.Literal["always", "if_required"] = (
        pydantic.Field(
            alias="payment_method_collection",
        )
    )
    """
    Configuration for collecting a payment method during checkout. Defaults to `always`.
    """
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
    """
    The list of payment method types that customers can use. When `null`, Stripe will dynamically show relevant payment methods you've enabled in your [payment method settings](https://dashboard.stripe.com/settings/payment_methods).
    """
    phone_number_collection: PaymentLinksResourcePhoneNumberCollection = pydantic.Field(
        alias="phone_number_collection",
    )
    restrictions: typing.Optional[PaymentLinksResourceRestrictions] = pydantic.Field(
        alias="restrictions", default=None
    )
    shipping_address_collection: typing.Optional[
        PaymentLinksResourceShippingAddressCollection
    ] = pydantic.Field(alias="shipping_address_collection", default=None)
    shipping_options: typing.List[PaymentLinksResourceShippingOption] = pydantic.Field(
        alias="shipping_options",
    )
    """
    The shipping rate options applied to the session.
    """
    submit_type: typing_extensions.Literal[
        "auto", "book", "donate", "pay", "subscribe"
    ] = pydantic.Field(
        alias="submit_type",
    )
    """
    Indicates the type of transaction being performed which customizes relevant text on the page, such as the submit button.
    """
    subscription_data: typing.Optional["PaymentLinksResourceSubscriptionData"] = (
        pydantic.Field(alias="subscription_data", default=None)
    )
    tax_id_collection: PaymentLinksResourceTaxIdCollection = pydantic.Field(
        alias="tax_id_collection",
    )
    transfer_data: typing.Optional["PaymentLinksResourceTransferData"] = pydantic.Field(
        alias="transfer_data", default=None
    )
    url: str = pydantic.Field(
        alias="url",
    )
    """
    The public URL that can be shared with customers.
    """
