import pydantic
import typing


class TreasuryTransactionsResourceAbstractTransactionResourceStatusTransitions(
    pydantic.BaseModel
):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    posted_at: typing.Optional[int] = pydantic.Field(alias="posted_at", default=None)
    """
    Timestamp describing when the Transaction changed status to `posted`.
    """
    void_at: typing.Optional[int] = pydantic.Field(alias="void_at", default=None)
    """
    Timestamp describing when the Transaction changed status to `void`.
    """
