import pydantic
import typing
import typing_extensions


if typing_extensions.TYPE_CHECKING:
    from .file import File


class LegalEntityCompanyVerificationDocument(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    back: typing.Optional[typing.Union[str, "File"]] = pydantic.Field(
        alias="back", default=None
    )
    """
    The back of a document returned by a [file upload](https://stripe.com/docs/api#create_file) with a `purpose` value of `additional_verification`.
    """
    details: typing.Optional[str] = pydantic.Field(alias="details", default=None)
    """
    A user-displayable string describing the verification state of this document.
    """
    details_code: typing.Optional[str] = pydantic.Field(
        alias="details_code", default=None
    )
    """
    One of `document_corrupt`, `document_expired`, `document_failed_copy`, `document_failed_greyscale`, `document_failed_other`, `document_failed_test_mode`, `document_fraudulent`, `document_incomplete`, `document_invalid`, `document_manipulated`, `document_not_readable`, `document_not_uploaded`, `document_type_not_supported`, or `document_too_large`. A machine-readable code specifying the verification state for this document.
    """
    front: typing.Optional[typing.Union[str, "File"]] = pydantic.Field(
        alias="front", default=None
    )
    """
    The front of a document returned by a [file upload](https://stripe.com/docs/api#create_file) with a `purpose` value of `additional_verification`.
    """
