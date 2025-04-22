import pydantic
import typing
import typing_extensions


if typing_extensions.TYPE_CHECKING:
    from .file import File


class IssuingDisputeMerchandiseNotAsDescribedEvidence(pydantic.BaseModel):
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
    received_at: typing.Optional[int] = pydantic.Field(
        alias="received_at", default=None
    )
    """
    Date when the product was received.
    """
    return_description: typing.Optional[str] = pydantic.Field(
        alias="return_description", default=None
    )
    """
    Description of the cardholder's attempt to return the product.
    """
    return_status: typing.Optional[
        typing_extensions.Literal["merchant_rejected", "successful"]
    ] = pydantic.Field(alias="return_status", default=None)
    """
    Result of cardholder's attempt to return the product.
    """
    returned_at: typing.Optional[int] = pydantic.Field(
        alias="returned_at", default=None
    )
    """
    Date when the product was returned or attempted to be returned.
    """
