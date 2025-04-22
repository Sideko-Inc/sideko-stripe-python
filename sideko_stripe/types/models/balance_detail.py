import pydantic
import typing

from .balance_amount import BalanceAmount


class BalanceDetail(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    available: typing.List[BalanceAmount] = pydantic.Field(
        alias="available",
    )
    """
    Funds that are available for use.
    """
