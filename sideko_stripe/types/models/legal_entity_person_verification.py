import pydantic
import typing
import typing_extensions


if typing_extensions.TYPE_CHECKING:
    from .legal_entity_person_verification_document import (
        LegalEntityPersonVerificationDocument,
    )


class LegalEntityPersonVerification(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    additional_document: typing.Optional["LegalEntityPersonVerificationDocument"] = (
        pydantic.Field(alias="additional_document", default=None)
    )
    details: typing.Optional[str] = pydantic.Field(alias="details", default=None)
    """
    A user-displayable string describing the verification state for the person. For example, this may say "Provided identity information could not be verified".
    """
    details_code: typing.Optional[str] = pydantic.Field(
        alias="details_code", default=None
    )
    """
    One of `document_address_mismatch`, `document_dob_mismatch`, `document_duplicate_type`, `document_id_number_mismatch`, `document_name_mismatch`, `document_nationality_mismatch`, `failed_keyed_identity`, or `failed_other`. A machine-readable code specifying the verification state for the person.
    """
    document: typing.Optional["LegalEntityPersonVerificationDocument"] = pydantic.Field(
        alias="document", default=None
    )
    status: str = pydantic.Field(
        alias="status",
    )
    """
    The state of verification for the person. Possible values are `unverified`, `pending`, or `verified`.
    """
