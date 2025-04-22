import pydantic
import typing_extensions

from .payment_intent_confirm_body_mandate_data_obj2_customer_acceptance_online import (
    PaymentIntentConfirmBodyMandateDataObj2CustomerAcceptanceOnline,
    _SerializerPaymentIntentConfirmBodyMandateDataObj2CustomerAcceptanceOnline,
)


class PaymentIntentConfirmBodyMandateDataObj2CustomerAcceptance(
    typing_extensions.TypedDict
):
    """
    PaymentIntentConfirmBodyMandateDataObj2CustomerAcceptance
    """

    online: typing_extensions.Required[
        PaymentIntentConfirmBodyMandateDataObj2CustomerAcceptanceOnline
    ]

    type_: typing_extensions.Required[typing_extensions.Literal["online"]]


class _SerializerPaymentIntentConfirmBodyMandateDataObj2CustomerAcceptance(
    pydantic.BaseModel
):
    """
    Serializer for PaymentIntentConfirmBodyMandateDataObj2CustomerAcceptance handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    online: _SerializerPaymentIntentConfirmBodyMandateDataObj2CustomerAcceptanceOnline = pydantic.Field(
        alias="online",
    )
    type_: typing_extensions.Literal["online"] = pydantic.Field(
        alias="type",
    )
