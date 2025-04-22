import pydantic
import typing
import typing_extensions

from .bank_connections_resource_link_account_session_filters import (
    BankConnectionsResourceLinkAccountSessionFilters,
)

if typing_extensions.TYPE_CHECKING:
    from .bank_connections_resource_accountholder import (
        BankConnectionsResourceAccountholder,
    )
    from .financial_connections_session_accounts import (
        FinancialConnectionsSessionAccounts,
    )


class FinancialConnectionsSession(pydantic.BaseModel):
    """
    A Financial Connections Session is the secure way to programmatically launch the client-side Stripe.js modal that lets your users link their accounts.
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    account_holder: typing.Optional["BankConnectionsResourceAccountholder"] = (
        pydantic.Field(alias="account_holder", default=None)
    )
    accounts: "FinancialConnectionsSessionAccounts" = pydantic.Field(
        alias="accounts",
    )
    """
    The accounts that were collected as part of this Session.
    """
    client_secret: str = pydantic.Field(
        alias="client_secret",
    )
    """
    A value that will be passed to the client to launch the authentication flow.
    """
    filters: typing.Optional[BankConnectionsResourceLinkAccountSessionFilters] = (
        pydantic.Field(alias="filters", default=None)
    )
    id: str = pydantic.Field(
        alias="id",
    )
    """
    Unique identifier for the object.
    """
    livemode: bool = pydantic.Field(
        alias="livemode",
    )
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    object: typing_extensions.Literal["financial_connections.session"] = pydantic.Field(
        alias="object",
    )
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    permissions: typing.List[
        typing_extensions.Literal[
            "balances", "ownership", "payment_method", "transactions"
        ]
    ] = pydantic.Field(
        alias="permissions",
    )
    """
    Permissions requested for accounts collected during this session.
    """
    prefetch: typing.Optional[
        typing.List[typing_extensions.Literal["balances", "ownership", "transactions"]]
    ] = pydantic.Field(alias="prefetch", default=None)
    """
    Data features requested to be retrieved upon account creation.
    """
    return_url: typing.Optional[str] = pydantic.Field(alias="return_url", default=None)
    """
    For webview integrations only. Upon completing OAuth login in the native browser, the user will be redirected to this URL to return to your app.
    """
