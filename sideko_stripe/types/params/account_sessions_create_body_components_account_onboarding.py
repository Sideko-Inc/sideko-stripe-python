import pydantic
import typing
import typing_extensions

from .account_sessions_create_body_components_account_onboarding_features import (
    AccountSessionsCreateBodyComponentsAccountOnboardingFeatures,
    _SerializerAccountSessionsCreateBodyComponentsAccountOnboardingFeatures,
)


class AccountSessionsCreateBodyComponentsAccountOnboarding(typing_extensions.TypedDict):
    """
    AccountSessionsCreateBodyComponentsAccountOnboarding
    """

    enabled: typing_extensions.Required[bool]

    features: typing_extensions.NotRequired[
        AccountSessionsCreateBodyComponentsAccountOnboardingFeatures
    ]


class _SerializerAccountSessionsCreateBodyComponentsAccountOnboarding(
    pydantic.BaseModel
):
    """
    Serializer for AccountSessionsCreateBodyComponentsAccountOnboarding handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    enabled: bool = pydantic.Field(
        alias="enabled",
    )
    features: typing.Optional[
        _SerializerAccountSessionsCreateBodyComponentsAccountOnboardingFeatures
    ] = pydantic.Field(alias="features", default=None)
