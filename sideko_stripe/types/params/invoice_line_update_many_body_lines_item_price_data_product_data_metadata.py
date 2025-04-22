import pydantic
import typing
import typing_extensions


class InvoiceLineUpdateManyBodyLinesItemPriceDataProductDataMetadata(
    typing_extensions.TypedDict, total=False
):
    """
    InvoiceLineUpdateManyBodyLinesItemPriceDataProductDataMetadata
    """


class _SerializerInvoiceLineUpdateManyBodyLinesItemPriceDataProductDataMetadata(
    pydantic.BaseModel
):
    """
    Serializer for InvoiceLineUpdateManyBodyLinesItemPriceDataProductDataMetadata handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, str]
