import pydantic


class PortalFlowsCouponOffer(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    coupon: str = pydantic.Field(
        alias="coupon",
    )
    """
    The ID of the coupon to be offered.
    """
