import pydantic
import typing
import typing_extensions


class IssuingDisputeUpdateBodyEvidenceDuplicateObj0(typing_extensions.TypedDict):
    """
    IssuingDisputeUpdateBodyEvidenceDuplicateObj0
    """

    additional_documentation: typing_extensions.NotRequired[typing.Union[str, str]]

    card_statement: typing_extensions.NotRequired[typing.Union[str, str]]

    cash_receipt: typing_extensions.NotRequired[typing.Union[str, str]]

    check_image: typing_extensions.NotRequired[typing.Union[str, str]]

    explanation: typing_extensions.NotRequired[typing.Union[str, str]]

    original_transaction: typing_extensions.NotRequired[str]


class _SerializerIssuingDisputeUpdateBodyEvidenceDuplicateObj0(pydantic.BaseModel):
    """
    Serializer for IssuingDisputeUpdateBodyEvidenceDuplicateObj0 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    additional_documentation: typing.Optional[typing.Union[str, str]] = pydantic.Field(
        alias="additional_documentation", default=None
    )
    card_statement: typing.Optional[typing.Union[str, str]] = pydantic.Field(
        alias="card_statement", default=None
    )
    cash_receipt: typing.Optional[typing.Union[str, str]] = pydantic.Field(
        alias="cash_receipt", default=None
    )
    check_image: typing.Optional[typing.Union[str, str]] = pydantic.Field(
        alias="check_image", default=None
    )
    explanation: typing.Optional[typing.Union[str, str]] = pydantic.Field(
        alias="explanation", default=None
    )
    original_transaction: typing.Optional[str] = pydantic.Field(
        alias="original_transaction", default=None
    )
