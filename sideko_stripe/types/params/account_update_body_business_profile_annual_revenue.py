import pydantic
import typing_extensions


class AccountUpdateBodyBusinessProfileAnnualRevenue(typing_extensions.TypedDict):
    """
    AccountUpdateBodyBusinessProfileAnnualRevenue
    """

    amount: typing_extensions.Required[int]

    currency: typing_extensions.Required[str]

    fiscal_year_end: typing_extensions.Required[str]


class _SerializerAccountUpdateBodyBusinessProfileAnnualRevenue(pydantic.BaseModel):
    """
    Serializer for AccountUpdateBodyBusinessProfileAnnualRevenue handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    amount: int = pydantic.Field(
        alias="amount",
    )
    currency: str = pydantic.Field(
        alias="currency",
    )
    fiscal_year_end: str = pydantic.Field(
        alias="fiscal_year_end",
    )
