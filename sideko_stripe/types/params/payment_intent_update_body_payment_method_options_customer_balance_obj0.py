import pydantic
import typing
import typing_extensions

from .payment_intent_update_body_payment_method_options_customer_balance_obj0_bank_transfer import (
    PaymentIntentUpdateBodyPaymentMethodOptionsCustomerBalanceObj0BankTransfer,
    _SerializerPaymentIntentUpdateBodyPaymentMethodOptionsCustomerBalanceObj0BankTransfer,
)


class PaymentIntentUpdateBodyPaymentMethodOptionsCustomerBalanceObj0(
    typing_extensions.TypedDict
):
    """
    PaymentIntentUpdateBodyPaymentMethodOptionsCustomerBalanceObj0
    """

    bank_transfer: typing_extensions.NotRequired[
        PaymentIntentUpdateBodyPaymentMethodOptionsCustomerBalanceObj0BankTransfer
    ]

    funding_type: typing_extensions.NotRequired[
        typing_extensions.Literal["bank_transfer"]
    ]

    setup_future_usage: typing_extensions.NotRequired[typing_extensions.Literal["none"]]


class _SerializerPaymentIntentUpdateBodyPaymentMethodOptionsCustomerBalanceObj0(
    pydantic.BaseModel
):
    """
    Serializer for PaymentIntentUpdateBodyPaymentMethodOptionsCustomerBalanceObj0 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    bank_transfer: typing.Optional[
        _SerializerPaymentIntentUpdateBodyPaymentMethodOptionsCustomerBalanceObj0BankTransfer
    ] = pydantic.Field(alias="bank_transfer", default=None)
    funding_type: typing.Optional[typing_extensions.Literal["bank_transfer"]] = (
        pydantic.Field(alias="funding_type", default=None)
    )
    setup_future_usage: typing.Optional[typing_extensions.Literal["none"]] = (
        pydantic.Field(alias="setup_future_usage", default=None)
    )
