import pydantic
import typing
import typing_extensions


class TreasuryFinancialAccountsResourcePlatformRestrictions(pydantic.BaseModel):
    """
    Restrictions that a Connect Platform has placed on this FinancialAccount.
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    inbound_flows: typing.Optional[
        typing_extensions.Literal["restricted", "unrestricted"]
    ] = pydantic.Field(alias="inbound_flows", default=None)
    """
    Restricts all inbound money movement.
    """
    outbound_flows: typing.Optional[
        typing_extensions.Literal["restricted", "unrestricted"]
    ] = pydantic.Field(alias="outbound_flows", default=None)
    """
    Restricts all outbound money movement.
    """
