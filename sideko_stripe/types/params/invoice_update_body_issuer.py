import pydantic
import typing
import typing_extensions


class InvoiceUpdateBodyIssuer(typing_extensions.TypedDict):
    """
    The connected account that issues the invoice. The invoice is presented with the branding and support information of the specified account.
    """

    account: typing_extensions.NotRequired[str]

    type_: typing_extensions.Required[typing_extensions.Literal["account", "self"]]


class _SerializerInvoiceUpdateBodyIssuer(pydantic.BaseModel):
    """
    Serializer for InvoiceUpdateBodyIssuer handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    account: typing.Optional[str] = pydantic.Field(alias="account", default=None)
    type_: typing_extensions.Literal["account", "self"] = pydantic.Field(
        alias="type",
    )
