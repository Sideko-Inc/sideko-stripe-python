import pydantic

from .connect_embedded_issuing_card_features import ConnectEmbeddedIssuingCardFeatures


class ConnectEmbeddedIssuingCardConfigClaim(pydantic.BaseModel):
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
    features: ConnectEmbeddedIssuingCardFeatures = pydantic.Field(
        alias="features",
    )
