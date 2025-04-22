import pydantic
import typing_extensions

from .payment_intent_confirm_body_mandate_data_obj2_customer_acceptance import (
    PaymentIntentConfirmBodyMandateDataObj2CustomerAcceptance,
    _SerializerPaymentIntentConfirmBodyMandateDataObj2CustomerAcceptance,
)


class PaymentIntentConfirmBodyMandateDataObj2(typing_extensions.TypedDict):
    """
    This hash contains details about the Mandate to create
    """

    customer_acceptance: typing_extensions.Required[
        PaymentIntentConfirmBodyMandateDataObj2CustomerAcceptance
    ]


class _SerializerPaymentIntentConfirmBodyMandateDataObj2(pydantic.BaseModel):
    """
    Serializer for PaymentIntentConfirmBodyMandateDataObj2 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    customer_acceptance: _SerializerPaymentIntentConfirmBodyMandateDataObj2CustomerAcceptance = pydantic.Field(
        alias="customer_acceptance",
    )
