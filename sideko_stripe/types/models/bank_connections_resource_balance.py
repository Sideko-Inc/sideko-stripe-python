import pydantic
import typing
import typing_extensions

from .bank_connections_resource_balance_api_resource_cash_balance import (
    BankConnectionsResourceBalanceApiResourceCashBalance,
)
from .bank_connections_resource_balance_api_resource_credit_balance import (
    BankConnectionsResourceBalanceApiResourceCreditBalance,
)
from .bank_connections_resource_balance_current import (
    BankConnectionsResourceBalanceCurrent,
)


class BankConnectionsResourceBalance(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    as_of: int = pydantic.Field(
        alias="as_of",
    )
    """
    The time that the external institution calculated this balance. Measured in seconds since the Unix epoch.
    """
    cash: typing.Optional[BankConnectionsResourceBalanceApiResourceCashBalance] = (
        pydantic.Field(alias="cash", default=None)
    )
    credit: typing.Optional[BankConnectionsResourceBalanceApiResourceCreditBalance] = (
        pydantic.Field(alias="credit", default=None)
    )
    current: BankConnectionsResourceBalanceCurrent = pydantic.Field(
        alias="current",
    )
    """
    The balances owed to (or by) the account holder, before subtracting any outbound pending transactions or adding any inbound pending transactions.
    
    Each key is a three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase.
    
    Each value is a integer amount. A positive amount indicates money owed to the account holder. A negative amount indicates money owed by the account holder.
    """
    type_: typing_extensions.Literal["cash", "credit"] = pydantic.Field(
        alias="type",
    )
    """
    The `type` of the balance. An additional hash is included on the balance with a name matching this value.
    """
