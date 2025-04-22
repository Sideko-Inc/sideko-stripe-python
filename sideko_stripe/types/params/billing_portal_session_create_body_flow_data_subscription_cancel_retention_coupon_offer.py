import pydantic
import typing_extensions


class BillingPortalSessionCreateBodyFlowDataSubscriptionCancelRetentionCouponOffer(
    typing_extensions.TypedDict
):
    """
    BillingPortalSessionCreateBodyFlowDataSubscriptionCancelRetentionCouponOffer
    """

    coupon: typing_extensions.Required[str]


class _SerializerBillingPortalSessionCreateBodyFlowDataSubscriptionCancelRetentionCouponOffer(
    pydantic.BaseModel
):
    """
    Serializer for BillingPortalSessionCreateBodyFlowDataSubscriptionCancelRetentionCouponOffer handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    coupon: str = pydantic.Field(
        alias="coupon",
    )
