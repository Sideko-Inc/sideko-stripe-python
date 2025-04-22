import pydantic


class ConnectEmbeddedIssuingCardsListFeatures(pydantic.BaseModel):
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
    disable_stripe_user_authentication: bool = pydantic.Field(
        alias="disable_stripe_user_authentication",
    )
    """
    Disables Stripe user authentication for this embedded component. This feature can only be false for accounts where you’re responsible for collecting updated information when requirements are due or change, like custom accounts.
    """
    spend_control_management: bool = pydantic.Field(
        alias="spend_control_management",
    )
    """
    Whether to allow spend control management features.
    """
