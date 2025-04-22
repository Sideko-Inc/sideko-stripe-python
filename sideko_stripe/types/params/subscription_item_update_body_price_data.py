import pydantic
import typing
import typing_extensions

from .subscription_item_update_body_price_data_recurring import (
    SubscriptionItemUpdateBodyPriceDataRecurring,
    _SerializerSubscriptionItemUpdateBodyPriceDataRecurring,
)


class SubscriptionItemUpdateBodyPriceData(typing_extensions.TypedDict):
    """
    Data used to generate a new [Price](https://stripe.com/docs/api/prices) object inline. One of `price` or `price_data` is required.
    """

    currency: typing_extensions.Required[str]

    product: typing_extensions.Required[str]

    recurring: typing_extensions.Required[SubscriptionItemUpdateBodyPriceDataRecurring]

    tax_behavior: typing_extensions.NotRequired[
        typing_extensions.Literal["exclusive", "inclusive", "unspecified"]
    ]

    unit_amount: typing_extensions.NotRequired[int]

    unit_amount_decimal: typing_extensions.NotRequired[str]


class _SerializerSubscriptionItemUpdateBodyPriceData(pydantic.BaseModel):
    """
    Serializer for SubscriptionItemUpdateBodyPriceData handling case conversions
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
    recurring: _SerializerSubscriptionItemUpdateBodyPriceDataRecurring = pydantic.Field(
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
