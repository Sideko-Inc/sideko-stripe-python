import pydantic
import typing
import typing_extensions

from .financial_connections_session_create_body_account_holder import (
    FinancialConnectionsSessionCreateBodyAccountHolder,
    _SerializerFinancialConnectionsSessionCreateBodyAccountHolder,
)
from .financial_connections_session_create_body_filters import (
    FinancialConnectionsSessionCreateBodyFilters,
    _SerializerFinancialConnectionsSessionCreateBodyFilters,
)


class FinancialConnectionsSessionCreateBody(typing_extensions.TypedDict, total=False):
    """
    FinancialConnectionsSessionCreateBody
    """

    account_holder: typing_extensions.Required[
        FinancialConnectionsSessionCreateBodyAccountHolder
    ]
    """
    The account holder to link accounts for.
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """

    filters: typing_extensions.NotRequired[FinancialConnectionsSessionCreateBodyFilters]
    """
    Filters to restrict the kinds of accounts to collect.
    """

    permissions: typing_extensions.Required[
        typing.List[
            typing_extensions.Literal[
                "balances", "ownership", "payment_method", "transactions"
            ]
        ]
    ]
    """
    List of data features that you would like to request access to.
    
    Possible values are `balances`, `transactions`, `ownership`, and `payment_method`.
    """

    prefetch: typing_extensions.NotRequired[
        typing.List[typing_extensions.Literal["balances", "ownership", "transactions"]]
    ]
    """
    List of data features that you would like to retrieve upon account creation.
    """

    return_url: typing_extensions.NotRequired[str]
    """
    For webview integrations only. Upon completing OAuth login in the native browser, the user will be redirected to this URL to return to your app.
    """


class _SerializerFinancialConnectionsSessionCreateBody(pydantic.BaseModel):
    """
    Serializer for FinancialConnectionsSessionCreateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    account_holder: _SerializerFinancialConnectionsSessionCreateBodyAccountHolder = (
        pydantic.Field(
            alias="account_holder",
        )
    )
    expand: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="expand", default=None
    )
    filters: typing.Optional[
        _SerializerFinancialConnectionsSessionCreateBodyFilters
    ] = pydantic.Field(alias="filters", default=None)
    permissions: typing.List[
        typing_extensions.Literal[
            "balances", "ownership", "payment_method", "transactions"
        ]
    ] = pydantic.Field(
        alias="permissions",
    )
    prefetch: typing.Optional[
        typing.List[typing_extensions.Literal["balances", "ownership", "transactions"]]
    ] = pydantic.Field(alias="prefetch", default=None)
    return_url: typing.Optional[str] = pydantic.Field(alias="return_url", default=None)
