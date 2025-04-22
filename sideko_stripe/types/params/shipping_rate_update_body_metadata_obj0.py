import pydantic
import typing
import typing_extensions


class ShippingRateUpdateBodyMetadataObj0(typing_extensions.TypedDict, total=False):
    """
    ShippingRateUpdateBodyMetadataObj0
    """


class _SerializerShippingRateUpdateBodyMetadataObj0(pydantic.BaseModel):
    """
    Serializer for ShippingRateUpdateBodyMetadataObj0 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, str]
