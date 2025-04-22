import pydantic
import typing
import typing_extensions

from .subscription_schedule_create_body_phases_item_items_item_discounts_arr0_item import (
    SubscriptionScheduleCreateBodyPhasesItemItemsItemDiscountsArr0Item,
    _SerializerSubscriptionScheduleCreateBodyPhasesItemItemsItemDiscountsArr0Item,
)
from .subscription_schedule_create_body_phases_item_items_item_metadata import (
    SubscriptionScheduleCreateBodyPhasesItemItemsItemMetadata,
    _SerializerSubscriptionScheduleCreateBodyPhasesItemItemsItemMetadata,
)
from .subscription_schedule_create_body_phases_item_items_item_price_data import (
    SubscriptionScheduleCreateBodyPhasesItemItemsItemPriceData,
    _SerializerSubscriptionScheduleCreateBodyPhasesItemItemsItemPriceData,
)


class SubscriptionScheduleCreateBodyPhasesItemItemsItem(typing_extensions.TypedDict):
    """
    SubscriptionScheduleCreateBodyPhasesItemItemsItem
    """

    discounts: typing_extensions.NotRequired[
        typing.Union[
            typing.List[
                SubscriptionScheduleCreateBodyPhasesItemItemsItemDiscountsArr0Item
            ],
            str,
        ]
    ]

    metadata: typing_extensions.NotRequired[
        SubscriptionScheduleCreateBodyPhasesItemItemsItemMetadata
    ]

    price: typing_extensions.NotRequired[str]

    price_data: typing_extensions.NotRequired[
        SubscriptionScheduleCreateBodyPhasesItemItemsItemPriceData
    ]

    quantity: typing_extensions.NotRequired[int]

    tax_rates: typing_extensions.NotRequired[typing.Union[typing.List[str], str]]


class _SerializerSubscriptionScheduleCreateBodyPhasesItemItemsItem(pydantic.BaseModel):
    """
    Serializer for SubscriptionScheduleCreateBodyPhasesItemItemsItem handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    discounts: typing.Optional[
        typing.Union[
            typing.List[
                _SerializerSubscriptionScheduleCreateBodyPhasesItemItemsItemDiscountsArr0Item
            ],
            str,
        ]
    ] = pydantic.Field(alias="discounts", default=None)
    metadata: typing.Optional[
        _SerializerSubscriptionScheduleCreateBodyPhasesItemItemsItemMetadata
    ] = pydantic.Field(alias="metadata", default=None)
    price: typing.Optional[str] = pydantic.Field(alias="price", default=None)
    price_data: typing.Optional[
        _SerializerSubscriptionScheduleCreateBodyPhasesItemItemsItemPriceData
    ] = pydantic.Field(alias="price_data", default=None)
    quantity: typing.Optional[int] = pydantic.Field(alias="quantity", default=None)
    tax_rates: typing.Optional[typing.Union[typing.List[str], str]] = pydantic.Field(
        alias="tax_rates", default=None
    )
