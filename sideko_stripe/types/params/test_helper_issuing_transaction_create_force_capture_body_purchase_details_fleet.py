import pydantic
import typing
import typing_extensions

from .test_helper_issuing_transaction_create_force_capture_body_purchase_details_fleet_cardholder_prompt_data import (
    TestHelperIssuingTransactionCreateForceCaptureBodyPurchaseDetailsFleetCardholderPromptData,
    _SerializerTestHelperIssuingTransactionCreateForceCaptureBodyPurchaseDetailsFleetCardholderPromptData,
)
from .test_helper_issuing_transaction_create_force_capture_body_purchase_details_fleet_reported_breakdown import (
    TestHelperIssuingTransactionCreateForceCaptureBodyPurchaseDetailsFleetReportedBreakdown,
    _SerializerTestHelperIssuingTransactionCreateForceCaptureBodyPurchaseDetailsFleetReportedBreakdown,
)


class TestHelperIssuingTransactionCreateForceCaptureBodyPurchaseDetailsFleet(
    typing_extensions.TypedDict
):
    """
    TestHelperIssuingTransactionCreateForceCaptureBodyPurchaseDetailsFleet
    """

    cardholder_prompt_data: typing_extensions.NotRequired[
        TestHelperIssuingTransactionCreateForceCaptureBodyPurchaseDetailsFleetCardholderPromptData
    ]

    purchase_type: typing_extensions.NotRequired[
        typing_extensions.Literal[
            "fuel_and_non_fuel_purchase", "fuel_purchase", "non_fuel_purchase"
        ]
    ]

    reported_breakdown: typing_extensions.NotRequired[
        TestHelperIssuingTransactionCreateForceCaptureBodyPurchaseDetailsFleetReportedBreakdown
    ]

    service_type: typing_extensions.NotRequired[
        typing_extensions.Literal[
            "full_service", "non_fuel_transaction", "self_service"
        ]
    ]


class _SerializerTestHelperIssuingTransactionCreateForceCaptureBodyPurchaseDetailsFleet(
    pydantic.BaseModel
):
    """
    Serializer for TestHelperIssuingTransactionCreateForceCaptureBodyPurchaseDetailsFleet handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    cardholder_prompt_data: typing.Optional[
        _SerializerTestHelperIssuingTransactionCreateForceCaptureBodyPurchaseDetailsFleetCardholderPromptData
    ] = pydantic.Field(alias="cardholder_prompt_data", default=None)
    purchase_type: typing.Optional[
        typing_extensions.Literal[
            "fuel_and_non_fuel_purchase", "fuel_purchase", "non_fuel_purchase"
        ]
    ] = pydantic.Field(alias="purchase_type", default=None)
    reported_breakdown: typing.Optional[
        _SerializerTestHelperIssuingTransactionCreateForceCaptureBodyPurchaseDetailsFleetReportedBreakdown
    ] = pydantic.Field(alias="reported_breakdown", default=None)
    service_type: typing.Optional[
        typing_extensions.Literal[
            "full_service", "non_fuel_transaction", "self_service"
        ]
    ] = pydantic.Field(alias="service_type", default=None)
