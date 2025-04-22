import pydantic
import typing
import typing_extensions


class GelatoSessionLastError(pydantic.BaseModel):
    """
    Shows last VerificationSession error
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    code: typing.Optional[
        typing_extensions.Literal[
            "abandoned",
            "consent_declined",
            "country_not_supported",
            "device_not_supported",
            "document_expired",
            "document_type_not_supported",
            "document_unverified_other",
            "email_unverified_other",
            "email_verification_declined",
            "id_number_insufficient_document_data",
            "id_number_mismatch",
            "id_number_unverified_other",
            "phone_unverified_other",
            "phone_verification_declined",
            "selfie_document_missing_photo",
            "selfie_face_mismatch",
            "selfie_manipulated",
            "selfie_unverified_other",
            "under_supported_age",
        ]
    ] = pydantic.Field(alias="code", default=None)
    """
    A short machine-readable string giving the reason for the verification or user-session failure.
    """
    reason: typing.Optional[str] = pydantic.Field(alias="reason", default=None)
    """
    A message that explains the reason for verification or user-session failure.
    """
