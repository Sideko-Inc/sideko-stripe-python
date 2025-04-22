import pydantic
import typing_extensions


class AccountCreateBodyBusinessProfileMonthlyEstimatedRevenue(
    typing_extensions.TypedDict
):
    """
    AccountCreateBodyBusinessProfileMonthlyEstimatedRevenue
    """

    amount: typing_extensions.Required[int]

    currency: typing_extensions.Required[str]


class _SerializerAccountCreateBodyBusinessProfileMonthlyEstimatedRevenue(
    pydantic.BaseModel
):
    """
    Serializer for AccountCreateBodyBusinessProfileMonthlyEstimatedRevenue handling case conversions
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
