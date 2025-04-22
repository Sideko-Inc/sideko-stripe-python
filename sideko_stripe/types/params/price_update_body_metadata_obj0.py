import pydantic
import typing
import typing_extensions


class PriceUpdateBodyMetadataObj0(typing_extensions.TypedDict, total=False):
    """
    PriceUpdateBodyMetadataObj0
    """


class _SerializerPriceUpdateBodyMetadataObj0(pydantic.BaseModel):
    """
    Serializer for PriceUpdateBodyMetadataObj0 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, str]
