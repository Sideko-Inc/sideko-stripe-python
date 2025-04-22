import pydantic
import typing
import typing_extensions

from .subscription_schedule_update_body_phases_item_add_invoice_items_item_discounts_item import (
    SubscriptionScheduleUpdateBodyPhasesItemAddInvoiceItemsItemDiscountsItem,
    _SerializerSubscriptionScheduleUpdateBodyPhasesItemAddInvoiceItemsItemDiscountsItem,
)
from .subscription_schedule_update_body_phases_item_add_invoice_items_item_price_data import (
    SubscriptionScheduleUpdateBodyPhasesItemAddInvoiceItemsItemPriceData,
    _SerializerSubscriptionScheduleUpdateBodyPhasesItemAddInvoiceItemsItemPriceData,
)


class SubscriptionScheduleUpdateBodyPhasesItemAddInvoiceItemsItem(
    typing_extensions.TypedDict
):
    """
    SubscriptionScheduleUpdateBodyPhasesItemAddInvoiceItemsItem
    """

    discounts: typing_extensions.NotRequired[
        typing.List[
            SubscriptionScheduleUpdateBodyPhasesItemAddInvoiceItemsItemDiscountsItem
        ]
    ]

    price: typing_extensions.NotRequired[str]

    price_data: typing_extensions.NotRequired[
        SubscriptionScheduleUpdateBodyPhasesItemAddInvoiceItemsItemPriceData
    ]

    quantity: typing_extensions.NotRequired[int]

    tax_rates: typing_extensions.NotRequired[typing.Union[typing.List[str], str]]


class _SerializerSubscriptionScheduleUpdateBodyPhasesItemAddInvoiceItemsItem(
    pydantic.BaseModel
):
    """
    Serializer for SubscriptionScheduleUpdateBodyPhasesItemAddInvoiceItemsItem handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    discounts: typing.Optional[
        typing.List[
            _SerializerSubscriptionScheduleUpdateBodyPhasesItemAddInvoiceItemsItemDiscountsItem
        ]
    ] = pydantic.Field(alias="discounts", default=None)
    price: typing.Optional[str] = pydantic.Field(alias="price", default=None)
    price_data: typing.Optional[
        _SerializerSubscriptionScheduleUpdateBodyPhasesItemAddInvoiceItemsItemPriceData
    ] = pydantic.Field(alias="price_data", default=None)
    quantity: typing.Optional[int] = pydantic.Field(alias="quantity", default=None)
    tax_rates: typing.Optional[typing.Union[typing.List[str], str]] = pydantic.Field(
        alias="tax_rates", default=None
    )
