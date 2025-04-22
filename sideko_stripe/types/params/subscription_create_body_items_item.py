import pydantic
import typing
import typing_extensions

from .subscription_create_body_items_item_discounts_arr0_item import (
    SubscriptionCreateBodyItemsItemDiscountsArr0Item,
    _SerializerSubscriptionCreateBodyItemsItemDiscountsArr0Item,
)
from .subscription_create_body_items_item_metadata import (
    SubscriptionCreateBodyItemsItemMetadata,
    _SerializerSubscriptionCreateBodyItemsItemMetadata,
)
from .subscription_create_body_items_item_price_data import (
    SubscriptionCreateBodyItemsItemPriceData,
    _SerializerSubscriptionCreateBodyItemsItemPriceData,
)


class SubscriptionCreateBodyItemsItem(typing_extensions.TypedDict):
    """
    SubscriptionCreateBodyItemsItem
    """

    discounts: typing_extensions.NotRequired[
        typing.Union[typing.List[SubscriptionCreateBodyItemsItemDiscountsArr0Item], str]
    ]

    metadata: typing_extensions.NotRequired[SubscriptionCreateBodyItemsItemMetadata]

    price: typing_extensions.NotRequired[str]

    price_data: typing_extensions.NotRequired[SubscriptionCreateBodyItemsItemPriceData]

    quantity: typing_extensions.NotRequired[int]

    tax_rates: typing_extensions.NotRequired[typing.Union[typing.List[str], str]]


class _SerializerSubscriptionCreateBodyItemsItem(pydantic.BaseModel):
    """
    Serializer for SubscriptionCreateBodyItemsItem handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    discounts: typing.Optional[
        typing.Union[
            typing.List[_SerializerSubscriptionCreateBodyItemsItemDiscountsArr0Item],
            str,
        ]
    ] = pydantic.Field(alias="discounts", default=None)
    metadata: typing.Optional[_SerializerSubscriptionCreateBodyItemsItemMetadata] = (
        pydantic.Field(alias="metadata", default=None)
    )
    price: typing.Optional[str] = pydantic.Field(alias="price", default=None)
    price_data: typing.Optional[_SerializerSubscriptionCreateBodyItemsItemPriceData] = (
        pydantic.Field(alias="price_data", default=None)
    )
    quantity: typing.Optional[int] = pydantic.Field(alias="quantity", default=None)
    tax_rates: typing.Optional[typing.Union[typing.List[str], str]] = pydantic.Field(
        alias="tax_rates", default=None
    )
