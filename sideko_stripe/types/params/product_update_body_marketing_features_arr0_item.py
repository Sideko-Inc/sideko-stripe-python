import pydantic
import typing_extensions


class ProductUpdateBodyMarketingFeaturesArr0Item(typing_extensions.TypedDict):
    """
    ProductUpdateBodyMarketingFeaturesArr0Item
    """

    name: typing_extensions.Required[str]


class _SerializerProductUpdateBodyMarketingFeaturesArr0Item(pydantic.BaseModel):
    """
    Serializer for ProductUpdateBodyMarketingFeaturesArr0Item handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    name: str = pydantic.Field(
        alias="name",
    )
