import pydantic
import typing_extensions


class ProductUpdateBodyPackageDimensionsObj0(typing_extensions.TypedDict):
    """
    ProductUpdateBodyPackageDimensionsObj0
    """

    height: typing_extensions.Required[float]

    length: typing_extensions.Required[float]

    weight: typing_extensions.Required[float]

    width: typing_extensions.Required[float]


class _SerializerProductUpdateBodyPackageDimensionsObj0(pydantic.BaseModel):
    """
    Serializer for ProductUpdateBodyPackageDimensionsObj0 handling case conversions
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
