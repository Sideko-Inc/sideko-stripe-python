import pydantic


class ConnectEmbeddedPayoutsFeatures(pydantic.BaseModel):
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
    edit_payout_schedule: bool = pydantic.Field(
        alias="edit_payout_schedule",
    )
    """
    Whether to allow payout schedule to be changed. Default `true` when Stripe owns Loss Liability, default `false` otherwise.
    """
    external_account_collection: bool = pydantic.Field(
        alias="external_account_collection",
    )
    """
    Whether to allow platforms to control bank account collection for their connected accounts. This feature can only be false for accounts where you’re responsible for collecting updated information when requirements are due or change, like custom accounts. Otherwise, bank account collection is determined by compliance requirements. The default value for this feature is `true`.
    """
    instant_payouts: bool = pydantic.Field(
        alias="instant_payouts",
    )
    """
    Whether to allow creation of instant payouts. Default `true` when Stripe owns Loss Liability, default `false` otherwise.
    """
    standard_payouts: bool = pydantic.Field(
        alias="standard_payouts",
    )
    """
    Whether to allow creation of standard payouts. Default `true` when Stripe owns Loss Liability, default `false` otherwise.
    """
