import pydantic
import typing


class IssuingAuthorizationTreasury(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    received_credits: typing.List[str] = pydantic.Field(
        alias="received_credits",
    )
    """
    The array of [ReceivedCredits](https://stripe.com/docs/api/treasury/received_credits) associated with this authorization
    """
    received_debits: typing.List[str] = pydantic.Field(
        alias="received_debits",
    )
    """
    The array of [ReceivedDebits](https://stripe.com/docs/api/treasury/received_debits) associated with this authorization
    """
    transaction: typing.Optional[str] = pydantic.Field(
        alias="transaction", default=None
    )
    """
    The Treasury [Transaction](https://stripe.com/docs/api/treasury/transactions) associated with this authorization
    """
