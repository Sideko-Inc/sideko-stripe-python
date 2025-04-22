import pydantic
import typing
import typing_extensions

from .invoice_preview_body_schedule_details_phases_item_items_item_price_data_recurring import (
    InvoicePreviewBodyScheduleDetailsPhasesItemItemsItemPriceDataRecurring,
    _SerializerInvoicePreviewBodyScheduleDetailsPhasesItemItemsItemPriceDataRecurring,
)


class InvoicePreviewBodyScheduleDetailsPhasesItemItemsItemPriceData(
    typing_extensions.TypedDict
):
    """
    InvoicePreviewBodyScheduleDetailsPhasesItemItemsItemPriceData
    """

    currency: typing_extensions.Required[str]

    product: typing_extensions.Required[str]

    recurring: typing_extensions.Required[
        InvoicePreviewBodyScheduleDetailsPhasesItemItemsItemPriceDataRecurring
    ]

    tax_behavior: typing_extensions.NotRequired[
        typing_extensions.Literal["exclusive", "inclusive", "unspecified"]
    ]

    unit_amount: typing_extensions.NotRequired[int]

    unit_amount_decimal: typing_extensions.NotRequired[str]


class _SerializerInvoicePreviewBodyScheduleDetailsPhasesItemItemsItemPriceData(
    pydantic.BaseModel
):
    """
    Serializer for InvoicePreviewBodyScheduleDetailsPhasesItemItemsItemPriceData handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    currency: str = pydantic.Field(
        alias="currency",
    )
    product: str = pydantic.Field(
        alias="product",
    )
    recurring: _SerializerInvoicePreviewBodyScheduleDetailsPhasesItemItemsItemPriceDataRecurring = pydantic.Field(
        alias="recurring",
    )
    tax_behavior: typing.Optional[
        typing_extensions.Literal["exclusive", "inclusive", "unspecified"]
    ] = pydantic.Field(alias="tax_behavior", default=None)
    unit_amount: typing.Optional[int] = pydantic.Field(
        alias="unit_amount", default=None
    )
    unit_amount_decimal: typing.Optional[str] = pydantic.Field(
        alias="unit_amount_decimal", default=None
    )
