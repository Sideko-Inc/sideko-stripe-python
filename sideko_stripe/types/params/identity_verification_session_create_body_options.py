import pydantic
import typing
import typing_extensions

from .identity_verification_session_create_body_options_document_obj0 import (
    IdentityVerificationSessionCreateBodyOptionsDocumentObj0,
    _SerializerIdentityVerificationSessionCreateBodyOptionsDocumentObj0,
)


class IdentityVerificationSessionCreateBodyOptions(typing_extensions.TypedDict):
    """
    A set of options for the session’s verification checks.
    """

    document: typing_extensions.NotRequired[
        typing.Union[IdentityVerificationSessionCreateBodyOptionsDocumentObj0, str]
    ]


class _SerializerIdentityVerificationSessionCreateBodyOptions(pydantic.BaseModel):
    """
    Serializer for IdentityVerificationSessionCreateBodyOptions handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    document: typing.Optional[
        typing.Union[
            _SerializerIdentityVerificationSessionCreateBodyOptionsDocumentObj0, str
        ]
    ] = pydantic.Field(alias="document", default=None)
