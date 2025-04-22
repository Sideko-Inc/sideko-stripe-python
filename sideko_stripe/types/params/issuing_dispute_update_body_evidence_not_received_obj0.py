import pydantic
import typing
import typing_extensions


class IssuingDisputeUpdateBodyEvidenceNotReceivedObj0(typing_extensions.TypedDict):
    """
    IssuingDisputeUpdateBodyEvidenceNotReceivedObj0
    """

    additional_documentation: typing_extensions.NotRequired[typing.Union[str, str]]

    expected_at: typing_extensions.NotRequired[typing.Union[int, str]]

    explanation: typing_extensions.NotRequired[typing.Union[str, str]]

    product_description: typing_extensions.NotRequired[typing.Union[str, str]]

    product_type: typing_extensions.NotRequired[
        typing_extensions.Literal["merchandise", "service"]
    ]


class _SerializerIssuingDisputeUpdateBodyEvidenceNotReceivedObj0(pydantic.BaseModel):
    """
    Serializer for IssuingDisputeUpdateBodyEvidenceNotReceivedObj0 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    additional_documentation: typing.Optional[typing.Union[str, str]] = pydantic.Field(
        alias="additional_documentation", default=None
    )
    expected_at: typing.Optional[typing.Union[int, str]] = pydantic.Field(
        alias="expected_at", default=None
    )
    explanation: typing.Optional[typing.Union[str, str]] = pydantic.Field(
        alias="explanation", default=None
    )
    product_description: typing.Optional[typing.Union[str, str]] = pydantic.Field(
        alias="product_description", default=None
    )
    product_type: typing.Optional[
        typing_extensions.Literal["merchandise", "service"]
    ] = pydantic.Field(alias="product_type", default=None)
