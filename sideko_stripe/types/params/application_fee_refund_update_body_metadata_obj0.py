import pydantic
import typing
import typing_extensions


class ApplicationFeeRefundUpdateBodyMetadataObj0(
    typing_extensions.TypedDict, total=False
):
    """
    ApplicationFeeRefundUpdateBodyMetadataObj0
    """


class _SerializerApplicationFeeRefundUpdateBodyMetadataObj0(pydantic.BaseModel):
    """
    Serializer for ApplicationFeeRefundUpdateBodyMetadataObj0 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, str]
