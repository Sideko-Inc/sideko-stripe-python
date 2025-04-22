import pydantic
import typing
import typing_extensions

from .subscription_schedule_create_body_phases_item_items_item_price_data_recurring import (
    SubscriptionScheduleCreateBodyPhasesItemItemsItemPriceDataRecurring,
    _SerializerSubscriptionScheduleCreateBodyPhasesItemItemsItemPriceDataRecurring,
)


class SubscriptionScheduleCreateBodyPhasesItemItemsItemPriceData(
    typing_extensions.TypedDict
):
    """
    SubscriptionScheduleCreateBodyPhasesItemItemsItemPriceData
    """

    currency: typing_extensions.Required[str]

    product: typing_extensions.Required[str]

    recurring: typing_extensions.Required[
        SubscriptionScheduleCreateBodyPhasesItemItemsItemPriceDataRecurring
    ]

    tax_behavior: typing_extensions.NotRequired[
        typing_extensions.Literal["exclusive", "inclusive", "unspecified"]
    ]

    unit_amount: typing_extensions.NotRequired[int]

    unit_amount_decimal: typing_extensions.NotRequired[str]


class _SerializerSubscriptionScheduleCreateBodyPhasesItemItemsItemPriceData(
    pydantic.BaseModel
):
    """
    Serializer for SubscriptionScheduleCreateBodyPhasesItemItemsItemPriceData handling case conversions
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
    recurring: _SerializerSubscriptionScheduleCreateBodyPhasesItemItemsItemPriceDataRecurring = pydantic.Field(
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
