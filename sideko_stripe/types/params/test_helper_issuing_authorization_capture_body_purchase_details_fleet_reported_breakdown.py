import pydantic
import typing
import typing_extensions

from .test_helper_issuing_authorization_capture_body_purchase_details_fleet_reported_breakdown_fuel import (
    TestHelperIssuingAuthorizationCaptureBodyPurchaseDetailsFleetReportedBreakdownFuel,
    _SerializerTestHelperIssuingAuthorizationCaptureBodyPurchaseDetailsFleetReportedBreakdownFuel,
)
from .test_helper_issuing_authorization_capture_body_purchase_details_fleet_reported_breakdown_non_fuel import (
    TestHelperIssuingAuthorizationCaptureBodyPurchaseDetailsFleetReportedBreakdownNonFuel,
    _SerializerTestHelperIssuingAuthorizationCaptureBodyPurchaseDetailsFleetReportedBreakdownNonFuel,
)
from .test_helper_issuing_authorization_capture_body_purchase_details_fleet_reported_breakdown_tax import (
    TestHelperIssuingAuthorizationCaptureBodyPurchaseDetailsFleetReportedBreakdownTax,
    _SerializerTestHelperIssuingAuthorizationCaptureBodyPurchaseDetailsFleetReportedBreakdownTax,
)


class TestHelperIssuingAuthorizationCaptureBodyPurchaseDetailsFleetReportedBreakdown(
    typing_extensions.TypedDict
):
    """
    TestHelperIssuingAuthorizationCaptureBodyPurchaseDetailsFleetReportedBreakdown
    """

    fuel: typing_extensions.NotRequired[
        TestHelperIssuingAuthorizationCaptureBodyPurchaseDetailsFleetReportedBreakdownFuel
    ]

    non_fuel: typing_extensions.NotRequired[
        TestHelperIssuingAuthorizationCaptureBodyPurchaseDetailsFleetReportedBreakdownNonFuel
    ]

    tax: typing_extensions.NotRequired[
        TestHelperIssuingAuthorizationCaptureBodyPurchaseDetailsFleetReportedBreakdownTax
    ]


class _SerializerTestHelperIssuingAuthorizationCaptureBodyPurchaseDetailsFleetReportedBreakdown(
    pydantic.BaseModel
):
    """
    Serializer for TestHelperIssuingAuthorizationCaptureBodyPurchaseDetailsFleetReportedBreakdown handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    fuel: typing.Optional[
        _SerializerTestHelperIssuingAuthorizationCaptureBodyPurchaseDetailsFleetReportedBreakdownFuel
    ] = pydantic.Field(alias="fuel", default=None)
    non_fuel: typing.Optional[
        _SerializerTestHelperIssuingAuthorizationCaptureBodyPurchaseDetailsFleetReportedBreakdownNonFuel
    ] = pydantic.Field(alias="non_fuel", default=None)
    tax: typing.Optional[
        _SerializerTestHelperIssuingAuthorizationCaptureBodyPurchaseDetailsFleetReportedBreakdownTax
    ] = pydantic.Field(alias="tax", default=None)
