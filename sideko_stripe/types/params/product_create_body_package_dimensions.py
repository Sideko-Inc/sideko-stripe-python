import pydantic
import typing_extensions


class ProductCreateBodyPackageDimensions(typing_extensions.TypedDict):
    """
    The dimensions of this product for shipping purposes.
    """

    height: typing_extensions.Required[float]

    length: typing_extensions.Required[float]

    weight: typing_extensions.Required[float]

    width: typing_extensions.Required[float]


class _SerializerProductCreateBodyPackageDimensions(pydantic.BaseModel):
    """
    Serializer for ProductCreateBodyPackageDimensions handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    height: float = pydantic.Field(
        alias="height",
    )
    length: float = pydantic.Field(
        alias="length",
    )
    weight: float = pydantic.Field(
        alias="weight",
    )
    width: float = pydantic.Field(
        alias="width",
    )
