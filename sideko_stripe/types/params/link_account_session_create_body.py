import pydantic
import typing
import typing_extensions

from .link_account_session_create_body_account_holder import (
    LinkAccountSessionCreateBodyAccountHolder,
    _SerializerLinkAccountSessionCreateBodyAccountHolder,
)
from .link_account_session_create_body_filters import (
    LinkAccountSessionCreateBodyFilters,
    _SerializerLinkAccountSessionCreateBodyFilters,
)


class LinkAccountSessionCreateBody(typing_extensions.TypedDict, total=False):
    """
    LinkAccountSessionCreateBody
    """

    account_holder: typing_extensions.Required[
        LinkAccountSessionCreateBodyAccountHolder
    ]
    """
    The account holder to link accounts for.
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """

    filters: typing_extensions.NotRequired[LinkAccountSessionCreateBodyFilters]
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


class _SerializerLinkAccountSessionCreateBody(pydantic.BaseModel):
    """
    Serializer for LinkAccountSessionCreateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    account_holder: _SerializerLinkAccountSessionCreateBodyAccountHolder = (
        pydantic.Field(
            alias="account_holder",
        )
    )
    expand: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="expand", default=None
    )
    filters: typing.Optional[_SerializerLinkAccountSessionCreateBodyFilters] = (
        pydantic.Field(alias="filters", default=None)
    )
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
