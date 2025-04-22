import pydantic
import typing
import typing_extensions


class InvoiceLineUpdateManyBodyLinesItemPricing(typing_extensions.TypedDict):
    """
    InvoiceLineUpdateManyBodyLinesItemPricing
    """

    price: typing_extensions.NotRequired[str]


class _SerializerInvoiceLineUpdateManyBodyLinesItemPricing(pydantic.BaseModel):
    """
    Serializer for InvoiceLineUpdateManyBodyLinesItemPricing handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    price: typing.Optional[str] = pydantic.Field(alias="price", default=None)
