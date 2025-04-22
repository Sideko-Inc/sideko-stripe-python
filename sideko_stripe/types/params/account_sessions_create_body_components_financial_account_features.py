import pydantic
import typing
import typing_extensions


class AccountSessionsCreateBodyComponentsFinancialAccountFeatures(
    typing_extensions.TypedDict
):
    """
    AccountSessionsCreateBodyComponentsFinancialAccountFeatures
    """

    disable_stripe_user_authentication: typing_extensions.NotRequired[bool]

    external_account_collection: typing_extensions.NotRequired[bool]

    send_money: typing_extensions.NotRequired[bool]

    transfer_balance: typing_extensions.NotRequired[bool]


class _SerializerAccountSessionsCreateBodyComponentsFinancialAccountFeatures(
    pydantic.BaseModel
):
    """
    Serializer for AccountSessionsCreateBodyComponentsFinancialAccountFeatures handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    disable_stripe_user_authentication: typing.Optional[bool] = pydantic.Field(
        alias="disable_stripe_user_authentication", default=None
    )
    external_account_collection: typing.Optional[bool] = pydantic.Field(
        alias="external_account_collection", default=None
    )
    send_money: typing.Optional[bool] = pydantic.Field(alias="send_money", default=None)
    transfer_balance: typing.Optional[bool] = pydantic.Field(
        alias="transfer_balance", default=None
    )
