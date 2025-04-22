import pydantic
import typing
import typing_extensions

from .test_helper_issuing_authorization_finalize_amount_body_fleet_reported_breakdown_fuel import (
    TestHelperIssuingAuthorizationFinalizeAmountBodyFleetReportedBreakdownFuel,
    _SerializerTestHelperIssuingAuthorizationFinalizeAmountBodyFleetReportedBreakdownFuel,
)
from .test_helper_issuing_authorization_finalize_amount_body_fleet_reported_breakdown_non_fuel import (
    TestHelperIssuingAuthorizationFinalizeAmountBodyFleetReportedBreakdownNonFuel,
    _SerializerTestHelperIssuingAuthorizationFinalizeAmountBodyFleetReportedBreakdownNonFuel,
)
from .test_helper_issuing_authorization_finalize_amount_body_fleet_reported_breakdown_tax import (
    TestHelperIssuingAuthorizationFinalizeAmountBodyFleetReportedBreakdownTax,
    _SerializerTestHelperIssuingAuthorizationFinalizeAmountBodyFleetReportedBreakdownTax,
)


class TestHelperIssuingAuthorizationFinalizeAmountBodyFleetReportedBreakdown(
    typing_extensions.TypedDict
):
    """
    TestHelperIssuingAuthorizationFinalizeAmountBodyFleetReportedBreakdown
    """

    fuel: typing_extensions.NotRequired[
        TestHelperIssuingAuthorizationFinalizeAmountBodyFleetReportedBreakdownFuel
    ]

    non_fuel: typing_extensions.NotRequired[
        TestHelperIssuingAuthorizationFinalizeAmountBodyFleetReportedBreakdownNonFuel
    ]

    tax: typing_extensions.NotRequired[
        TestHelperIssuingAuthorizationFinalizeAmountBodyFleetReportedBreakdownTax
    ]


class _SerializerTestHelperIssuingAuthorizationFinalizeAmountBodyFleetReportedBreakdown(
    pydantic.BaseModel
):
    """
    Serializer for TestHelperIssuingAuthorizationFinalizeAmountBodyFleetReportedBreakdown handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    fuel: typing.Optional[
        _SerializerTestHelperIssuingAuthorizationFinalizeAmountBodyFleetReportedBreakdownFuel
    ] = pydantic.Field(alias="fuel", default=None)
    non_fuel: typing.Optional[
        _SerializerTestHelperIssuingAuthorizationFinalizeAmountBodyFleetReportedBreakdownNonFuel
    ] = pydantic.Field(alias="non_fuel", default=None)
    tax: typing.Optional[
        _SerializerTestHelperIssuingAuthorizationFinalizeAmountBodyFleetReportedBreakdownTax
    ] = pydantic.Field(alias="tax", default=None)
