import pydantic
import typing


class TreasuryReceivedDebitsResourceStatusTransitions(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    completed_at: typing.Optional[int] = pydantic.Field(
        alias="completed_at", default=None
    )
    """
    Timestamp describing when the DebitReversal changed status to `completed`.
    """
