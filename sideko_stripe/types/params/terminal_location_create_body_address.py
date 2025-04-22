import pydantic
import typing
import typing_extensions


class TerminalLocationCreateBodyAddress(typing_extensions.TypedDict):
    """
    The full address of the location.
    """

    city: typing_extensions.NotRequired[str]

    country: typing_extensions.Required[str]

    line1: typing_extensions.NotRequired[str]

    line2: typing_extensions.NotRequired[str]

    postal_code: typing_extensions.NotRequired[str]

    state: typing_extensions.NotRequired[str]


class _SerializerTerminalLocationCreateBodyAddress(pydantic.BaseModel):
    """
    Serializer for TerminalLocationCreateBodyAddress handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    city: typing.Optional[str] = pydantic.Field(alias="city", default=None)
    country: str = pydantic.Field(
        alias="country",
    )
    line1: typing.Optional[str] = pydantic.Field(alias="line1", default=None)
    line2: typing.Optional[str] = pydantic.Field(alias="line2", default=None)
    postal_code: typing.Optional[str] = pydantic.Field(
        alias="postal_code", default=None
    )
    state: typing.Optional[str] = pydantic.Field(alias="state", default=None)
