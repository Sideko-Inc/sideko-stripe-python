import pydantic
import typing
import typing_extensions


class TerminalConnectionTokenCreateBody(typing_extensions.TypedDict, total=False):
    """
    TerminalConnectionTokenCreateBody
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """

    location: typing_extensions.NotRequired[str]
    """
    The id of the location that this connection token is scoped to. If specified the connection token will only be usable with readers assigned to that location, otherwise the connection token will be usable with all readers. Note that location scoping only applies to internet-connected readers. For more details, see [the docs on scoping connection tokens](https://docs.stripe.com/terminal/fleet/locations-and-zones?dashboard-or-api=api#connection-tokens).
    """


class _SerializerTerminalConnectionTokenCreateBody(pydantic.BaseModel):
    """
    Serializer for TerminalConnectionTokenCreateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    expand: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="expand", default=None
    )
    location: typing.Optional[str] = pydantic.Field(alias="location", default=None)
