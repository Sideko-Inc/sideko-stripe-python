import pydantic
import typing
import typing_extensions

from .invoice_item_create_body_discounts_arr0_item import (
    InvoiceItemCreateBodyDiscountsArr0Item,
    _SerializerInvoiceItemCreateBodyDiscountsArr0Item,
)
from .invoice_item_create_body_metadata_obj0 import (
    InvoiceItemCreateBodyMetadataObj0,
    _SerializerInvoiceItemCreateBodyMetadataObj0,
)
from .invoice_item_create_body_period import (
    InvoiceItemCreateBodyPeriod,
    _SerializerInvoiceItemCreateBodyPeriod,
)
from .invoice_item_create_body_price_data import (
    InvoiceItemCreateBodyPriceData,
    _SerializerInvoiceItemCreateBodyPriceData,
)
from .invoice_item_create_body_pricing import (
    InvoiceItemCreateBodyPricing,
    _SerializerInvoiceItemCreateBodyPricing,
)


class InvoiceItemCreateBody(typing_extensions.TypedDict, total=False):
    """
    InvoiceItemCreateBody
    """

    amount: typing_extensions.NotRequired[int]
    """
    The integer amount in cents (or local equivalent) of the charge to be applied to the upcoming invoice. Passing in a negative `amount` will reduce the `amount_due` on the invoice.
    """

    currency: typing_extensions.NotRequired[str]
    """
    Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    """

    customer: typing_extensions.Required[str]
    """
    The ID of the customer who will be billed when this invoice item is billed.
    """

    description: typing_extensions.NotRequired[str]
    """
    An arbitrary string which you can attach to the invoice item. The description is displayed in the invoice for easy tracking.
    """

    discountable: typing_extensions.NotRequired[bool]
    """
    Controls whether discounts apply to this invoice item. Defaults to false for prorations or negative invoice items, and true for all other invoice items.
    """

    discounts: typing_extensions.NotRequired[
        typing.Union[typing.List[InvoiceItemCreateBodyDiscountsArr0Item], str]
    ]
    """
    The coupons and promotion codes to redeem into discounts for the invoice item or invoice line item.
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """

    invoice: typing_extensions.NotRequired[str]
    """
    The ID of an existing invoice to add this invoice item to. When left blank, the invoice item will be added to the next upcoming scheduled invoice. This is useful when adding invoice items in response to an invoice.created webhook. You can only add invoice items to draft invoices and there is a maximum of 250 items per invoice.
    """

    metadata: typing_extensions.NotRequired[
        typing.Union[InvoiceItemCreateBodyMetadataObj0, str]
    ]
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    """

    period: typing_extensions.NotRequired[InvoiceItemCreateBodyPeriod]
    """
    The period associated with this invoice item. When set to different values, the period will be rendered on the invoice. If you have [Stripe Revenue Recognition](https://stripe.com/docs/revenue-recognition) enabled, the period will be used to recognize and defer revenue. See the [Revenue Recognition documentation](https://stripe.com/docs/revenue-recognition/methodology/subscriptions-and-invoicing) for details.
    """

    price_data: typing_extensions.NotRequired[InvoiceItemCreateBodyPriceData]
    """
    Data used to generate a new [Price](https://stripe.com/docs/api/prices) object inline.
    """

    pricing: typing_extensions.NotRequired[InvoiceItemCreateBodyPricing]
    """
    The pricing information for the invoice item.
    """

    quantity: typing_extensions.NotRequired[int]
    """
    Non-negative integer. The quantity of units for the invoice item.
    """

    subscription: typing_extensions.NotRequired[str]
    """
    The ID of a subscription to add this invoice item to. When left blank, the invoice item is added to the next upcoming scheduled invoice. When set, scheduled invoices for subscriptions other than the specified subscription will ignore the invoice item. Use this when you want to express that an invoice item has been accrued within the context of a particular subscription.
    """

    tax_behavior: typing_extensions.NotRequired[
        typing_extensions.Literal["exclusive", "inclusive", "unspecified"]
    ]
    """
    Only required if a [default tax behavior](https://stripe.com/docs/tax/products-prices-tax-categories-tax-behavior#setting-a-default-tax-behavior-(recommended)) was not provided in the Stripe Tax settings. Specifies whether the price is considered inclusive of taxes or exclusive of taxes. One of `inclusive`, `exclusive`, or `unspecified`. Once specified as either `inclusive` or `exclusive`, it cannot be changed.
    """

    tax_code: typing_extensions.NotRequired[typing.Union[str, str]]
    """
    A [tax code](https://stripe.com/docs/tax/tax-categories) ID.
    """

    tax_rates: typing_extensions.NotRequired[typing.List[str]]
    """
    The tax rates which apply to the invoice item. When set, the `default_tax_rates` on the invoice do not apply to this invoice item.
    """

    unit_amount_decimal: typing_extensions.NotRequired[str]
    """
    The decimal unit amount in cents (or local equivalent) of the charge to be applied to the upcoming invoice. This `unit_amount_decimal` will be multiplied by the quantity to get the full amount. Passing in a negative `unit_amount_decimal` will reduce the `amount_due` on the invoice. Accepts at most 12 decimal places.
    """


class _SerializerInvoiceItemCreateBody(pydantic.BaseModel):
    """
    Serializer for InvoiceItemCreateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    amount: typing.Optional[int] = pydantic.Field(alias="amount", default=None)
    currency: typing.Optional[str] = pydantic.Field(alias="currency", default=None)
    customer: str = pydantic.Field(
        alias="customer",
    )
    description: typing.Optional[str] = pydantic.Field(
        alias="description", default=None
    )
    discountable: typing.Optional[bool] = pydantic.Field(
        alias="discountable", default=None
    )
    discounts: typing.Optional[
        typing.Union[
            typing.List[_SerializerInvoiceItemCreateBodyDiscountsArr0Item], str
        ]
    ] = pydantic.Field(alias="discounts", default=None)
    expand: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="expand", default=None
    )
    invoice: typing.Optional[str] = pydantic.Field(alias="invoice", default=None)
    metadata: typing.Optional[
        typing.Union[_SerializerInvoiceItemCreateBodyMetadataObj0, str]
    ] = pydantic.Field(alias="metadata", default=None)
    period: typing.Optional[_SerializerInvoiceItemCreateBodyPeriod] = pydantic.Field(
        alias="period", default=None
    )
    price_data: typing.Optional[_SerializerInvoiceItemCreateBodyPriceData] = (
        pydantic.Field(alias="price_data", default=None)
    )
    pricing: typing.Optional[_SerializerInvoiceItemCreateBodyPricing] = pydantic.Field(
        alias="pricing", default=None
    )
    quantity: typing.Optional[int] = pydantic.Field(alias="quantity", default=None)
    subscription: typing.Optional[str] = pydantic.Field(
        alias="subscription", default=None
    )
    tax_behavior: typing.Optional[
        typing_extensions.Literal["exclusive", "inclusive", "unspecified"]
    ] = pydantic.Field(alias="tax_behavior", default=None)
    tax_code: typing.Optional[typing.Union[str, str]] = pydantic.Field(
        alias="tax_code", default=None
    )
    tax_rates: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="tax_rates", default=None
    )
    unit_amount_decimal: typing.Optional[str] = pydantic.Field(
        alias="unit_amount_decimal", default=None
    )
