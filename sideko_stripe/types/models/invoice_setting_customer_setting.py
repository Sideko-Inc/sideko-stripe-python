import pydantic
import typing
import typing_extensions

from .invoice_setting_custom_field import InvoiceSettingCustomField
from .invoice_setting_customer_rendering_options import (
    InvoiceSettingCustomerRenderingOptions,
)

if typing_extensions.TYPE_CHECKING:
    from .payment_method import PaymentMethod


class InvoiceSettingCustomerSetting(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    custom_fields: typing.Optional[typing.List[InvoiceSettingCustomField]] = (
        pydantic.Field(alias="custom_fields", default=None)
    )
    """
    Default custom fields to be displayed on invoices for this customer.
    """
    default_payment_method: typing.Optional[typing.Union[str, "PaymentMethod"]] = (
        pydantic.Field(alias="default_payment_method", default=None)
    )
    """
    ID of a payment method that's attached to the customer, to be used as the customer's default payment method for subscriptions and invoices.
    """
    footer: typing.Optional[str] = pydantic.Field(alias="footer", default=None)
    """
    Default footer to be displayed on invoices for this customer.
    """
    rendering_options: typing.Optional[InvoiceSettingCustomerRenderingOptions] = (
        pydantic.Field(alias="rendering_options", default=None)
    )
