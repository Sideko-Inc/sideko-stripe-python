import pydantic
import typing
import typing_extensions

from .payment_links_resource_completion_behavior_confirmation_page import (
    PaymentLinksResourceCompletionBehaviorConfirmationPage,
)
from .payment_links_resource_completion_behavior_redirect import (
    PaymentLinksResourceCompletionBehaviorRedirect,
)


class PaymentLinksResourceAfterCompletion(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    hosted_confirmation: typing.Optional[
        PaymentLinksResourceCompletionBehaviorConfirmationPage
    ] = pydantic.Field(alias="hosted_confirmation", default=None)
    redirect: typing.Optional[PaymentLinksResourceCompletionBehaviorRedirect] = (
        pydantic.Field(alias="redirect", default=None)
    )
    type_: typing_extensions.Literal["hosted_confirmation", "redirect"] = (
        pydantic.Field(
            alias="type",
        )
    )
    """
    The specified behavior after the purchase is complete.
    """
