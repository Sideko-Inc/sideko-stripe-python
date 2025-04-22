import pydantic
import typing
import typing_extensions


class SubscriptionScheduleCreateBodyPhasesItemAddInvoiceItemsItemDiscountsItem(
    typing_extensions.TypedDict
):
    """
    SubscriptionScheduleCreateBodyPhasesItemAddInvoiceItemsItemDiscountsItem
    """

    coupon: typing_extensions.NotRequired[str]

    discount: typing_extensions.NotRequired[str]

    promotion_code: typing_extensions.NotRequired[str]


class _SerializerSubscriptionScheduleCreateBodyPhasesItemAddInvoiceItemsItemDiscountsItem(
    pydantic.BaseModel
):
    """
    Serializer for SubscriptionScheduleCreateBodyPhasesItemAddInvoiceItemsItemDiscountsItem handling case conversions
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
