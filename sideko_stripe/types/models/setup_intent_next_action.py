import pydantic
import typing

from .payment_intent_next_action_cashapp_handle_redirect_or_display_qr_code import (
    PaymentIntentNextActionCashappHandleRedirectOrDisplayQrCode,
)
from .setup_intent_next_action_redirect_to_url import SetupIntentNextActionRedirectToUrl
from .setup_intent_next_action_verify_with_microdeposits import (
    SetupIntentNextActionVerifyWithMicrodeposits,
)


class SetupIntentNextAction(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    cashapp_handle_redirect_or_display_qr_code: typing.Optional[
        PaymentIntentNextActionCashappHandleRedirectOrDisplayQrCode
    ] = pydantic.Field(alias="cashapp_handle_redirect_or_display_qr_code", default=None)
    redirect_to_url: typing.Optional[SetupIntentNextActionRedirectToUrl] = (
        pydantic.Field(alias="redirect_to_url", default=None)
    )
    type_: str = pydantic.Field(
        alias="type",
    )
    """
    Type of the next action to perform, one of `redirect_to_url`, `use_stripe_sdk`, `alipay_handle_redirect`, `oxxo_display_details`, or `verify_with_microdeposits`.
    """
    use_stripe_sdk: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="use_stripe_sdk", default=None
    )
    """
    When confirming a SetupIntent with Stripe.js, Stripe.js depends on the contents of this dictionary to invoke authentication flows. The shape of the contents is subject to change and is only intended to be used by Stripe.js.
    """
    verify_with_microdeposits: typing.Optional[
        SetupIntentNextActionVerifyWithMicrodeposits
    ] = pydantic.Field(alias="verify_with_microdeposits", default=None)
