import pydantic
import typing


class IssuingTransactionTreasury(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    received_credit: typing.Optional[str] = pydantic.Field(
        alias="received_credit", default=None
    )
    """
    The Treasury [ReceivedCredit](https://stripe.com/docs/api/treasury/received_credits) representing this Issuing transaction if it is a refund
    """
    received_debit: typing.Optional[str] = pydantic.Field(
        alias="received_debit", default=None
    )
    """
    The Treasury [ReceivedDebit](https://stripe.com/docs/api/treasury/received_debits) representing this Issuing transaction if it is a capture
    """
