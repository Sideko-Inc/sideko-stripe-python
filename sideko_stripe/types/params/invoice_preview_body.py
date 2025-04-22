import pydantic
import typing
import typing_extensions

from .invoice_preview_body_automatic_tax import (
    InvoicePreviewBodyAutomaticTax,
    _SerializerInvoicePreviewBodyAutomaticTax,
)
from .invoice_preview_body_customer_details import (
    InvoicePreviewBodyCustomerDetails,
    _SerializerInvoicePreviewBodyCustomerDetails,
)
from .invoice_preview_body_discounts_arr0_item import (
    InvoicePreviewBodyDiscountsArr0Item,
    _SerializerInvoicePreviewBodyDiscountsArr0Item,
)
from .invoice_preview_body_invoice_items_item import (
    InvoicePreviewBodyInvoiceItemsItem,
    _SerializerInvoicePreviewBodyInvoiceItemsItem,
)
from .invoice_preview_body_issuer import (
    InvoicePreviewBodyIssuer,
    _SerializerInvoicePreviewBodyIssuer,
)
from .invoice_preview_body_schedule_details import (
    InvoicePreviewBodyScheduleDetails,
    _SerializerInvoicePreviewBodyScheduleDetails,
)
from .invoice_preview_body_subscription_details import (
    InvoicePreviewBodySubscriptionDetails,
    _SerializerInvoicePreviewBodySubscriptionDetails,
)


class InvoicePreviewBody(typing_extensions.TypedDict, total=False):
    """
    InvoicePreviewBody
    """

    automatic_tax: typing_extensions.NotRequired[InvoicePreviewBodyAutomaticTax]
    """
    Settings for automatic tax lookup for this invoice preview.
    """

    currency: typing_extensions.NotRequired[str]
    """
    The currency to preview this invoice in. Defaults to that of `customer` if not specified.
    """

    customer: typing_extensions.NotRequired[str]
    """
    The identifier of the customer whose upcoming invoice you'd like to retrieve. If `automatic_tax` is enabled then one of `customer`, `customer_details`, `subscription`, or `schedule` must be set.
    """

    customer_details: typing_extensions.NotRequired[InvoicePreviewBodyCustomerDetails]
    """
    Details about the customer you want to invoice or overrides for an existing customer. If `automatic_tax` is enabled then one of `customer`, `customer_details`, `subscription`, or `schedule` must be set.
    """

    discounts: typing_extensions.NotRequired[
        typing.Union[typing.List[InvoicePreviewBodyDiscountsArr0Item], str]
    ]
    """
    The coupons to redeem into discounts for the invoice preview. If not specified, inherits the discount from the subscription or customer. This works for both coupons directly applied to an invoice and coupons applied to a subscription. Pass an empty string to avoid inheriting any discounts.
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """

    invoice_items: typing_extensions.NotRequired[
        typing.List[InvoicePreviewBodyInvoiceItemsItem]
    ]
    """
    List of invoice items to add or update in the upcoming invoice preview (up to 250).
    """

    issuer: typing_extensions.NotRequired[InvoicePreviewBodyIssuer]
    """
    The connected account that issues the invoice. The invoice is presented with the branding and support information of the specified account.
    """

    on_behalf_of: typing_extensions.NotRequired[typing.Union[str, str]]
    """
    The account (if any) for which the funds of the invoice payment are intended. If set, the invoice will be presented with the branding and support information of the specified account. See the [Invoices with Connect](https://stripe.com/docs/billing/invoices/connect) documentation for details.
    """

    preview_mode: typing_extensions.NotRequired[
        typing_extensions.Literal["next", "recurring"]
    ]
    """
    Customizes the types of values to include when calculating the invoice. Defaults to `next` if unspecified.
    """

    schedule: typing_extensions.NotRequired[str]
    """
    The identifier of the schedule whose upcoming invoice you'd like to retrieve. Cannot be used with subscription or subscription fields.
    """

    schedule_details: typing_extensions.NotRequired[InvoicePreviewBodyScheduleDetails]
    """
    The schedule creation or modification params to apply as a preview. Cannot be used with `subscription` or `subscription_` prefixed fields.
    """

    subscription: typing_extensions.NotRequired[str]
    """
    The identifier of the subscription for which you'd like to retrieve the upcoming invoice. If not provided, but a `subscription_details.items` is provided, you will preview creating a subscription with those items. If neither `subscription` nor `subscription_details.items` is provided, you will retrieve the next upcoming invoice from among the customer's subscriptions.
    """

    subscription_details: typing_extensions.NotRequired[
        InvoicePreviewBodySubscriptionDetails
    ]
    """
    The subscription creation or modification params to apply as a preview. Cannot be used with `schedule` or `schedule_details` fields.
    """


class _SerializerInvoicePreviewBody(pydantic.BaseModel):
    """
    Serializer for InvoicePreviewBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    automatic_tax: typing.Optional[_SerializerInvoicePreviewBodyAutomaticTax] = (
        pydantic.Field(alias="automatic_tax", default=None)
    )
    currency: typing.Optional[str] = pydantic.Field(alias="currency", default=None)
    customer: typing.Optional[str] = pydantic.Field(alias="customer", default=None)
    customer_details: typing.Optional[_SerializerInvoicePreviewBodyCustomerDetails] = (
        pydantic.Field(alias="customer_details", default=None)
    )
    discounts: typing.Optional[
        typing.Union[typing.List[_SerializerInvoicePreviewBodyDiscountsArr0Item], str]
    ] = pydantic.Field(alias="discounts", default=None)
    expand: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="expand", default=None
    )
    invoice_items: typing.Optional[
        typing.List[_SerializerInvoicePreviewBodyInvoiceItemsItem]
    ] = pydantic.Field(alias="invoice_items", default=None)
    issuer: typing.Optional[_SerializerInvoicePreviewBodyIssuer] = pydantic.Field(
        alias="issuer", default=None
    )
    on_behalf_of: typing.Optional[typing.Union[str, str]] = pydantic.Field(
        alias="on_behalf_of", default=None
    )
    preview_mode: typing.Optional[typing_extensions.Literal["next", "recurring"]] = (
        pydantic.Field(alias="preview_mode", default=None)
    )
    schedule: typing.Optional[str] = pydantic.Field(alias="schedule", default=None)
    schedule_details: typing.Optional[_SerializerInvoicePreviewBodyScheduleDetails] = (
        pydantic.Field(alias="schedule_details", default=None)
    )
    subscription: typing.Optional[str] = pydantic.Field(
        alias="subscription", default=None
    )
    subscription_details: typing.Optional[
        _SerializerInvoicePreviewBodySubscriptionDetails
    ] = pydantic.Field(alias="subscription_details", default=None)
