import pydantic
import typing


class TreasuryFinancialAccountsResourceBalanceInboundPending(pydantic.BaseModel):
    """
    Funds not spendable yet, but will become available at a later time.
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
        extra="allow",
    )

    __pydantic_extra__: typing.Dict[str, int]
