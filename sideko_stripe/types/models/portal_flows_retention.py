import pydantic
import typing
import typing_extensions

from .portal_flows_coupon_offer import PortalFlowsCouponOffer


class PortalFlowsRetention(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    coupon_offer: typing.Optional[PortalFlowsCouponOffer] = pydantic.Field(
        alias="coupon_offer", default=None
    )
    type_: typing_extensions.Literal["coupon_offer"] = pydantic.Field(
        alias="type",
    )
    """
    Type of retention strategy that will be used.
    """
