import pydantic
import typing


class PaymentIntentNextActionCardAwaitNotification(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    charge_attempt_at: typing.Optional[int] = pydantic.Field(
        alias="charge_attempt_at", default=None
    )
    """
    The time that payment will be attempted. If customer approval is required, they need to provide approval before this time.
    """
    customer_approval_required: typing.Optional[bool] = pydantic.Field(
        alias="customer_approval_required", default=None
    )
    """
    For payments greater than INR 15000, the customer must provide explicit approval of the payment with their bank. For payments of lower amount, no customer action is required.
    """
