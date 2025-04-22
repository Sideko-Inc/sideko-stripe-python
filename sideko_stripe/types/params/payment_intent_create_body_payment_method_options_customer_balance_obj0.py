import pydantic
import typing
import typing_extensions

from .payment_intent_create_body_payment_method_options_customer_balance_obj0_bank_transfer import (
    PaymentIntentCreateBodyPaymentMethodOptionsCustomerBalanceObj0BankTransfer,
    _SerializerPaymentIntentCreateBodyPaymentMethodOptionsCustomerBalanceObj0BankTransfer,
)


class PaymentIntentCreateBodyPaymentMethodOptionsCustomerBalanceObj0(
    typing_extensions.TypedDict
):
    """
    PaymentIntentCreateBodyPaymentMethodOptionsCustomerBalanceObj0
    """

    bank_transfer: typing_extensions.NotRequired[
        PaymentIntentCreateBodyPaymentMethodOptionsCustomerBalanceObj0BankTransfer
    ]

    funding_type: typing_extensions.NotRequired[
        typing_extensions.Literal["bank_transfer"]
    ]

    setup_future_usage: typing_extensions.NotRequired[typing_extensions.Literal["none"]]


class _SerializerPaymentIntentCreateBodyPaymentMethodOptionsCustomerBalanceObj0(
    pydantic.BaseModel
):
    """
    Serializer for PaymentIntentCreateBodyPaymentMethodOptionsCustomerBalanceObj0 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    bank_transfer: typing.Optional[
        _SerializerPaymentIntentCreateBodyPaymentMethodOptionsCustomerBalanceObj0BankTransfer
    ] = pydantic.Field(alias="bank_transfer", default=None)
    funding_type: typing.Optional[typing_extensions.Literal["bank_transfer"]] = (
        pydantic.Field(alias="funding_type", default=None)
    )
    setup_future_usage: typing.Optional[typing_extensions.Literal["none"]] = (
        pydantic.Field(alias="setup_future_usage", default=None)
    )
