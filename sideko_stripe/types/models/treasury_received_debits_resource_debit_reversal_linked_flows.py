import pydantic
import typing


class TreasuryReceivedDebitsResourceDebitReversalLinkedFlows(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    issuing_dispute: typing.Optional[str] = pydantic.Field(
        alias="issuing_dispute", default=None
    )
    """
    Set if there is an Issuing dispute associated with the DebitReversal.
    """
