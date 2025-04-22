import pydantic
import typing
import typing_extensions

from .checkout_session_create_body_payment_method_options_acss_debit_mandate_options import (
    CheckoutSessionCreateBodyPaymentMethodOptionsAcssDebitMandateOptions,
    _SerializerCheckoutSessionCreateBodyPaymentMethodOptionsAcssDebitMandateOptions,
)


class CheckoutSessionCreateBodyPaymentMethodOptionsAcssDebit(
    typing_extensions.TypedDict
):
    """
    CheckoutSessionCreateBodyPaymentMethodOptionsAcssDebit
    """

    currency: typing_extensions.NotRequired[typing_extensions.Literal["cad", "usd"]]

    mandate_options: typing_extensions.NotRequired[
        CheckoutSessionCreateBodyPaymentMethodOptionsAcssDebitMandateOptions
    ]

    setup_future_usage: typing_extensions.NotRequired[
        typing_extensions.Literal["none", "off_session", "on_session"]
    ]

    target_date: typing_extensions.NotRequired[str]

    verification_method: typing_extensions.NotRequired[
        typing_extensions.Literal["automatic", "instant", "microdeposits"]
    ]


class _SerializerCheckoutSessionCreateBodyPaymentMethodOptionsAcssDebit(
    pydantic.BaseModel
):
    """
    Serializer for CheckoutSessionCreateBodyPaymentMethodOptionsAcssDebit handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    currency: typing.Optional[typing_extensions.Literal["cad", "usd"]] = pydantic.Field(
        alias="currency", default=None
    )
    mandate_options: typing.Optional[
        _SerializerCheckoutSessionCreateBodyPaymentMethodOptionsAcssDebitMandateOptions
    ] = pydantic.Field(alias="mandate_options", default=None)
    setup_future_usage: typing.Optional[
        typing_extensions.Literal["none", "off_session", "on_session"]
    ] = pydantic.Field(alias="setup_future_usage", default=None)
    target_date: typing.Optional[str] = pydantic.Field(
        alias="target_date", default=None
    )
    verification_method: typing.Optional[
        typing_extensions.Literal["automatic", "instant", "microdeposits"]
    ] = pydantic.Field(alias="verification_method", default=None)
