import pydantic
import typing
import typing_extensions

from .payment_intent_confirm_body_payment_method_data_klarna_dob import (
    PaymentIntentConfirmBodyPaymentMethodDataKlarnaDob,
    _SerializerPaymentIntentConfirmBodyPaymentMethodDataKlarnaDob,
)


class PaymentIntentConfirmBodyPaymentMethodDataKlarna(typing_extensions.TypedDict):
    """
    PaymentIntentConfirmBodyPaymentMethodDataKlarna
    """

    dob: typing_extensions.NotRequired[
        PaymentIntentConfirmBodyPaymentMethodDataKlarnaDob
    ]


class _SerializerPaymentIntentConfirmBodyPaymentMethodDataKlarna(pydantic.BaseModel):
    """
    Serializer for PaymentIntentConfirmBodyPaymentMethodDataKlarna handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    dob: typing.Optional[
        _SerializerPaymentIntentConfirmBodyPaymentMethodDataKlarnaDob
    ] = pydantic.Field(alias="dob", default=None)
