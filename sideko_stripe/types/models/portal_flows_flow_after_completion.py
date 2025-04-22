import pydantic
import typing
import typing_extensions

from .portal_flows_after_completion_hosted_confirmation import (
    PortalFlowsAfterCompletionHostedConfirmation,
)
from .portal_flows_after_completion_redirect import PortalFlowsAfterCompletionRedirect


class PortalFlowsFlowAfterCompletion(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    hosted_confirmation: typing.Optional[
        PortalFlowsAfterCompletionHostedConfirmation
    ] = pydantic.Field(alias="hosted_confirmation", default=None)
    redirect: typing.Optional[PortalFlowsAfterCompletionRedirect] = pydantic.Field(
        alias="redirect", default=None
    )
    type_: typing_extensions.Literal[
        "hosted_confirmation", "portal_homepage", "redirect"
    ] = pydantic.Field(
        alias="type",
    )
    """
    The specified type of behavior after the flow is completed.
    """
