import pydantic
import typing
import typing_extensions

from .payment_flows_installment_options import PaymentFlowsInstallmentOptions
from .payment_method_options_card_present_routing import (
    PaymentMethodOptionsCardPresentRouting,
)


class PaymentIntentTypeSpecificPaymentMethodOptionsClient(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    capture_method: typing.Optional[
        typing_extensions.Literal["manual", "manual_preferred"]
    ] = pydantic.Field(alias="capture_method", default=None)
    """
    Controls when the funds will be captured from the customer's account.
    """
    installments: typing.Optional[PaymentFlowsInstallmentOptions] = pydantic.Field(
        alias="installments", default=None
    )
    request_incremental_authorization_support: typing.Optional[bool] = pydantic.Field(
        alias="request_incremental_authorization_support", default=None
    )
    """
    Request ability to [increment](https://stripe.com/docs/terminal/features/incremental-authorizations) this PaymentIntent if the combination of MCC and card brand is eligible. Check [incremental_authorization_supported](https://stripe.com/docs/api/charges/object#charge_object-payment_method_details-card_present-incremental_authorization_supported) in the [Confirm](https://stripe.com/docs/api/payment_intents/confirm) response to verify support.
    """
    require_cvc_recollection: typing.Optional[bool] = pydantic.Field(
        alias="require_cvc_recollection", default=None
    )
    """
    When enabled, using a card that is attached to a customer will require the CVC to be provided again (i.e. using the cvc_token parameter).
    """
    routing: typing.Optional[PaymentMethodOptionsCardPresentRouting] = pydantic.Field(
        alias="routing", default=None
    )
    setup_future_usage: typing.Optional[
        typing_extensions.Literal["none", "off_session", "on_session"]
    ] = pydantic.Field(alias="setup_future_usage", default=None)
    """
    Indicates that you intend to make future payments with this PaymentIntent's payment method.
    
    If you provide a Customer with the PaymentIntent, you can use this parameter to [attach the payment method](/payments/save-during-payment) to the Customer after the PaymentIntent is confirmed and the customer completes any required actions. If you don't provide a Customer, you can still [attach](/api/payment_methods/attach) the payment method to a Customer after the transaction completes.
    
    If the payment method is `card_present` and isn't a digital wallet, Stripe creates and attaches a [generated_card](/api/charges/object#charge_object-payment_method_details-card_present-generated_card) payment method representing the card to the Customer instead.
    
    When processing card payments, Stripe uses `setup_future_usage` to help you comply with regional legislation and network rules, such as [SCA](/strong-customer-authentication).
    """
    verification_method: typing.Optional[
        typing_extensions.Literal["automatic", "instant", "microdeposits"]
    ] = pydantic.Field(alias="verification_method", default=None)
    """
    Bank account verification method.
    """
