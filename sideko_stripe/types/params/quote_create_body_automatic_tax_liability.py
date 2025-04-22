import pydantic
import typing
import typing_extensions


class QuoteCreateBodyAutomaticTaxLiability(typing_extensions.TypedDict):
    """
    QuoteCreateBodyAutomaticTaxLiability
    """

    account: typing_extensions.NotRequired[str]

    type_: typing_extensions.Required[typing_extensions.Literal["account", "self"]]


class _SerializerQuoteCreateBodyAutomaticTaxLiability(pydantic.BaseModel):
    """
    Serializer for QuoteCreateBodyAutomaticTaxLiability handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    account: typing.Optional[str] = pydantic.Field(alias="account", default=None)
    type_: typing_extensions.Literal["account", "self"] = pydantic.Field(
        alias="type",
    )
