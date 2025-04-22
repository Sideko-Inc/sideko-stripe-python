import pydantic
import typing
import typing_extensions

from .customer_update_body_address_obj0 import (
    CustomerUpdateBodyAddressObj0,
    _SerializerCustomerUpdateBodyAddressObj0,
)
from .customer_update_body_bank_account_obj0 import (
    CustomerUpdateBodyBankAccountObj0,
    _SerializerCustomerUpdateBodyBankAccountObj0,
)
from .customer_update_body_card_obj0 import (
    CustomerUpdateBodyCardObj0,
    _SerializerCustomerUpdateBodyCardObj0,
)
from .customer_update_body_cash_balance import (
    CustomerUpdateBodyCashBalance,
    _SerializerCustomerUpdateBodyCashBalance,
)
from .customer_update_body_invoice_settings import (
    CustomerUpdateBodyInvoiceSettings,
    _SerializerCustomerUpdateBodyInvoiceSettings,
)
from .customer_update_body_metadata_obj0 import (
    CustomerUpdateBodyMetadataObj0,
    _SerializerCustomerUpdateBodyMetadataObj0,
)
from .customer_update_body_shipping_obj0 import (
    CustomerUpdateBodyShippingObj0,
    _SerializerCustomerUpdateBodyShippingObj0,
)
from .customer_update_body_tax import (
    CustomerUpdateBodyTax,
    _SerializerCustomerUpdateBodyTax,
)


