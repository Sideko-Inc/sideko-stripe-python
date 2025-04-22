import pydantic
import typing


class ProductMarketingFeature(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    """
    The marketing feature name. Up to 80 characters long.
    """
