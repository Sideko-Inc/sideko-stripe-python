import pydantic
import typing
import typing_extensions


class IssuingDisputeUpdateBodyEvidenceOtherObj0(typing_extensions.TypedDict):
    """
    IssuingDisputeUpdateBodyEvidenceOtherObj0
    """

    additional_documentation: typing_extensions.NotRequired[typing.Union[str, str]]

    explanation: typing_extensions.NotRequired[typing.Union[str, str]]

    product_description: typing_extensions.NotRequired[typing.Union[str, str]]

    product_type: typing_extensions.NotRequired[
        typing_extensions.Literal["merchandise", "service"]
    ]


class _SerializerIssuingDisputeUpdateBodyEvidenceOtherObj0(pydantic.BaseModel):
    """
    Serializer for IssuingDisputeUpdateBodyEvidenceOtherObj0 handling case conversions
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
    product_description: typing.Optional[typing.Union[str, str]] = pydantic.Field(
        alias="product_description", default=None
    )
    product_type: typing.Optional[
        typing_extensions.Literal["merchandise", "service"]
    ] = pydantic.Field(alias="product_type", default=None)
