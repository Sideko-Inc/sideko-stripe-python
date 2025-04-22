import pydantic
import typing_extensions


class ProductCreateBodyMarketingFeaturesItem(typing_extensions.TypedDict):
    """
    ProductCreateBodyMarketingFeaturesItem
    """

    name: typing_extensions.Required[str]


class _SerializerProductCreateBodyMarketingFeaturesItem(pydantic.BaseModel):
    """
    Serializer for ProductCreateBodyMarketingFeaturesItem handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    name: str = pydantic.Field(
        alias="name",
    )
