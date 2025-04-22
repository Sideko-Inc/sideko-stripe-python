import pydantic
import typing
import typing_extensions

from .invoice_create_body_shipping_details_address import (
    InvoiceCreateBodyShippingDetailsAddress,
    _SerializerInvoiceCreateBodyShippingDetailsAddress,
)


class InvoiceCreateBodyShippingDetails(typing_extensions.TypedDict):
    """
    Shipping details for the invoice. The Invoice PDF will use the `shipping_details` value if it is set, otherwise the PDF will render the shipping address from the customer.
    """

    address: typing_extensions.Required[InvoiceCreateBodyShippingDetailsAddress]

    name: typing_extensions.Required[str]

    phone: typing_extensions.NotRequired[typing.Union[str, str]]


class _SerializerInvoiceCreateBodyShippingDetails(pydantic.BaseModel):
    """
    Serializer for InvoiceCreateBodyShippingDetails handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    address: _SerializerInvoiceCreateBodyShippingDetailsAddress = pydantic.Field(
        alias="address",
    )
    name: str = pydantic.Field(
        alias="name",
    )
    phone: typing.Optional[typing.Union[str, str]] = pydantic.Field(
        alias="phone", default=None
    )
