import pydantic
import typing


class TreasuryFinancialAccountsResourceBalanceCash(pydantic.BaseModel):
    """
    Funds the user can spend right now.
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
        extra="allow",
    )

    __pydantic_extra__: typing.Dict[str, int]
