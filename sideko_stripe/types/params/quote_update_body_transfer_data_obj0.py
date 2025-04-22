import pydantic
import typing
import typing_extensions


class QuoteUpdateBodyTransferDataObj0(typing_extensions.TypedDict):
    """
    QuoteUpdateBodyTransferDataObj0
    """

    amount: typing_extensions.NotRequired[int]

    amount_percent: typing_extensions.NotRequired[float]

    destination: typing_extensions.Required[str]


class _SerializerQuoteUpdateBodyTransferDataObj0(pydantic.BaseModel):
    """
    Serializer for QuoteUpdateBodyTransferDataObj0 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    amount: typing.Optional[int] = pydantic.Field(alias="amount", default=None)
    amount_percent: typing.Optional[float] = pydantic.Field(
        alias="amount_percent", default=None
    )
    destination: str = pydantic.Field(
        alias="destination",
    )
