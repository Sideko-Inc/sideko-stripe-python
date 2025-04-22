import pydantic
import typing
import typing_extensions


class InvoiceLineCreateManyBodyLinesItemPricing(typing_extensions.TypedDict):
    """
    InvoiceLineCreateManyBodyLinesItemPricing
    """

    price: typing_extensions.NotRequired[str]


class _SerializerInvoiceLineCreateManyBodyLinesItemPricing(pydantic.BaseModel):
    """
    Serializer for InvoiceLineCreateManyBodyLinesItemPricing handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    price: typing.Optional[str] = pydantic.Field(alias="price", default=None)
