import pydantic


class ConnectEmbeddedFinancialAccountFeatures(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    disable_stripe_user_authentication: bool = pydantic.Field(
        alias="disable_stripe_user_authentication",
    )
    """
    Disables Stripe user authentication for this embedded component. This value can only be true for accounts where `controller.requirement_collection` is `application`. The default value is the opposite of the `external_account_collection` value. For example, if you don’t set `external_account_collection`, it defaults to true and `disable_stripe_user_authentication` defaults to false.
    """
    external_account_collection: bool = pydantic.Field(
        alias="external_account_collection",
    )
    """
    Whether to allow external accounts to be linked for money transfer.
    """
    send_money: bool = pydantic.Field(
        alias="send_money",
    )
    """
    Whether to allow sending money.
    """
    transfer_balance: bool = pydantic.Field(
        alias="transfer_balance",
    )
    """
    Whether to allow transferring balance.
    """
