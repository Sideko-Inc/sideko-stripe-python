import pydantic
import typing
import typing_extensions

from .checkout_session_create_body_payment_method_options_bacs_debit_mandate_options import (
    CheckoutSessionCreateBodyPaymentMethodOptionsBacsDebitMandateOptions,
    _SerializerCheckoutSessionCreateBodyPaymentMethodOptionsBacsDebitMandateOptions,
)


class CheckoutSessionCreateBodyPaymentMethodOptionsBacsDebit(
    typing_extensions.TypedDict
):
    """
    CheckoutSessionCreateBodyPaymentMethodOptionsBacsDebit
    """

    mandate_options: typing_extensions.NotRequired[
        CheckoutSessionCreateBodyPaymentMethodOptionsBacsDebitMandateOptions
    ]

    setup_future_usage: typing_extensions.NotRequired[
        typing_extensions.Literal["none", "off_session", "on_session"]
    ]

    target_date: typing_extensions.NotRequired[str]


class _SerializerCheckoutSessionCreateBodyPaymentMethodOptionsBacsDebit(
    pydantic.BaseModel
):
    """
    Serializer for CheckoutSessionCreateBodyPaymentMethodOptionsBacsDebit handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    mandate_options: typing.Optional[
        _SerializerCheckoutSessionCreateBodyPaymentMethodOptionsBacsDebitMandateOptions
    ] = pydantic.Field(alias="mandate_options", default=None)
    setup_future_usage: typing.Optional[
        typing_extensions.Literal["none", "off_session", "on_session"]
    ] = pydantic.Field(alias="setup_future_usage", default=None)
    target_date: typing.Optional[str] = pydantic.Field(
        alias="target_date", default=None
    )
