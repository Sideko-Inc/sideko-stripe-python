import pydantic
import typing

from .bank_connections_resource_balance_api_resource_credit_balance_used import (
    BankConnectionsResourceBalanceApiResourceCreditBalanceUsed,
)


class BankConnectionsResourceBalanceApiResourceCreditBalance(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    used: typing.Optional[
        BankConnectionsResourceBalanceApiResourceCreditBalanceUsed
    ] = pydantic.Field(alias="used", default=None)
    """
    The credit that has been used by the account holder.
    
    Each key is a three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase.
    
    Each value is a integer amount. A positive amount indicates money owed to the account holder. A negative amount indicates money owed by the account holder.
    """
