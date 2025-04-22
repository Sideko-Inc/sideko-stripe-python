import pydantic
import typing
import typing_extensions

from .test_helper_issuing_transaction_create_unlinked_refund_body_purchase_details_fleet_reported_breakdown_fuel import (
    TestHelperIssuingTransactionCreateUnlinkedRefundBodyPurchaseDetailsFleetReportedBreakdownFuel,
    _SerializerTestHelperIssuingTransactionCreateUnlinkedRefundBodyPurchaseDetailsFleetReportedBreakdownFuel,
)
from .test_helper_issuing_transaction_create_unlinked_refund_body_purchase_details_fleet_reported_breakdown_non_fuel import (
    TestHelperIssuingTransactionCreateUnlinkedRefundBodyPurchaseDetailsFleetReportedBreakdownNonFuel,
    _SerializerTestHelperIssuingTransactionCreateUnlinkedRefundBodyPurchaseDetailsFleetReportedBreakdownNonFuel,
)
from .test_helper_issuing_transaction_create_unlinked_refund_body_purchase_details_fleet_reported_breakdown_tax import (
    TestHelperIssuingTransactionCreateUnlinkedRefundBodyPurchaseDetailsFleetReportedBreakdownTax,
    _SerializerTestHelperIssuingTransactionCreateUnlinkedRefundBodyPurchaseDetailsFleetReportedBreakdownTax,
)


class TestHelperIssuingTransactionCreateUnlinkedRefundBodyPurchaseDetailsFleetReportedBreakdown(
    typing_extensions.TypedDict
):
    """
    TestHelperIssuingTransactionCreateUnlinkedRefundBodyPurchaseDetailsFleetReportedBreakdown
    """

    fuel: typing_extensions.NotRequired[
        TestHelperIssuingTransactionCreateUnlinkedRefundBodyPurchaseDetailsFleetReportedBreakdownFuel
    ]

    non_fuel: typing_extensions.NotRequired[
        TestHelperIssuingTransactionCreateUnlinkedRefundBodyPurchaseDetailsFleetReportedBreakdownNonFuel
    ]

    tax: typing_extensions.NotRequired[
        TestHelperIssuingTransactionCreateUnlinkedRefundBodyPurchaseDetailsFleetReportedBreakdownTax
    ]


class _SerializerTestHelperIssuingTransactionCreateUnlinkedRefundBodyPurchaseDetailsFleetReportedBreakdown(
    pydantic.BaseModel
):
    """
    Serializer for TestHelperIssuingTransactionCreateUnlinkedRefundBodyPurchaseDetailsFleetReportedBreakdown handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    fuel: typing.Optional[
        _SerializerTestHelperIssuingTransactionCreateUnlinkedRefundBodyPurchaseDetailsFleetReportedBreakdownFuel
    ] = pydantic.Field(alias="fuel", default=None)
    non_fuel: typing.Optional[
        _SerializerTestHelperIssuingTransactionCreateUnlinkedRefundBodyPurchaseDetailsFleetReportedBreakdownNonFuel
    ] = pydantic.Field(alias="non_fuel", default=None)
    tax: typing.Optional[
        _SerializerTestHelperIssuingTransactionCreateUnlinkedRefundBodyPurchaseDetailsFleetReportedBreakdownTax
    ] = pydantic.Field(alias="tax", default=None)
