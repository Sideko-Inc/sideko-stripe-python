import pydantic
import typing
import typing_extensions


class TestHelperIssuingAuthorizationCaptureBodyPurchaseDetailsFleetReportedBreakdownFuel(
    typing_extensions.TypedDict
):
    """
    TestHelperIssuingAuthorizationCaptureBodyPurchaseDetailsFleetReportedBreakdownFuel
    """

    gross_amount_decimal: typing_extensions.NotRequired[str]


class _SerializerTestHelperIssuingAuthorizationCaptureBodyPurchaseDetailsFleetReportedBreakdownFuel(
    pydantic.BaseModel
):
    """
    Serializer for TestHelperIssuingAuthorizationCaptureBodyPurchaseDetailsFleetReportedBreakdownFuel handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    gross_amount_decimal: typing.Optional[str] = pydantic.Field(
        alias="gross_amount_decimal", default=None
    )
