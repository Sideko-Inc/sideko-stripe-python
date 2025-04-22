import pydantic
import typing


class TerminalReaderReaderResourceRefundPaymentConfig(pydantic.BaseModel):
    """
    Represents a per-transaction override of a reader configuration
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    enable_customer_cancellation: typing.Optional[bool] = pydantic.Field(
        alias="enable_customer_cancellation", default=None
    )
    """
    Enable customer initiated cancellation when refunding this payment.
    """
