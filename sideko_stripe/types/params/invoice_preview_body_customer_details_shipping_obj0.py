import pydantic
import typing
import typing_extensions

from .invoice_preview_body_customer_details_shipping_obj0_address import (
    InvoicePreviewBodyCustomerDetailsShippingObj0Address,
    _SerializerInvoicePreviewBodyCustomerDetailsShippingObj0Address,
)


class InvoicePreviewBodyCustomerDetailsShippingObj0(typing_extensions.TypedDict):
    """
    InvoicePreviewBodyCustomerDetailsShippingObj0
    """

    address: typing_extensions.Required[
        InvoicePreviewBodyCustomerDetailsShippingObj0Address
    ]

    name: typing_extensions.Required[str]

    phone: typing_extensions.NotRequired[str]


class _SerializerInvoicePreviewBodyCustomerDetailsShippingObj0(pydantic.BaseModel):
    """
    Serializer for InvoicePreviewBodyCustomerDetailsShippingObj0 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    address: _SerializerInvoicePreviewBodyCustomerDetailsShippingObj0Address = (
        pydantic.Field(
            alias="address",
        )
    )
    name: str = pydantic.Field(
        alias="name",
    )
    phone: typing.Optional[str] = pydantic.Field(alias="phone", default=None)
