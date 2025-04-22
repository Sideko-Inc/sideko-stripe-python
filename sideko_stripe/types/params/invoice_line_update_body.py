import pydantic
import typing
import typing_extensions

from .invoice_line_update_body_discounts_arr0_item import (
    InvoiceLineUpdateBodyDiscountsArr0Item,
    _SerializerInvoiceLineUpdateBodyDiscountsArr0Item,
)
from .invoice_line_update_body_metadata_obj0 import (
    InvoiceLineUpdateBodyMetadataObj0,
    _SerializerInvoiceLineUpdateBodyMetadataObj0,
)
from .invoice_line_update_body_period import (
    InvoiceLineUpdateBodyPeriod,
    _SerializerInvoiceLineUpdateBodyPeriod,
)
from .invoice_line_update_body_price_data import (
    InvoiceLineUpdateBodyPriceData,
    _SerializerInvoiceLineUpdateBodyPriceData,
)
from .invoice_line_update_body_pricing import (
    InvoiceLineUpdateBodyPricing,
    _SerializerInvoiceLineUpdateBodyPricing,
)
from .invoice_line_update_body_tax_amounts_arr0_item import (
    InvoiceLineUpdateBodyTaxAmountsArr0Item,
    _SerializerInvoiceLineUpdateBodyTaxAmountsArr0Item,
)


class InvoiceLineUpdateBody(typing_extensions.TypedDict, total=False):
    """
    InvoiceLineUpdateBody
    """

    amount: typing_extensions.NotRequired[int]
    """
    The integer amount in cents (or local equivalent) of the charge to be applied to the upcoming invoice. If you want to apply a credit to the customer's account, pass a negative amount.
    """

    description: typing_extensions.NotRequired[str]
    """
    An arbitrary string which you can attach to the invoice item. The description is displayed in the invoice for easy tracking.
    """

    discountable: typing_extensions.NotRequired[bool]
    """
    Controls whether discounts apply to this line item. Defaults to false for prorations or negative line items, and true for all other line items. Cannot be set to true for prorations.
    """

    discounts: typing_extensions.NotRequired[
        typing.Union[typing.List[InvoiceLineUpdateBodyDiscountsArr0Item], str]
    ]
    """
    The coupons, promotion codes & existing discounts which apply to the line item. Item discounts are applied before invoice discounts. Pass an empty string to remove previously-defined discounts.
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """

    metadata: typing_extensions.NotRequired[
        typing.Union[InvoiceLineUpdateBodyMetadataObj0, str]
    ]
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`. For [type=subscription](https://stripe.com/docs/api/invoices/line_item#invoice_line_item_object-type) line items, the incoming metadata specified on the request is directly used to set this value, in contrast to [type=invoiceitem](api/invoices/line_item#invoice_line_item_object-type) line items, where any existing metadata on the invoice line is merged with the incoming data.
    """

    period: typing_extensions.NotRequired[InvoiceLineUpdateBodyPeriod]
    """
    The period associated with this invoice item. When set to different values, the period will be rendered on the invoice. If you have [Stripe Revenue Recognition](https://stripe.com/docs/revenue-recognition) enabled, the period will be used to recognize and defer revenue. See the [Revenue Recognition documentation](https://stripe.com/docs/revenue-recognition/methodology/subscriptions-and-invoicing) for details.
    """

    price_data: typing_extensions.NotRequired[InvoiceLineUpdateBodyPriceData]
    """
    Data used to generate a new [Price](https://stripe.com/docs/api/prices) object inline.
    """

    pricing: typing_extensions.NotRequired[InvoiceLineUpdateBodyPricing]
    """
    The pricing information for the invoice item.
    """

    quantity: typing_extensions.NotRequired[int]
    """
    Non-negative integer. The quantity of units for the line item.
    """

    tax_amounts: typing_extensions.NotRequired[
        typing.Union[typing.List[InvoiceLineUpdateBodyTaxAmountsArr0Item], str]
    ]
    """
    A list of up to 10 tax amounts for this line item. This can be useful if you calculate taxes on your own or use a third-party to calculate them. You cannot set tax amounts if any line item has [tax_rates](https://stripe.com/docs/api/invoices/line_item#invoice_line_item_object-tax_rates) or if the invoice has [default_tax_rates](https://stripe.com/docs/api/invoices/object#invoice_object-default_tax_rates) or uses [automatic tax](https://stripe.com/docs/tax/invoicing). Pass an empty string to remove previously defined tax amounts.
    """

    tax_rates: typing_extensions.NotRequired[typing.Union[typing.List[str], str]]
    """
    The tax rates which apply to the line item. When set, the `default_tax_rates` on the invoice do not apply to this line item. Pass an empty string to remove previously-defined tax rates.
    """


class _SerializerInvoiceLineUpdateBody(pydantic.BaseModel):
    """
    Serializer for InvoiceLineUpdateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    amount: typing.Optional[int] = pydantic.Field(alias="amount", default=None)
    description: typing.Optional[str] = pydantic.Field(
        alias="description", default=None
    )
    discountable: typing.Optional[bool] = pydantic.Field(
        alias="discountable", default=None
    )
    discounts: typing.Optional[
        typing.Union[
            typing.List[_SerializerInvoiceLineUpdateBodyDiscountsArr0Item], str
        ]
    ] = pydantic.Field(alias="discounts", default=None)
    expand: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="expand", default=None
    )
    metadata: typing.Optional[
        typing.Union[_SerializerInvoiceLineUpdateBodyMetadataObj0, str]
    ] = pydantic.Field(alias="metadata", default=None)
    period: typing.Optional[_SerializerInvoiceLineUpdateBodyPeriod] = pydantic.Field(
        alias="period", default=None
    )
    price_data: typing.Optional[_SerializerInvoiceLineUpdateBodyPriceData] = (
        pydantic.Field(alias="price_data", default=None)
    )
    pricing: typing.Optional[_SerializerInvoiceLineUpdateBodyPricing] = pydantic.Field(
        alias="pricing", default=None
    )
    quantity: typing.Optional[int] = pydantic.Field(alias="quantity", default=None)
    tax_amounts: typing.Optional[
        typing.Union[
            typing.List[_SerializerInvoiceLineUpdateBodyTaxAmountsArr0Item], str
        ]
    ] = pydantic.Field(alias="tax_amounts", default=None)
    tax_rates: typing.Optional[typing.Union[typing.List[str], str]] = pydantic.Field(
        alias="tax_rates", default=None
    )
