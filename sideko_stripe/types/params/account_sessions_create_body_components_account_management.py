import pydantic
import typing
import typing_extensions

from .account_sessions_create_body_components_account_management_features import (
    AccountSessionsCreateBodyComponentsAccountManagementFeatures,
    _SerializerAccountSessionsCreateBodyComponentsAccountManagementFeatures,
)


class AccountSessionsCreateBodyComponentsAccountManagement(typing_extensions.TypedDict):
    """
    AccountSessionsCreateBodyComponentsAccountManagement
    """

    enabled: typing_extensions.Required[bool]

    features: typing_extensions.NotRequired[
        AccountSessionsCreateBodyComponentsAccountManagementFeatures
    ]


class _SerializerAccountSessionsCreateBodyComponentsAccountManagement(
    pydantic.BaseModel
):
    """
    Serializer for AccountSessionsCreateBodyComponentsAccountManagement handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    enabled: bool = pydantic.Field(
        alias="enabled",
    )
    features: typing.Optional[
        _SerializerAccountSessionsCreateBodyComponentsAccountManagementFeatures
    ] = pydantic.Field(alias="features", default=None)
