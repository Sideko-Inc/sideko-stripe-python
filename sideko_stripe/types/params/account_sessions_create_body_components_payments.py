import pydantic
import typing
import typing_extensions

from .account_sessions_create_body_components_payments_features import (
    AccountSessionsCreateBodyComponentsPaymentsFeatures,
    _SerializerAccountSessionsCreateBodyComponentsPaymentsFeatures,
)


class AccountSessionsCreateBodyComponentsPayments(typing_extensions.TypedDict):
    """
    AccountSessionsCreateBodyComponentsPayments
    """

    enabled: typing_extensions.Required[bool]

    features: typing_extensions.NotRequired[
        AccountSessionsCreateBodyComponentsPaymentsFeatures
    ]


class _SerializerAccountSessionsCreateBodyComponentsPayments(pydantic.BaseModel):
    """
    Serializer for AccountSessionsCreateBodyComponentsPayments handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    enabled: bool = pydantic.Field(
        alias="enabled",
    )
    features: typing.Optional[
        _SerializerAccountSessionsCreateBodyComponentsPaymentsFeatures
    ] = pydantic.Field(alias="features", default=None)
