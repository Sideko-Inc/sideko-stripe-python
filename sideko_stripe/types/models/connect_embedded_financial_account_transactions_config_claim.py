import pydantic

from .connect_embedded_financial_account_transactions_features import (
    ConnectEmbeddedFinancialAccountTransactionsFeatures,
)


class ConnectEmbeddedFinancialAccountTransactionsConfigClaim(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    enabled: bool = pydantic.Field(
        alias="enabled",
    )
    """
    Whether the embedded component is enabled.
    """
    features: ConnectEmbeddedFinancialAccountTransactionsFeatures = pydantic.Field(
        alias="features",
    )
