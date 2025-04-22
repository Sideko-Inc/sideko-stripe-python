import pydantic
import typing
import typing_extensions

from .invoice_create_body_automatic_tax import (
    InvoiceCreateBodyAutomaticTax,
    _SerializerInvoiceCreateBodyAutomaticTax,
)
from .invoice_create_body_custom_fields_arr0_item import (
    InvoiceCreateBodyCustomFieldsArr0Item,
    _SerializerInvoiceCreateBodyCustomFieldsArr0Item,
)
from .invoice_create_body_discounts_arr0_item import (
    InvoiceCreateBodyDiscountsArr0Item,
    _SerializerInvoiceCreateBodyDiscountsArr0Item,
)
from .invoice_create_body_from_invoice import (
    InvoiceCreateBodyFromInvoice,
    _SerializerInvoiceCreateBodyFromInvoice,
)
from .invoice_create_body_issuer import (
    InvoiceCreateBodyIssuer,
    _SerializerInvoiceCreateBodyIssuer,
)
from .invoice_create_body_metadata_obj0 import (
    InvoiceCreateBodyMetadataObj0,
    _SerializerInvoiceCreateBodyMetadataObj0,
)
from .invoice_create_body_payment_settings import (
    InvoiceCreateBodyPaymentSettings,
    _SerializerInvoiceCreateBodyPaymentSettings,
)
from .invoice_create_body_rendering import (
    InvoiceCreateBodyRendering,
    _SerializerInvoiceCreateBodyRendering,
)
from .invoice_create_body_shipping_cost import (
    InvoiceCreateBodyShippingCost,
    _SerializerInvoiceCreateBodyShippingCost,
)
from .invoice_create_body_shipping_details import (
    InvoiceCreateBodyShippingDetails,
    _SerializerInvoiceCreateBodyShippingDetails,
)
from .invoice_create_body_transfer_data import (
    InvoiceCreateBodyTransferData,
    _SerializerInvoiceCreateBodyTransferData,
)


