import pydantic
import typing
import typing_extensions

from .checkout_session_create_body_line_items_item_price_data_product_data import (
    CheckoutSessionCreateBodyLineItemsItemPriceDataProductData,
    _SerializerCheckoutSessionCreateBodyLineItemsItemPriceDataProductData,
)
from .checkout_session_create_body_line_items_item_price_data_recurring import (
    CheckoutSessionCreateBodyLineItemsItemPriceDataRecurring,
    _SerializerCheckoutSessionCreateBodyLineItemsItemPriceDataRecurring,
)


class CheckoutSessionCreateBodyLineItemsItemPriceData(typing_extensions.TypedDict):
    """
    CheckoutSessionCreateBodyLineItemsItemPriceData
    """

    currency: typing_extensions.Required[str]

    product: typing_extensions.NotRequired[str]

    product_data: typing_extensions.NotRequired[
        CheckoutSessionCreateBodyLineItemsItemPriceDataProductData
    ]

    recurring: typing_extensions.NotRequired[
        CheckoutSessionCreateBodyLineItemsItemPriceDataRecurring
    ]

    tax_behavior: typing_extensions.NotRequired[
        typing_extensions.Literal["exclusive", "inclusive", "unspecified"]
    ]

    unit_amount: typing_extensions.NotRequired[int]

    unit_amount_decimal: typing_extensions.NotRequired[str]


class _SerializerCheckoutSessionCreateBodyLineItemsItemPriceData(pydantic.BaseModel):
    """
    Serializer for CheckoutSessionCreateBodyLineItemsItemPriceData handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    currency: str = pydantic.Field(
        alias="currency",
    )
    product: typing.Optional[str] = pydantic.Field(alias="product", default=None)
    product_data: typing.Optional[
        _SerializerCheckoutSessionCreateBodyLineItemsItemPriceDataProductData
    ] = pydantic.Field(alias="product_data", default=None)
    recurring: typing.Optional[
        _SerializerCheckoutSessionCreateBodyLineItemsItemPriceDataRecurring
    ] = pydantic.Field(alias="recurring", default=None)
    tax_behavior: typing.Optional[
        typing_extensions.Literal["exclusive", "inclusive", "unspecified"]
    ] = pydantic.Field(alias="tax_behavior", default=None)
    unit_amount: typing.Optional[int] = pydantic.Field(
        alias="unit_amount", default=None
    )
    unit_amount_decimal: typing.Optional[str] = pydantic.Field(
        alias="unit_amount_decimal", default=None
    )
