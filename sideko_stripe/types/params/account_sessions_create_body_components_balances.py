import pydantic
import typing
import typing_extensions

from .account_sessions_create_body_components_balances_features import (
    AccountSessionsCreateBodyComponentsBalancesFeatures,
    _SerializerAccountSessionsCreateBodyComponentsBalancesFeatures,
)


class AccountSessionsCreateBodyComponentsBalances(typing_extensions.TypedDict):
    """
    AccountSessionsCreateBodyComponentsBalances
    """

    enabled: typing_extensions.Required[bool]

    features: typing_extensions.NotRequired[
        AccountSessionsCreateBodyComponentsBalancesFeatures
    ]


class _SerializerAccountSessionsCreateBodyComponentsBalances(pydantic.BaseModel):
    """
    Serializer for AccountSessionsCreateBodyComponentsBalances handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    enabled: bool = pydantic.Field(
        alias="enabled",
    )
    features: typing.Optional[
        _SerializerAccountSessionsCreateBodyComponentsBalancesFeatures
    ] = pydantic.Field(alias="features", default=None)
