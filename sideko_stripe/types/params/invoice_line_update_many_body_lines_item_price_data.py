import pydantic
import typing
import typing_extensions

from .invoice_line_update_many_body_lines_item_price_data_product_data import (
    InvoiceLineUpdateManyBodyLinesItemPriceDataProductData,
    _SerializerInvoiceLineUpdateManyBodyLinesItemPriceDataProductData,
)


class InvoiceLineUpdateManyBodyLinesItemPriceData(typing_extensions.TypedDict):
    """
    InvoiceLineUpdateManyBodyLinesItemPriceData
    """

    currency: typing_extensions.Required[str]

    product: typing_extensions.NotRequired[str]

    product_data: typing_extensions.NotRequired[
        InvoiceLineUpdateManyBodyLinesItemPriceDataProductData
    ]

    tax_behavior: typing_extensions.NotRequired[
        typing_extensions.Literal["exclusive", "inclusive", "unspecified"]
    ]

    unit_amount: typing_extensions.NotRequired[int]

    unit_amount_decimal: typing_extensions.NotRequired[str]


class _SerializerInvoiceLineUpdateManyBodyLinesItemPriceData(pydantic.BaseModel):
    """
    Serializer for InvoiceLineUpdateManyBodyLinesItemPriceData handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    currency: str = pydantic.Field(
        alias="currency",
    )
    product: typing.Optional[str] = pydantic.Field(alias="product", default=None)
    product_data: typing.Optional[
        _SerializerInvoiceLineUpdateManyBodyLinesItemPriceDataProductData
    ] = pydantic.Field(alias="product_data", default=None)
    tax_behavior: typing.Optional[
        typing_extensions.Literal["exclusive", "inclusive", "unspecified"]
    ] = pydantic.Field(alias="tax_behavior", default=None)
    unit_amount: typing.Optional[int] = pydantic.Field(
        alias="unit_amount", default=None
    )
    unit_amount_decimal: typing.Optional[str] = pydantic.Field(
        alias="unit_amount_decimal", default=None
    )
