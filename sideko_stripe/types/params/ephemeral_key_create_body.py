import pydantic
import typing
import typing_extensions


class EphemeralKeyCreateBody(typing_extensions.TypedDict, total=False):
    """
    EphemeralKeyCreateBody
    """

    customer: typing_extensions.NotRequired[str]
    """
    The ID of the Customer you'd like to modify using the resulting ephemeral key.
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """

    issuing_card: typing_extensions.NotRequired[str]
    """
    The ID of the Issuing Card you'd like to access using the resulting ephemeral key.
    """

    nonce: typing_extensions.NotRequired[str]
    """
    A single-use token, created by Stripe.js, used for creating ephemeral keys for Issuing Cards without exchanging sensitive information.
    """

    verification_session: typing_extensions.NotRequired[str]
    """
    The ID of the Identity VerificationSession you'd like to access using the resulting ephemeral key
    """


class _SerializerEphemeralKeyCreateBody(pydantic.BaseModel):
    """
    Serializer for EphemeralKeyCreateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    customer: typing.Optional[str] = pydantic.Field(alias="customer", default=None)
    expand: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="expand", default=None
    )
    issuing_card: typing.Optional[str] = pydantic.Field(
        alias="issuing_card", default=None
    )
    nonce: typing.Optional[str] = pydantic.Field(alias="nonce", default=None)
    verification_session: typing.Optional[str] = pydantic.Field(
        alias="verification_session", default=None
    )
