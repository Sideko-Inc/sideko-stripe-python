import pydantic
import typing
import typing_extensions

from .bank_connections_resource_balance import BankConnectionsResourceBalance
from .bank_connections_resource_balance_refresh import (
    BankConnectionsResourceBalanceRefresh,
)
from .bank_connections_resource_ownership_refresh import (
    BankConnectionsResourceOwnershipRefresh,
)
from .bank_connections_resource_transaction_refresh import (
    BankConnectionsResourceTransactionRefresh,
)
from .financial_connections_account_ownership1 import (
    FinancialConnectionsAccountOwnership1,
)

if typing_extensions.TYPE_CHECKING:
    from .bank_connections_resource_accountholder import (
        BankConnectionsResourceAccountholder,
    )


class FinancialConnectionsAccount(pydantic.BaseModel):
    """
    A Financial Connections Account represents an account that exists outside of Stripe, to which you have been granted some degree of access.
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    account_holder: typing.Optional["BankConnectionsResourceAccountholder"] = (
        pydantic.Field(alias="account_holder", default=None)
    )
    balance: typing.Optional[BankConnectionsResourceBalance] = pydantic.Field(
        alias="balance", default=None
    )
    balance_refresh: typing.Optional[BankConnectionsResourceBalanceRefresh] = (
        pydantic.Field(alias="balance_refresh", default=None)
    )
    category: typing_extensions.Literal["cash", "credit", "investment", "other"] = (
        pydantic.Field(
            alias="category",
        )
    )
    """
    The type of the account. Account category is further divided in `subcategory`.
    """
    created: int = pydantic.Field(
        alias="created",
    )
    """
    Time at which the object was created. Measured in seconds since the Unix epoch.
    """
    display_name: typing.Optional[str] = pydantic.Field(
        alias="display_name", default=None
    )
    """
    A human-readable name that has been assigned to this account, either by the account holder or by the institution.
    """
    id: str = pydantic.Field(
        alias="id",
    )
    """
    Unique identifier for the object.
    """
    institution_name: str = pydantic.Field(
        alias="institution_name",
    )
    """
    The name of the institution that holds this account.
    """
    last4: typing.Optional[str] = pydantic.Field(alias="last4", default=None)
    """
    The last 4 digits of the account number. If present, this will be 4 numeric characters.
    """
    livemode: bool = pydantic.Field(
        alias="livemode",
    )
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    object: typing_extensions.Literal["financial_connections.account"] = pydantic.Field(
        alias="object",
    )
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    ownership: typing.Optional[
        typing.Union[str, FinancialConnectionsAccountOwnership1]
    ] = pydantic.Field(alias="ownership", default=None)
    """
    The most recent information about the account's owners.
    """
    ownership_refresh: typing.Optional[BankConnectionsResourceOwnershipRefresh] = (
        pydantic.Field(alias="ownership_refresh", default=None)
    )
    permissions: typing.Optional[
        typing.List[
            typing_extensions.Literal[
                "balances", "ownership", "payment_method", "transactions"
            ]
        ]
    ] = pydantic.Field(alias="permissions", default=None)
    """
    The list of permissions granted by this account.
    """
    status: typing_extensions.Literal["active", "disconnected", "inactive"] = (
        pydantic.Field(
            alias="status",
        )
    )
    """
    The status of the link to the account.
    """
    subcategory: typing_extensions.Literal[
        "checking", "credit_card", "line_of_credit", "mortgage", "other", "savings"
    ] = pydantic.Field(
        alias="subcategory",
    )
    """
    If `category` is `cash`, one of:
    
     - `checking`
     - `savings`
     - `other`
    
    If `category` is `credit`, one of:
    
     - `mortgage`
     - `line_of_credit`
     - `credit_card`
     - `other`
    
    If `category` is `investment` or `other`, this will be `other`.
    """
    subscriptions: typing.Optional[
        typing.List[typing_extensions.Literal["transactions"]]
    ] = pydantic.Field(alias="subscriptions", default=None)
    """
    The list of data refresh subscriptions requested on this account.
    """
    supported_payment_method_types: typing.List[
        typing_extensions.Literal["link", "us_bank_account"]
    ] = pydantic.Field(
        alias="supported_payment_method_types",
    )
    """
    The [PaymentMethod type](https://stripe.com/docs/api/payment_methods/object#payment_method_object-type)(s) that can be created from this account.
    """
    transaction_refresh: typing.Optional[BankConnectionsResourceTransactionRefresh] = (
        pydantic.Field(alias="transaction_refresh", default=None)
    )
