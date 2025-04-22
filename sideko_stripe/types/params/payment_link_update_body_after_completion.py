import pydantic
import typing
import typing_extensions

from .payment_link_update_body_after_completion_hosted_confirmation import (
    PaymentLinkUpdateBodyAfterCompletionHostedConfirmation,
    _SerializerPaymentLinkUpdateBodyAfterCompletionHostedConfirmation,
)
from .payment_link_update_body_after_completion_redirect import (
    PaymentLinkUpdateBodyAfterCompletionRedirect,
    _SerializerPaymentLinkUpdateBodyAfterCompletionRedirect,
)


class PaymentLinkUpdateBodyAfterCompletion(typing_extensions.TypedDict):
    """
    Behavior after the purchase is complete.
    """

    hosted_confirmation: typing_extensions.NotRequired[
        PaymentLinkUpdateBodyAfterCompletionHostedConfirmation
    ]

    redirect: typing_extensions.NotRequired[
        PaymentLinkUpdateBodyAfterCompletionRedirect
    ]

    type_: typing_extensions.Required[
        typing_extensions.Literal["hosted_confirmation", "redirect"]
    ]


class _SerializerPaymentLinkUpdateBodyAfterCompletion(pydantic.BaseModel):
    """
    Serializer for PaymentLinkUpdateBodyAfterCompletion handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    hosted_confirmation: typing.Optional[
        _SerializerPaymentLinkUpdateBodyAfterCompletionHostedConfirmation
    ] = pydantic.Field(alias="hosted_confirmation", default=None)
    redirect: typing.Optional[
        _SerializerPaymentLinkUpdateBodyAfterCompletionRedirect
    ] = pydantic.Field(alias="redirect", default=None)
    type_: typing_extensions.Literal["hosted_confirmation", "redirect"] = (
        pydantic.Field(
            alias="type",
        )
    )
