import pydantic
import typing


class IssuingTransactionAmountDetails(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    atm_fee: typing.Optional[int] = pydantic.Field(alias="atm_fee", default=None)
    """
    The fee charged by the ATM for the cash withdrawal.
    """
    cashback_amount: typing.Optional[int] = pydantic.Field(
        alias="cashback_amount", default=None
    )
    """
    The amount of cash requested by the cardholder.
    """
