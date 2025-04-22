import pydantic
import typing
import typing_extensions


if typing_extensions.TYPE_CHECKING:
    from .invoice import Invoice


class InvoicesResourceFromInvoice(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    action: str = pydantic.Field(
        alias="action",
    )
    """
    The relation between this invoice and the cloned invoice
    """
    invoice: typing.Union[str, "Invoice"] = pydantic.Field(
        alias="invoice",
    )
    """
    The invoice that was cloned.
    """
