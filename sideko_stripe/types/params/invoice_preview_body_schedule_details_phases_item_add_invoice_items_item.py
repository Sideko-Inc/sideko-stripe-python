import pydantic
import typing
import typing_extensions

from .invoice_preview_body_schedule_details_phases_item_add_invoice_items_item_discounts_item import (
    InvoicePreviewBodyScheduleDetailsPhasesItemAddInvoiceItemsItemDiscountsItem,
    _SerializerInvoicePreviewBodyScheduleDetailsPhasesItemAddInvoiceItemsItemDiscountsItem,
)
from .invoice_preview_body_schedule_details_phases_item_add_invoice_items_item_price_data import (
    InvoicePreviewBodyScheduleDetailsPhasesItemAddInvoiceItemsItemPriceData,
    _SerializerInvoicePreviewBodyScheduleDetailsPhasesItemAddInvoiceItemsItemPriceData,
)


class InvoicePreviewBodyScheduleDetailsPhasesItemAddInvoiceItemsItem(
    typing_extensions.TypedDict
):
    """
    InvoicePreviewBodyScheduleDetailsPhasesItemAddInvoiceItemsItem
    """

    discounts: typing_extensions.NotRequired[
        typing.List[
            InvoicePreviewBodyScheduleDetailsPhasesItemAddInvoiceItemsItemDiscountsItem
        ]
    ]

    price: typing_extensions.NotRequired[str]

    price_data: typing_extensions.NotRequired[
        InvoicePreviewBodyScheduleDetailsPhasesItemAddInvoiceItemsItemPriceData
    ]

    quantity: typing_extensions.NotRequired[int]

    tax_rates: typing_extensions.NotRequired[typing.Union[typing.List[str], str]]


class _SerializerInvoicePreviewBodyScheduleDetailsPhasesItemAddInvoiceItemsItem(
    pydantic.BaseModel
):
    """
    Serializer for InvoicePreviewBodyScheduleDetailsPhasesItemAddInvoiceItemsItem handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    discounts: typing.Optional[
        typing.List[
            _SerializerInvoicePreviewBodyScheduleDetailsPhasesItemAddInvoiceItemsItemDiscountsItem
        ]
    ] = pydantic.Field(alias="discounts", default=None)
    price: typing.Optional[str] = pydantic.Field(alias="price", default=None)
    price_data: typing.Optional[
        _SerializerInvoicePreviewBodyScheduleDetailsPhasesItemAddInvoiceItemsItemPriceData
    ] = pydantic.Field(alias="price_data", default=None)
    quantity: typing.Optional[int] = pydantic.Field(alias="quantity", default=None)
    tax_rates: typing.Optional[typing.Union[typing.List[str], str]] = pydantic.Field(
        alias="tax_rates", default=None
    )
