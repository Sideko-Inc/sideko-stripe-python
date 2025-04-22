import pydantic
import typing
import typing_extensions

from .checkout_customer_balance_bank_transfer_payment_method_options import (
    CheckoutCustomerBalanceBankTransferPaymentMethodOptions,
)


class CheckoutCustomerBalancePaymentMethodOptions(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    bank_transfer: typing.Optional[
        CheckoutCustomerBalanceBankTransferPaymentMethodOptions
    ] = pydantic.Field(alias="bank_transfer", default=None)
    funding_type: typing.Optional[typing_extensions.Literal["bank_transfer"]] = (
        pydantic.Field(alias="funding_type", default=None)
    )
    """
    The funding method type to be used when there are not enough funds in the customer balance. Permitted values include: `bank_transfer`.
    """
    setup_future_usage: typing.Optional[typing_extensions.Literal["none"]] = (
        pydantic.Field(alias="setup_future_usage", default=None)
    )
    """
    Indicates that you intend to make future payments with this PaymentIntent's payment method.
    
    If you provide a Customer with the PaymentIntent, you can use this parameter to [attach the payment method](/payments/save-during-payment) to the Customer after the PaymentIntent is confirmed and the customer completes any required actions. If you don't provide a Customer, you can still [attach](/api/payment_methods/attach) the payment method to a Customer after the transaction completes.
    
    If the payment method is `card_present` and isn't a digital wallet, Stripe creates and attaches a [generated_card](/api/charges/object#charge_object-payment_method_details-card_present-generated_card) payment method representing the card to the Customer instead.
    
    When processing card payments, Stripe uses `setup_future_usage` to help you comply with regional legislation and network rules, such as [SCA](/strong-customer-authentication).
    """
