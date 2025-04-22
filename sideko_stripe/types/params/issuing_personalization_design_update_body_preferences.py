import pydantic
import typing_extensions


class IssuingPersonalizationDesignUpdateBodyPreferences(typing_extensions.TypedDict):
    """
    Information on whether this personalization design is used to create cards when one is not specified.
    """

    is_default: typing_extensions.Required[bool]


class _SerializerIssuingPersonalizationDesignUpdateBodyPreferences(pydantic.BaseModel):
    """
    Serializer for IssuingPersonalizationDesignUpdateBodyPreferences handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    is_default: bool = pydantic.Field(
        alias="is_default",
    )
