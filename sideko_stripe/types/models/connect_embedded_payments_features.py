import pydantic


class ConnectEmbeddedPaymentsFeatures(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    capture_payments: bool = pydantic.Field(
        alias="capture_payments",
    )
    """
    Whether to allow capturing and cancelling payment intents. This is `true` by default.
    """
    destination_on_behalf_of_charge_management: bool = pydantic.Field(
        alias="destination_on_behalf_of_charge_management",
    )
    """
    Whether to allow connected accounts to manage destination charges that are created on behalf of them. This is `false` by default.
    """
    dispute_management: bool = pydantic.Field(
        alias="dispute_management",
    )
    """
    Whether to allow responding to disputes, including submitting evidence and accepting disputes. This is `true` by default.
    """
    refund_management: bool = pydantic.Field(
        alias="refund_management",
    )
    """
    Whether to allow sending refunds. This is `true` by default.
    """
