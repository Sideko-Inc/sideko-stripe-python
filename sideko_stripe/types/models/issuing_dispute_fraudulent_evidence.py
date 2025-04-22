import pydantic
import typing
import typing_extensions


if typing_extensions.TYPE_CHECKING:
    from .file import File


class IssuingDisputeFraudulentEvidence(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    additional_documentation: typing.Optional[typing.Union[str, "File"]] = (
        pydantic.Field(alias="additional_documentation", default=None)
    )
    """
    (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) Additional documentation supporting the dispute.
    """
    explanation: typing.Optional[str] = pydantic.Field(
        alias="explanation", default=None
    )
    """
    Explanation of why the cardholder is disputing this transaction.
    """
