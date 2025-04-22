import pydantic
import typing
import typing_extensions


class SubscriptionScheduleCreateBodyPhasesItemDiscountsArr0Item(
    typing_extensions.TypedDict
):
    """
    SubscriptionScheduleCreateBodyPhasesItemDiscountsArr0Item
    """

    coupon: typing_extensions.NotRequired[str]

    discount: typing_extensions.NotRequired[str]

    promotion_code: typing_extensions.NotRequired[str]


class _SerializerSubscriptionScheduleCreateBodyPhasesItemDiscountsArr0Item(
    pydantic.BaseModel
):
    """
    Serializer for SubscriptionScheduleCreateBodyPhasesItemDiscountsArr0Item handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    coupon: typing.Optional[str] = pydantic.Field(alias="coupon", default=None)
    discount: typing.Optional[str] = pydantic.Field(alias="discount", default=None)
    promotion_code: typing.Optional[str] = pydantic.Field(
        alias="promotion_code", default=None
    )
