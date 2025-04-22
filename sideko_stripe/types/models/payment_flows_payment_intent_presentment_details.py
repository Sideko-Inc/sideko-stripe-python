import pydantic


class PaymentFlowsPaymentIntentPresentmentDetails(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    presentment_amount: int = pydantic.Field(
        alias="presentment_amount",
    )
    """
    Amount intended to be collected by this payment, denominated in presentment_currency.
    """
    presentment_currency: str = pydantic.Field(
        alias="presentment_currency",
    )
    """
    Currency presented to the customer during payment.
    """
