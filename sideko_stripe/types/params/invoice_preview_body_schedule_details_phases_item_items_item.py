import pydantic
import typing
import typing_extensions

from .invoice_preview_body_schedule_details_phases_item_items_item_discounts_arr0_item import (
    InvoicePreviewBodyScheduleDetailsPhasesItemItemsItemDiscountsArr0Item,
    _SerializerInvoicePreviewBodyScheduleDetailsPhasesItemItemsItemDiscountsArr0Item,
)
from .invoice_preview_body_schedule_details_phases_item_items_item_metadata import (
    InvoicePreviewBodyScheduleDetailsPhasesItemItemsItemMetadata,
    _SerializerInvoicePreviewBodyScheduleDetailsPhasesItemItemsItemMetadata,
)
from .invoice_preview_body_schedule_details_phases_item_items_item_price_data import (
    InvoicePreviewBodyScheduleDetailsPhasesItemItemsItemPriceData,
    _SerializerInvoicePreviewBodyScheduleDetailsPhasesItemItemsItemPriceData,
)


class InvoicePreviewBodyScheduleDetailsPhasesItemItemsItem(typing_extensions.TypedDict):
    """
    InvoicePreviewBodyScheduleDetailsPhasesItemItemsItem
    """

    discounts: typing_extensions.NotRequired[
        typing.Union[
            typing.List[
                InvoicePreviewBodyScheduleDetailsPhasesItemItemsItemDiscountsArr0Item
            ],
            str,
        ]
    ]

    metadata: typing_extensions.NotRequired[
        InvoicePreviewBodyScheduleDetailsPhasesItemItemsItemMetadata
    ]

    price: typing_extensions.NotRequired[str]

    price_data: typing_extensions.NotRequired[
        InvoicePreviewBodyScheduleDetailsPhasesItemItemsItemPriceData
    ]

    quantity: typing_extensions.NotRequired[int]

    tax_rates: typing_extensions.NotRequired[typing.Union[typing.List[str], str]]


class _SerializerInvoicePreviewBodyScheduleDetailsPhasesItemItemsItem(
    pydantic.BaseModel
):
    """
    Serializer for InvoicePreviewBodyScheduleDetailsPhasesItemItemsItem handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    discounts: typing.Optional[
        typing.Union[
            typing.List[
                _SerializerInvoicePreviewBodyScheduleDetailsPhasesItemItemsItemDiscountsArr0Item
            ],
            str,
        ]
    ] = pydantic.Field(alias="discounts", default=None)
    metadata: typing.Optional[
        _SerializerInvoicePreviewBodyScheduleDetailsPhasesItemItemsItemMetadata
    ] = pydantic.Field(alias="metadata", default=None)
    price: typing.Optional[str] = pydantic.Field(alias="price", default=None)
    price_data: typing.Optional[
        _SerializerInvoicePreviewBodyScheduleDetailsPhasesItemItemsItemPriceData
    ] = pydantic.Field(alias="price_data", default=None)
    quantity: typing.Optional[int] = pydantic.Field(alias="quantity", default=None)
    tax_rates: typing.Optional[typing.Union[typing.List[str], str]] = pydantic.Field(
        alias="tax_rates", default=None
    )
