import pydantic
import typing
import typing_extensions


class AccountSessionsCreateBodyComponentsPayoutsFeatures(typing_extensions.TypedDict):
    """
    AccountSessionsCreateBodyComponentsPayoutsFeatures
    """

    disable_stripe_user_authentication: typing_extensions.NotRequired[bool]

    edit_payout_schedule: typing_extensions.NotRequired[bool]

    external_account_collection: typing_extensions.NotRequired[bool]

    instant_payouts: typing_extensions.NotRequired[bool]

    standard_payouts: typing_extensions.NotRequired[bool]


class _SerializerAccountSessionsCreateBodyComponentsPayoutsFeatures(pydantic.BaseModel):
    """
    Serializer for AccountSessionsCreateBodyComponentsPayoutsFeatures handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    disable_stripe_user_authentication: typing.Optional[bool] = pydantic.Field(
        alias="disable_stripe_user_authentication", default=None
    )
    edit_payout_schedule: typing.Optional[bool] = pydantic.Field(
        alias="edit_payout_schedule", default=None
    )
    external_account_collection: typing.Optional[bool] = pydantic.Field(
        alias="external_account_collection", default=None
    )
    instant_payouts: typing.Optional[bool] = pydantic.Field(
        alias="instant_payouts", default=None
    )
    standard_payouts: typing.Optional[bool] = pydantic.Field(
        alias="standard_payouts", default=None
    )
