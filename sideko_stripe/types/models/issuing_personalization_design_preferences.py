import pydantic
import typing


class IssuingPersonalizationDesignPreferences(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    is_default: bool = pydantic.Field(
        alias="is_default",
    )
    """
    Whether we use this personalization design to create cards when one isn't specified. A connected account uses the Connect platform's default design if no personalization design is set as the default design.
    """
    is_platform_default: typing.Optional[bool] = pydantic.Field(
        alias="is_platform_default", default=None
    )
    """
    Whether this personalization design is used to create cards when one is not specified and a default for this connected account does not exist.
    """
