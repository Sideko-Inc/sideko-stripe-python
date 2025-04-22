import pydantic


class ConnectEmbeddedFinancialAccountTransactionsFeatures(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    card_spend_dispute_management: bool = pydantic.Field(
        alias="card_spend_dispute_management",
    )
    """
    Whether to allow card spend dispute management features.
    """
