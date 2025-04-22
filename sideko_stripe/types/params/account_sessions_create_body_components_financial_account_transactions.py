import pydantic
import typing
import typing_extensions

from .account_sessions_create_body_components_financial_account_transactions_features import (
    AccountSessionsCreateBodyComponentsFinancialAccountTransactionsFeatures,
    _SerializerAccountSessionsCreateBodyComponentsFinancialAccountTransactionsFeatures,
)


class AccountSessionsCreateBodyComponentsFinancialAccountTransactions(
    typing_extensions.TypedDict
):
    """
    AccountSessionsCreateBodyComponentsFinancialAccountTransactions
    """

    enabled: typing_extensions.Required[bool]

    features: typing_extensions.NotRequired[
        AccountSessionsCreateBodyComponentsFinancialAccountTransactionsFeatures
    ]


class _SerializerAccountSessionsCreateBodyComponentsFinancialAccountTransactions(
    pydantic.BaseModel
):
    """
    Serializer for AccountSessionsCreateBodyComponentsFinancialAccountTransactions handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    enabled: bool = pydantic.Field(
        alias="enabled",
    )
    features: typing.Optional[
        _SerializerAccountSessionsCreateBodyComponentsFinancialAccountTransactionsFeatures
    ] = pydantic.Field(alias="features", default=None)
