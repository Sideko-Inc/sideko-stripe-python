import pydantic
import typing
import typing_extensions


class IssuingDisputeCreateBodyEvidenceFraudulentObj0(typing_extensions.TypedDict):
    """
    IssuingDisputeCreateBodyEvidenceFraudulentObj0
    """

    additional_documentation: typing_extensions.NotRequired[typing.Union[str, str]]

    explanation: typing_extensions.NotRequired[typing.Union[str, str]]


class _SerializerIssuingDisputeCreateBodyEvidenceFraudulentObj0(pydantic.BaseModel):
    """
    Serializer for IssuingDisputeCreateBodyEvidenceFraudulentObj0 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    additional_documentation: typing.Optional[typing.Union[str, str]] = pydantic.Field(
        alias="additional_documentation", default=None
    )
    explanation: typing.Optional[typing.Union[str, str]] = pydantic.Field(
        alias="explanation", default=None
    )
