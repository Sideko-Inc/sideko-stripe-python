import pydantic
import typing

from .payment_intent_next_action_alipay_handle_redirect import (
    PaymentIntentNextActionAlipayHandleRedirect,
)
from .payment_intent_next_action_boleto import PaymentIntentNextActionBoleto
from .payment_intent_next_action_card_await_notification import (
    PaymentIntentNextActionCardAwaitNotification,
)
from .payment_intent_next_action_cashapp_handle_redirect_or_display_qr_code import (
    PaymentIntentNextActionCashappHandleRedirectOrDisplayQrCode,
)
from .payment_intent_next_action_display_bank_transfer_instructions import (
    PaymentIntentNextActionDisplayBankTransferInstructions,
)
from .payment_intent_next_action_display_multibanco_details import (
    PaymentIntentNextActionDisplayMultibancoDetails,
)
from .payment_intent_next_action_display_oxxo_details import (
    PaymentIntentNextActionDisplayOxxoDetails,
)
from .payment_intent_next_action_konbini import PaymentIntentNextActionKonbini
from .payment_intent_next_action_paynow_display_qr_code import (
    PaymentIntentNextActionPaynowDisplayQrCode,
)
from .payment_intent_next_action_pix_display_qr_code import (
    PaymentIntentNextActionPixDisplayQrCode,
)
from .payment_intent_next_action_promptpay_display_qr_code import (
    PaymentIntentNextActionPromptpayDisplayQrCode,
)
from .payment_intent_next_action_redirect_to_url import (
    PaymentIntentNextActionRedirectToUrl,
)
from .payment_intent_next_action_swish_handle_redirect_or_display_qr_code import (
    PaymentIntentNextActionSwishHandleRedirectOrDisplayQrCode,
)
from .payment_intent_next_action_verify_with_microdeposits import (
    PaymentIntentNextActionVerifyWithMicrodeposits,
)
from .payment_intent_next_action_wechat_pay_display_qr_code import (
    PaymentIntentNextActionWechatPayDisplayQrCode,
)
from .payment_intent_next_action_wechat_pay_redirect_to_android_app import (
    PaymentIntentNextActionWechatPayRedirectToAndroidApp,
)
from .payment_intent_next_action_wechat_pay_redirect_to_ios_app import (
    PaymentIntentNextActionWechatPayRedirectToIosApp,
)


class PaymentIntentNextAction(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    alipay_handle_redirect: typing.Optional[
        PaymentIntentNextActionAlipayHandleRedirect
    ] = pydantic.Field(alias="alipay_handle_redirect", default=None)
    boleto_display_details: typing.Optional[PaymentIntentNextActionBoleto] = (
        pydantic.Field(alias="boleto_display_details", default=None)
    )
    card_await_notification: typing.Optional[
        PaymentIntentNextActionCardAwaitNotification
    ] = pydantic.Field(alias="card_await_notification", default=None)
    cashapp_handle_redirect_or_display_qr_code: typing.Optional[
        PaymentIntentNextActionCashappHandleRedirectOrDisplayQrCode
    ] = pydantic.Field(alias="cashapp_handle_redirect_or_display_qr_code", default=None)
    display_bank_transfer_instructions: typing.Optional[
        PaymentIntentNextActionDisplayBankTransferInstructions
    ] = pydantic.Field(alias="display_bank_transfer_instructions", default=None)
    konbini_display_details: typing.Optional[PaymentIntentNextActionKonbini] = (
        pydantic.Field(alias="konbini_display_details", default=None)
    )
    multibanco_display_details: typing.Optional[
        PaymentIntentNextActionDisplayMultibancoDetails
    ] = pydantic.Field(alias="multibanco_display_details", default=None)
    oxxo_display_details: typing.Optional[PaymentIntentNextActionDisplayOxxoDetails] = (
        pydantic.Field(alias="oxxo_display_details", default=None)
    )
    paynow_display_qr_code: typing.Optional[
        PaymentIntentNextActionPaynowDisplayQrCode
    ] = pydantic.Field(alias="paynow_display_qr_code", default=None)
    pix_display_qr_code: typing.Optional[PaymentIntentNextActionPixDisplayQrCode] = (
        pydantic.Field(alias="pix_display_qr_code", default=None)
    )
    promptpay_display_qr_code: typing.Optional[
        PaymentIntentNextActionPromptpayDisplayQrCode
    ] = pydantic.Field(alias="promptpay_display_qr_code", default=None)
    redirect_to_url: typing.Optional[PaymentIntentNextActionRedirectToUrl] = (
        pydantic.Field(alias="redirect_to_url", default=None)
    )
    swish_handle_redirect_or_display_qr_code: typing.Optional[
        PaymentIntentNextActionSwishHandleRedirectOrDisplayQrCode
    ] = pydantic.Field(alias="swish_handle_redirect_or_display_qr_code", default=None)
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
    When confirming a PaymentIntent with Stripe.js, Stripe.js depends on the contents of this dictionary to invoke authentication flows. The shape of the contents is subject to change and is only intended to be used by Stripe.js.
    """
    verify_with_microdeposits: typing.Optional[
        PaymentIntentNextActionVerifyWithMicrodeposits
    ] = pydantic.Field(alias="verify_with_microdeposits", default=None)
    wechat_pay_display_qr_code: typing.Optional[
        PaymentIntentNextActionWechatPayDisplayQrCode
    ] = pydantic.Field(alias="wechat_pay_display_qr_code", default=None)
    wechat_pay_redirect_to_android_app: typing.Optional[
        PaymentIntentNextActionWechatPayRedirectToAndroidApp
    ] = pydantic.Field(alias="wechat_pay_redirect_to_android_app", default=None)
    wechat_pay_redirect_to_ios_app: typing.Optional[
        PaymentIntentNextActionWechatPayRedirectToIosApp
    ] = pydantic.Field(alias="wechat_pay_redirect_to_ios_app", default=None)
