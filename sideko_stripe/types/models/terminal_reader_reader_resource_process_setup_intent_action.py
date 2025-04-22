import pydantic
import typing
import typing_extensions

from .terminal_reader_reader_resource_process_setup_config import (
    TerminalReaderReaderResourceProcessSetupConfig,
)

if typing_extensions.TYPE_CHECKING:
    from .setup_intent import SetupIntent


class TerminalReaderReaderResourceProcessSetupIntentAction(pydantic.BaseModel):
    """
    Represents a reader action to process a setup intent
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    generated_card: typing.Optional[str] = pydantic.Field(
        alias="generated_card", default=None
    )
    """
    ID of a card PaymentMethod generated from the card_present PaymentMethod that may be attached to a Customer for future transactions. Only present if it was possible to generate a card PaymentMethod.
    """
    process_config: typing.Optional[TerminalReaderReaderResourceProcessSetupConfig] = (
        pydantic.Field(alias="process_config", default=None)
    )
    """
    Represents a per-setup override of a reader configuration
    """
    setup_intent: typing.Union[str, "SetupIntent"] = pydantic.Field(
        alias="setup_intent",
    )
    """
    Most recent SetupIntent processed by the reader.
    """
