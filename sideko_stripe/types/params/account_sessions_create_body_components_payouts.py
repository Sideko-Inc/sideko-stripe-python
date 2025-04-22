import pydantic
import typing
import typing_extensions

from .account_sessions_create_body_components_payouts_features import (
    AccountSessionsCreateBodyComponentsPayoutsFeatures,
    _SerializerAccountSessionsCreateBodyComponentsPayoutsFeatures,
)


class AccountSessionsCreateBodyComponentsPayouts(typing_extensions.TypedDict):
    """
    AccountSessionsCreateBodyComponentsPayouts
    """

    enabled: typing_extensions.Required[bool]

    features: typing_extensions.NotRequired[
        AccountSessionsCreateBodyComponentsPayoutsFeatures
    ]


class _SerializerAccountSessionsCreateBodyComponentsPayouts(pydantic.BaseModel):
    """
    Serializer for AccountSessionsCreateBodyComponentsPayouts handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    enabled: bool = pydantic.Field(
        alias="enabled",
    )
    features: typing.Optional[
        _SerializerAccountSessionsCreateBodyComponentsPayoutsFeatures
    ] = pydantic.Field(alias="features", default=None)
