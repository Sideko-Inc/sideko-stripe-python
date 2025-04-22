import pydantic
import typing
import typing_extensions

from .payment_intent_update_body_payment_method_options_sepa_debit_obj0_mandate_options import (
    PaymentIntentUpdateBodyPaymentMethodOptionsSepaDebitObj0MandateOptions,
    _SerializerPaymentIntentUpdateBodyPaymentMethodOptionsSepaDebitObj0MandateOptions,
)


class PaymentIntentUpdateBodyPaymentMethodOptionsSepaDebitObj0(
    typing_extensions.TypedDict
):
    """
    PaymentIntentUpdateBodyPaymentMethodOptionsSepaDebitObj0
    """

    mandate_options: typing_extensions.NotRequired[
        PaymentIntentUpdateBodyPaymentMethodOptionsSepaDebitObj0MandateOptions
    ]

    setup_future_usage: typing_extensions.NotRequired[
        typing_extensions.Literal["none", "off_session", "on_session"]
    ]

    target_date: typing_extensions.NotRequired[str]


class _SerializerPaymentIntentUpdateBodyPaymentMethodOptionsSepaDebitObj0(
    pydantic.BaseModel
):
    """
    Serializer for PaymentIntentUpdateBodyPaymentMethodOptionsSepaDebitObj0 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    mandate_options: typing.Optional[
        _SerializerPaymentIntentUpdateBodyPaymentMethodOptionsSepaDebitObj0MandateOptions
    ] = pydantic.Field(alias="mandate_options", default=None)
    setup_future_usage: typing.Optional[
        typing_extensions.Literal["none", "off_session", "on_session"]
    ] = pydantic.Field(alias="setup_future_usage", default=None)
    target_date: typing.Optional[str] = pydantic.Field(
        alias="target_date", default=None
    )
