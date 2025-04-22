import pydantic
import typing


class TerminalReaderReaderResourceTippingConfig(pydantic.BaseModel):
    """
    Represents a per-transaction tipping configuration
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    amount_eligible: typing.Optional[int] = pydantic.Field(
        alias="amount_eligible", default=None
    )
    """
    Amount used to calculate tip suggestions on tipping selection screen for this transaction. Must be a positive integer in the smallest currency unit (e.g., 100 cents to represent $1.00 or 100 to represent ¥100, a zero-decimal currency).
    """
