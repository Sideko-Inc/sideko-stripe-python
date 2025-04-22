import pydantic
import typing
import typing_extensions

from .billing_portal_session_create_body_flow_data_subscription_cancel_retention import (
    BillingPortalSessionCreateBodyFlowDataSubscriptionCancelRetention,
    _SerializerBillingPortalSessionCreateBodyFlowDataSubscriptionCancelRetention,
)


class BillingPortalSessionCreateBodyFlowDataSubscriptionCancel(
    typing_extensions.TypedDict
):
    """
    BillingPortalSessionCreateBodyFlowDataSubscriptionCancel
    """

    retention: typing_extensions.NotRequired[
        BillingPortalSessionCreateBodyFlowDataSubscriptionCancelRetention
    ]

    subscription: typing_extensions.Required[str]


class _SerializerBillingPortalSessionCreateBodyFlowDataSubscriptionCancel(
    pydantic.BaseModel
):
    """
    Serializer for BillingPortalSessionCreateBodyFlowDataSubscriptionCancel handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    retention: typing.Optional[
        _SerializerBillingPortalSessionCreateBodyFlowDataSubscriptionCancelRetention
    ] = pydantic.Field(alias="retention", default=None)
    subscription: str = pydantic.Field(
        alias="subscription",
    )
