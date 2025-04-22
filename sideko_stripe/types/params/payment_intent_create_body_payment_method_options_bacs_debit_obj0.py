import pydantic
import typing
import typing_extensions

from .payment_intent_create_body_payment_method_options_bacs_debit_obj0_mandate_options import (
    PaymentIntentCreateBodyPaymentMethodOptionsBacsDebitObj0MandateOptions,
    _SerializerPaymentIntentCreateBodyPaymentMethodOptionsBacsDebitObj0MandateOptions,
)


class PaymentIntentCreateBodyPaymentMethodOptionsBacsDebitObj0(
    typing_extensions.TypedDict
):
    """
    PaymentIntentCreateBodyPaymentMethodOptionsBacsDebitObj0
    """

    mandate_options: typing_extensions.NotRequired[
        PaymentIntentCreateBodyPaymentMethodOptionsBacsDebitObj0MandateOptions
    ]

    setup_future_usage: typing_extensions.NotRequired[
        typing_extensions.Literal["none", "off_session", "on_session"]
    ]

    target_date: typing_extensions.NotRequired[str]


class _SerializerPaymentIntentCreateBodyPaymentMethodOptionsBacsDebitObj0(
    pydantic.BaseModel
):
    """
    Serializer for PaymentIntentCreateBodyPaymentMethodOptionsBacsDebitObj0 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    mandate_options: typing.Optional[
        _SerializerPaymentIntentCreateBodyPaymentMethodOptionsBacsDebitObj0MandateOptions
    ] = pydantic.Field(alias="mandate_options", default=None)
    setup_future_usage: typing.Optional[
        typing_extensions.Literal["none", "off_session", "on_session"]
    ] = pydantic.Field(alias="setup_future_usage", default=None)
    target_date: typing.Optional[str] = pydantic.Field(
        alias="target_date", default=None
    )
