import pydantic
import typing
import typing_extensions

from .subscription_schedule_create_body_phases_item_add_invoice_items_item_discounts_item import (
    SubscriptionScheduleCreateBodyPhasesItemAddInvoiceItemsItemDiscountsItem,
    _SerializerSubscriptionScheduleCreateBodyPhasesItemAddInvoiceItemsItemDiscountsItem,
)
from .subscription_schedule_create_body_phases_item_add_invoice_items_item_price_data import (
    SubscriptionScheduleCreateBodyPhasesItemAddInvoiceItemsItemPriceData,
    _SerializerSubscriptionScheduleCreateBodyPhasesItemAddInvoiceItemsItemPriceData,
)


class SubscriptionScheduleCreateBodyPhasesItemAddInvoiceItemsItem(
    typing_extensions.TypedDict
):
    """
    SubscriptionScheduleCreateBodyPhasesItemAddInvoiceItemsItem
    """

    discounts: typing_extensions.NotRequired[
        typing.List[
            SubscriptionScheduleCreateBodyPhasesItemAddInvoiceItemsItemDiscountsItem
        ]
    ]

    price: typing_extensions.NotRequired[str]

    price_data: typing_extensions.NotRequired[
        SubscriptionScheduleCreateBodyPhasesItemAddInvoiceItemsItemPriceData
    ]

    quantity: typing_extensions.NotRequired[int]

    tax_rates: typing_extensions.NotRequired[typing.Union[typing.List[str], str]]


class _SerializerSubscriptionScheduleCreateBodyPhasesItemAddInvoiceItemsItem(
    pydantic.BaseModel
):
    """
    Serializer for SubscriptionScheduleCreateBodyPhasesItemAddInvoiceItemsItem handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    discounts: typing.Optional[
        typing.List[
            _SerializerSubscriptionScheduleCreateBodyPhasesItemAddInvoiceItemsItemDiscountsItem
        ]
    ] = pydantic.Field(alias="discounts", default=None)
    price: typing.Optional[str] = pydantic.Field(alias="price", default=None)
    price_data: typing.Optional[
        _SerializerSubscriptionScheduleCreateBodyPhasesItemAddInvoiceItemsItemPriceData
    ] = pydantic.Field(alias="price_data", default=None)
    quantity: typing.Optional[int] = pydantic.Field(alias="quantity", default=None)
    tax_rates: typing.Optional[typing.Union[typing.List[str], str]] = pydantic.Field(
        alias="tax_rates", default=None
    )
