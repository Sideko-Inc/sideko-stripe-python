import pydantic
import typing
import typing_extensions

from .account_sessions_create_body_components_notification_banner_features import (
    AccountSessionsCreateBodyComponentsNotificationBannerFeatures,
    _SerializerAccountSessionsCreateBodyComponentsNotificationBannerFeatures,
)


class AccountSessionsCreateBodyComponentsNotificationBanner(
    typing_extensions.TypedDict
):
    """
    AccountSessionsCreateBodyComponentsNotificationBanner
    """

    enabled: typing_extensions.Required[bool]

    features: typing_extensions.NotRequired[
        AccountSessionsCreateBodyComponentsNotificationBannerFeatures
    ]


class _SerializerAccountSessionsCreateBodyComponentsNotificationBanner(
    pydantic.BaseModel
):
    """
    Serializer for AccountSessionsCreateBodyComponentsNotificationBanner handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    enabled: bool = pydantic.Field(
        alias="enabled",
    )
    features: typing.Optional[
        _SerializerAccountSessionsCreateBodyComponentsNotificationBannerFeatures
    ] = pydantic.Field(alias="features", default=None)
