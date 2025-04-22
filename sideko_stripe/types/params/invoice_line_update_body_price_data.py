import pydantic
import typing
import typing_extensions

from .invoice_line_update_body_price_data_product_data import (
    InvoiceLineUpdateBodyPriceDataProductData,
    _SerializerInvoiceLineUpdateBodyPriceDataProductData,
)


class InvoiceLineUpdateBodyPriceData(typing_extensions.TypedDict):
    """
    Data used to generate a new [Price](https://stripe.com/docs/api/prices) object inline.
    """

    currency: typing_extensions.Required[str]

    product: typing_extensions.NotRequired[str]

    product_data: typing_extensions.NotRequired[
        InvoiceLineUpdateBodyPriceDataProductData
    ]

    tax_behavior: typing_extensions.NotRequired[
        typing_extensions.Literal["exclusive", "inclusive", "unspecified"]
    ]

    unit_amount: typing_extensions.NotRequired[int]

    unit_amount_decimal: typing_extensions.NotRequired[str]


class _SerializerInvoiceLineUpdateBodyPriceData(pydantic.BaseModel):
    """
    Serializer for InvoiceLineUpdateBodyPriceData handling case conversions
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
        _SerializerInvoiceLineUpdateBodyPriceDataProductData
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
