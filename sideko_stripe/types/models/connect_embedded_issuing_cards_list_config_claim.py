import pydantic

from .connect_embedded_issuing_cards_list_features import (
    ConnectEmbeddedIssuingCardsListFeatures,
)


class ConnectEmbeddedIssuingCardsListConfigClaim(pydantic.BaseModel):
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
    features: ConnectEmbeddedIssuingCardsListFeatures = pydantic.Field(
        alias="features",
    )
