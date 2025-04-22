import pydantic
import typing
import typing_extensions

from .payment_method_create_body_klarna_dob import (
    PaymentMethodCreateBodyKlarnaDob,
    _SerializerPaymentMethodCreateBodyKlarnaDob,
)


class PaymentMethodCreateBodyKlarna(typing_extensions.TypedDict):
    """
    If this is a `klarna` PaymentMethod, this hash contains details about the Klarna payment method.
    """

    dob: typing_extensions.NotRequired[PaymentMethodCreateBodyKlarnaDob]


class _SerializerPaymentMethodCreateBodyKlarna(pydantic.BaseModel):
    """
    Serializer for PaymentMethodCreateBodyKlarna handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    dob: typing.Optional[_SerializerPaymentMethodCreateBodyKlarnaDob] = pydantic.Field(
        alias="dob", default=None
    )
