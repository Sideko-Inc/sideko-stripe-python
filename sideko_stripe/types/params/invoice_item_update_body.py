import pydantic
import typing
import typing_extensions

from .invoice_item_update_body_discounts_arr0_item import (
    InvoiceItemUpdateBodyDiscountsArr0Item,
    _SerializerInvoiceItemUpdateBodyDiscountsArr0Item,
)
from .invoice_item_update_body_metadata_obj0 import (
    InvoiceItemUpdateBodyMetadataObj0,
    _SerializerInvoiceItemUpdateBodyMetadataObj0,
)
from .invoice_item_update_body_period import (
    InvoiceItemUpdateBodyPeriod,
    _SerializerInvoiceItemUpdateBodyPeriod,
)
from .invoice_item_update_body_price_data import (
    InvoiceItemUpdateBodyPriceData,
    _SerializerInvoiceItemUpdateBodyPriceData,
)
from .invoice_item_update_body_pricing import (
    InvoiceItemUpdateBodyPricing,
    _SerializerInvoiceItemUpdateBodyPricing,
)


class InvoiceItemUpdateBody(typing_extensions.TypedDict, total=False):
    """
    InvoiceItemUpdateBody
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
    Controls whether discounts apply to this invoice item. Defaults to false for prorations or negative invoice items, and true for all other invoice items. Cannot be set to true for prorations.
    """

    discounts: typing_extensions.NotRequired[
        typing.Union[typing.List[InvoiceItemUpdateBodyDiscountsArr0Item], str]
    ]
    """
    The coupons, promotion codes & existing discounts which apply to the invoice item or invoice line item. Item discounts are applied before invoice discounts. Pass an empty string to remove previously-defined discounts.
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """

    metadata: typing_extensions.NotRequired[
        typing.Union[InvoiceItemUpdateBodyMetadataObj0, str]
    ]
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    """

    period: typing_extensions.NotRequired[InvoiceItemUpdateBodyPeriod]
    """
    The period associated with this invoice item. When set to different values, the period will be rendered on the invoice. If you have [Stripe Revenue Recognition](https://stripe.com/docs/revenue-recognition) enabled, the period will be used to recognize and defer revenue. See the [Revenue Recognition documentation](https://stripe.com/docs/revenue-recognition/methodology/subscriptions-and-invoicing) for details.
    """

    price_data: typing_extensions.NotRequired[InvoiceItemUpdateBodyPriceData]
    """
    Data used to generate a new [Price](https://stripe.com/docs/api/prices) object inline.
    """

    pricing: typing_extensions.NotRequired[InvoiceItemUpdateBodyPricing]
    """
    The pricing information for the invoice item.
    """

    quantity: typing_extensions.NotRequired[int]
    """
    Non-negative integer. The quantity of units for the invoice item.
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

    tax_rates: typing_extensions.NotRequired[typing.Union[typing.List[str], str]]
    """
    The tax rates which apply to the invoice item. When set, the `default_tax_rates` on the invoice do not apply to this invoice item. Pass an empty string to remove previously-defined tax rates.
    """

    unit_amount_decimal: typing_extensions.NotRequired[str]
    """
    The decimal unit amount in cents (or local equivalent) of the charge to be applied to the upcoming invoice. This `unit_amount_decimal` will be multiplied by the quantity to get the full amount. Passing in a negative `unit_amount_decimal` will reduce the `amount_due` on the invoice. Accepts at most 12 decimal places.
    """


class _SerializerInvoiceItemUpdateBody(pydantic.BaseModel):
    """
    Serializer for InvoiceItemUpdateBody handling case conversions
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
            typing.List[_SerializerInvoiceItemUpdateBodyDiscountsArr0Item], str
        ]
    ] = pydantic.Field(alias="discounts", default=None)
    expand: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="expand", default=None
    )
    metadata: typing.Optional[
        typing.Union[_SerializerInvoiceItemUpdateBodyMetadataObj0, str]
    ] = pydantic.Field(alias="metadata", default=None)
    period: typing.Optional[_SerializerInvoiceItemUpdateBodyPeriod] = pydantic.Field(
        alias="period", default=None
    )
    price_data: typing.Optional[_SerializerInvoiceItemUpdateBodyPriceData] = (
        pydantic.Field(alias="price_data", default=None)
    )
    pricing: typing.Optional[_SerializerInvoiceItemUpdateBodyPricing] = pydantic.Field(
        alias="pricing", default=None
    )
    quantity: typing.Optional[int] = pydantic.Field(alias="quantity", default=None)
    tax_behavior: typing.Optional[
        typing_extensions.Literal["exclusive", "inclusive", "unspecified"]
    ] = pydantic.Field(alias="tax_behavior", default=None)
    tax_code: typing.Optional[typing.Union[str, str]] = pydantic.Field(
        alias="tax_code", default=None
    )
    tax_rates: typing.Optional[typing.Union[typing.List[str], str]] = pydantic.Field(
        alias="tax_rates", default=None
    )
    unit_amount_decimal: typing.Optional[str] = pydantic.Field(
        alias="unit_amount_decimal", default=None
    )
