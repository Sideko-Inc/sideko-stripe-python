import pydantic
import typing
import typing_extensions


class IssuingDisputeCreateBodyEvidenceMerchandiseNotAsDescribedObj0(
    typing_extensions.TypedDict
):
    """
    IssuingDisputeCreateBodyEvidenceMerchandiseNotAsDescribedObj0
    """

    additional_documentation: typing_extensions.NotRequired[typing.Union[str, str]]

    explanation: typing_extensions.NotRequired[typing.Union[str, str]]

    received_at: typing_extensions.NotRequired[typing.Union[int, str]]

    return_description: typing_extensions.NotRequired[typing.Union[str, str]]

    return_status: typing_extensions.NotRequired[
        typing_extensions.Literal["merchant_rejected", "successful"]
    ]

    returned_at: typing_extensions.NotRequired[typing.Union[int, str]]


class _SerializerIssuingDisputeCreateBodyEvidenceMerchandiseNotAsDescribedObj0(
    pydantic.BaseModel
):
    """
    Serializer for IssuingDisputeCreateBodyEvidenceMerchandiseNotAsDescribedObj0 handling case conversions
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
    received_at: typing.Optional[typing.Union[int, str]] = pydantic.Field(
        alias="received_at", default=None
    )
    return_description: typing.Optional[typing.Union[str, str]] = pydantic.Field(
        alias="return_description", default=None
    )
    return_status: typing.Optional[
        typing_extensions.Literal["merchant_rejected", "successful"]
    ] = pydantic.Field(alias="return_status", default=None)
    returned_at: typing.Optional[typing.Union[int, str]] = pydantic.Field(
        alias="returned_at", default=None
    )
