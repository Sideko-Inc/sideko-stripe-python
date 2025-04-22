import pydantic
import typing_extensions


class InvoiceCreateBodyFromInvoice(typing_extensions.TypedDict):
    """
    Revise an existing invoice. The new invoice will be created in `status=draft`. See the [revision documentation](https://stripe.com/docs/invoicing/invoice-revisions) for more details.
    """

    action: typing_extensions.Required[typing_extensions.Literal["revision"]]

    invoice: typing_extensions.Required[str]


class _SerializerInvoiceCreateBodyFromInvoice(pydantic.BaseModel):
    """
    Serializer for InvoiceCreateBodyFromInvoice handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    action: typing_extensions.Literal["revision"] = pydantic.Field(
        alias="action",
    )
    invoice: str = pydantic.Field(
        alias="invoice",
    )
