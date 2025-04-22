import pydantic
import typing
import typing_extensions


class AccountSessionsCreateBodyComponentsNotificationBannerFeatures(
    typing_extensions.TypedDict
):
    """
    AccountSessionsCreateBodyComponentsNotificationBannerFeatures
    """

    disable_stripe_user_authentication: typing_extensions.NotRequired[bool]

    external_account_collection: typing_extensions.NotRequired[bool]


class _SerializerAccountSessionsCreateBodyComponentsNotificationBannerFeatures(
    pydantic.BaseModel
):
    """
    Serializer for AccountSessionsCreateBodyComponentsNotificationBannerFeatures handling case conversions
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
