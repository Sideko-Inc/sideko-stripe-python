import pydantic
import typing
import typing_extensions

from .subscription_schedule_update_body_phases_item_items_item_discounts_arr0_item import (
    SubscriptionScheduleUpdateBodyPhasesItemItemsItemDiscountsArr0Item,
    _SerializerSubscriptionScheduleUpdateBodyPhasesItemItemsItemDiscountsArr0Item,
)
from .subscription_schedule_update_body_phases_item_items_item_metadata import (
    SubscriptionScheduleUpdateBodyPhasesItemItemsItemMetadata,
    _SerializerSubscriptionScheduleUpdateBodyPhasesItemItemsItemMetadata,
)
from .subscription_schedule_update_body_phases_item_items_item_price_data import (
    SubscriptionScheduleUpdateBodyPhasesItemItemsItemPriceData,
    _SerializerSubscriptionScheduleUpdateBodyPhasesItemItemsItemPriceData,
)


class SubscriptionScheduleUpdateBodyPhasesItemItemsItem(typing_extensions.TypedDict):
    """
    SubscriptionScheduleUpdateBodyPhasesItemItemsItem
    """

    discounts: typing_extensions.NotRequired[
        typing.Union[
            typing.List[
                SubscriptionScheduleUpdateBodyPhasesItemItemsItemDiscountsArr0Item
            ],
            str,
        ]
    ]

    metadata: typing_extensions.NotRequired[
        SubscriptionScheduleUpdateBodyPhasesItemItemsItemMetadata
    ]

    price: typing_extensions.NotRequired[str]

    price_data: typing_extensions.NotRequired[
        SubscriptionScheduleUpdateBodyPhasesItemItemsItemPriceData
    ]

    quantity: typing_extensions.NotRequired[int]

    tax_rates: typing_extensions.NotRequired[typing.Union[typing.List[str], str]]


class _SerializerSubscriptionScheduleUpdateBodyPhasesItemItemsItem(pydantic.BaseModel):
    """
    Serializer for SubscriptionScheduleUpdateBodyPhasesItemItemsItem handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    discounts: typing.Optional[
        typing.Union[
            typing.List[
                _SerializerSubscriptionScheduleUpdateBodyPhasesItemItemsItemDiscountsArr0Item
            ],
            str,
        ]
    ] = pydantic.Field(alias="discounts", default=None)
    metadata: typing.Optional[
        _SerializerSubscriptionScheduleUpdateBodyPhasesItemItemsItemMetadata
    ] = pydantic.Field(alias="metadata", default=None)
    price: typing.Optional[str] = pydantic.Field(alias="price", default=None)
    price_data: typing.Optional[
        _SerializerSubscriptionScheduleUpdateBodyPhasesItemItemsItemPriceData
    ] = pydantic.Field(alias="price_data", default=None)
    quantity: typing.Optional[int] = pydantic.Field(alias="quantity", default=None)
    tax_rates: typing.Optional[typing.Union[typing.List[str], str]] = pydantic.Field(
        alias="tax_rates", default=None
    )
