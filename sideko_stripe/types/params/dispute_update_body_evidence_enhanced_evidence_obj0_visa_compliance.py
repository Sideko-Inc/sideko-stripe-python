import pydantic
import typing
import typing_extensions


class DisputeUpdateBodyEvidenceEnhancedEvidenceObj0VisaCompliance(
    typing_extensions.TypedDict
):
    """
    DisputeUpdateBodyEvidenceEnhancedEvidenceObj0VisaCompliance
    """

    fee_acknowledged: typing_extensions.NotRequired[bool]


class _SerializerDisputeUpdateBodyEvidenceEnhancedEvidenceObj0VisaCompliance(
    pydantic.BaseModel
):
    """
    Serializer for DisputeUpdateBodyEvidenceEnhancedEvidenceObj0VisaCompliance handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    fee_acknowledged: typing.Optional[bool] = pydantic.Field(
        alias="fee_acknowledged", default=None
    )
