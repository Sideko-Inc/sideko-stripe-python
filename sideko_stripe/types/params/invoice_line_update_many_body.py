import pydantic
import typing
import typing_extensions

from .invoice_line_update_many_body_invoice_metadata_obj0 import (
    InvoiceLineUpdateManyBodyInvoiceMetadataObj0,
    _SerializerInvoiceLineUpdateManyBodyInvoiceMetadataObj0,
)
from .invoice_line_update_many_body_lines_item import (
    InvoiceLineUpdateManyBodyLinesItem,
    _SerializerInvoiceLineUpdateManyBodyLinesItem,
)


class InvoiceLineUpdateManyBody(typing_extensions.TypedDict, total=False):
    """
    InvoiceLineUpdateManyBody
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """

    invoice_metadata: typing_extensions.NotRequired[
        typing.Union[InvoiceLineUpdateManyBodyInvoiceMetadataObj0, str]
    ]
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`. For [type=subscription](https://stripe.com/docs/api/invoices/line_item#invoice_line_item_object-type) line items, the incoming metadata specified on the request is directly used to set this value, in contrast to [type=invoiceitem](api/invoices/line_item#invoice_line_item_object-type) line items, where any existing metadata on the invoice line is merged with the incoming data.
    """

    lines: typing_extensions.Required[typing.List[InvoiceLineUpdateManyBodyLinesItem]]
    """
    The line items to update.
    """


class _SerializerInvoiceLineUpdateManyBody(pydantic.BaseModel):
    """
    Serializer for InvoiceLineUpdateManyBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    expand: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="expand", default=None
    )
    invoice_metadata: typing.Optional[
        typing.Union[_SerializerInvoiceLineUpdateManyBodyInvoiceMetadataObj0, str]
    ] = pydantic.Field(alias="invoice_metadata", default=None)
    lines: typing.List[_SerializerInvoiceLineUpdateManyBodyLinesItem] = pydantic.Field(
        alias="lines",
    )
