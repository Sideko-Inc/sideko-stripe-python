import pydantic
import typing

from .bank_connections_resource_balance_api_resource_cash_balance_available import (
    BankConnectionsResourceBalanceApiResourceCashBalanceAvailable,
)


class BankConnectionsResourceBalanceApiResourceCashBalance(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    available: typing.Optional[
        BankConnectionsResourceBalanceApiResourceCashBalanceAvailable
    ] = pydantic.Field(alias="available", default=None)
    """
    The funds available to the account holder. Typically this is the current balance after subtracting any outbound pending transactions and adding any inbound pending transactions.
    
    Each key is a three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase.
    
    Each value is a integer amount. A positive amount indicates money owed to the account holder. A negative amount indicates money owed by the account holder.
    """
