import pydantic
import typing
import typing_extensions

from .setup_intent_update_body_payment_method_data_klarna_dob import (
    SetupIntentUpdateBodyPaymentMethodDataKlarnaDob,
    _SerializerSetupIntentUpdateBodyPaymentMethodDataKlarnaDob,
)


class SetupIntentUpdateBodyPaymentMethodDataKlarna(typing_extensions.TypedDict):
    """
    SetupIntentUpdateBodyPaymentMethodDataKlarna
    """

    dob: typing_extensions.NotRequired[SetupIntentUpdateBodyPaymentMethodDataKlarnaDob]


class _SerializerSetupIntentUpdateBodyPaymentMethodDataKlarna(pydantic.BaseModel):
    """
    Serializer for SetupIntentUpdateBodyPaymentMethodDataKlarna handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    dob: typing.Optional[_SerializerSetupIntentUpdateBodyPaymentMethodDataKlarnaDob] = (
        pydantic.Field(alias="dob", default=None)
    )
