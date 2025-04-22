import pydantic
import typing_extensions


class FinancialConnectionsTransactionListTransactionRefresh(
    typing_extensions.TypedDict
):
    """
    A filter on the list based on the object `transaction_refresh` field. The value can be a dictionary with the following options:
    """

    after: typing_extensions.Required[str]


class _SerializerFinancialConnectionsTransactionListTransactionRefresh(
    pydantic.BaseModel
):
    """
    Serializer for FinancialConnectionsTransactionListTransactionRefresh handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    after: str = pydantic.Field(
        alias="after",
    )
