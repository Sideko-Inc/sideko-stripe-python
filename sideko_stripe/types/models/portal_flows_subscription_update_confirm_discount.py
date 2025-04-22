import pydantic
import typing


class PortalFlowsSubscriptionUpdateConfirmDiscount(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    coupon: typing.Optional[str] = pydantic.Field(alias="coupon", default=None)
    """
    The ID of the coupon to apply to this subscription update.
    """
    promotion_code: typing.Optional[str] = pydantic.Field(
        alias="promotion_code", default=None
    )
    """
    The ID of a promotion code to apply to this subscription update.
    """
