import pydantic

from .connect_embedded_account_features_claim import ConnectEmbeddedAccountFeaturesClaim


class ConnectEmbeddedAccountConfigClaim(pydantic.BaseModel):
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
    features: ConnectEmbeddedAccountFeaturesClaim = pydantic.Field(
        alias="features",
    )
