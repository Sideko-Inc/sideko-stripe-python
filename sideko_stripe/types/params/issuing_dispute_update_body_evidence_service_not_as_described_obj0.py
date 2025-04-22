import pydantic
import typing
import typing_extensions


class IssuingDisputeUpdateBodyEvidenceServiceNotAsDescribedObj0(
    typing_extensions.TypedDict
):
    """
    IssuingDisputeUpdateBodyEvidenceServiceNotAsDescribedObj0
    """

    additional_documentation: typing_extensions.NotRequired[typing.Union[str, str]]

    canceled_at: typing_extensions.NotRequired[typing.Union[int, str]]

    cancellation_reason: typing_extensions.NotRequired[typing.Union[str, str]]

    explanation: typing_extensions.NotRequired[typing.Union[str, str]]

    received_at: typing_extensions.NotRequired[typing.Union[int, str]]


class _SerializerIssuingDisputeUpdateBodyEvidenceServiceNotAsDescribedObj0(
    pydantic.BaseModel
):
    """
    Serializer for IssuingDisputeUpdateBodyEvidenceServiceNotAsDescribedObj0 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    additional_documentation: typing.Optional[typing.Union[str, str]] = pydantic.Field(
        alias="additional_documentation", default=None
    )
    canceled_at: typing.Optional[typing.Union[int, str]] = pydantic.Field(
        alias="canceled_at", default=None
    )
    cancellation_reason: typing.Optional[typing.Union[str, str]] = pydantic.Field(
        alias="cancellation_reason", default=None
    )
    explanation: typing.Optional[typing.Union[str, str]] = pydantic.Field(
        alias="explanation", default=None
    )
    received_at: typing.Optional[typing.Union[int, str]] = pydantic.Field(
        alias="received_at", default=None
    )
