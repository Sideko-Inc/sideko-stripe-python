import pydantic
import typing


class QuotesResourceStatusTransitions(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    accepted_at: typing.Optional[int] = pydantic.Field(
        alias="accepted_at", default=None
    )
    """
    The time that the quote was accepted. Measured in seconds since Unix epoch.
    """
    canceled_at: typing.Optional[int] = pydantic.Field(
        alias="canceled_at", default=None
    )
    """
    The time that the quote was canceled. Measured in seconds since Unix epoch.
    """
    finalized_at: typing.Optional[int] = pydantic.Field(
        alias="finalized_at", default=None
    )
    """
    The time that the quote was finalized. Measured in seconds since Unix epoch.
    """
