import pydantic


class PaymentMethodDomainResourcePaymentMethodStatusDetails(pydantic.BaseModel):
    """
    Contains additional details about the status of a payment method for a specific payment method domain.
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    error_message: str = pydantic.Field(
        alias="error_message",
    )
    """
    The error message associated with the status of the payment method on the domain.
    """
