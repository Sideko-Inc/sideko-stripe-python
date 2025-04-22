import pydantic
import typing
import typing_extensions

from .coupon import Coupon

if typing_extensions.TYPE_CHECKING:
    from .discount import Discount
    from .promotion_code import PromotionCode


class DiscountsResourceStackableDiscount(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    coupon: typing.Optional[typing.Union[str, Coupon]] = pydantic.Field(
        alias="coupon", default=None
    )
    """
    ID of the coupon to create a new discount for.
    """
    discount: typing.Optional[typing.Union[str, "Discount"]] = pydantic.Field(
        alias="discount", default=None
    )
    """
    ID of an existing discount on the object (or one of its ancestors) to reuse.
    """
    promotion_code: typing.Optional[typing.Union[str, "PromotionCode"]] = (
        pydantic.Field(alias="promotion_code", default=None)
    )
    """
    ID of the promotion code to create a new discount for.
    """
