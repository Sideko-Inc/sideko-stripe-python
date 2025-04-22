import pydantic
import typing_extensions

from .payment_intent_create_body_mandate_data_obj0_customer_acceptance import (
    PaymentIntentCreateBodyMandateDataObj0CustomerAcceptance,
    _SerializerPaymentIntentCreateBodyMandateDataObj0CustomerAcceptance,
)


class PaymentIntentCreateBodyMandateDataObj0(typing_extensions.TypedDict):
    """
    PaymentIntentCreateBodyMandateDataObj0
    """

    customer_acceptance: typing_extensions.Required[
        PaymentIntentCreateBodyMandateDataObj0CustomerAcceptance
    ]


class _SerializerPaymentIntentCreateBodyMandateDataObj0(pydantic.BaseModel):
    """
    Serializer for PaymentIntentCreateBodyMandateDataObj0 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    customer_acceptance: _SerializerPaymentIntentCreateBodyMandateDataObj0CustomerAcceptance = pydantic.Field(
        alias="customer_acceptance",
    )
