import pydantic
import typing
import typing_extensions

from .invoice_preview_body_invoice_items_item_discounts_arr0_item import (
    InvoicePreviewBodyInvoiceItemsItemDiscountsArr0Item,
    _SerializerInvoicePreviewBodyInvoiceItemsItemDiscountsArr0Item,
)
from .invoice_preview_body_invoice_items_item_metadata_obj0 import (
    InvoicePreviewBodyInvoiceItemsItemMetadataObj0,
    _SerializerInvoicePreviewBodyInvoiceItemsItemMetadataObj0,
)
from .invoice_preview_body_invoice_items_item_period import (
    InvoicePreviewBodyInvoiceItemsItemPeriod,
    _SerializerInvoicePreviewBodyInvoiceItemsItemPeriod,
)
from .invoice_preview_body_invoice_items_item_price_data import (
    InvoicePreviewBodyInvoiceItemsItemPriceData,
    _SerializerInvoicePreviewBodyInvoiceItemsItemPriceData,
)


class InvoicePreviewBodyInvoiceItemsItem(typing_extensions.TypedDict):
    """
    InvoicePreviewBodyInvoiceItemsItem
    """

    amount: typing_extensions.NotRequired[int]

    currency: typing_extensions.NotRequired[str]

    description: typing_extensions.NotRequired[str]

    discountable: typing_extensions.NotRequired[bool]

    discounts: typing_extensions.NotRequired[
        typing.Union[
            typing.List[InvoicePreviewBodyInvoiceItemsItemDiscountsArr0Item], str
        ]
    ]

    invoiceitem: typing_extensions.NotRequired[str]

    metadata: typing_extensions.NotRequired[
        typing.Union[InvoicePreviewBodyInvoiceItemsItemMetadataObj0, str]
    ]

    period: typing_extensions.NotRequired[InvoicePreviewBodyInvoiceItemsItemPeriod]

    price: typing_extensions.NotRequired[str]

    price_data: typing_extensions.NotRequired[
        InvoicePreviewBodyInvoiceItemsItemPriceData
    ]

    quantity: typing_extensions.NotRequired[int]

    tax_behavior: typing_extensions.NotRequired[
        typing_extensions.Literal["exclusive", "inclusive", "unspecified"]
    ]

    tax_code: typing_extensions.NotRequired[typing.Union[str, str]]

    tax_rates: typing_extensions.NotRequired[typing.Union[typing.List[str], str]]

    unit_amount: typing_extensions.NotRequired[int]

    unit_amount_decimal: typing_extensions.NotRequired[str]


class _SerializerInvoicePreviewBodyInvoiceItemsItem(pydantic.BaseModel):
    """
    Serializer for InvoicePreviewBodyInvoiceItemsItem handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    amount: typing.Optional[int] = pydantic.Field(alias="amount", default=None)
    currency: typing.Optional[str] = pydantic.Field(alias="currency", default=None)
    description: typing.Optional[str] = pydantic.Field(
        alias="description", default=None
    )
    discountable: typing.Optional[bool] = pydantic.Field(
        alias="discountable", default=None
    )
    discounts: typing.Optional[
        typing.Union[
            typing.List[_SerializerInvoicePreviewBodyInvoiceItemsItemDiscountsArr0Item],
            str,
        ]
    ] = pydantic.Field(alias="discounts", default=None)
    invoiceitem: typing.Optional[str] = pydantic.Field(
        alias="invoiceitem", default=None
    )
    metadata: typing.Optional[
        typing.Union[_SerializerInvoicePreviewBodyInvoiceItemsItemMetadataObj0, str]
    ] = pydantic.Field(alias="metadata", default=None)
    period: typing.Optional[_SerializerInvoicePreviewBodyInvoiceItemsItemPeriod] = (
        pydantic.Field(alias="period", default=None)
    )
    price: typing.Optional[str] = pydantic.Field(alias="price", default=None)
    price_data: typing.Optional[
        _SerializerInvoicePreviewBodyInvoiceItemsItemPriceData
    ] = pydantic.Field(alias="price_data", default=None)
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
    unit_amount: typing.Optional[int] = pydantic.Field(
        alias="unit_amount", default=None
    )
    unit_amount_decimal: typing.Optional[str] = pydantic.Field(
        alias="unit_amount_decimal", default=None
    )
