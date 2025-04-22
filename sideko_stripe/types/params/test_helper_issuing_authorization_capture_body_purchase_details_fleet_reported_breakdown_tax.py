import pydantic
import typing
import typing_extensions


class TestHelperIssuingAuthorizationCaptureBodyPurchaseDetailsFleetReportedBreakdownTax(
    typing_extensions.TypedDict
):
    """
    TestHelperIssuingAuthorizationCaptureBodyPurchaseDetailsFleetReportedBreakdownTax
    """

    local_amount_decimal: typing_extensions.NotRequired[str]

    national_amount_decimal: typing_extensions.NotRequired[str]


class _SerializerTestHelperIssuingAuthorizationCaptureBodyPurchaseDetailsFleetReportedBreakdownTax(
    pydantic.BaseModel
):
    """
    Serializer for TestHelperIssuingAuthorizationCaptureBodyPurchaseDetailsFleetReportedBreakdownTax handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    local_amount_decimal: typing.Optional[str] = pydantic.Field(
        alias="local_amount_decimal", default=None
    )
    national_amount_decimal: typing.Optional[str] = pydantic.Field(
        alias="national_amount_decimal", default=None
    )
