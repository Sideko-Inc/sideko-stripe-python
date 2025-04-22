import pydantic
import typing
import typing_extensions


class CouponCreateBodyAppliesTo(typing_extensions.TypedDict):
    """
    A hash containing directions for what this Coupon will apply discounts to.
    """

    products: typing_extensions.NotRequired[typing.List[str]]


class _SerializerCouponCreateBodyAppliesTo(pydantic.BaseModel):
    """
    Serializer for CouponCreateBodyAppliesTo handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    products: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="products", default=None
    )
