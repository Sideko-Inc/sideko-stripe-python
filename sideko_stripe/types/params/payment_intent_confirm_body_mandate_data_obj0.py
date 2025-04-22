import pydantic
import typing_extensions

from .payment_intent_confirm_body_mandate_data_obj0_customer_acceptance import (
    PaymentIntentConfirmBodyMandateDataObj0CustomerAcceptance,
    _SerializerPaymentIntentConfirmBodyMandateDataObj0CustomerAcceptance,
)


class PaymentIntentConfirmBodyMandateDataObj0(typing_extensions.TypedDict):
    """
    PaymentIntentConfirmBodyMandateDataObj0
    """

    customer_acceptance: typing_extensions.Required[
        PaymentIntentConfirmBodyMandateDataObj0CustomerAcceptance
    ]


class _SerializerPaymentIntentConfirmBodyMandateDataObj0(pydantic.BaseModel):
    """
    Serializer for PaymentIntentConfirmBodyMandateDataObj0 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    customer_acceptance: _SerializerPaymentIntentConfirmBodyMandateDataObj0CustomerAcceptance = pydantic.Field(
        alias="customer_acceptance",
    )
