import pydantic
import typing_extensions

from .financial_connections_account_ownership_owners import (
    FinancialConnectionsAccountOwnershipOwners,
)


class FinancialConnectionsAccountOwnership1(pydantic.BaseModel):
    """
    Describes a snapshot of the owners of an account at a particular point in time.
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    created: int = pydantic.Field(
        alias="created",
    )
    """
    Time at which the object was created. Measured in seconds since the Unix epoch.
    """
    id: str = pydantic.Field(
        alias="id",
    )
    """
    Unique identifier for the object.
    """
    object: typing_extensions.Literal["financial_connections.account_ownership"] = (
        pydantic.Field(
            alias="object",
        )
    )
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    owners: FinancialConnectionsAccountOwnershipOwners = pydantic.Field(
        alias="owners",
    )
    """
    A paginated list of owners for this account.
    """
