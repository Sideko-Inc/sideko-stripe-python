import pydantic
import typing
import typing_extensions

from .checkout_session_create_body_payment_method_options_us_bank_account_financial_connections import (
    CheckoutSessionCreateBodyPaymentMethodOptionsUsBankAccountFinancialConnections,
    _SerializerCheckoutSessionCreateBodyPaymentMethodOptionsUsBankAccountFinancialConnections,
)


class CheckoutSessionCreateBodyPaymentMethodOptionsUsBankAccount(
    typing_extensions.TypedDict
):
    """
    CheckoutSessionCreateBodyPaymentMethodOptionsUsBankAccount
    """

    financial_connections: typing_extensions.NotRequired[
        CheckoutSessionCreateBodyPaymentMethodOptionsUsBankAccountFinancialConnections
    ]

    setup_future_usage: typing_extensions.NotRequired[
        typing_extensions.Literal["none", "off_session", "on_session"]
    ]

    target_date: typing_extensions.NotRequired[str]

    verification_method: typing_extensions.NotRequired[
        typing_extensions.Literal["automatic", "instant"]
    ]


class _SerializerCheckoutSessionCreateBodyPaymentMethodOptionsUsBankAccount(
    pydantic.BaseModel
):
    """
    Serializer for CheckoutSessionCreateBodyPaymentMethodOptionsUsBankAccount handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    financial_connections: typing.Optional[
        _SerializerCheckoutSessionCreateBodyPaymentMethodOptionsUsBankAccountFinancialConnections
    ] = pydantic.Field(alias="financial_connections", default=None)
    setup_future_usage: typing.Optional[
        typing_extensions.Literal["none", "off_session", "on_session"]
    ] = pydantic.Field(alias="setup_future_usage", default=None)
    target_date: typing.Optional[str] = pydantic.Field(
        alias="target_date", default=None
    )
    verification_method: typing.Optional[
        typing_extensions.Literal["automatic", "instant"]
    ] = pydantic.Field(alias="verification_method", default=None)
