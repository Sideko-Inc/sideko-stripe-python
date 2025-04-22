import pydantic
import typing
import typing_extensions


class CheckoutSessionCreateBodyDiscountsItem(typing_extensions.TypedDict):
    """
    CheckoutSessionCreateBodyDiscountsItem
    """

    coupon: typing_extensions.NotRequired[str]

    promotion_code: typing_extensions.NotRequired[str]


class _SerializerCheckoutSessionCreateBodyDiscountsItem(pydantic.BaseModel):
    """
    Serializer for CheckoutSessionCreateBodyDiscountsItem handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    coupon: typing.Optional[str] = pydantic.Field(alias="coupon", default=None)
    promotion_code: typing.Optional[str] = pydantic.Field(
        alias="promotion_code", default=None
    )
