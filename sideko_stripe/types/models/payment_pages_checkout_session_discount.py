import pydantic
import typing
import typing_extensions

from .coupon import Coupon

if typing_extensions.TYPE_CHECKING:
    from .promotion_code import PromotionCode


class PaymentPagesCheckoutSessionDiscount(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    coupon: typing.Optional[typing.Union[str, Coupon]] = pydantic.Field(
        alias="coupon", default=None
    )
    """
    Coupon attached to the Checkout Session.
    """
    promotion_code: typing.Optional[typing.Union[str, "PromotionCode"]] = (
        pydantic.Field(alias="promotion_code", default=None)
    )
    """
    Promotion code attached to the Checkout Session.
    """
