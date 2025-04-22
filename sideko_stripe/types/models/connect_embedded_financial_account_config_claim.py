import pydantic

from .connect_embedded_financial_account_features import (
    ConnectEmbeddedFinancialAccountFeatures,
)


class ConnectEmbeddedFinancialAccountConfigClaim(pydantic.BaseModel):
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
    features: ConnectEmbeddedFinancialAccountFeatures = pydantic.Field(
        alias="features",
    )
