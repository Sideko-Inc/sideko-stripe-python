import pydantic
import typing
import typing_extensions


class ChargeDisputeCreateBodyEvidenceEnhancedEvidenceObj0VisaCompliance(
    typing_extensions.TypedDict
):
    """
    ChargeDisputeCreateBodyEvidenceEnhancedEvidenceObj0VisaCompliance
    """

    fee_acknowledged: typing_extensions.NotRequired[bool]


class _SerializerChargeDisputeCreateBodyEvidenceEnhancedEvidenceObj0VisaCompliance(
    pydantic.BaseModel
):
    """
    Serializer for ChargeDisputeCreateBodyEvidenceEnhancedEvidenceObj0VisaCompliance handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    fee_acknowledged: typing.Optional[bool] = pydantic.Field(
        alias="fee_acknowledged", default=None
    )
