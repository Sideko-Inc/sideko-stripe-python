import pydantic

from .treasury_financial_accounts_resource_balance_cash import (
    TreasuryFinancialAccountsResourceBalanceCash,
)
from .treasury_financial_accounts_resource_balance_inbound_pending import (
    TreasuryFinancialAccountsResourceBalanceInboundPending,
)
from .treasury_financial_accounts_resource_balance_outbound_pending import (
    TreasuryFinancialAccountsResourceBalanceOutboundPending,
)


class TreasuryFinancialAccountsResourceBalance(pydantic.BaseModel):
    """
    Balance information for the FinancialAccount
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    cash: TreasuryFinancialAccountsResourceBalanceCash = pydantic.Field(
        alias="cash",
    )
    """
    Funds the user can spend right now.
    """
    inbound_pending: TreasuryFinancialAccountsResourceBalanceInboundPending = (
        pydantic.Field(
            alias="inbound_pending",
        )
    )
    """
    Funds not spendable yet, but will become available at a later time.
    """
    outbound_pending: TreasuryFinancialAccountsResourceBalanceOutboundPending = (
        pydantic.Field(
            alias="outbound_pending",
        )
    )
    """
    Funds in the account, but not spendable because they are being held for pending outbound flows.
    """
