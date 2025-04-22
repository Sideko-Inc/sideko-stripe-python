import pydantic
import typing
import typing_extensions


class TestHelperIssuingAuthorizationFinalizeAmountBodyFleetReportedBreakdownFuel(
    typing_extensions.TypedDict
):
    """
    TestHelperIssuingAuthorizationFinalizeAmountBodyFleetReportedBreakdownFuel
    """

    gross_amount_decimal: typing_extensions.NotRequired[str]


class _SerializerTestHelperIssuingAuthorizationFinalizeAmountBodyFleetReportedBreakdownFuel(
    pydantic.BaseModel
):
    """
    Serializer for TestHelperIssuingAuthorizationFinalizeAmountBodyFleetReportedBreakdownFuel handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    gross_amount_decimal: typing.Optional[str] = pydantic.Field(
        alias="gross_amount_decimal", default=None
    )
