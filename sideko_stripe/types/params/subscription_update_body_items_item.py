import pydantic
import typing
import typing_extensions

from .subscription_update_body_items_item_discounts_arr0_item import (
    SubscriptionUpdateBodyItemsItemDiscountsArr0Item,
    _SerializerSubscriptionUpdateBodyItemsItemDiscountsArr0Item,
)
from .subscription_update_body_items_item_metadata_obj0 import (
    SubscriptionUpdateBodyItemsItemMetadataObj0,
    _SerializerSubscriptionUpdateBodyItemsItemMetadataObj0,
)
from .subscription_update_body_items_item_price_data import (
    SubscriptionUpdateBodyItemsItemPriceData,
    _SerializerSubscriptionUpdateBodyItemsItemPriceData,
)


class SubscriptionUpdateBodyItemsItem(typing_extensions.TypedDict):
    """
    SubscriptionUpdateBodyItemsItem
    """

    clear_usage: typing_extensions.NotRequired[bool]

    deleted: typing_extensions.NotRequired[bool]

    discounts: typing_extensions.NotRequired[
        typing.Union[typing.List[SubscriptionUpdateBodyItemsItemDiscountsArr0Item], str]
    ]

    id: typing_extensions.NotRequired[str]

    metadata: typing_extensions.NotRequired[
        typing.Union[SubscriptionUpdateBodyItemsItemMetadataObj0, str]
    ]

    price: typing_extensions.NotRequired[str]

    price_data: typing_extensions.NotRequired[SubscriptionUpdateBodyItemsItemPriceData]

    quantity: typing_extensions.NotRequired[int]

    tax_rates: typing_extensions.NotRequired[typing.Union[typing.List[str], str]]


class _SerializerSubscriptionUpdateBodyItemsItem(pydantic.BaseModel):
    """
    Serializer for SubscriptionUpdateBodyItemsItem handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    clear_usage: typing.Optional[bool] = pydantic.Field(
        alias="clear_usage", default=None
    )
    deleted: typing.Optional[bool] = pydantic.Field(alias="deleted", default=None)
    discounts: typing.Optional[
        typing.Union[
            typing.List[_SerializerSubscriptionUpdateBodyItemsItemDiscountsArr0Item],
            str,
        ]
    ] = pydantic.Field(alias="discounts", default=None)
    id: typing.Optional[str] = pydantic.Field(alias="id", default=None)
    metadata: typing.Optional[
        typing.Union[_SerializerSubscriptionUpdateBodyItemsItemMetadataObj0, str]
    ] = pydantic.Field(alias="metadata", default=None)
    price: typing.Optional[str] = pydantic.Field(alias="price", default=None)
    price_data: typing.Optional[_SerializerSubscriptionUpdateBodyItemsItemPriceData] = (
        pydantic.Field(alias="price_data", default=None)
    )
    quantity: typing.Optional[int] = pydantic.Field(alias="quantity", default=None)
    tax_rates: typing.Optional[typing.Union[typing.List[str], str]] = pydantic.Field(
        alias="tax_rates", default=None
    )
