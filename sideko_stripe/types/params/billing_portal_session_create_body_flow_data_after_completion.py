import pydantic
import typing
import typing_extensions

from .billing_portal_session_create_body_flow_data_after_completion_hosted_confirmation import (
    BillingPortalSessionCreateBodyFlowDataAfterCompletionHostedConfirmation,
    _SerializerBillingPortalSessionCreateBodyFlowDataAfterCompletionHostedConfirmation,
)
from .billing_portal_session_create_body_flow_data_after_completion_redirect import (
    BillingPortalSessionCreateBodyFlowDataAfterCompletionRedirect,
    _SerializerBillingPortalSessionCreateBodyFlowDataAfterCompletionRedirect,
)


class BillingPortalSessionCreateBodyFlowDataAfterCompletion(
    typing_extensions.TypedDict
):
    """
    BillingPortalSessionCreateBodyFlowDataAfterCompletion
    """

    hosted_confirmation: typing_extensions.NotRequired[
        BillingPortalSessionCreateBodyFlowDataAfterCompletionHostedConfirmation
    ]

    redirect: typing_extensions.NotRequired[
        BillingPortalSessionCreateBodyFlowDataAfterCompletionRedirect
    ]

    type_: typing_extensions.Required[
        typing_extensions.Literal["hosted_confirmation", "portal_homepage", "redirect"]
    ]


class _SerializerBillingPortalSessionCreateBodyFlowDataAfterCompletion(
    pydantic.BaseModel
):
    """
    Serializer for BillingPortalSessionCreateBodyFlowDataAfterCompletion handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    hosted_confirmation: typing.Optional[
        _SerializerBillingPortalSessionCreateBodyFlowDataAfterCompletionHostedConfirmation
    ] = pydantic.Field(alias="hosted_confirmation", default=None)
    redirect: typing.Optional[
        _SerializerBillingPortalSessionCreateBodyFlowDataAfterCompletionRedirect
    ] = pydantic.Field(alias="redirect", default=None)
    type_: typing_extensions.Literal[
        "hosted_confirmation", "portal_homepage", "redirect"
    ] = pydantic.Field(
        alias="type",
    )
