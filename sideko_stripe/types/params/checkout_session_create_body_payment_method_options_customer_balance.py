import pydantic
import typing
import typing_extensions

from .checkout_session_create_body_payment_method_options_customer_balance_bank_transfer import (
    CheckoutSessionCreateBodyPaymentMethodOptionsCustomerBalanceBankTransfer,
    _SerializerCheckoutSessionCreateBodyPaymentMethodOptionsCustomerBalanceBankTransfer,
)


class CheckoutSessionCreateBodyPaymentMethodOptionsCustomerBalance(
    typing_extensions.TypedDict
):
    """
    CheckoutSessionCreateBodyPaymentMethodOptionsCustomerBalance
    """

    bank_transfer: typing_extensions.NotRequired[
        CheckoutSessionCreateBodyPaymentMethodOptionsCustomerBalanceBankTransfer
    ]

    funding_type: typing_extensions.NotRequired[
        typing_extensions.Literal["bank_transfer"]
    ]

    setup_future_usage: typing_extensions.NotRequired[typing_extensions.Literal["none"]]


class _SerializerCheckoutSessionCreateBodyPaymentMethodOptionsCustomerBalance(
    pydantic.BaseModel
):
    """
    Serializer for CheckoutSessionCreateBodyPaymentMethodOptionsCustomerBalance handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    bank_transfer: typing.Optional[
        _SerializerCheckoutSessionCreateBodyPaymentMethodOptionsCustomerBalanceBankTransfer
    ] = pydantic.Field(alias="bank_transfer", default=None)
    funding_type: typing.Optional[typing_extensions.Literal["bank_transfer"]] = (
        pydantic.Field(alias="funding_type", default=None)
    )
    setup_future_usage: typing.Optional[typing_extensions.Literal["none"]] = (
        pydantic.Field(alias="setup_future_usage", default=None)
    )
