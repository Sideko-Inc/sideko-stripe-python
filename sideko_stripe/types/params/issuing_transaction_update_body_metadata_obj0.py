import pydantic
import typing
import typing_extensions


class IssuingTransactionUpdateBodyMetadataObj0(
    typing_extensions.TypedDict, total=False
):
    """
    IssuingTransactionUpdateBodyMetadataObj0
    """


class _SerializerIssuingTransactionUpdateBodyMetadataObj0(pydantic.BaseModel):
    """
    Serializer for IssuingTransactionUpdateBodyMetadataObj0 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, str]
