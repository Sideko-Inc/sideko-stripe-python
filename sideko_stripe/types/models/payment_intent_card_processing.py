import pydantic
import typing

from .payment_intent_processing_customer_notification import (
    PaymentIntentProcessingCustomerNotification,
)


class PaymentIntentCardProcessing(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    customer_notification: typing.Optional[
        PaymentIntentProcessingCustomerNotification
    ] = pydantic.Field(alias="customer_notification", default=None)
