import pydantic

from .connect_embedded_payments_features import ConnectEmbeddedPaymentsFeatures


class ConnectEmbeddedPaymentsConfigClaim(pydantic.BaseModel):
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
    features: ConnectEmbeddedPaymentsFeatures = pydantic.Field(
        alias="features",
    )
