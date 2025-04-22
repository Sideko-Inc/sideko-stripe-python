import pydantic


class TreasuryTransactionsResourceBalanceImpact(pydantic.BaseModel):
    """
    Change to a FinancialAccount's balance
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    cash: int = pydantic.Field(
        alias="cash",
    )
    """
    The change made to funds the user can spend right now.
    """
    inbound_pending: int = pydantic.Field(
        alias="inbound_pending",
    )
    """
    The change made to funds that are not spendable yet, but will become available at a later time.
    """
    outbound_pending: int = pydantic.Field(
        alias="outbound_pending",
    )
    """
    The change made to funds in the account, but not spendable because they are being held for pending outbound flows.
    """
