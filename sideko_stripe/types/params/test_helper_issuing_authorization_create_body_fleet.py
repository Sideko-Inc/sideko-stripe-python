import pydantic
import typing
import typing_extensions

from .test_helper_issuing_authorization_create_body_fleet_cardholder_prompt_data import (
    TestHelperIssuingAuthorizationCreateBodyFleetCardholderPromptData,
    _SerializerTestHelperIssuingAuthorizationCreateBodyFleetCardholderPromptData,
)
from .test_helper_issuing_authorization_create_body_fleet_reported_breakdown import (
    TestHelperIssuingAuthorizationCreateBodyFleetReportedBreakdown,
    _SerializerTestHelperIssuingAuthorizationCreateBodyFleetReportedBreakdown,
)


class TestHelperIssuingAuthorizationCreateBodyFleet(typing_extensions.TypedDict):
    """
    Fleet-specific information for authorizations using Fleet cards.
    """

    cardholder_prompt_data: typing_extensions.NotRequired[
        TestHelperIssuingAuthorizationCreateBodyFleetCardholderPromptData
    ]

    purchase_type: typing_extensions.NotRequired[
        typing_extensions.Literal[
            "fuel_and_non_fuel_purchase", "fuel_purchase", "non_fuel_purchase"
        ]
    ]

    reported_breakdown: typing_extensions.NotRequired[
        TestHelperIssuingAuthorizationCreateBodyFleetReportedBreakdown
    ]

    service_type: typing_extensions.NotRequired[
        typing_extensions.Literal[
            "full_service", "non_fuel_transaction", "self_service"
        ]
    ]


class _SerializerTestHelperIssuingAuthorizationCreateBodyFleet(pydantic.BaseModel):
    """
    Serializer for TestHelperIssuingAuthorizationCreateBodyFleet handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    cardholder_prompt_data: typing.Optional[
        _SerializerTestHelperIssuingAuthorizationCreateBodyFleetCardholderPromptData
    ] = pydantic.Field(alias="cardholder_prompt_data", default=None)
    purchase_type: typing.Optional[
        typing_extensions.Literal[
            "fuel_and_non_fuel_purchase", "fuel_purchase", "non_fuel_purchase"
        ]
    ] = pydantic.Field(alias="purchase_type", default=None)
    reported_breakdown: typing.Optional[
        _SerializerTestHelperIssuingAuthorizationCreateBodyFleetReportedBreakdown
    ] = pydantic.Field(alias="reported_breakdown", default=None)
    service_type: typing.Optional[
        typing_extensions.Literal[
            "full_service", "non_fuel_transaction", "self_service"
        ]
    ] = pydantic.Field(alias="service_type", default=None)
