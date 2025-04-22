import pydantic
import typing
import typing_extensions

from .terminal_reader_reader_resource_process_config import (
    TerminalReaderReaderResourceProcessConfig,
)

if typing_extensions.TYPE_CHECKING:
    from .payment_intent import PaymentIntent


class TerminalReaderReaderResourceProcessPaymentIntentAction(pydantic.BaseModel):
    """
    Represents a reader action to process a payment intent
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    payment_intent: typing.Union[str, "PaymentIntent"] = pydantic.Field(
        alias="payment_intent",
    )
    """
    Most recent PaymentIntent processed by the reader.
    """
    process_config: typing.Optional[TerminalReaderReaderResourceProcessConfig] = (
        pydantic.Field(alias="process_config", default=None)
    )
    """
    Represents a per-transaction override of a reader configuration
    """
