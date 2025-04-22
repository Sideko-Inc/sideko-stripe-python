import pydantic
import typing
import typing_extensions

from .account_sessions_create_body_components_financial_account_features import (
    AccountSessionsCreateBodyComponentsFinancialAccountFeatures,
    _SerializerAccountSessionsCreateBodyComponentsFinancialAccountFeatures,
)


class AccountSessionsCreateBodyComponentsFinancialAccount(typing_extensions.TypedDict):
    """
    AccountSessionsCreateBodyComponentsFinancialAccount
    """

    enabled: typing_extensions.Required[bool]

    features: typing_extensions.NotRequired[
        AccountSessionsCreateBodyComponentsFinancialAccountFeatures
    ]


class _SerializerAccountSessionsCreateBodyComponentsFinancialAccount(
    pydantic.BaseModel
):
    """
    Serializer for AccountSessionsCreateBodyComponentsFinancialAccount handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    enabled: bool = pydantic.Field(
        alias="enabled",
    )
    features: typing.Optional[
        _SerializerAccountSessionsCreateBodyComponentsFinancialAccountFeatures
    ] = pydantic.Field(alias="features", default=None)
