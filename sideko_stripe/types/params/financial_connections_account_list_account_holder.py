import pydantic
import typing
import typing_extensions


class FinancialConnectionsAccountListAccountHolder(typing_extensions.TypedDict):
    """
    If present, only return accounts that belong to the specified account holder. `account_holder[customer]` and `account_holder[account]` are mutually exclusive.
    """

    account: typing_extensions.NotRequired[str]

    customer: typing_extensions.NotRequired[str]


class _SerializerFinancialConnectionsAccountListAccountHolder(pydantic.BaseModel):
    """
    Serializer for FinancialConnectionsAccountListAccountHolder handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    account: typing.Optional[str] = pydantic.Field(alias="account", default=None)
    customer: typing.Optional[str] = pydantic.Field(alias="customer", default=None)
