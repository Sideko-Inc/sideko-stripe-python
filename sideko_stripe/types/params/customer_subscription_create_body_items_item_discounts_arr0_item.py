import pydantic
import typing
import typing_extensions


class CustomerSubscriptionCreateBodyItemsItemDiscountsArr0Item(
    typing_extensions.TypedDict
):
    """
    CustomerSubscriptionCreateBodyItemsItemDiscountsArr0Item
    """

    coupon: typing_extensions.NotRequired[str]

    discount: typing_extensions.NotRequired[str]

    promotion_code: typing_extensions.NotRequired[str]


class _SerializerCustomerSubscriptionCreateBodyItemsItemDiscountsArr0Item(
    pydantic.BaseModel
):
    """
    Serializer for CustomerSubscriptionCreateBodyItemsItemDiscountsArr0Item handling case conversions
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
