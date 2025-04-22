import pydantic
import typing_extensions


class IssuingPersonalizationDesignCreateBodyPreferences(typing_extensions.TypedDict):
    """
    Information on whether this personalization design is used to create cards when one is not specified.
    """

    is_default: typing_extensions.Required[bool]


class _SerializerIssuingPersonalizationDesignCreateBodyPreferences(pydantic.BaseModel):
    """
    Serializer for IssuingPersonalizationDesignCreateBodyPreferences handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    is_default: bool = pydantic.Field(
        alias="is_default",
    )
