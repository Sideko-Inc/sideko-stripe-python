import pydantic
import typing
import typing_extensions

from .identity_verification_session_create_body_metadata import (
    IdentityVerificationSessionCreateBodyMetadata,
    _SerializerIdentityVerificationSessionCreateBodyMetadata,
)
from .identity_verification_session_create_body_options import (
    IdentityVerificationSessionCreateBodyOptions,
    _SerializerIdentityVerificationSessionCreateBodyOptions,
)
from .identity_verification_session_create_body_provided_details import (
    IdentityVerificationSessionCreateBodyProvidedDetails,
    _SerializerIdentityVerificationSessionCreateBodyProvidedDetails,
)


class IdentityVerificationSessionCreateBody(typing_extensions.TypedDict, total=False):
    """
    IdentityVerificationSessionCreateBody
    """

    client_reference_id: typing_extensions.NotRequired[str]
    """
    A string to reference this user. This can be a customer ID, a session ID, or similar, and can be used to reconcile this verification with your internal systems.
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """

    metadata: typing_extensions.NotRequired[
        IdentityVerificationSessionCreateBodyMetadata
    ]
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    """

    options: typing_extensions.NotRequired[IdentityVerificationSessionCreateBodyOptions]
    """
    A set of options for the session’s verification checks.
    """

    provided_details: typing_extensions.NotRequired[
        IdentityVerificationSessionCreateBodyProvidedDetails
    ]
    """
    Details provided about the user being verified. These details may be shown to the user.
    """

    related_customer: typing_extensions.NotRequired[str]
    """
    Customer ID
    """

    return_url: typing_extensions.NotRequired[str]
    """
    The URL that the user will be redirected to upon completing the verification flow.
    """

    type_: typing_extensions.NotRequired[
        typing_extensions.Literal["document", "id_number"]
    ]
    """
    The type of [verification check](https://stripe.com/docs/identity/verification-checks) to be performed. You must provide a `type` if not passing `verification_flow`.
    """

    verification_flow: typing_extensions.NotRequired[str]
    """
    The ID of a verification flow from the Dashboard. See https://docs.stripe.com/identity/verification-flows.
    """


class _SerializerIdentityVerificationSessionCreateBody(pydantic.BaseModel):
    """
    Serializer for IdentityVerificationSessionCreateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    client_reference_id: typing.Optional[str] = pydantic.Field(
        alias="client_reference_id", default=None
    )
    expand: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="expand", default=None
    )
    metadata: typing.Optional[
        _SerializerIdentityVerificationSessionCreateBodyMetadata
    ] = pydantic.Field(alias="metadata", default=None)
    options: typing.Optional[
        _SerializerIdentityVerificationSessionCreateBodyOptions
    ] = pydantic.Field(alias="options", default=None)
    provided_details: typing.Optional[
        _SerializerIdentityVerificationSessionCreateBodyProvidedDetails
    ] = pydantic.Field(alias="provided_details", default=None)
    related_customer: typing.Optional[str] = pydantic.Field(
        alias="related_customer", default=None
    )
    return_url: typing.Optional[str] = pydantic.Field(alias="return_url", default=None)
    type_: typing.Optional[typing_extensions.Literal["document", "id_number"]] = (
        pydantic.Field(alias="type", default=None)
    )
    verification_flow: typing.Optional[str] = pydantic.Field(
        alias="verification_flow", default=None
    )
