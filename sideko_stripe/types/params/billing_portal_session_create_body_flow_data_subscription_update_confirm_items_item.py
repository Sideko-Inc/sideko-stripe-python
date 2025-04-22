import pydantic
import typing
import typing_extensions


class BillingPortalSessionCreateBodyFlowDataSubscriptionUpdateConfirmItemsItem(
    typing_extensions.TypedDict
):
    """
    BillingPortalSessionCreateBodyFlowDataSubscriptionUpdateConfirmItemsItem
    """

    id: typing_extensions.Required[str]

    price: typing_extensions.NotRequired[str]

    quantity: typing_extensions.NotRequired[int]


class _SerializerBillingPortalSessionCreateBodyFlowDataSubscriptionUpdateConfirmItemsItem(
    pydantic.BaseModel
):
    """
    Serializer for BillingPortalSessionCreateBodyFlowDataSubscriptionUpdateConfirmItemsItem handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    id: str = pydantic.Field(
        alias="id",
    )
    price: typing.Optional[str] = pydantic.Field(alias="price", default=None)
    quantity: typing.Optional[int] = pydantic.Field(alias="quantity", default=None)
