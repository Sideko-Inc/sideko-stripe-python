import pydantic
import typing
import typing_extensions


if typing_extensions.TYPE_CHECKING:
    from .file import File


class IssuingDisputeCanceledEvidence(pydantic.BaseModel):
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
    canceled_at: typing.Optional[int] = pydantic.Field(
        alias="canceled_at", default=None
    )
    """
    Date when order was canceled.
    """
    cancellation_policy_provided: typing.Optional[bool] = pydantic.Field(
        alias="cancellation_policy_provided", default=None
    )
    """
    Whether the cardholder was provided with a cancellation policy.
    """
    cancellation_reason: typing.Optional[str] = pydantic.Field(
        alias="cancellation_reason", default=None
    )
    """
    Reason for canceling the order.
    """
    expected_at: typing.Optional[int] = pydantic.Field(
        alias="expected_at", default=None
    )
    """
    Date when the cardholder expected to receive the product.
    """
    explanation: typing.Optional[str] = pydantic.Field(
        alias="explanation", default=None
    )
    """
    Explanation of why the cardholder is disputing this transaction.
    """
    product_description: typing.Optional[str] = pydantic.Field(
        alias="product_description", default=None
    )
    """
    Description of the merchandise or service that was purchased.
    """
    product_type: typing.Optional[
        typing_extensions.Literal["merchandise", "service"]
    ] = pydantic.Field(alias="product_type", default=None)
    """
    Whether the product was a merchandise or service.
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
