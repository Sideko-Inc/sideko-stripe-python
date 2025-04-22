import pydantic
import typing
import typing_extensions


class IssuingPersonalizationDesignListPreferences(typing_extensions.TypedDict):
    """
    Only return personalization designs with the given preferences.
    """

    is_default: typing_extensions.NotRequired[bool]

    is_platform_default: typing_extensions.NotRequired[bool]


class _SerializerIssuingPersonalizationDesignListPreferences(pydantic.BaseModel):
    """
    Serializer for IssuingPersonalizationDesignListPreferences handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    is_default: typing.Optional[bool] = pydantic.Field(alias="is_default", default=None)
    is_platform_default: typing.Optional[bool] = pydantic.Field(
        alias="is_platform_default", default=None
    )
