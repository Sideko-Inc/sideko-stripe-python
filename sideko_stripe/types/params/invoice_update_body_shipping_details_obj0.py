import pydantic
import typing
import typing_extensions

from .invoice_update_body_shipping_details_obj0_address import (
    InvoiceUpdateBodyShippingDetailsObj0Address,
    _SerializerInvoiceUpdateBodyShippingDetailsObj0Address,
)


class InvoiceUpdateBodyShippingDetailsObj0(typing_extensions.TypedDict):
    """
    InvoiceUpdateBodyShippingDetailsObj0
    """

    address: typing_extensions.Required[InvoiceUpdateBodyShippingDetailsObj0Address]

    name: typing_extensions.Required[str]

    phone: typing_extensions.NotRequired[typing.Union[str, str]]


class _SerializerInvoiceUpdateBodyShippingDetailsObj0(pydantic.BaseModel):
    """
    Serializer for InvoiceUpdateBodyShippingDetailsObj0 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    address: _SerializerInvoiceUpdateBodyShippingDetailsObj0Address = pydantic.Field(
        alias="address",
    )
    name: str = pydantic.Field(
        alias="name",
    )
    phone: typing.Optional[typing.Union[str, str]] = pydantic.Field(
        alias="phone", default=None
    )
