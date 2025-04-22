import pydantic
import typing
import typing_extensions


class QuoteCreateBodyFromQuote(typing_extensions.TypedDict):
    """
    Clone an existing quote. The new quote will be created in `status=draft`. When using this parameter, you cannot specify any other parameters except for `expires_at`.
    """

    is_revision: typing_extensions.NotRequired[bool]

    quote: typing_extensions.Required[str]


class _SerializerQuoteCreateBodyFromQuote(pydantic.BaseModel):
    """
    Serializer for QuoteCreateBodyFromQuote handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    is_revision: typing.Optional[bool] = pydantic.Field(
        alias="is_revision", default=None
    )
    quote: str = pydantic.Field(
        alias="quote",
    )
