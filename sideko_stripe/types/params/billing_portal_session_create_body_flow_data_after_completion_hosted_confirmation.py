import pydantic
import typing
import typing_extensions


class BillingPortalSessionCreateBodyFlowDataAfterCompletionHostedConfirmation(
    typing_extensions.TypedDict
):
    """
    BillingPortalSessionCreateBodyFlowDataAfterCompletionHostedConfirmation
    """

    custom_message: typing_extensions.NotRequired[str]


class _SerializerBillingPortalSessionCreateBodyFlowDataAfterCompletionHostedConfirmation(
    pydantic.BaseModel
):
    """
    Serializer for BillingPortalSessionCreateBodyFlowDataAfterCompletionHostedConfirmation handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    custom_message: typing.Optional[str] = pydantic.Field(
        alias="custom_message", default=None
    )
