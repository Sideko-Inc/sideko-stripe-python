import pydantic
import typing
import typing_extensions

from .customer_subscription_create_body_items_item_discounts_arr0_item import (
    CustomerSubscriptionCreateBodyItemsItemDiscountsArr0Item,
    _SerializerCustomerSubscriptionCreateBodyItemsItemDiscountsArr0Item,
)
from .customer_subscription_create_body_items_item_metadata import (
    CustomerSubscriptionCreateBodyItemsItemMetadata,
    _SerializerCustomerSubscriptionCreateBodyItemsItemMetadata,
)
from .customer_subscription_create_body_items_item_price_data import (
    CustomerSubscriptionCreateBodyItemsItemPriceData,
    _SerializerCustomerSubscriptionCreateBodyItemsItemPriceData,
)


class CustomerSubscriptionCreateBodyItemsItem(typing_extensions.TypedDict):
    """
    CustomerSubscriptionCreateBodyItemsItem
    """

    discounts: typing_extensions.NotRequired[
        typing.Union[
            typing.List[CustomerSubscriptionCreateBodyItemsItemDiscountsArr0Item], str
        ]
    ]

    metadata: typing_extensions.NotRequired[
        CustomerSubscriptionCreateBodyItemsItemMetadata
    ]

    price: typing_extensions.NotRequired[str]

    price_data: typing_extensions.NotRequired[
        CustomerSubscriptionCreateBodyItemsItemPriceData
    ]

    quantity: typing_extensions.NotRequired[int]

    tax_rates: typing_extensions.NotRequired[typing.Union[typing.List[str], str]]


class _SerializerCustomerSubscriptionCreateBodyItemsItem(pydantic.BaseModel):
    """
    Serializer for CustomerSubscriptionCreateBodyItemsItem handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    discounts: typing.Optional[
        typing.Union[
            typing.List[
                _SerializerCustomerSubscriptionCreateBodyItemsItemDiscountsArr0Item
            ],
            str,
        ]
    ] = pydantic.Field(alias="discounts", default=None)
    metadata: typing.Optional[
        _SerializerCustomerSubscriptionCreateBodyItemsItemMetadata
    ] = pydantic.Field(alias="metadata", default=None)
    price: typing.Optional[str] = pydantic.Field(alias="price", default=None)
    price_data: typing.Optional[
        _SerializerCustomerSubscriptionCreateBodyItemsItemPriceData
    ] = pydantic.Field(alias="price_data", default=None)
    quantity: typing.Optional[int] = pydantic.Field(alias="quantity", default=None)
    tax_rates: typing.Optional[typing.Union[typing.List[str], str]] = pydantic.Field(
        alias="tax_rates", default=None
    )
