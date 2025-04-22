import pydantic
import typing
import typing_extensions

from .quote_create_body_automatic_tax import (
    QuoteCreateBodyAutomaticTax,
    _SerializerQuoteCreateBodyAutomaticTax,
)
from .quote_create_body_discounts_arr0_item import (
    QuoteCreateBodyDiscountsArr0Item,
    _SerializerQuoteCreateBodyDiscountsArr0Item,
)
from .quote_create_body_from_quote import (
    QuoteCreateBodyFromQuote,
    _SerializerQuoteCreateBodyFromQuote,
)
from .quote_create_body_invoice_settings import (
    QuoteCreateBodyInvoiceSettings,
    _SerializerQuoteCreateBodyInvoiceSettings,
)
from .quote_create_body_line_items_item import (
    QuoteCreateBodyLineItemsItem,
    _SerializerQuoteCreateBodyLineItemsItem,
)
from .quote_create_body_metadata import (
    QuoteCreateBodyMetadata,
    _SerializerQuoteCreateBodyMetadata,
)
from .quote_create_body_subscription_data import (
    QuoteCreateBodySubscriptionData,
    _SerializerQuoteCreateBodySubscriptionData,
)
from .quote_create_body_transfer_data_obj0 import (
    QuoteCreateBodyTransferDataObj0,
    _SerializerQuoteCreateBodyTransferDataObj0,
)


