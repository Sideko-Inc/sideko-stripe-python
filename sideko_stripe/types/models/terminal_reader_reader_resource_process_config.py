import pydantic
import typing

from .terminal_reader_reader_resource_tipping_config import (
    TerminalReaderReaderResourceTippingConfig,
)


class TerminalReaderReaderResourceProcessConfig(pydantic.BaseModel):
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
    Enable customer initiated cancellation when processing this payment.
    """
    skip_tipping: typing.Optional[bool] = pydantic.Field(
        alias="skip_tipping", default=None
    )
    """
    Override showing a tipping selection screen on this transaction.
    """
    tipping: typing.Optional[TerminalReaderReaderResourceTippingConfig] = (
        pydantic.Field(alias="tipping", default=None)
    )
    """
    Represents a per-transaction tipping configuration
    """
