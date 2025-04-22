import pydantic
import typing
import typing_extensions

from .payment_intent_update_body_payment_method_data_klarna_dob import (
    PaymentIntentUpdateBodyPaymentMethodDataKlarnaDob,
    _SerializerPaymentIntentUpdateBodyPaymentMethodDataKlarnaDob,
)


class PaymentIntentUpdateBodyPaymentMethodDataKlarna(typing_extensions.TypedDict):
    """
    PaymentIntentUpdateBodyPaymentMethodDataKlarna
    """

    dob: typing_extensions.NotRequired[
        PaymentIntentUpdateBodyPaymentMethodDataKlarnaDob
    ]


class _SerializerPaymentIntentUpdateBodyPaymentMethodDataKlarna(pydantic.BaseModel):
    """
    Serializer for PaymentIntentUpdateBodyPaymentMethodDataKlarna handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    dob: typing.Optional[
        _SerializerPaymentIntentUpdateBodyPaymentMethodDataKlarnaDob
    ] = pydantic.Field(alias="dob", default=None)
