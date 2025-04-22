import pydantic
import typing

from .balance_amount_by_source_type import BalanceAmountBySourceType


class BalanceNetAvailable(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    amount: int = pydantic.Field(
        alias="amount",
    )
    """
    Net balance amount, subtracting fees from platform-set pricing.
    """
    destination: str = pydantic.Field(
        alias="destination",
    )
    """
    ID of the external account for this net balance (not expandable).
    """
    source_types: typing.Optional[BalanceAmountBySourceType] = pydantic.Field(
        alias="source_types", default=None
    )
