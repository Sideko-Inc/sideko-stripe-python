import pydantic
import typing
import typing_extensions


class SourceCreateBodyMetadata(typing_extensions.TypedDict, total=False):
    """
    SourceCreateBodyMetadata
    """


class _SerializerSourceCreateBodyMetadata(pydantic.BaseModel):
    """
    Serializer for SourceCreateBodyMetadata handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, str]
