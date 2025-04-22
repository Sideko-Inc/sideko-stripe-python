import pydantic
import typing
import typing_extensions


class InvoiceLineCreateManyBodyLinesItemPriceDataProductDataMetadata(
    typing_extensions.TypedDict, total=False
):
    """
    InvoiceLineCreateManyBodyLinesItemPriceDataProductDataMetadata
    """


class _SerializerInvoiceLineCreateManyBodyLinesItemPriceDataProductDataMetadata(
    pydantic.BaseModel
):
    """
    Serializer for InvoiceLineCreateManyBodyLinesItemPriceDataProductDataMetadata handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, str]
