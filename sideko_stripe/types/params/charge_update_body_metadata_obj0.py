import pydantic
import typing
import typing_extensions


class ChargeUpdateBodyMetadataObj0(typing_extensions.TypedDict, total=False):
    """
    ChargeUpdateBodyMetadataObj0
    """


class _SerializerChargeUpdateBodyMetadataObj0(pydantic.BaseModel):
    """
    Serializer for ChargeUpdateBodyMetadataObj0 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, str]
