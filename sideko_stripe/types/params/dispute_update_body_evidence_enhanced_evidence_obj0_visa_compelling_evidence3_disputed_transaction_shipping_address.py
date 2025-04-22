import pydantic
import typing
import typing_extensions


class DisputeUpdateBodyEvidenceEnhancedEvidenceObj0VisaCompellingEvidence3DisputedTransactionShippingAddress(
    typing_extensions.TypedDict
):
    """
    DisputeUpdateBodyEvidenceEnhancedEvidenceObj0VisaCompellingEvidence3DisputedTransactionShippingAddress
    """

    city: typing_extensions.NotRequired[typing.Union[str, str]]

    country: typing_extensions.NotRequired[typing.Union[str, str]]

    line1: typing_extensions.NotRequired[typing.Union[str, str]]

    line2: typing_extensions.NotRequired[typing.Union[str, str]]

    postal_code: typing_extensions.NotRequired[typing.Union[str, str]]

    state: typing_extensions.NotRequired[typing.Union[str, str]]


class _SerializerDisputeUpdateBodyEvidenceEnhancedEvidenceObj0VisaCompellingEvidence3DisputedTransactionShippingAddress(
    pydantic.BaseModel
):
    """
    Serializer for DisputeUpdateBodyEvidenceEnhancedEvidenceObj0VisaCompellingEvidence3DisputedTransactionShippingAddress handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    city: typing.Optional[typing.Union[str, str]] = pydantic.Field(
        alias="city", default=None
    )
    country: typing.Optional[typing.Union[str, str]] = pydantic.Field(
        alias="country", default=None
    )
    line1: typing.Optional[typing.Union[str, str]] = pydantic.Field(
        alias="line1", default=None
    )
    line2: typing.Optional[typing.Union[str, str]] = pydantic.Field(
        alias="line2", default=None
    )
    postal_code: typing.Optional[typing.Union[str, str]] = pydantic.Field(
        alias="postal_code", default=None
    )
    state: typing.Optional[typing.Union[str, str]] = pydantic.Field(
        alias="state", default=None
    )
