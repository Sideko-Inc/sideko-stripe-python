import pydantic
import typing_extensions


class BillingPortalSessionCreateBodyFlowDataAfterCompletionRedirect(
    typing_extensions.TypedDict
):
    """
    BillingPortalSessionCreateBodyFlowDataAfterCompletionRedirect
    """

    return_url: typing_extensions.Required[str]


class _SerializerBillingPortalSessionCreateBodyFlowDataAfterCompletionRedirect(
    pydantic.BaseModel
):
    """
    Serializer for BillingPortalSessionCreateBodyFlowDataAfterCompletionRedirect handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    return_url: str = pydantic.Field(
        alias="return_url",
    )
