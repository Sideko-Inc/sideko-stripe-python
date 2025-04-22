import pydantic
import typing
import typing_extensions


if typing_extensions.TYPE_CHECKING:
    from .file import File


class IssuingDisputeDuplicateEvidence(pydantic.BaseModel):
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
    card_statement: typing.Optional[typing.Union[str, "File"]] = pydantic.Field(
        alias="card_statement", default=None
    )
    """
    (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) Copy of the card statement showing that the product had already been paid for.
    """
    cash_receipt: typing.Optional[typing.Union[str, "File"]] = pydantic.Field(
        alias="cash_receipt", default=None
    )
    """
    (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) Copy of the receipt showing that the product had been paid for in cash.
    """
    check_image: typing.Optional[typing.Union[str, "File"]] = pydantic.Field(
        alias="check_image", default=None
    )
    """
    (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) Image of the front and back of the check that was used to pay for the product.
    """
    explanation: typing.Optional[str] = pydantic.Field(
        alias="explanation", default=None
    )
    """
    Explanation of why the cardholder is disputing this transaction.
    """
    original_transaction: typing.Optional[str] = pydantic.Field(
        alias="original_transaction", default=None
    )
    """
    Transaction (e.g., ipi_...) that the disputed transaction is a duplicate of. Of the two or more transactions that are copies of each other, this is original undisputed one.
    """
