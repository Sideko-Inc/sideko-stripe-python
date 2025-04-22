import pydantic
import typing
import typing_extensions

from .address import Address
from .cash_balance import CashBalance
from .customer_invoice_credit_balance import CustomerInvoiceCreditBalance
from .customer_metadata import CustomerMetadata
from .customer_tax import CustomerTax
from .shipping import Shipping
from .source import Source
from .test_helpers_test_clock import TestHelpersTestClock

if typing_extensions.TYPE_CHECKING:
    from .bank_account import BankAccount
    from .card import Card
    from .customer_sources import CustomerSources
    from .customer_subscriptions import CustomerSubscriptions
    from .customer_tax_ids import CustomerTaxIds
    from .discount import Discount
    from .invoice_setting_customer_setting import InvoiceSettingCustomerSetting


class Customer(pydantic.BaseModel):
    """
    This object represents a customer of your business. Use it to [create recurring charges](https://stripe.com/docs/invoicing/customer), [save payment](https://stripe.com/docs/payments/save-during-payment) and contact information,
    and track payments that belong to the same customer.
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    address: typing.Optional[Address] = pydantic.Field(alias="address", default=None)
    balance: typing.Optional[int] = pydantic.Field(alias="balance", default=None)
    """
    The current balance, if any, that's stored on the customer. If negative, the customer has credit to apply to their next invoice. If positive, the customer has an amount owed that's added to their next invoice. The balance only considers amounts that Stripe hasn't successfully applied to any invoice. It doesn't reflect unpaid invoices. This balance is only taken into account after invoices finalize.
    """
    cash_balance: typing.Optional[CashBalance] = pydantic.Field(
        alias="cash_balance", default=None
    )
    """
    A customer's `Cash balance` represents real funds. Customers can add funds to their cash balance by sending a bank transfer. These funds can be used for payment and can eventually be paid out to your bank account.
    """
    created: int = pydantic.Field(
        alias="created",
    )
    """
    Time at which the object was created. Measured in seconds since the Unix epoch.
    """
    currency: typing.Optional[str] = pydantic.Field(alias="currency", default=None)
    """
    Three-letter [ISO code for the currency](https://stripe.com/docs/currencies) the customer can be charged in for recurring billing purposes.
    """
    default_source: typing.Optional[
        typing.Union[str, "BankAccount", "Card", Source]
    ] = pydantic.Field(alias="default_source", default=None)
    """
    ID of the default payment source for the customer.
    
    If you use payment methods created through the PaymentMethods API, see the [invoice_settings.default_payment_method](https://stripe.com/docs/api/customers/object#customer_object-invoice_settings-default_payment_method) field instead.
    """
    delinquent: typing.Optional[bool] = pydantic.Field(alias="delinquent", default=None)
    """
    Tracks the most recent state change on any invoice belonging to the customer. Paying an invoice or marking it uncollectible via the API will set this field to false. An automatic payment failure or passing the `invoice.due_date` will set this field to `true`.
    
    If an invoice becomes uncollectible by [dunning](https://stripe.com/docs/billing/automatic-collection), `delinquent` doesn't reset to `false`.
    
    If you care whether the customer has paid their most recent subscription invoice, use `subscription.status` instead. Paying or marking uncollectible any customer invoice regardless of whether it is the latest invoice for a subscription will always set this field to `false`.
    """
    description: typing.Optional[str] = pydantic.Field(
        alias="description", default=None
    )
    """
    An arbitrary string attached to the object. Often useful for displaying to users.
    """
    discount: typing.Optional["Discount"] = pydantic.Field(
        alias="discount", default=None
    )
    """
    A discount represents the actual application of a [coupon](https://stripe.com/docs/api#coupons) or [promotion code](https://stripe.com/docs/api#promotion_codes).
    It contains information about when the discount began, when it will end, and what it is applied to.
    
    Related guide: [Applying discounts to subscriptions](https://stripe.com/docs/billing/subscriptions/discounts)
    """
    email: typing.Optional[str] = pydantic.Field(alias="email", default=None)
    """
    The customer's email address.
    """
    id: str = pydantic.Field(
        alias="id",
    )
    """
    Unique identifier for the object.
    """
    invoice_credit_balance: typing.Optional[CustomerInvoiceCreditBalance] = (
        pydantic.Field(alias="invoice_credit_balance", default=None)
    )
    """
    The current multi-currency balances, if any, that's stored on the customer. If positive in a currency, the customer has a credit to apply to their next invoice denominated in that currency. If negative, the customer has an amount owed that's added to their next invoice denominated in that currency. These balances don't apply to unpaid invoices. They solely track amounts that Stripe hasn't successfully applied to any invoice. Stripe only applies a balance in a specific currency to an invoice after that invoice (which is in the same currency) finalizes.
    """
    invoice_prefix: typing.Optional[str] = pydantic.Field(
        alias="invoice_prefix", default=None
    )
    """
    The prefix for the customer used to generate unique invoice numbers.
    """
    invoice_settings: typing.Optional["InvoiceSettingCustomerSetting"] = pydantic.Field(
        alias="invoice_settings", default=None
    )
    livemode: bool = pydantic.Field(
        alias="livemode",
    )
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    metadata: typing.Optional[CustomerMetadata] = pydantic.Field(
        alias="metadata", default=None
    )
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    """
    The customer's full name or business name.
    """
    next_invoice_sequence: typing.Optional[int] = pydantic.Field(
        alias="next_invoice_sequence", default=None
    )
    """
    The suffix of the customer's next invoice number (for example, 0001). When the account uses account level sequencing, this parameter is ignored in API requests and the field omitted in API responses.
    """
    object: typing_extensions.Literal["customer"] = pydantic.Field(
        alias="object",
    )
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    phone: typing.Optional[str] = pydantic.Field(alias="phone", default=None)
    """
    The customer's phone number.
    """
    preferred_locales: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="preferred_locales", default=None
    )
    """
    The customer's preferred locales (languages), ordered by preference.
    """
    shipping: typing.Optional[Shipping] = pydantic.Field(alias="shipping", default=None)
    sources: typing.Optional["CustomerSources"] = pydantic.Field(
        alias="sources", default=None
    )
    """
    The customer's payment sources, if any.
    """
    subscriptions: typing.Optional["CustomerSubscriptions"] = pydantic.Field(
        alias="subscriptions", default=None
    )
    """
    The customer's current subscriptions, if any.
    """
    tax: typing.Optional[CustomerTax] = pydantic.Field(alias="tax", default=None)
    tax_exempt: typing.Optional[
        typing_extensions.Literal["exempt", "none", "reverse"]
    ] = pydantic.Field(alias="tax_exempt", default=None)
    """
    Describes the customer's tax exemption status, which is `none`, `exempt`, or `reverse`. When set to `reverse`, invoice and receipt PDFs include the following text: **"Reverse charge"**.
    """
    tax_ids: typing.Optional["CustomerTaxIds"] = pydantic.Field(
        alias="tax_ids", default=None
    )
    """
    The customer's tax IDs.
    """
    test_clock: typing.Optional[typing.Union[str, TestHelpersTestClock]] = (
        pydantic.Field(alias="test_clock", default=None)
    )
    """
    ID of the test clock that this customer belongs to.
    """
