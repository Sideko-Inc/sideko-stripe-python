import pydantic


class ConnectEmbeddedIssuingCardFeatures(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    card_management: bool = pydantic.Field(
        alias="card_management",
    )
    """
    Whether to allow card management features.
    """
    card_spend_dispute_management: bool = pydantic.Field(
        alias="card_spend_dispute_management",
    )
    """
    Whether to allow card spend dispute management features.
    """
    cardholder_management: bool = pydantic.Field(
        alias="cardholder_management",
    )
    """
    Whether to allow cardholder management features.
    """
    spend_control_management: bool = pydantic.Field(
        alias="spend_control_management",
    )
    """
    Whether to allow spend control management features.
    """
