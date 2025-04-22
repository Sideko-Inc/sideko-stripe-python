import pydantic
import typing
import typing_extensions


if typing_extensions.TYPE_CHECKING:
    from .quote import Quote


class QuotesResourceFromQuote(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    is_revision: bool = pydantic.Field(
        alias="is_revision",
    )
    """
    Whether this quote is a revision of a different quote.
    """
    quote: typing.Union[str, "Quote"] = pydantic.Field(
        alias="quote",
    )
    """
    The quote that was cloned.
    """
