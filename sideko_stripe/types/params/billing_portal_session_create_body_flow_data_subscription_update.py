import pydantic
import typing_extensions


class BillingPortalSessionCreateBodyFlowDataSubscriptionUpdate(
    typing_extensions.TypedDict
):
    """
    BillingPortalSessionCreateBodyFlowDataSubscriptionUpdate
    """

    subscription: typing_extensions.Required[str]


class _SerializerBillingPortalSessionCreateBodyFlowDataSubscriptionUpdate(
    pydantic.BaseModel
):
    """
    Serializer for BillingPortalSessionCreateBodyFlowDataSubscriptionUpdate handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    subscription: str = pydantic.Field(
        alias="subscription",
    )
