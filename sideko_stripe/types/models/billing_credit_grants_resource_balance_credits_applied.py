import pydantic
import typing
import typing_extensions


if typing_extensions.TYPE_CHECKING:
    from .invoice import Invoice


class BillingCreditGrantsResourceBalanceCreditsApplied(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    invoice: typing.Union[str, "Invoice"] = pydantic.Field(
        alias="invoice",
    )
    """
    The invoice to which the billing credits were applied.
    """
    invoice_line_item: str = pydantic.Field(
        alias="invoice_line_item",
    )
    """
    The invoice line item to which the billing credits were applied.
    """
