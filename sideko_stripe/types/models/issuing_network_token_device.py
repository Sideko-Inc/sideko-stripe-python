import pydantic
import typing
import typing_extensions


class IssuingNetworkTokenDevice(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    device_fingerprint: typing.Optional[str] = pydantic.Field(
        alias="device_fingerprint", default=None
    )
    """
    An obfuscated ID derived from the device ID.
    """
    ip_address: typing.Optional[str] = pydantic.Field(alias="ip_address", default=None)
    """
    The IP address of the device at provisioning time.
    """
    location: typing.Optional[str] = pydantic.Field(alias="location", default=None)
    """
    The geographic latitude/longitude coordinates of the device at provisioning time. The format is [+-]decimal/[+-]decimal.
    """
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    """
    The name of the device used for tokenization.
    """
    phone_number: typing.Optional[str] = pydantic.Field(
        alias="phone_number", default=None
    )
    """
    The phone number of the device used for tokenization.
    """
    type_: typing.Optional[typing_extensions.Literal["other", "phone", "watch"]] = (
        pydantic.Field(alias="type", default=None)
    )
    """
    The type of device used for tokenization.
    """
