import pydantic
import typing


class TreasuryReceivedCreditsResourceStatusTransitions(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    posted_at: typing.Optional[int] = pydantic.Field(alias="posted_at", default=None)
    """
    Timestamp describing when the CreditReversal changed status to `posted`
    """
