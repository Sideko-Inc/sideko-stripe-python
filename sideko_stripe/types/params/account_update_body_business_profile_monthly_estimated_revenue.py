import pydantic
import typing_extensions


class AccountUpdateBodyBusinessProfileMonthlyEstimatedRevenue(
    typing_extensions.TypedDict
):
    """
    AccountUpdateBodyBusinessProfileMonthlyEstimatedRevenue
    """

    amount: typing_extensions.Required[int]

    currency: typing_extensions.Required[str]


class _SerializerAccountUpdateBodyBusinessProfileMonthlyEstimatedRevenue(
    pydantic.BaseModel
):
    """
    Serializer for AccountUpdateBodyBusinessProfileMonthlyEstimatedRevenue handling case conversions
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
