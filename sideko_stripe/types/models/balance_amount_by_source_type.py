import pydantic
import typing


class BalanceAmountBySourceType(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    bank_account: typing.Optional[int] = pydantic.Field(
        alias="bank_account", default=None
    )
    """
    Amount coming from [legacy US ACH payments](https://docs.stripe.com/ach-deprecated).
    """
    card: typing.Optional[int] = pydantic.Field(alias="card", default=None)
    """
    Amount coming from most payment methods, including cards as well as [non-legacy bank debits](https://docs.stripe.com/payments/bank-debits).
    """
    fpx: typing.Optional[int] = pydantic.Field(alias="fpx", default=None)
    """
    Amount coming from [FPX](https://docs.stripe.com/payments/fpx), a Malaysian payment method.
    """
