import pydantic
import typing
import typing_extensions

from .terminal_reader_reader_resource_set_reader_display_action import (
    TerminalReaderReaderResourceSetReaderDisplayAction,
)

if typing_extensions.TYPE_CHECKING:
    from .terminal_reader_reader_resource_process_payment_intent_action import (
        TerminalReaderReaderResourceProcessPaymentIntentAction,
    )
    from .terminal_reader_reader_resource_process_setup_intent_action import (
        TerminalReaderReaderResourceProcessSetupIntentAction,
    )
    from .terminal_reader_reader_resource_refund_payment_action import (
        TerminalReaderReaderResourceRefundPaymentAction,
    )


class TerminalReaderReaderResourceReaderAction(pydantic.BaseModel):
    """
    Represents an action performed by the reader
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    failure_code: typing.Optional[str] = pydantic.Field(
        alias="failure_code", default=None
    )
    """
    Failure code, only set if status is `failed`.
    """
    failure_message: typing.Optional[str] = pydantic.Field(
        alias="failure_message", default=None
    )
    """
    Detailed failure message, only set if status is `failed`.
    """
    process_payment_intent: typing.Optional[
        "TerminalReaderReaderResourceProcessPaymentIntentAction"
    ] = pydantic.Field(alias="process_payment_intent", default=None)
    """
    Represents a reader action to process a payment intent
    """
    process_setup_intent: typing.Optional[
        "TerminalReaderReaderResourceProcessSetupIntentAction"
    ] = pydantic.Field(alias="process_setup_intent", default=None)
    """
    Represents a reader action to process a setup intent
    """
    refund_payment: typing.Optional[
        "TerminalReaderReaderResourceRefundPaymentAction"
    ] = pydantic.Field(alias="refund_payment", default=None)
    """
    Represents a reader action to refund a payment
    """
    set_reader_display: typing.Optional[
        TerminalReaderReaderResourceSetReaderDisplayAction
    ] = pydantic.Field(alias="set_reader_display", default=None)
    """
    Represents a reader action to set the reader display
    """
    status: typing_extensions.Literal["failed", "in_progress", "succeeded"] = (
        pydantic.Field(
            alias="status",
        )
    )
    """
    Status of the action performed by the reader.
    """
    type_: typing_extensions.Literal[
        "process_payment_intent",
        "process_setup_intent",
        "refund_payment",
        "set_reader_display",
    ] = pydantic.Field(
        alias="type",
    )
    """
    Type of action performed by the reader.
    """
