import pydantic
import typing


class InvoicesPaymentsInvoicePaymentStatusTransitions(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    canceled_at: typing.Optional[int] = pydantic.Field(
        alias="canceled_at", default=None
    )
    """
    The time that the payment was canceled.
    """
    paid_at: typing.Optional[int] = pydantic.Field(alias="paid_at", default=None)
    """
    The time that the payment succeeded.
    """
