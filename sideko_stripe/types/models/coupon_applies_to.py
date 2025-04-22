import pydantic
import typing


class CouponAppliesTo(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    products: typing.List[str] = pydantic.Field(
        alias="products",
    )
    """
    A list of product IDs this coupon applies to
    """
