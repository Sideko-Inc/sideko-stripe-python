import pydantic
import typing
import typing_extensions


class TreasuryTransactionListCreatedObj0(typing_extensions.TypedDict):
    """
    TreasuryTransactionListCreatedObj0
    """

    gt: typing_extensions.NotRequired[int]

    gte: typing_extensions.NotRequired[int]

    lt: typing_extensions.NotRequired[int]

    lte: typing_extensions.NotRequired[int]


class _SerializerTreasuryTransactionListCreatedObj0(pydantic.BaseModel):
    """
    Serializer for TreasuryTransactionListCreatedObj0 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    gt: typing.Optional[int] = pydantic.Field(alias="gt", default=None)
    gte: typing.Optional[int] = pydantic.Field(alias="gte", default=None)
    lt: typing.Optional[int] = pydantic.Field(alias="lt", default=None)
    lte: typing.Optional[int] = pydantic.Field(alias="lte", default=None)
