import pydantic
import typing
import typing_extensions

from .payment_intent_confirm_body_payment_method_options_customer_balance_obj0_bank_transfer import (
    PaymentIntentConfirmBodyPaymentMethodOptionsCustomerBalanceObj0BankTransfer,
    _SerializerPaymentIntentConfirmBodyPaymentMethodOptionsCustomerBalanceObj0BankTransfer,
)


class PaymentIntentConfirmBodyPaymentMethodOptionsCustomerBalanceObj0(
    typing_extensions.TypedDict
):
    """
    PaymentIntentConfirmBodyPaymentMethodOptionsCustomerBalanceObj0
    """

    bank_transfer: typing_extensions.NotRequired[
        PaymentIntentConfirmBodyPaymentMethodOptionsCustomerBalanceObj0BankTransfer
    ]

    funding_type: typing_extensions.NotRequired[
        typing_extensions.Literal["bank_transfer"]
    ]

    setup_future_usage: typing_extensions.NotRequired[typing_extensions.Literal["none"]]


class _SerializerPaymentIntentConfirmBodyPaymentMethodOptionsCustomerBalanceObj0(
    pydantic.BaseModel
):
    """
    Serializer for PaymentIntentConfirmBodyPaymentMethodOptionsCustomerBalanceObj0 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    bank_transfer: typing.Optional[
        _SerializerPaymentIntentConfirmBodyPaymentMethodOptionsCustomerBalanceObj0BankTransfer
    ] = pydantic.Field(alias="bank_transfer", default=None)
    funding_type: typing.Optional[typing_extensions.Literal["bank_transfer"]] = (
        pydantic.Field(alias="funding_type", default=None)
    )
    setup_future_usage: typing.Optional[typing_extensions.Literal["none"]] = (
        pydantic.Field(alias="setup_future_usage", default=None)
    )
