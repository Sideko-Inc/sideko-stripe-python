import pydantic
import typing
import typing_extensions

from .identity_verification_session_update_body_options_document_obj0 import (
    IdentityVerificationSessionUpdateBodyOptionsDocumentObj0,
    _SerializerIdentityVerificationSessionUpdateBodyOptionsDocumentObj0,
)


class IdentityVerificationSessionUpdateBodyOptions(typing_extensions.TypedDict):
    """
    A set of options for the session’s verification checks.
    """

    document: typing_extensions.NotRequired[
        typing.Union[IdentityVerificationSessionUpdateBodyOptionsDocumentObj0, str]
    ]


class _SerializerIdentityVerificationSessionUpdateBodyOptions(pydantic.BaseModel):
    """
    Serializer for IdentityVerificationSessionUpdateBodyOptions handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    document: typing.Optional[
        typing.Union[
            _SerializerIdentityVerificationSessionUpdateBodyOptionsDocumentObj0, str
        ]
    ] = pydantic.Field(alias="document", default=None)
