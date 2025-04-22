import pydantic
import typing_extensions

from .billing_portal_session_create_body_flow_data_subscription_cancel_retention_coupon_offer import (
    BillingPortalSessionCreateBodyFlowDataSubscriptionCancelRetentionCouponOffer,
    _SerializerBillingPortalSessionCreateBodyFlowDataSubscriptionCancelRetentionCouponOffer,
)


class BillingPortalSessionCreateBodyFlowDataSubscriptionCancelRetention(
    typing_extensions.TypedDict
):
    """
    BillingPortalSessionCreateBodyFlowDataSubscriptionCancelRetention
    """

    coupon_offer: typing_extensions.Required[
        BillingPortalSessionCreateBodyFlowDataSubscriptionCancelRetentionCouponOffer
    ]

    type_: typing_extensions.Required[typing_extensions.Literal["coupon_offer"]]


class _SerializerBillingPortalSessionCreateBodyFlowDataSubscriptionCancelRetention(
    pydantic.BaseModel
):
    """
    Serializer for BillingPortalSessionCreateBodyFlowDataSubscriptionCancelRetention handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    coupon_offer: _SerializerBillingPortalSessionCreateBodyFlowDataSubscriptionCancelRetentionCouponOffer = pydantic.Field(
        alias="coupon_offer",
    )
    type_: typing_extensions.Literal["coupon_offer"] = pydantic.Field(
        alias="type",
    )
