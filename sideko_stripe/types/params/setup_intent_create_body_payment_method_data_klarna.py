import pydantic
import typing
import typing_extensions

from .setup_intent_create_body_payment_method_data_klarna_dob import (
    SetupIntentCreateBodyPaymentMethodDataKlarnaDob,
    _SerializerSetupIntentCreateBodyPaymentMethodDataKlarnaDob,
)


class SetupIntentCreateBodyPaymentMethodDataKlarna(typing_extensions.TypedDict):
    """
    SetupIntentCreateBodyPaymentMethodDataKlarna
    """

    dob: typing_extensions.NotRequired[SetupIntentCreateBodyPaymentMethodDataKlarnaDob]


class _SerializerSetupIntentCreateBodyPaymentMethodDataKlarna(pydantic.BaseModel):
    """
    Serializer for SetupIntentCreateBodyPaymentMethodDataKlarna handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    dob: typing.Optional[_SerializerSetupIntentCreateBodyPaymentMethodDataKlarnaDob] = (
        pydantic.Field(alias="dob", default=None)
    )
