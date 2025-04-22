import pydantic
import typing
import typing_extensions


class IssuingDisputeUpdateBodyMetadataObj0(typing_extensions.TypedDict, total=False):
    """
    IssuingDisputeUpdateBodyMetadataObj0
    """


class _SerializerIssuingDisputeUpdateBodyMetadataObj0(pydantic.BaseModel):
    """
    Serializer for IssuingDisputeUpdateBodyMetadataObj0 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, str]
