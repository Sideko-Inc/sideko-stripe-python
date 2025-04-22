import pydantic
import typing
import typing_extensions

from .invoice_line_create_many_body_lines_item_discounts_arr0_item import (
    InvoiceLineCreateManyBodyLinesItemDiscountsArr0Item,
    _SerializerInvoiceLineCreateManyBodyLinesItemDiscountsArr0Item,
)
from .invoice_line_create_many_body_lines_item_metadata_obj0 import (
    InvoiceLineCreateManyBodyLinesItemMetadataObj0,
    _SerializerInvoiceLineCreateManyBodyLinesItemMetadataObj0,
)
from .invoice_line_create_many_body_lines_item_period import (
    InvoiceLineCreateManyBodyLinesItemPeriod,
    _SerializerInvoiceLineCreateManyBodyLinesItemPeriod,
)
from .invoice_line_create_many_body_lines_item_price_data import (
    InvoiceLineCreateManyBodyLinesItemPriceData,
    _SerializerInvoiceLineCreateManyBodyLinesItemPriceData,
)
from .invoice_line_create_many_body_lines_item_pricing import (
    InvoiceLineCreateManyBodyLinesItemPricing,
    _SerializerInvoiceLineCreateManyBodyLinesItemPricing,
)
from .invoice_line_create_many_body_lines_item_tax_amounts_arr0_item import (
    InvoiceLineCreateManyBodyLinesItemTaxAmountsArr0Item,
    _SerializerInvoiceLineCreateManyBodyLinesItemTaxAmountsArr0Item,
)


class InvoiceLineCreateManyBodyLinesItem(typing_extensions.TypedDict):
    """
    InvoiceLineCreateManyBodyLinesItem
    """

    amount: typing_extensions.NotRequired[int]

    description: typing_extensions.NotRequired[str]

    discountable: typing_extensions.NotRequired[bool]

    discounts: typing_extensions.NotRequired[
        typing.Union[
            typing.List[InvoiceLineCreateManyBodyLinesItemDiscountsArr0Item], str
        ]
    ]

    invoice_item: typing_extensions.NotRequired[str]

    metadata: typing_extensions.NotRequired[
        typing.Union[InvoiceLineCreateManyBodyLinesItemMetadataObj0, str]
    ]

    period: typing_extensions.NotRequired[InvoiceLineCreateManyBodyLinesItemPeriod]

    price_data: typing_extensions.NotRequired[
        InvoiceLineCreateManyBodyLinesItemPriceData
    ]

    pricing: typing_extensions.NotRequired[InvoiceLineCreateManyBodyLinesItemPricing]

    quantity: typing_extensions.NotRequired[int]

    tax_amounts: typing_extensions.NotRequired[
        typing.Union[
            typing.List[InvoiceLineCreateManyBodyLinesItemTaxAmountsArr0Item], str
        ]
    ]

    tax_rates: typing_extensions.NotRequired[typing.Union[typing.List[str], str]]


class _SerializerInvoiceLineCreateManyBodyLinesItem(pydantic.BaseModel):
    """
    Serializer for InvoiceLineCreateManyBodyLinesItem handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    amount: typing.Optional[int] = pydantic.Field(alias="amount", default=None)
    description: typing.Optional[str] = pydantic.Field(
        alias="description", default=None
    )
    discountable: typing.Optional[bool] = pydantic.Field(
        alias="discountable", default=None
    )
    discounts: typing.Optional[
        typing.Union[
            typing.List[_SerializerInvoiceLineCreateManyBodyLinesItemDiscountsArr0Item],
            str,
        ]
    ] = pydantic.Field(alias="discounts", default=None)
    invoice_item: typing.Optional[str] = pydantic.Field(
        alias="invoice_item", default=None
    )
    metadata: typing.Optional[
        typing.Union[_SerializerInvoiceLineCreateManyBodyLinesItemMetadataObj0, str]
    ] = pydantic.Field(alias="metadata", default=None)
    period: typing.Optional[_SerializerInvoiceLineCreateManyBodyLinesItemPeriod] = (
        pydantic.Field(alias="period", default=None)
    )
    price_data: typing.Optional[
        _SerializerInvoiceLineCreateManyBodyLinesItemPriceData
    ] = pydantic.Field(alias="price_data", default=None)
    pricing: typing.Optional[_SerializerInvoiceLineCreateManyBodyLinesItemPricing] = (
        pydantic.Field(alias="pricing", default=None)
    )
    quantity: typing.Optional[int] = pydantic.Field(alias="quantity", default=None)
    tax_amounts: typing.Optional[
        typing.Union[
            typing.List[
                _SerializerInvoiceLineCreateManyBodyLinesItemTaxAmountsArr0Item
            ],
            str,
        ]
    ] = pydantic.Field(alias="tax_amounts", default=None)
    tax_rates: typing.Optional[typing.Union[typing.List[str], str]] = pydantic.Field(
        alias="tax_rates", default=None
    )
