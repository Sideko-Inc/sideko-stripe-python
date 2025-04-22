import pydantic
import typing


class BankConnectionsResourceBalanceCurrent(pydantic.BaseModel):
    """
    The balances owed to (or by) the account holder, before subtracting any outbound pending transactions or adding any inbound pending transactions.

    Each key is a three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase.

    Each value is a integer amount. A positive amount indicates money owed to the account holder. A negative amount indicates money owed by the account holder.
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
        extra="allow",
    )

    __pydantic_extra__: typing.Dict[str, int]
