import pydantic
import typing
import typing_extensions

from .invoice_line_update_many_body_lines_item_discounts_arr0_item import (
    InvoiceLineUpdateManyBodyLinesItemDiscountsArr0Item,
    _SerializerInvoiceLineUpdateManyBodyLinesItemDiscountsArr0Item,
)
from .invoice_line_update_many_body_lines_item_metadata_obj0 import (
    InvoiceLineUpdateManyBodyLinesItemMetadataObj0,
    _SerializerInvoiceLineUpdateManyBodyLinesItemMetadataObj0,
)
from .invoice_line_update_many_body_lines_item_period import (
    InvoiceLineUpdateManyBodyLinesItemPeriod,
    _SerializerInvoiceLineUpdateManyBodyLinesItemPeriod,
)
from .invoice_line_update_many_body_lines_item_price_data import (
    InvoiceLineUpdateManyBodyLinesItemPriceData,
    _SerializerInvoiceLineUpdateManyBodyLinesItemPriceData,
)
from .invoice_line_update_many_body_lines_item_pricing import (
    InvoiceLineUpdateManyBodyLinesItemPricing,
    _SerializerInvoiceLineUpdateManyBodyLinesItemPricing,
)
from .invoice_line_update_many_body_lines_item_tax_amounts_arr0_item import (
    InvoiceLineUpdateManyBodyLinesItemTaxAmountsArr0Item,
    _SerializerInvoiceLineUpdateManyBodyLinesItemTaxAmountsArr0Item,
)


class InvoiceLineUpdateManyBodyLinesItem(typing_extensions.TypedDict):
    """
    InvoiceLineUpdateManyBodyLinesItem
    """

    amount: typing_extensions.NotRequired[int]

    description: typing_extensions.NotRequired[str]

    discountable: typing_extensions.NotRequired[bool]

    discounts: typing_extensions.NotRequired[
        typing.Union[
            typing.List[InvoiceLineUpdateManyBodyLinesItemDiscountsArr0Item], str
        ]
    ]

    id: typing_extensions.Required[str]

    metadata: typing_extensions.NotRequired[
        typing.Union[InvoiceLineUpdateManyBodyLinesItemMetadataObj0, str]
    ]

    period: typing_extensions.NotRequired[InvoiceLineUpdateManyBodyLinesItemPeriod]

    price_data: typing_extensions.NotRequired[
        InvoiceLineUpdateManyBodyLinesItemPriceData
    ]

    pricing: typing_extensions.NotRequired[InvoiceLineUpdateManyBodyLinesItemPricing]

    quantity: typing_extensions.NotRequired[int]

    tax_amounts: typing_extensions.NotRequired[
        typing.Union[
            typing.List[InvoiceLineUpdateManyBodyLinesItemTaxAmountsArr0Item], str
        ]
    ]

    tax_rates: typing_extensions.NotRequired[typing.Union[typing.List[str], str]]


class _SerializerInvoiceLineUpdateManyBodyLinesItem(pydantic.BaseModel):
    """
    Serializer for InvoiceLineUpdateManyBodyLinesItem handling case conversions
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
            typing.List[_SerializerInvoiceLineUpdateManyBodyLinesItemDiscountsArr0Item],
            str,
        ]
    ] = pydantic.Field(alias="discounts", default=None)
    id: str = pydantic.Field(
        alias="id",
    )
    metadata: typing.Optional[
        typing.Union[_SerializerInvoiceLineUpdateManyBodyLinesItemMetadataObj0, str]
    ] = pydantic.Field(alias="metadata", default=None)
    period: typing.Optional[_SerializerInvoiceLineUpdateManyBodyLinesItemPeriod] = (
        pydantic.Field(alias="period", default=None)
    )
    price_data: typing.Optional[
        _SerializerInvoiceLineUpdateManyBodyLinesItemPriceData
    ] = pydantic.Field(alias="price_data", default=None)
    pricing: typing.Optional[_SerializerInvoiceLineUpdateManyBodyLinesItemPricing] = (
        pydantic.Field(alias="pricing", default=None)
    )
    quantity: typing.Optional[int] = pydantic.Field(alias="quantity", default=None)
    tax_amounts: typing.Optional[
        typing.Union[
            typing.List[
                _SerializerInvoiceLineUpdateManyBodyLinesItemTaxAmountsArr0Item
            ],
            str,
        ]
    ] = pydantic.Field(alias="tax_amounts", default=None)
    tax_rates: typing.Optional[typing.Union[typing.List[str], str]] = pydantic.Field(
        alias="tax_rates", default=None
    )
