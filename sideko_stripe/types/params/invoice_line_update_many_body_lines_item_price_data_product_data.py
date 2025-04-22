import pydantic
import typing
import typing_extensions

from .invoice_line_update_many_body_lines_item_price_data_product_data_metadata import (
    InvoiceLineUpdateManyBodyLinesItemPriceDataProductDataMetadata,
    _SerializerInvoiceLineUpdateManyBodyLinesItemPriceDataProductDataMetadata,
)


class InvoiceLineUpdateManyBodyLinesItemPriceDataProductData(
    typing_extensions.TypedDict
):
    """
    InvoiceLineUpdateManyBodyLinesItemPriceDataProductData
    """

    description: typing_extensions.NotRequired[str]

    images: typing_extensions.NotRequired[typing.List[str]]

    metadata: typing_extensions.NotRequired[
        InvoiceLineUpdateManyBodyLinesItemPriceDataProductDataMetadata
    ]

    name: typing_extensions.Required[str]

    tax_code: typing_extensions.NotRequired[str]


class _SerializerInvoiceLineUpdateManyBodyLinesItemPriceDataProductData(
    pydantic.BaseModel
):
    """
    Serializer for InvoiceLineUpdateManyBodyLinesItemPriceDataProductData handling case conversions
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
        _SerializerInvoiceLineUpdateManyBodyLinesItemPriceDataProductDataMetadata
    ] = pydantic.Field(alias="metadata", default=None)
    name: str = pydantic.Field(
        alias="name",
    )
    tax_code: typing.Optional[str] = pydantic.Field(alias="tax_code", default=None)
