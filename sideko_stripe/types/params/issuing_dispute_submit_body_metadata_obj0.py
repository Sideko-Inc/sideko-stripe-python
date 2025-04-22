import pydantic
import typing
import typing_extensions


class IssuingDisputeSubmitBodyMetadataObj0(typing_extensions.TypedDict, total=False):
    """
    IssuingDisputeSubmitBodyMetadataObj0
    """


class _SerializerIssuingDisputeSubmitBodyMetadataObj0(pydantic.BaseModel):
    """
    Serializer for IssuingDisputeSubmitBodyMetadataObj0 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, str]
