import pydantic
import typing


class IssuingDisputeTreasury(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    debit_reversal: typing.Optional[str] = pydantic.Field(
        alias="debit_reversal", default=None
    )
    """
    The Treasury [DebitReversal](https://stripe.com/docs/api/treasury/debit_reversals) representing this Issuing dispute
    """
    received_debit: str = pydantic.Field(
        alias="received_debit",
    )
    """
    The Treasury [ReceivedDebit](https://stripe.com/docs/api/treasury/received_debits) that is being disputed.
    """
