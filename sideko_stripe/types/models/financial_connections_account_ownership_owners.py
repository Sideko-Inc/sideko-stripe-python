import pydantic
import typing
import typing_extensions

from .financial_connections_account_owner import FinancialConnectionsAccountOwner


class FinancialConnectionsAccountOwnershipOwners(pydantic.BaseModel):
    """
    A paginated list of owners for this account.
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    data: typing.List[FinancialConnectionsAccountOwner] = pydantic.Field(
        alias="data",
    )
    """
    Details about each object.
    """
    has_more: bool = pydantic.Field(
        alias="has_more",
    )
    """
    True if this list has another page of items after this one that can be fetched.
    """
    object: typing_extensions.Literal["list"] = pydantic.Field(
        alias="object",
    )
    """
    String representing the object's type. Objects of the same type share the same value. Always has the value `list`.
    """
    url: str = pydantic.Field(
        alias="url",
    )
    """
    The URL where this list can be accessed.
    """