class QuoteCreateBody(typing_extensions.TypedDict, total=False):
    """
    QuoteCreateBody
    """

    application_fee_amount: typing_extensions.NotRequired[typing.Union[int, str]]
    """
    The amount of the application fee (if any) that will be requested to be applied to the payment and transferred to the application owner's Stripe account. There cannot be any line items with recurring prices when using this field.
    """

    application_fee_percent: typing_extensions.NotRequired[typing.Union[float, str]]
    """
    A non-negative decimal between 0 and 100, with at most two decimal places. This represents the percentage of the subscription invoice total that will be transferred to the application owner's Stripe account. There must be at least 1 line item with a recurring price to use this field.
    """

    automatic_tax: typing_extensions.NotRequired[QuoteCreateBodyAutomaticTax]
    """
    Settings for automatic tax lookup for this quote and resulting invoices and subscriptions.
    """

    collection_method: typing_extensions.NotRequired[
        typing_extensions.Literal["charge_automatically", "send_invoice"]
    ]
    """
    Either `charge_automatically`, or `send_invoice`. When charging automatically, Stripe will attempt to pay invoices at the end of the subscription cycle or at invoice finalization using the default payment method attached to the subscription or customer. When sending an invoice, Stripe will email your customer an invoice with payment instructions and mark the subscription as `active`. Defaults to `charge_automatically`.
    """

    customer: typing_extensions.NotRequired[str]
    """
    The customer for which this quote belongs to. A customer is required before finalizing the quote. Once specified, it cannot be changed.
    """

    default_tax_rates: typing_extensions.NotRequired[
        typing.Union[typing.List[str], str]
    ]
    """
    The tax rates that will apply to any line item that does not have `tax_rates` set.
    """

    description: typing_extensions.NotRequired[typing.Union[str, str]]
    """
    A description that will be displayed on the quote PDF. If no value is passed, the default description configured in your [quote template settings](https://dashboard.stripe.com/settings/billing/quote) will be used.
    """

    discounts: typing_extensions.NotRequired[
        typing.Union[typing.List[QuoteCreateBodyDiscountsArr0Item], str]
    ]
    """
    The discounts applied to the quote.
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """

    expires_at: typing_extensions.NotRequired[int]
    """
    A future timestamp on which the quote will be canceled if in `open` or `draft` status. Measured in seconds since the Unix epoch. If no value is passed, the default expiration date configured in your [quote template settings](https://dashboard.stripe.com/settings/billing/quote) will be used.
    """

    footer: typing_extensions.NotRequired[typing.Union[str, str]]
    """
    A footer that will be displayed on the quote PDF. If no value is passed, the default footer configured in your [quote template settings](https://dashboard.stripe.com/settings/billing/quote) will be used.
    """

    from_quote: typing_extensions.NotRequired[QuoteCreateBodyFromQuote]
    """
    Clone an existing quote. The new quote will be created in `status=draft`. When using this parameter, you cannot specify any other parameters except for `expires_at`.
    """

    header: typing_extensions.NotRequired[typing.Union[str, str]]
    """
    A header that will be displayed on the quote PDF. If no value is passed, the default header configured in your [quote template settings](https://dashboard.stripe.com/settings/billing/quote) will be used.
    """

    invoice_settings: typing_extensions.NotRequired[QuoteCreateBodyInvoiceSettings]
    """
    All invoices will be billed using the specified settings.
    """

    line_items: typing_extensions.NotRequired[typing.List[QuoteCreateBodyLineItemsItem]]
    """
    A list of line items the customer is being quoted for. Each line item includes information about the product, the quantity, and the resulting cost.
    """

    metadata: typing_extensions.NotRequired[QuoteCreateBodyMetadata]
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    """

    on_behalf_of: typing_extensions.NotRequired[typing.Union[str, str]]
    """
    The account on behalf of which to charge.
    """

    subscription_data: typing_extensions.NotRequired[QuoteCreateBodySubscriptionData]
    """
    When creating a subscription or subscription schedule, the specified configuration data will be used. There must be at least one line item with a recurring price for a subscription or subscription schedule to be created. A subscription schedule is created if `subscription_data[effective_date]` is present and in the future, otherwise a subscription is created.
    """

    test_clock: typing_extensions.NotRequired[str]
    """
    ID of the test clock to attach to the quote.
    """

    transfer_data: typing_extensions.NotRequired[
        typing.Union[QuoteCreateBodyTransferDataObj0, str]
    ]
    """
    The data with which to automatically create a Transfer for each of the invoices.
    """


class _SerializerQuoteCreateBody(pydantic.BaseModel):
    """
    Serializer for QuoteCreateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    application_fee_amount: typing.Optional[typing.Union[int, str]] = pydantic.Field(
        alias="application_fee_amount", default=None
    )
    application_fee_percent: typing.Optional[typing.Union[float, str]] = pydantic.Field(
        alias="application_fee_percent", default=None
    )
    automatic_tax: typing.Optional[_SerializerQuoteCreateBodyAutomaticTax] = (
        pydantic.Field(alias="automatic_tax", default=None)
    )
    collection_method: typing.Optional[
        typing_extensions.Literal["charge_automatically", "send_invoice"]
    ] = pydantic.Field(alias="collection_method", default=None)
    customer: typing.Optional[str] = pydantic.Field(alias="customer", default=None)
    default_tax_rates: typing.Optional[typing.Union[typing.List[str], str]] = (
        pydantic.Field(alias="default_tax_rates", default=None)
    )
    description: typing.Optional[typing.Union[str, str]] = pydantic.Field(
        alias="description", default=None
    )
    discounts: typing.Optional[
        typing.Union[typing.List[_SerializerQuoteCreateBodyDiscountsArr0Item], str]
    ] = pydantic.Field(alias="discounts", default=None)
    expand: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="expand", default=None
    )
    expires_at: typing.Optional[int] = pydantic.Field(alias="expires_at", default=None)
    footer: typing.Optional[typing.Union[str, str]] = pydantic.Field(
        alias="footer", default=None
    )
    from_quote: typing.Optional[_SerializerQuoteCreateBodyFromQuote] = pydantic.Field(
        alias="from_quote", default=None
    )
    header: typing.Optional[typing.Union[str, str]] = pydantic.Field(
        alias="header", default=None
    )
    invoice_settings: typing.Optional[_SerializerQuoteCreateBodyInvoiceSettings] = (
        pydantic.Field(alias="invoice_settings", default=None)
    )
    line_items: typing.Optional[
        typing.List[_SerializerQuoteCreateBodyLineItemsItem]
    ] = pydantic.Field(alias="line_items", default=None)
    metadata: typing.Optional[_SerializerQuoteCreateBodyMetadata] = pydantic.Field(
        alias="metadata", default=None
    )
    on_behalf_of: typing.Optional[typing.Union[str, str]] = pydantic.Field(
        alias="on_behalf_of", default=None
    )
    subscription_data: typing.Optional[_SerializerQuoteCreateBodySubscriptionData] = (
        pydantic.Field(alias="subscription_data", default=None)
    )
    test_clock: typing.Optional[str] = pydantic.Field(alias="test_clock", default=None)
    transfer_data: typing.Optional[
        typing.Union[_SerializerQuoteCreateBodyTransferDataObj0, str]
    ] = pydantic.Field(alias="transfer_data", default=None)
