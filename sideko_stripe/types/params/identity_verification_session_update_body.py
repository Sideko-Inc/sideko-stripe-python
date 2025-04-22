import pydantic
import typing
import typing_extensions

from .identity_verification_session_update_body_metadata import (
    IdentityVerificationSessionUpdateBodyMetadata,
    _SerializerIdentityVerificationSessionUpdateBodyMetadata,
)
from .identity_verification_session_update_body_options import (
    IdentityVerificationSessionUpdateBodyOptions,
    _SerializerIdentityVerificationSessionUpdateBodyOptions,
)
from .identity_verification_session_update_body_provided_details import (
    IdentityVerificationSessionUpdateBodyProvidedDetails,
    _SerializerIdentityVerificationSessionUpdateBodyProvidedDetails,
)


class IdentityVerificationSessionUpdateBody(typing_extensions.TypedDict, total=False):
    """
    IdentityVerificationSessionUpdateBody
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """

    metadata: typing_extensions.NotRequired[
        IdentityVerificationSessionUpdateBodyMetadata
    ]
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    """

    options: typing_extensions.NotRequired[IdentityVerificationSessionUpdateBodyOptions]
    """
    A set of options for the session’s verification checks.
    """

    provided_details: typing_extensions.NotRequired[
        IdentityVerificationSessionUpdateBodyProvidedDetails
    ]
    """
    Details provided about the user being verified. These details may be shown to the user.
    """

    type_: typing_extensions.NotRequired[
        typing_extensions.Literal["document", "id_number"]
    ]
    """
    The type of [verification check](https://stripe.com/docs/identity/verification-checks) to be performed.
    """


class _SerializerIdentityVerificationSessionUpdateBody(pydantic.BaseModel):
    """
    Serializer for IdentityVerificationSessionUpdateBody handling case conversions
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
    metadata: typing.Optional[
        _SerializerIdentityVerificationSessionUpdateBodyMetadata
    ] = pydantic.Field(alias="metadata", default=None)
    options: typing.Optional[
        _SerializerIdentityVerificationSessionUpdateBodyOptions
    ] = pydantic.Field(alias="options", default=None)
    provided_details: typing.Optional[
        _SerializerIdentityVerificationSessionUpdateBodyProvidedDetails
    ] = pydantic.Field(alias="provided_details", default=None)
    type_: typing.Optional[typing_extensions.Literal["document", "id_number"]] = (
        pydantic.Field(alias="type", default=None)
    )
