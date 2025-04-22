import pydantic
import typing
import typing_extensions

from .invoice_line_create_many_body_lines_item_price_data_product_data_metadata import (
    InvoiceLineCreateManyBodyLinesItemPriceDataProductDataMetadata,
    _SerializerInvoiceLineCreateManyBodyLinesItemPriceDataProductDataMetadata,
)


class InvoiceLineCreateManyBodyLinesItemPriceDataProductData(
    typing_extensions.TypedDict
):
    """
    InvoiceLineCreateManyBodyLinesItemPriceDataProductData
    """

    description: typing_extensions.NotRequired[str]

    images: typing_extensions.NotRequired[typing.List[str]]

    metadata: typing_extensions.NotRequired[
        InvoiceLineCreateManyBodyLinesItemPriceDataProductDataMetadata
    ]

    name: typing_extensions.Required[str]

    tax_code: typing_extensions.NotRequired[str]


class _SerializerInvoiceLineCreateManyBodyLinesItemPriceDataProductData(
    pydantic.BaseModel
):
    """
    Serializer for InvoiceLineCreateManyBodyLinesItemPriceDataProductData handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    description: typing.Optional[str] = pydantic.Field(
        alias="description", default=None
    )
    images: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="images", default=None
    )
    metadata: typing.Optional[
        _SerializerInvoiceLineCreateManyBodyLinesItemPriceDataProductDataMetadata
    ] = pydantic.Field(alias="metadata", default=None)
    name: str = pydantic.Field(
        alias="name",
    )
    tax_code: typing.Optional[str] = pydantic.Field(alias="tax_code", default=None)
