import pydantic
import typing
import typing_extensions


class TerminalConnectionToken(pydantic.BaseModel):
    """
    A Connection Token is used by the Stripe Terminal SDK to connect to a reader.

    Related guide: [Fleet management](https://stripe.com/docs/terminal/fleet/locations)
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    location: typing.Optional[str] = pydantic.Field(alias="location", default=None)
    """
    The id of the location that this connection token is scoped to. Note that location scoping only applies to internet-connected readers. For more details, see [the docs on scoping connection tokens](https://docs.stripe.com/terminal/fleet/locations-and-zones?dashboard-or-api=api#connection-tokens).
    """
    object: typing_extensions.Literal["terminal.connection_token"] = pydantic.Field(
        alias="object",
    )
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    secret: str = pydantic.Field(
        alias="secret",
    )
    """
    Your application should pass this token to the Stripe Terminal SDK.
    """
