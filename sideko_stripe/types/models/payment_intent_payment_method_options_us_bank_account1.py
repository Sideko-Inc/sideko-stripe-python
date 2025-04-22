import pydantic
import typing
import typing_extensions

from .linked_account_options_us_bank_account import LinkedAccountOptionsUsBankAccount
from .payment_method_options_us_bank_account_mandate_options import (
    PaymentMethodOptionsUsBankAccountMandateOptions,
)


class PaymentIntentPaymentMethodOptionsUsBankAccount1(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    financial_connections: typing.Optional[LinkedAccountOptionsUsBankAccount] = (
        pydantic.Field(alias="financial_connections", default=None)
    )
    mandate_options: typing.Optional[
        PaymentMethodOptionsUsBankAccountMandateOptions
    ] = pydantic.Field(alias="mandate_options", default=None)
    preferred_settlement_speed: typing.Optional[
        typing_extensions.Literal["fastest", "standard"]
    ] = pydantic.Field(alias="preferred_settlement_speed", default=None)
    """
    Preferred transaction settlement speed
    """
    setup_future_usage: typing.Optional[
        typing_extensions.Literal["none", "off_session", "on_session"]
    ] = pydantic.Field(alias="setup_future_usage", default=None)
    """
    Indicates that you intend to make future payments with this PaymentIntent's payment method.
    
    If you provide a Customer with the PaymentIntent, you can use this parameter to [attach the payment method](/payments/save-during-payment) to the Customer after the PaymentIntent is confirmed and the customer completes any required actions. If you don't provide a Customer, you can still [attach](/api/payment_methods/attach) the payment method to a Customer after the transaction completes.
    
    If the payment method is `card_present` and isn't a digital wallet, Stripe creates and attaches a [generated_card](/api/charges/object#charge_object-payment_method_details-card_present-generated_card) payment method representing the card to the Customer instead.
    
    When processing card payments, Stripe uses `setup_future_usage` to help you comply with regional legislation and network rules, such as [SCA](/strong-customer-authentication).
    """
    target_date: typing.Optional[str] = pydantic.Field(
        alias="target_date", default=None
    )
    """
    Controls when Stripe will attempt to debit the funds from the customer's account. The date must be a string in YYYY-MM-DD format. The date must be in the future and between 3 and 15 calendar days from now.
    """
    verification_method: typing.Optional[
        typing_extensions.Literal["automatic", "instant", "microdeposits"]
    ] = pydantic.Field(alias="verification_method", default=None)
    """
    Bank account verification method.
    """
