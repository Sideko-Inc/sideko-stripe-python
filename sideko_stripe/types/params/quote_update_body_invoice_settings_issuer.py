import pydantic
import typing
import typing_extensions


class QuoteUpdateBodyInvoiceSettingsIssuer(typing_extensions.TypedDict):
    """
    QuoteUpdateBodyInvoiceSettingsIssuer
    """

    account: typing_extensions.NotRequired[str]

    type_: typing_extensions.Required[typing_extensions.Literal["account", "self"]]


class _SerializerQuoteUpdateBodyInvoiceSettingsIssuer(pydantic.BaseModel):
    """
    Serializer for QuoteUpdateBodyInvoiceSettingsIssuer handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    account: typing.Optional[str] = pydantic.Field(alias="account", default=None)
    type_: typing_extensions.Literal["account", "self"] = pydantic.Field(
        alias="type",
    )
