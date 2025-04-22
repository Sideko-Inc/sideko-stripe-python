import pydantic
import typing

from .balance_amount_by_source_type import BalanceAmountBySourceType
from .balance_net_available import BalanceNetAvailable


class BalanceAmountNet(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    amount: int = pydantic.Field(
        alias="amount",
    )
    """
    Balance amount.
    """
    currency: str = pydantic.Field(
        alias="currency",
    )
    """
    Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    """
    net_available: typing.Optional[typing.List[BalanceNetAvailable]] = pydantic.Field(
        alias="net_available", default=None
    )
    """
    Breakdown of balance by destination.
    """
    source_types: typing.Optional[BalanceAmountBySourceType] = pydantic.Field(
        alias="source_types", default=None
    )
