import pydantic
import typing
import typing_extensions

from .setup_intent_confirm_body_payment_method_data_klarna_dob import (
    SetupIntentConfirmBodyPaymentMethodDataKlarnaDob,
    _SerializerSetupIntentConfirmBodyPaymentMethodDataKlarnaDob,
)


class SetupIntentConfirmBodyPaymentMethodDataKlarna(typing_extensions.TypedDict):
    """
    SetupIntentConfirmBodyPaymentMethodDataKlarna
    """

    dob: typing_extensions.NotRequired[SetupIntentConfirmBodyPaymentMethodDataKlarnaDob]


class _SerializerSetupIntentConfirmBodyPaymentMethodDataKlarna(pydantic.BaseModel):
    """
    Serializer for SetupIntentConfirmBodyPaymentMethodDataKlarna handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    dob: typing.Optional[
        _SerializerSetupIntentConfirmBodyPaymentMethodDataKlarnaDob
    ] = pydantic.Field(alias="dob", default=None)
