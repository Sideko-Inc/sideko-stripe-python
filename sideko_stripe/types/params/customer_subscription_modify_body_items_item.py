import pydantic
import typing
import typing_extensions

from .customer_subscription_modify_body_items_item_discounts_arr0_item import (
    CustomerSubscriptionModifyBodyItemsItemDiscountsArr0Item,
    _SerializerCustomerSubscriptionModifyBodyItemsItemDiscountsArr0Item,
)
from .customer_subscription_modify_body_items_item_metadata_obj0 import (
    CustomerSubscriptionModifyBodyItemsItemMetadataObj0,
    _SerializerCustomerSubscriptionModifyBodyItemsItemMetadataObj0,
)
from .customer_subscription_modify_body_items_item_price_data import (
    CustomerSubscriptionModifyBodyItemsItemPriceData,
    _SerializerCustomerSubscriptionModifyBodyItemsItemPriceData,
)


class CustomerSubscriptionModifyBodyItemsItem(typing_extensions.TypedDict):
    """
    CustomerSubscriptionModifyBodyItemsItem
    """

    clear_usage: typing_extensions.NotRequired[bool]

    deleted: typing_extensions.NotRequired[bool]

    discounts: typing_extensions.NotRequired[
        typing.Union[
            typing.List[CustomerSubscriptionModifyBodyItemsItemDiscountsArr0Item], str
        ]
    ]

    id: typing_extensions.NotRequired[str]

    metadata: typing_extensions.NotRequired[
        typing.Union[CustomerSubscriptionModifyBodyItemsItemMetadataObj0, str]
    ]

    price: typing_extensions.NotRequired[str]

    price_data: typing_extensions.NotRequired[
        CustomerSubscriptionModifyBodyItemsItemPriceData
    ]

    quantity: typing_extensions.NotRequired[int]

    tax_rates: typing_extensions.NotRequired[typing.Union[typing.List[str], str]]


class _SerializerCustomerSubscriptionModifyBodyItemsItem(pydantic.BaseModel):
    """
    Serializer for CustomerSubscriptionModifyBodyItemsItem handling case conversions
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
            typing.List[
                _SerializerCustomerSubscriptionModifyBodyItemsItemDiscountsArr0Item
            ],
            str,
        ]
    ] = pydantic.Field(alias="discounts", default=None)
    id: typing.Optional[str] = pydantic.Field(alias="id", default=None)
    metadata: typing.Optional[
        typing.Union[
            _SerializerCustomerSubscriptionModifyBodyItemsItemMetadataObj0, str
        ]
    ] = pydantic.Field(alias="metadata", default=None)
    price: typing.Optional[str] = pydantic.Field(alias="price", default=None)
    price_data: typing.Optional[
        _SerializerCustomerSubscriptionModifyBodyItemsItemPriceData
    ] = pydantic.Field(alias="price_data", default=None)
    quantity: typing.Optional[int] = pydantic.Field(alias="quantity", default=None)
    tax_rates: typing.Optional[typing.Union[typing.List[str], str]] = pydantic.Field(
        alias="tax_rates", default=None
    )
