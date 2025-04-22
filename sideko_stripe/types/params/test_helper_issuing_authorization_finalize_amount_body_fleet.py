import pydantic
import typing
import typing_extensions

from .test_helper_issuing_authorization_finalize_amount_body_fleet_cardholder_prompt_data import (
    TestHelperIssuingAuthorizationFinalizeAmountBodyFleetCardholderPromptData,
    _SerializerTestHelperIssuingAuthorizationFinalizeAmountBodyFleetCardholderPromptData,
)
from .test_helper_issuing_authorization_finalize_amount_body_fleet_reported_breakdown import (
    TestHelperIssuingAuthorizationFinalizeAmountBodyFleetReportedBreakdown,
    _SerializerTestHelperIssuingAuthorizationFinalizeAmountBodyFleetReportedBreakdown,
)


class TestHelperIssuingAuthorizationFinalizeAmountBodyFleet(
    typing_extensions.TypedDict
):
    """
    Fleet-specific information for authorizations using Fleet cards.
    """

    cardholder_prompt_data: typing_extensions.NotRequired[
        TestHelperIssuingAuthorizationFinalizeAmountBodyFleetCardholderPromptData
    ]

    purchase_type: typing_extensions.NotRequired[
        typing_extensions.Literal[
            "fuel_and_non_fuel_purchase", "fuel_purchase", "non_fuel_purchase"
        ]
    ]

    reported_breakdown: typing_extensions.NotRequired[
        TestHelperIssuingAuthorizationFinalizeAmountBodyFleetReportedBreakdown
    ]

    service_type: typing_extensions.NotRequired[
        typing_extensions.Literal[
            "full_service", "non_fuel_transaction", "self_service"
        ]
    ]


class _SerializerTestHelperIssuingAuthorizationFinalizeAmountBodyFleet(
    pydantic.BaseModel
):
    """
    Serializer for TestHelperIssuingAuthorizationFinalizeAmountBodyFleet handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    cardholder_prompt_data: typing.Optional[
        _SerializerTestHelperIssuingAuthorizationFinalizeAmountBodyFleetCardholderPromptData
    ] = pydantic.Field(alias="cardholder_prompt_data", default=None)
    purchase_type: typing.Optional[
        typing_extensions.Literal[
            "fuel_and_non_fuel_purchase", "fuel_purchase", "non_fuel_purchase"
        ]
    ] = pydantic.Field(alias="purchase_type", default=None)
    reported_breakdown: typing.Optional[
        _SerializerTestHelperIssuingAuthorizationFinalizeAmountBodyFleetReportedBreakdown
    ] = pydantic.Field(alias="reported_breakdown", default=None)
    service_type: typing.Optional[
        typing_extensions.Literal[
            "full_service", "non_fuel_transaction", "self_service"
        ]
    ] = pydantic.Field(alias="service_type", default=None)
