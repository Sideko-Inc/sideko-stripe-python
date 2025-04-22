import pydantic
import typing
import typing_extensions


class IssuingDisputeUpdateBodyEvidenceCanceledObj0(typing_extensions.TypedDict):
    """
    IssuingDisputeUpdateBodyEvidenceCanceledObj0
    """

    additional_documentation: typing_extensions.NotRequired[typing.Union[str, str]]

    canceled_at: typing_extensions.NotRequired[typing.Union[int, str]]

    cancellation_policy_provided: typing_extensions.NotRequired[typing.Union[bool, str]]

    cancellation_reason: typing_extensions.NotRequired[typing.Union[str, str]]

    expected_at: typing_extensions.NotRequired[typing.Union[int, str]]

    explanation: typing_extensions.NotRequired[typing.Union[str, str]]

    product_description: typing_extensions.NotRequired[typing.Union[str, str]]

    product_type: typing_extensions.NotRequired[
        typing_extensions.Literal["merchandise", "service"]
    ]

    return_status: typing_extensions.NotRequired[
        typing_extensions.Literal["merchant_rejected", "successful"]
    ]

    returned_at: typing_extensions.NotRequired[typing.Union[int, str]]


class _SerializerIssuingDisputeUpdateBodyEvidenceCanceledObj0(pydantic.BaseModel):
    """
    Serializer for IssuingDisputeUpdateBodyEvidenceCanceledObj0 handling case conversions
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
    cancellation_policy_provided: typing.Optional[typing.Union[bool, str]] = (
        pydantic.Field(alias="cancellation_policy_provided", default=None)
    )
    cancellation_reason: typing.Optional[typing.Union[str, str]] = pydantic.Field(
        alias="cancellation_reason", default=None
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
    return_status: typing.Optional[
        typing_extensions.Literal["merchant_rejected", "successful"]
    ] = pydantic.Field(alias="return_status", default=None)
    returned_at: typing.Optional[typing.Union[int, str]] = pydantic.Field(
        alias="returned_at", default=None
    )
