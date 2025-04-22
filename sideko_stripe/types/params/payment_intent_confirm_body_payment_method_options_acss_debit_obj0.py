import pydantic
import typing
import typing_extensions

from .payment_intent_confirm_body_payment_method_options_acss_debit_obj0_mandate_options import (
    PaymentIntentConfirmBodyPaymentMethodOptionsAcssDebitObj0MandateOptions,
    _SerializerPaymentIntentConfirmBodyPaymentMethodOptionsAcssDebitObj0MandateOptions,
)


class PaymentIntentConfirmBodyPaymentMethodOptionsAcssDebitObj0(
    typing_extensions.TypedDict
):
    """
    PaymentIntentConfirmBodyPaymentMethodOptionsAcssDebitObj0
    """

    mandate_options: typing_extensions.NotRequired[
        PaymentIntentConfirmBodyPaymentMethodOptionsAcssDebitObj0MandateOptions
    ]

    setup_future_usage: typing_extensions.NotRequired[
        typing_extensions.Literal["none", "off_session", "on_session"]
    ]

    target_date: typing_extensions.NotRequired[str]

    verification_method: typing_extensions.NotRequired[
        typing_extensions.Literal["automatic", "instant", "microdeposits"]
    ]


class _SerializerPaymentIntentConfirmBodyPaymentMethodOptionsAcssDebitObj0(
    pydantic.BaseModel
):
    """
    Serializer for PaymentIntentConfirmBodyPaymentMethodOptionsAcssDebitObj0 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    mandate_options: typing.Optional[
        _SerializerPaymentIntentConfirmBodyPaymentMethodOptionsAcssDebitObj0MandateOptions
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
