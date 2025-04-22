import pydantic
import typing
import typing_extensions


class FinancialConnectionsAccountOwner(pydantic.BaseModel):
    """
    Describes an owner of an account.
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    email: typing.Optional[str] = pydantic.Field(alias="email", default=None)
    """
    The email address of the owner.
    """
    id: str = pydantic.Field(
        alias="id",
    )
    """
    Unique identifier for the object.
    """
    name: str = pydantic.Field(
        alias="name",
    )
    """
    The full name of the owner.
    """
    object: typing_extensions.Literal["financial_connections.account_owner"] = (
        pydantic.Field(
            alias="object",
        )
    )
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    ownership: str = pydantic.Field(
        alias="ownership",
    )
    """
    The ownership object that this owner belongs to.
    """
    phone: typing.Optional[str] = pydantic.Field(alias="phone", default=None)
    """
    The raw phone number of the owner.
    """
    raw_address: typing.Optional[str] = pydantic.Field(
        alias="raw_address", default=None
    )
    """
    The raw physical address of the owner.
    """
    refreshed_at: typing.Optional[int] = pydantic.Field(
        alias="refreshed_at", default=None
    )
    """
    The timestamp of the refresh that updated this owner.
    """
