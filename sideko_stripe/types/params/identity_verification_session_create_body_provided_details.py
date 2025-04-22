import pydantic
import typing
import typing_extensions


class IdentityVerificationSessionCreateBodyProvidedDetails(typing_extensions.TypedDict):
    """
    Details provided about the user being verified. These details may be shown to the user.
    """

    email: typing_extensions.NotRequired[str]

    phone: typing_extensions.NotRequired[str]


class _SerializerIdentityVerificationSessionCreateBodyProvidedDetails(
    pydantic.BaseModel
):
    """
    Serializer for IdentityVerificationSessionCreateBodyProvidedDetails handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    email: typing.Optional[str] = pydantic.Field(alias="email", default=None)
    phone: typing.Optional[str] = pydantic.Field(alias="phone", default=None)
