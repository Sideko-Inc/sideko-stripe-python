import pydantic
import typing
import typing_extensions

from .payment_link_create_body_after_completion_hosted_confirmation import (
    PaymentLinkCreateBodyAfterCompletionHostedConfirmation,
    _SerializerPaymentLinkCreateBodyAfterCompletionHostedConfirmation,
)
from .payment_link_create_body_after_completion_redirect import (
    PaymentLinkCreateBodyAfterCompletionRedirect,
    _SerializerPaymentLinkCreateBodyAfterCompletionRedirect,
)


class PaymentLinkCreateBodyAfterCompletion(typing_extensions.TypedDict):
    """
    Behavior after the purchase is complete.
    """

    hosted_confirmation: typing_extensions.NotRequired[
        PaymentLinkCreateBodyAfterCompletionHostedConfirmation
    ]

    redirect: typing_extensions.NotRequired[
        PaymentLinkCreateBodyAfterCompletionRedirect
    ]

    type_: typing_extensions.Required[
        typing_extensions.Literal["hosted_confirmation", "redirect"]
    ]


class _SerializerPaymentLinkCreateBodyAfterCompletion(pydantic.BaseModel):
    """
    Serializer for PaymentLinkCreateBodyAfterCompletion handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    hosted_confirmation: typing.Optional[
        _SerializerPaymentLinkCreateBodyAfterCompletionHostedConfirmation
    ] = pydantic.Field(alias="hosted_confirmation", default=None)
    redirect: typing.Optional[
        _SerializerPaymentLinkCreateBodyAfterCompletionRedirect
    ] = pydantic.Field(alias="redirect", default=None)
    type_: typing_extensions.Literal["hosted_confirmation", "redirect"] = (
        pydantic.Field(
            alias="type",
        )
    )
