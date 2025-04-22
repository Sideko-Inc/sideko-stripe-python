import pydantic
import typing
import typing_extensions


class PriceCreateBodyProductDataMetadata(typing_extensions.TypedDict, total=False):
    """
    PriceCreateBodyProductDataMetadata
    """


class _SerializerPriceCreateBodyProductDataMetadata(pydantic.BaseModel):
    """
    Serializer for PriceCreateBodyProductDataMetadata handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, str]
