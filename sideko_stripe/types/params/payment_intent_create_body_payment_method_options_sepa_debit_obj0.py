import pydantic
import typing
import typing_extensions

from .payment_intent_create_body_payment_method_options_sepa_debit_obj0_mandate_options import (
    PaymentIntentCreateBodyPaymentMethodOptionsSepaDebitObj0MandateOptions,
    _SerializerPaymentIntentCreateBodyPaymentMethodOptionsSepaDebitObj0MandateOptions,
)


class PaymentIntentCreateBodyPaymentMethodOptionsSepaDebitObj0(
    typing_extensions.TypedDict
):
    """
    PaymentIntentCreateBodyPaymentMethodOptionsSepaDebitObj0
    """

    mandate_options: typing_extensions.NotRequired[
        PaymentIntentCreateBodyPaymentMethodOptionsSepaDebitObj0MandateOptions
    ]

    setup_future_usage: typing_extensions.NotRequired[
        typing_extensions.Literal["none", "off_session", "on_session"]
    ]

    target_date: typing_extensions.NotRequired[str]


class _SerializerPaymentIntentCreateBodyPaymentMethodOptionsSepaDebitObj0(
    pydantic.BaseModel
):
    """
    Serializer for PaymentIntentCreateBodyPaymentMethodOptionsSepaDebitObj0 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    mandate_options: typing.Optional[
        _SerializerPaymentIntentCreateBodyPaymentMethodOptionsSepaDebitObj0MandateOptions
    ] = pydantic.Field(alias="mandate_options", default=None)
    setup_future_usage: typing.Optional[
        typing_extensions.Literal["none", "off_session", "on_session"]
    ] = pydantic.Field(alias="setup_future_usage", default=None)
    target_date: typing.Optional[str] = pydantic.Field(
        alias="target_date", default=None
    )
