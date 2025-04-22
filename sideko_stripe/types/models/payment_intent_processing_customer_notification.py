import pydantic
import typing


class PaymentIntentProcessingCustomerNotification(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    approval_requested: typing.Optional[bool] = pydantic.Field(
        alias="approval_requested", default=None
    )
    """
    Whether customer approval has been requested for this payment. For payments greater than INR 15000 or mandate amount, the customer must provide explicit approval of the payment with their bank.
    """
    completes_at: typing.Optional[int] = pydantic.Field(
        alias="completes_at", default=None
    )
    """
    If customer approval is required, they need to provide approval before this time.
    """
