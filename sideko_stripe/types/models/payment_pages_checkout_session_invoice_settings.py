import pydantic
import typing
import typing_extensions

from .deleted_tax_id import DeletedTaxId
from .invoice_setting_checkout_rendering_options import (
    InvoiceSettingCheckoutRenderingOptions,
)
from .invoice_setting_custom_field import InvoiceSettingCustomField
from .payment_pages_checkout_session_invoice_settings_metadata import (
    PaymentPagesCheckoutSessionInvoiceSettingsMetadata,
)

if typing_extensions.TYPE_CHECKING:
    from .connect_account_reference import ConnectAccountReference
    from .tax_id import TaxId


class PaymentPagesCheckoutSessionInvoiceSettings(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    account_tax_ids: typing.Optional[
        typing.List[typing.Union[str, "TaxId", DeletedTaxId]]
    ] = pydantic.Field(alias="account_tax_ids", default=None)
    """
    The account tax IDs associated with the invoice.
    """
    custom_fields: typing.Optional[typing.List[InvoiceSettingCustomField]] = (
        pydantic.Field(alias="custom_fields", default=None)
    )
    """
    Custom fields displayed on the invoice.
    """
    description: typing.Optional[str] = pydantic.Field(
        alias="description", default=None
    )
    """
    An arbitrary string attached to the object. Often useful for displaying to users.
    """
    footer: typing.Optional[str] = pydantic.Field(alias="footer", default=None)
    """
    Footer displayed on the invoice.
    """
    issuer: typing.Optional["ConnectAccountReference"] = pydantic.Field(
        alias="issuer", default=None
    )
    metadata: typing.Optional[PaymentPagesCheckoutSessionInvoiceSettingsMetadata] = (
        pydantic.Field(alias="metadata", default=None)
    )
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    rendering_options: typing.Optional[InvoiceSettingCheckoutRenderingOptions] = (
        pydantic.Field(alias="rendering_options", default=None)
    )