class CustomerUpdateBody(typing_extensions.TypedDict, total=False):
    """
    CustomerUpdateBody
    """

    address: typing_extensions.NotRequired[
        typing.Union[CustomerUpdateBodyAddressObj0, str]
    ]
    """
    The customer's address.
    """

    balance: typing_extensions.NotRequired[int]
    """
    An integer amount in cents (or local equivalent) that represents the customer's current balance, which affect the customer's future invoices. A negative amount represents a credit that decreases the amount due on an invoice; a positive amount increases the amount due on an invoice.
    """

    bank_account: typing_extensions.NotRequired[
        typing.Union[CustomerUpdateBodyBankAccountObj0, str]
    ]
    """
    Either a token, like the ones returned by [Stripe.js](https://stripe.com/docs/js), or a dictionary containing a user's bank account details.
    """

    card: typing_extensions.NotRequired[typing.Union[CustomerUpdateBodyCardObj0, str]]
    """
    A token, like the ones returned by [Stripe.js](https://stripe.com/docs/js).
    """

    cash_balance: typing_extensions.NotRequired[CustomerUpdateBodyCashBalance]
    """
    Balance information and default balance settings for this customer.
    """

    default_alipay_account: typing_extensions.NotRequired[str]
    """
    ID of Alipay account to make the customer's new default for invoice payments.
    """

    default_bank_account: typing_extensions.NotRequired[str]
    """
    ID of bank account to make the customer's new default for invoice payments.
    """

    default_card: typing_extensions.NotRequired[str]
    """
    ID of card to make the customer's new default for invoice payments.
    """

    default_source: typing_extensions.NotRequired[str]
    """
    If you are using payment methods created via the PaymentMethods API, see the [invoice_settings.default_payment_method](https://stripe.com/docs/api/customers/update#update_customer-invoice_settings-default_payment_method) parameter.
    
    Provide the ID of a payment source already attached to this customer to make it this customer's default payment source.
    
    If you want to add a new payment source and make it the default, see the [source](https://stripe.com/docs/api/customers/update#update_customer-source) property.
    """

    description: typing_extensions.NotRequired[str]
    """
    An arbitrary string that you can attach to a customer object. It is displayed alongside the customer in the dashboard.
    """

    email: typing_extensions.NotRequired[str]
    """
    Customer's email address. It's displayed alongside the customer in your dashboard and can be useful for searching and tracking. This may be up to *512 characters*.
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """

    invoice_prefix: typing_extensions.NotRequired[str]
    """
    The prefix for the customer used to generate unique invoice numbers. Must be 3–12 uppercase letters or numbers.
    """

    invoice_settings: typing_extensions.NotRequired[CustomerUpdateBodyInvoiceSettings]
    """
    Default invoice settings for this customer.
    """

    metadata: typing_extensions.NotRequired[
        typing.Union[CustomerUpdateBodyMetadataObj0, str]
    ]
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    """

    name: typing_extensions.NotRequired[str]
    """
    The customer's full name or business name.
    """

    next_invoice_sequence: typing_extensions.NotRequired[int]
    """
    The sequence to be used on the customer's next invoice. Defaults to 1.
    """

    phone: typing_extensions.NotRequired[str]
    """
    The customer's phone number.
    """

    preferred_locales: typing_extensions.NotRequired[typing.List[str]]
    """
    Customer's preferred languages, ordered by preference.
    """

    shipping: typing_extensions.NotRequired[
        typing.Union[CustomerUpdateBodyShippingObj0, str]
    ]
    """
    The customer's shipping information. Appears on invoices emailed to this customer.
    """

    source: typing_extensions.NotRequired[str]

    tax: typing_extensions.NotRequired[CustomerUpdateBodyTax]
    """
    Tax details about the customer.
    """

    tax_exempt: typing_extensions.NotRequired[
        typing_extensions.Literal["exempt", "none", "reverse"]
    ]
    """
    The customer's tax exemption. One of `none`, `exempt`, or `reverse`.
    """


class _SerializerCustomerUpdateBody(pydantic.BaseModel):
    """
    Serializer for CustomerUpdateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    address: typing.Optional[
        typing.Union[_SerializerCustomerUpdateBodyAddressObj0, str]
    ] = pydantic.Field(alias="address", default=None)
    balance: typing.Optional[int] = pydantic.Field(alias="balance", default=None)
    bank_account: typing.Optional[
        typing.Union[_SerializerCustomerUpdateBodyBankAccountObj0, str]
    ] = pydantic.Field(alias="bank_account", default=None)
    card: typing.Optional[typing.Union[_SerializerCustomerUpdateBodyCardObj0, str]] = (
        pydantic.Field(alias="card", default=None)
    )
    cash_balance: typing.Optional[_SerializerCustomerUpdateBodyCashBalance] = (
        pydantic.Field(alias="cash_balance", default=None)
    )
    default_alipay_account: typing.Optional[str] = pydantic.Field(
        alias="default_alipay_account", default=None
    )
    default_bank_account: typing.Optional[str] = pydantic.Field(
        alias="default_bank_account", default=None
    )
    default_card: typing.Optional[str] = pydantic.Field(
        alias="default_card", default=None
    )
    default_source: typing.Optional[str] = pydantic.Field(
        alias="default_source", default=None
    )
    description: typing.Optional[str] = pydantic.Field(
        alias="description", default=None
    )
    email: typing.Optional[str] = pydantic.Field(alias="email", default=None)
    expand: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="expand", default=None
    )
    invoice_prefix: typing.Optional[str] = pydantic.Field(
        alias="invoice_prefix", default=None
    )
    invoice_settings: typing.Optional[_SerializerCustomerUpdateBodyInvoiceSettings] = (
        pydantic.Field(alias="invoice_settings", default=None)
    )
    metadata: typing.Optional[
        typing.Union[_SerializerCustomerUpdateBodyMetadataObj0, str]
    ] = pydantic.Field(alias="metadata", default=None)
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    next_invoice_sequence: typing.Optional[int] = pydantic.Field(
        alias="next_invoice_sequence", default=None
    )
    phone: typing.Optional[str] = pydantic.Field(alias="phone", default=None)
    preferred_locales: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="preferred_locales", default=None
    )
    shipping: typing.Optional[
        typing.Union[_SerializerCustomerUpdateBodyShippingObj0, str]
    ] = pydantic.Field(alias="shipping", default=None)
    source: typing.Optional[str] = pydantic.Field(alias="source", default=None)
    tax: typing.Optional[_SerializerCustomerUpdateBodyTax] = pydantic.Field(
        alias="tax", default=None
    )
    tax_exempt: typing.Optional[
        typing_extensions.Literal["exempt", "none", "reverse"]
    ] = pydantic.Field(alias="tax_exempt", default=None)