class InvoiceCreateBody(typing_extensions.TypedDict, total=False):
    """
    InvoiceCreateBody
    """

    account_tax_ids: typing_extensions.NotRequired[typing.Union[typing.List[str], str]]
    """
    The account tax IDs associated with the invoice. Only editable when the invoice is a draft.
    """

    application_fee_amount: typing_extensions.NotRequired[int]
    """
    A fee in cents (or local equivalent) that will be applied to the invoice and transferred to the application owner's Stripe account. The request must be made with an OAuth key or the Stripe-Account header in order to take an application fee. For more information, see the application fees [documentation](https://stripe.com/docs/billing/invoices/connect#collecting-fees).
    """

    auto_advance: typing_extensions.NotRequired[bool]
    """
    Controls whether Stripe performs [automatic collection](https://stripe.com/docs/invoicing/integration/automatic-advancement-collection) of the invoice. If `false`, the invoice's state doesn't automatically advance without an explicit action.
    """

    automatic_tax: typing_extensions.NotRequired[InvoiceCreateBodyAutomaticTax]
    """
    Settings for automatic tax lookup for this invoice.
    """

    automatically_finalizes_at: typing_extensions.NotRequired[int]
    """
    The time when this invoice should be scheduled to finalize. The invoice will be finalized at this time if it is still in draft state.
    """

    collection_method: typing_extensions.NotRequired[
        typing_extensions.Literal["charge_automatically", "send_invoice"]
    ]
    """
    Either `charge_automatically`, or `send_invoice`. When charging automatically, Stripe will attempt to pay this invoice using the default source attached to the customer. When sending an invoice, Stripe will email this invoice to the customer with payment instructions. Defaults to `charge_automatically`.
    """

    currency: typing_extensions.NotRequired[str]
    """
    The currency to create this invoice in. Defaults to that of `customer` if not specified.
    """

    custom_fields: typing_extensions.NotRequired[
        typing.Union[typing.List[InvoiceCreateBodyCustomFieldsArr0Item], str]
    ]
    """
    A list of up to 4 custom fields to be displayed on the invoice.
    """

    customer: typing_extensions.NotRequired[str]
    """
    The ID of the customer who will be billed.
    """

    days_until_due: typing_extensions.NotRequired[int]
    """
    The number of days from when the invoice is created until it is due. Valid only for invoices where `collection_method=send_invoice`.
    """

    default_payment_method: typing_extensions.NotRequired[str]
    """
    ID of the default payment method for the invoice. It must belong to the customer associated with the invoice. If not set, defaults to the subscription's default payment method, if any, or to the default payment method in the customer's invoice settings.
    """

    default_source: typing_extensions.NotRequired[str]
    """
    ID of the default payment source for the invoice. It must belong to the customer associated with the invoice and be in a chargeable state. If not set, defaults to the subscription's default source, if any, or to the customer's default source.
    """

    default_tax_rates: typing_extensions.NotRequired[typing.List[str]]
    """
    The tax rates that will apply to any line item that does not have `tax_rates` set.
    """

    description: typing_extensions.NotRequired[str]
    """
    An arbitrary string attached to the object. Often useful for displaying to users. Referenced as 'memo' in the Dashboard.
    """

    discounts: typing_extensions.NotRequired[
        typing.Union[typing.List[InvoiceCreateBodyDiscountsArr0Item], str]
    ]
    """
    The coupons and promotion codes to redeem into discounts for the invoice. If not specified, inherits the discount from the invoice's customer. Pass an empty string to avoid inheriting any discounts.
    """

    due_date: typing_extensions.NotRequired[int]
    """
    The date on which payment for this invoice is due. Valid only for invoices where `collection_method=send_invoice`.
    """

    effective_at: typing_extensions.NotRequired[int]
    """
    The date when this invoice is in effect. Same as `finalized_at` unless overwritten. When defined, this value replaces the system-generated 'Date of issue' printed on the invoice PDF and receipt.
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """

    footer: typing_extensions.NotRequired[str]
    """
    Footer to be displayed on the invoice.
    """

    from_invoice: typing_extensions.NotRequired[InvoiceCreateBodyFromInvoice]
    """
    Revise an existing invoice. The new invoice will be created in `status=draft`. See the [revision documentation](https://stripe.com/docs/invoicing/invoice-revisions) for more details.
    """

    issuer: typing_extensions.NotRequired[InvoiceCreateBodyIssuer]
    """
    The connected account that issues the invoice. The invoice is presented with the branding and support information of the specified account.
    """

    metadata: typing_extensions.NotRequired[
        typing.Union[InvoiceCreateBodyMetadataObj0, str]
    ]
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    """

    number: typing_extensions.NotRequired[str]
    """
    Set the number for this invoice. If no number is present then a number will be assigned automatically when the invoice is finalized. In many markets, regulations require invoices to be unique, sequential and / or gapless. You are responsible for ensuring this is true across all your different invoicing systems in the event that you edit the invoice number using our API. If you use only Stripe for your invoices and do not change invoice numbers, Stripe handles this aspect of compliance for you automatically.
    """

    on_behalf_of: typing_extensions.NotRequired[str]
    """
    The account (if any) for which the funds of the invoice payment are intended. If set, the invoice will be presented with the branding and support information of the specified account. See the [Invoices with Connect](https://stripe.com/docs/billing/invoices/connect) documentation for details.
    """

    payment_settings: typing_extensions.NotRequired[InvoiceCreateBodyPaymentSettings]
    """
    Configuration settings for the PaymentIntent that is generated when the invoice is finalized.
    """

    pending_invoice_items_behavior: typing_extensions.NotRequired[
        typing_extensions.Literal["exclude", "include"]
    ]
    """
    How to handle pending invoice items on invoice creation. Defaults to `exclude` if the parameter is omitted.
    """

    rendering: typing_extensions.NotRequired[InvoiceCreateBodyRendering]
    """
    The rendering-related settings that control how the invoice is displayed on customer-facing surfaces such as PDF and Hosted Invoice Page.
    """

    shipping_cost: typing_extensions.NotRequired[InvoiceCreateBodyShippingCost]
    """
    Settings for the cost of shipping for this invoice.
    """

    shipping_details: typing_extensions.NotRequired[InvoiceCreateBodyShippingDetails]
    """
    Shipping details for the invoice. The Invoice PDF will use the `shipping_details` value if it is set, otherwise the PDF will render the shipping address from the customer.
    """

    statement_descriptor: typing_extensions.NotRequired[str]
    """
    Extra information about a charge for the customer's credit card statement. It must contain at least one letter. If not specified and this invoice is part of a subscription, the default `statement_descriptor` will be set to the first subscription item's product's `statement_descriptor`.
    """

    subscription: typing_extensions.NotRequired[str]
    """
    The ID of the subscription to invoice, if any. If set, the created invoice will only include pending invoice items for that subscription. The subscription's billing cycle and regular subscription events won't be affected.
    """

    transfer_data: typing_extensions.NotRequired[InvoiceCreateBodyTransferData]
    """
    If specified, the funds from the invoice will be transferred to the destination and the ID of the resulting transfer will be found on the invoice's charge.
    """


class _SerializerInvoiceCreateBody(pydantic.BaseModel):
    """
    Serializer for InvoiceCreateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    account_tax_ids: typing.Optional[typing.Union[typing.List[str], str]] = (
        pydantic.Field(alias="account_tax_ids", default=None)
    )
    application_fee_amount: typing.Optional[int] = pydantic.Field(
        alias="application_fee_amount", default=None
    )
    auto_advance: typing.Optional[bool] = pydantic.Field(
        alias="auto_advance", default=None
    )
    automatic_tax: typing.Optional[_SerializerInvoiceCreateBodyAutomaticTax] = (
        pydantic.Field(alias="automatic_tax", default=None)
    )
    automatically_finalizes_at: typing.Optional[int] = pydantic.Field(
        alias="automatically_finalizes_at", default=None
    )
    collection_method: typing.Optional[
        typing_extensions.Literal["charge_automatically", "send_invoice"]
    ] = pydantic.Field(alias="collection_method", default=None)
    currency: typing.Optional[str] = pydantic.Field(alias="currency", default=None)
    custom_fields: typing.Optional[
        typing.Union[typing.List[_SerializerInvoiceCreateBodyCustomFieldsArr0Item], str]
    ] = pydantic.Field(alias="custom_fields", default=None)
    customer: typing.Optional[str] = pydantic.Field(alias="customer", default=None)
    days_until_due: typing.Optional[int] = pydantic.Field(
        alias="days_until_due", default=None
    )
    default_payment_method: typing.Optional[str] = pydantic.Field(
        alias="default_payment_method", default=None
    )
    default_source: typing.Optional[str] = pydantic.Field(
        alias="default_source", default=None
    )
    default_tax_rates: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="default_tax_rates", default=None
    )
    description: typing.Optional[str] = pydantic.Field(
        alias="description", default=None
    )
    discounts: typing.Optional[
        typing.Union[typing.List[_SerializerInvoiceCreateBodyDiscountsArr0Item], str]
    ] = pydantic.Field(alias="discounts", default=None)
    due_date: typing.Optional[int] = pydantic.Field(alias="due_date", default=None)
    effective_at: typing.Optional[int] = pydantic.Field(
        alias="effective_at", default=None
    )
    expand: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="expand", default=None
    )
    footer: typing.Optional[str] = pydantic.Field(alias="footer", default=None)
    from_invoice: typing.Optional[_SerializerInvoiceCreateBodyFromInvoice] = (
        pydantic.Field(alias="from_invoice", default=None)
    )
    issuer: typing.Optional[_SerializerInvoiceCreateBodyIssuer] = pydantic.Field(
        alias="issuer", default=None
    )
    metadata: typing.Optional[
        typing.Union[_SerializerInvoiceCreateBodyMetadataObj0, str]
    ] = pydantic.Field(alias="metadata", default=None)
    number: typing.Optional[str] = pydantic.Field(alias="number", default=None)
    on_behalf_of: typing.Optional[str] = pydantic.Field(
        alias="on_behalf_of", default=None
    )
    payment_settings: typing.Optional[_SerializerInvoiceCreateBodyPaymentSettings] = (
        pydantic.Field(alias="payment_settings", default=None)
    )
    pending_invoice_items_behavior: typing.Optional[
        typing_extensions.Literal["exclude", "include"]
    ] = pydantic.Field(alias="pending_invoice_items_behavior", default=None)
    rendering: typing.Optional[_SerializerInvoiceCreateBodyRendering] = pydantic.Field(
        alias="rendering", default=None
    )
    shipping_cost: typing.Optional[_SerializerInvoiceCreateBodyShippingCost] = (
        pydantic.Field(alias="shipping_cost", default=None)
    )
    shipping_details: typing.Optional[_SerializerInvoiceCreateBodyShippingDetails] = (
        pydantic.Field(alias="shipping_details", default=None)
    )
    statement_descriptor: typing.Optional[str] = pydantic.Field(
        alias="statement_descriptor", default=None
    )
    subscription: typing.Optional[str] = pydantic.Field(
        alias="subscription", default=None
    )
    transfer_data: typing.Optional[_SerializerInvoiceCreateBodyTransferData] = (
        pydantic.Field(alias="transfer_data", default=None)
    )
