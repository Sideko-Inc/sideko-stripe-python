import pydantic

from .connect_embedded_payouts_features import ConnectEmbeddedPayoutsFeatures


class ConnectEmbeddedPayoutsConfig(pydantic.BaseModel):
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
    features: ConnectEmbeddedPayoutsFeatures = pydantic.Field(
        alias="features",
    )
