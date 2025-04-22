import pydantic
import typing
import typing_extensions

from .test_helper_issuing_transaction_create_force_capture_body_purchase_details_fleet_reported_breakdown_fuel import (
    TestHelperIssuingTransactionCreateForceCaptureBodyPurchaseDetailsFleetReportedBreakdownFuel,
    _SerializerTestHelperIssuingTransactionCreateForceCaptureBodyPurchaseDetailsFleetReportedBreakdownFuel,
)
from .test_helper_issuing_transaction_create_force_capture_body_purchase_details_fleet_reported_breakdown_non_fuel import (
    TestHelperIssuingTransactionCreateForceCaptureBodyPurchaseDetailsFleetReportedBreakdownNonFuel,
    _SerializerTestHelperIssuingTransactionCreateForceCaptureBodyPurchaseDetailsFleetReportedBreakdownNonFuel,
)
from .test_helper_issuing_transaction_create_force_capture_body_purchase_details_fleet_reported_breakdown_tax import (
    TestHelperIssuingTransactionCreateForceCaptureBodyPurchaseDetailsFleetReportedBreakdownTax,
    _SerializerTestHelperIssuingTransactionCreateForceCaptureBodyPurchaseDetailsFleetReportedBreakdownTax,
)


class TestHelperIssuingTransactionCreateForceCaptureBodyPurchaseDetailsFleetReportedBreakdown(
    typing_extensions.TypedDict
):
    """
    TestHelperIssuingTransactionCreateForceCaptureBodyPurchaseDetailsFleetReportedBreakdown
    """

    fuel: typing_extensions.NotRequired[
        TestHelperIssuingTransactionCreateForceCaptureBodyPurchaseDetailsFleetReportedBreakdownFuel
    ]

    non_fuel: typing_extensions.NotRequired[
        TestHelperIssuingTransactionCreateForceCaptureBodyPurchaseDetailsFleetReportedBreakdownNonFuel
    ]

    tax: typing_extensions.NotRequired[
        TestHelperIssuingTransactionCreateForceCaptureBodyPurchaseDetailsFleetReportedBreakdownTax
    ]


class _SerializerTestHelperIssuingTransactionCreateForceCaptureBodyPurchaseDetailsFleetReportedBreakdown(
    pydantic.BaseModel
):
    """
    Serializer for TestHelperIssuingTransactionCreateForceCaptureBodyPurchaseDetailsFleetReportedBreakdown handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    fuel: typing.Optional[
        _SerializerTestHelperIssuingTransactionCreateForceCaptureBodyPurchaseDetailsFleetReportedBreakdownFuel
    ] = pydantic.Field(alias="fuel", default=None)
    non_fuel: typing.Optional[
        _SerializerTestHelperIssuingTransactionCreateForceCaptureBodyPurchaseDetailsFleetReportedBreakdownNonFuel
    ] = pydantic.Field(alias="non_fuel", default=None)
    tax: typing.Optional[
        _SerializerTestHelperIssuingTransactionCreateForceCaptureBodyPurchaseDetailsFleetReportedBreakdownTax
    ] = pydantic.Field(alias="tax", default=None)
