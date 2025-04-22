import pydantic
import typing
import typing_extensions


class ProductCreateBodyDefaultPriceDataMetadata(
    typing_extensions.TypedDict, total=False
):
    """
    ProductCreateBodyDefaultPriceDataMetadata
    """


class _SerializerProductCreateBodyDefaultPriceDataMetadata(pydantic.BaseModel):
    """
    Serializer for ProductCreateBodyDefaultPriceDataMetadata handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, str]
