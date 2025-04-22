import pydantic
import typing_extensions


class SourceCreateBodyRedirect(typing_extensions.TypedDict):
    """
    Parameters required for the redirect flow. Required if the source is authenticated by a redirect (`flow` is `redirect`).
    """

    return_url: typing_extensions.Required[str]


class _SerializerSourceCreateBodyRedirect(pydantic.BaseModel):
    """
    Serializer for SourceCreateBodyRedirect handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    return_url: str = pydantic.Field(
        alias="return_url",
    )
