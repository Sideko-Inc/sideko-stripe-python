import pydantic
import typing
import typing_extensions

from .checkout_card_installments_options import CheckoutCardInstallmentsOptions
from .payment_pages_private_card_payment_method_options_resource_restrictions import (
    PaymentPagesPrivateCardPaymentMethodOptionsResourceRestrictions,
)


class CheckoutCardPaymentMethodOptions(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    installments: typing.Optional[CheckoutCardInstallmentsOptions] = pydantic.Field(
        alias="installments", default=None
    )
    request_extended_authorization: typing.Optional[
        typing_extensions.Literal["if_available", "never"]
    ] = pydantic.Field(alias="request_extended_authorization", default=None)
    """
    Request ability to [capture beyond the standard authorization validity window](/payments/extended-authorization) for this CheckoutSession.
    """
    request_incremental_authorization: typing.Optional[
        typing_extensions.Literal["if_available", "never"]
    ] = pydantic.Field(alias="request_incremental_authorization", default=None)
    """
    Request ability to [increment the authorization](/payments/incremental-authorization) for this CheckoutSession.
    """
    request_multicapture: typing.Optional[
        typing_extensions.Literal["if_available", "never"]
    ] = pydantic.Field(alias="request_multicapture", default=None)
    """
    Request ability to make [multiple captures](/payments/multicapture) for this CheckoutSession.
    """
    request_overcapture: typing.Optional[
        typing_extensions.Literal["if_available", "never"]
    ] = pydantic.Field(alias="request_overcapture", default=None)
    """
    Request ability to [overcapture](/payments/overcapture) for this CheckoutSession.
    """
    request_three_d_secure: typing_extensions.Literal[
        "any", "automatic", "challenge"
    ] = pydantic.Field(
        alias="request_three_d_secure",
    )
    """
    We strongly recommend that you rely on our SCA Engine to automatically prompt your customers for authentication based on risk level and [other requirements](https://stripe.com/docs/strong-customer-authentication). However, if you wish to request 3D Secure based on logic from your own fraud engine, provide this option. If not provided, this value defaults to `automatic`. Read our guide on [manually requesting 3D Secure](https://stripe.com/docs/payments/3d-secure/authentication-flow#manual-three-ds) for more information on how this configuration interacts with Radar and our SCA Engine.
    """
    restrictions: typing.Optional[
        PaymentPagesPrivateCardPaymentMethodOptionsResourceRestrictions
    ] = pydantic.Field(alias="restrictions", default=None)
    setup_future_usage: typing.Optional[
        typing_extensions.Literal["none", "off_session", "on_session"]
    ] = pydantic.Field(alias="setup_future_usage", default=None)
    """
    Indicates that you intend to make future payments with this PaymentIntent's payment method.
    
    If you provide a Customer with the PaymentIntent, you can use this parameter to [attach the payment method](/payments/save-during-payment) to the Customer after the PaymentIntent is confirmed and the customer completes any required actions. If you don't provide a Customer, you can still [attach](/api/payment_methods/attach) the payment method to a Customer after the transaction completes.
    
    If the payment method is `card_present` and isn't a digital wallet, Stripe creates and attaches a [generated_card](/api/charges/object#charge_object-payment_method_details-card_present-generated_card) payment method representing the card to the Customer instead.
    
    When processing card payments, Stripe uses `setup_future_usage` to help you comply with regional legislation and network rules, such as [SCA](/strong-customer-authentication).
    """
    statement_descriptor_suffix_kana: typing.Optional[str] = pydantic.Field(
        alias="statement_descriptor_suffix_kana", default=None
    )
    """
    Provides information about a card payment that customers see on their statements. Concatenated with the Kana prefix (shortened Kana descriptor) or Kana statement descriptor that’s set on the account to form the complete statement descriptor. Maximum 22 characters. On card statements, the *concatenation* of both prefix and suffix (including separators) will appear truncated to 22 characters.
    """
    statement_descriptor_suffix_kanji: typing.Optional[str] = pydantic.Field(
        alias="statement_descriptor_suffix_kanji", default=None
    )
    """
    Provides information about a card payment that customers see on their statements. Concatenated with the Kanji prefix (shortened Kanji descriptor) or Kanji statement descriptor that’s set on the account to form the complete statement descriptor. Maximum 17 characters. On card statements, the *concatenation* of both prefix and suffix (including separators) will appear truncated to 17 characters.
    """
