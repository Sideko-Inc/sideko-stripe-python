import pydantic
import typing_extensions


if typing_extensions.TYPE_CHECKING:
    from .discount import Discount


class LineItemsDiscountAmount(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    amount: int = pydantic.Field(
        alias="amount",
    )
    """
    The amount discounted.
    """
    discount: "Discount" = pydantic.Field(
        alias="discount",
    )
    """
    A discount represents the actual application of a [coupon](https://stripe.com/docs/api#coupons) or [promotion code](https://stripe.com/docs/api#promotion_codes).
    It contains information about when the discount began, when it will end, and what it is applied to.
    
    Related guide: [Applying discounts to subscriptions](https://stripe.com/docs/billing/subscriptions/discounts)
    """
