import pydantic
import typing
import typing_extensions

from .invoice_line_create_many_body_invoice_metadata_obj0 import (
    InvoiceLineCreateManyBodyInvoiceMetadataObj0,
    _SerializerInvoiceLineCreateManyBodyInvoiceMetadataObj0,
)
from .invoice_line_create_many_body_lines_item import (
    InvoiceLineCreateManyBodyLinesItem,
    _SerializerInvoiceLineCreateManyBodyLinesItem,
)


class InvoiceLineCreateManyBody(typing_extensions.TypedDict, total=False):
    """
    InvoiceLineCreateManyBody
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """

    invoice_metadata: typing_extensions.NotRequired[
        typing.Union[InvoiceLineCreateManyBodyInvoiceMetadataObj0, str]
    ]
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    """

    lines: typing_extensions.Required[typing.List[InvoiceLineCreateManyBodyLinesItem]]
    """
    The line items to add.
    """


class _SerializerInvoiceLineCreateManyBody(pydantic.BaseModel):
    """
    Serializer for InvoiceLineCreateManyBody handling case conversions
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
        typing.Union[_SerializerInvoiceLineCreateManyBodyInvoiceMetadataObj0, str]
    ] = pydantic.Field(alias="invoice_metadata", default=None)
    lines: typing.List[_SerializerInvoiceLineCreateManyBodyLinesItem] = pydantic.Field(
        alias="lines",
    )
