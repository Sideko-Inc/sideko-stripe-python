import pydantic
import typing
import typing_extensions


class ChargeRefundCreate1BodyMetadataObj0(typing_extensions.TypedDict, total=False):
    """
    ChargeRefundCreate1BodyMetadataObj0
    """


class _SerializerChargeRefundCreate1BodyMetadataObj0(pydantic.BaseModel):
    """
    Serializer for ChargeRefundCreate1BodyMetadataObj0 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, str]
