import pydantic
import typing
import typing_extensions


class CouponCreateBodyMetadataObj0(typing_extensions.TypedDict, total=False):
    """
    CouponCreateBodyMetadataObj0
    """


class _SerializerCouponCreateBodyMetadataObj0(pydantic.BaseModel):
    """
    Serializer for CouponCreateBodyMetadataObj0 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, str]
