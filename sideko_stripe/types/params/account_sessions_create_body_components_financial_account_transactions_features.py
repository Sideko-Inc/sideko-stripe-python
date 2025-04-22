import pydantic
import typing
import typing_extensions


class AccountSessionsCreateBodyComponentsFinancialAccountTransactionsFeatures(
    typing_extensions.TypedDict
):
    """
    AccountSessionsCreateBodyComponentsFinancialAccountTransactionsFeatures
    """

    card_spend_dispute_management: typing_extensions.NotRequired[bool]


class _SerializerAccountSessionsCreateBodyComponentsFinancialAccountTransactionsFeatures(
    pydantic.BaseModel
):
    """
    Serializer for AccountSessionsCreateBodyComponentsFinancialAccountTransactionsFeatures handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    card_spend_dispute_management: typing.Optional[bool] = pydantic.Field(
        alias="card_spend_dispute_management", default=None
    )
