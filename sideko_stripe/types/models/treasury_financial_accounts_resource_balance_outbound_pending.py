import pydantic
import typing


class TreasuryFinancialAccountsResourceBalanceOutboundPending(pydantic.BaseModel):
    """
    Funds in the account, but not spendable because they are being held for pending outbound flows.
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
        extra="allow",
    )

    __pydantic_extra__: typing.Dict[str, int]
