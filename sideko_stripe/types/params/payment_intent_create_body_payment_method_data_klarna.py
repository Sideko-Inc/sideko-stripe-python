import pydantic
import typing
import typing_extensions

from .payment_intent_create_body_payment_method_data_klarna_dob import (
    PaymentIntentCreateBodyPaymentMethodDataKlarnaDob,
    _SerializerPaymentIntentCreateBodyPaymentMethodDataKlarnaDob,
)


class PaymentIntentCreateBodyPaymentMethodDataKlarna(typing_extensions.TypedDict):
    """
    PaymentIntentCreateBodyPaymentMethodDataKlarna
    """

    dob: typing_extensions.NotRequired[
        PaymentIntentCreateBodyPaymentMethodDataKlarnaDob
    ]


class _SerializerPaymentIntentCreateBodyPaymentMethodDataKlarna(pydantic.BaseModel):
    """
    Serializer for PaymentIntentCreateBodyPaymentMethodDataKlarna handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    dob: typing.Optional[
        _SerializerPaymentIntentCreateBodyPaymentMethodDataKlarnaDob
    ] = pydantic.Field(alias="dob", default=None)
