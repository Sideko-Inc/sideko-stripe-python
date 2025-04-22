import pydantic
import typing
import typing_extensions

from .customer_create_body_address_obj0 import (
    CustomerCreateBodyAddressObj0,
    _SerializerCustomerCreateBodyAddressObj0,
)
from .customer_create_body_cash_balance import (
    CustomerCreateBodyCashBalance,
    _SerializerCustomerCreateBodyCashBalance,
)
from .customer_create_body_invoice_settings import (
    CustomerCreateBodyInvoiceSettings,
    _SerializerCustomerCreateBodyInvoiceSettings,
)
from .customer_create_body_metadata_obj0 import (
    CustomerCreateBodyMetadataObj0,
    _SerializerCustomerCreateBodyMetadataObj0,
)
from .customer_create_body_shipping_obj0 import (
    CustomerCreateBodyShippingObj0,
    _SerializerCustomerCreateBodyShippingObj0,
)
from .customer_create_body_tax import (
    CustomerCreateBodyTax,
    _SerializerCustomerCreateBodyTax,
)
from .customer_create_body_tax_id_data_item import (
    CustomerCreateBodyTaxIdDataItem,
    _SerializerCustomerCreateBodyTaxIdDataItem,
)


class CustomerCreateBody(typing_extensions.TypedDict, total=False):
    """
    CustomerCreateBody
    """

    address: typing_extensions.NotRequired[
        typing.Union[CustomerCreateBodyAddressObj0, str]
    ]
    """
    The customer's address.
    """

    balance: typing_extensions.NotRequired[int]
    """
    An integer amount in cents (or local equivalent) that represents the customer's current balance, which affect the customer's future invoices. A negative amount represents a credit that decreases the amount due on an invoice; a positive amount increases the amount due on an invoice.
    """

    cash_balance: typing_extensions.NotRequired[CustomerCreateBodyCashBalance]
    """
    Balance information and default balance settings for this customer.
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

    invoice_settings: typing_extensions.NotRequired[CustomerCreateBodyInvoiceSettings]
    """
    Default invoice settings for this customer.
    """

    metadata: typing_extensions.NotRequired[
        typing.Union[CustomerCreateBodyMetadataObj0, str]
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

    payment_method: typing_extensions.NotRequired[str]

    phone: typing_extensions.NotRequired[str]
    """
    The customer's phone number.
    """

    preferred_locales: typing_extensions.NotRequired[typing.List[str]]
    """
    Customer's preferred languages, ordered by preference.
    """

    shipping: typing_extensions.NotRequired[
        typing.Union[CustomerCreateBodyShippingObj0, str]
    ]
    """
    The customer's shipping information. Appears on invoices emailed to this customer.
    """

    source: typing_extensions.NotRequired[str]

    tax: typing_extensions.NotRequired[CustomerCreateBodyTax]
    """
    Tax details about the customer.
    """

    tax_exempt: typing_extensions.NotRequired[
        typing_extensions.Literal["exempt", "none", "reverse"]
    ]
    """
    The customer's tax exemption. One of `none`, `exempt`, or `reverse`.
    """

    tax_id_data: typing_extensions.NotRequired[
        typing.List[CustomerCreateBodyTaxIdDataItem]
    ]
    """
    The customer's tax IDs.
    """

    test_clock: typing_extensions.NotRequired[str]
    """
    ID of the test clock to attach to the customer.
    """


class _SerializerCustomerCreateBody(pydantic.BaseModel):
    """
    Serializer for CustomerCreateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    address: typing.Optional[
        typing.Union[_SerializerCustomerCreateBodyAddressObj0, str]
    ] = pydantic.Field(alias="address", default=None)
    balance: typing.Optional[int] = pydantic.Field(alias="balance", default=None)
    cash_balance: typing.Optional[_SerializerCustomerCreateBodyCashBalance] = (
        pydantic.Field(alias="cash_balance", default=None)
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
    invoice_settings: typing.Optional[_SerializerCustomerCreateBodyInvoiceSettings] = (
        pydantic.Field(alias="invoice_settings", default=None)
    )
    metadata: typing.Optional[
        typing.Union[_SerializerCustomerCreateBodyMetadataObj0, str]
    ] = pydantic.Field(alias="metadata", default=None)
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    next_invoice_sequence: typing.Optional[int] = pydantic.Field(
        alias="next_invoice_sequence", default=None
    )
    payment_method: typing.Optional[str] = pydantic.Field(
        alias="payment_method", default=None
    )
    phone: typing.Optional[str] = pydantic.Field(alias="phone", default=None)
    preferred_locales: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="preferred_locales", default=None
    )
    shipping: typing.Optional[
        typing.Union[_SerializerCustomerCreateBodyShippingObj0, str]
    ] = pydantic.Field(alias="shipping", default=None)
    source: typing.Optional[str] = pydantic.Field(alias="source", default=None)
    tax: typing.Optional[_SerializerCustomerCreateBodyTax] = pydantic.Field(
        alias="tax", default=None
    )
    tax_exempt: typing.Optional[
        typing_extensions.Literal["exempt", "none", "reverse"]
    ] = pydantic.Field(alias="tax_exempt", default=None)
    tax_id_data: typing.Optional[
        typing.List[_SerializerCustomerCreateBodyTaxIdDataItem]
    ] = pydantic.Field(alias="tax_id_data", default=None)
    test_clock: typing.Optional[str] = pydantic.Field(alias="test_clock", default=None)
