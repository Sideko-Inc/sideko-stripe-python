import pydantic
import typing
import typing_extensions


if typing_extensions.TYPE_CHECKING:
    from .tax_id import TaxId


class AccountInvoicesSettings(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    default_account_tax_ids: typing.Optional[
        typing.List[typing.Union[str, "TaxId"]]
    ] = pydantic.Field(alias="default_account_tax_ids", default=None)
    """
    The list of default Account Tax IDs to automatically include on invoices. Account Tax IDs get added when an invoice is finalized.
    """
    hosted_payment_method_save: typing.Optional[
        typing_extensions.Literal["always", "never", "offer"]
    ] = pydantic.Field(alias="hosted_payment_method_save", default=None)
    """
    Whether payment methods should be saved when a payment is completed for a one-time invoices on a hosted invoice page.
    """
