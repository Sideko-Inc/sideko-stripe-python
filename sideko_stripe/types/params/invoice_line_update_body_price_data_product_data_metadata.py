import pydantic
import typing
import typing_extensions


class InvoiceLineUpdateBodyPriceDataProductDataMetadata(
    typing_extensions.TypedDict, total=False
):
    """
    InvoiceLineUpdateBodyPriceDataProductDataMetadata
    """


class _SerializerInvoiceLineUpdateBodyPriceDataProductDataMetadata(pydantic.BaseModel):
    """
    Serializer for InvoiceLineUpdateBodyPriceDataProductDataMetadata handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, str]
