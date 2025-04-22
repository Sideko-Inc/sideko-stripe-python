import pydantic
import typing
import typing_extensions

from .test_helper_issuing_authorization_create_body_fleet_reported_breakdown_fuel import (
    TestHelperIssuingAuthorizationCreateBodyFleetReportedBreakdownFuel,
    _SerializerTestHelperIssuingAuthorizationCreateBodyFleetReportedBreakdownFuel,
)
from .test_helper_issuing_authorization_create_body_fleet_reported_breakdown_non_fuel import (
    TestHelperIssuingAuthorizationCreateBodyFleetReportedBreakdownNonFuel,
    _SerializerTestHelperIssuingAuthorizationCreateBodyFleetReportedBreakdownNonFuel,
)
from .test_helper_issuing_authorization_create_body_fleet_reported_breakdown_tax import (
    TestHelperIssuingAuthorizationCreateBodyFleetReportedBreakdownTax,
    _SerializerTestHelperIssuingAuthorizationCreateBodyFleetReportedBreakdownTax,
)


class TestHelperIssuingAuthorizationCreateBodyFleetReportedBreakdown(
    typing_extensions.TypedDict
):
    """
    TestHelperIssuingAuthorizationCreateBodyFleetReportedBreakdown
    """

    fuel: typing_extensions.NotRequired[
        TestHelperIssuingAuthorizationCreateBodyFleetReportedBreakdownFuel
    ]

    non_fuel: typing_extensions.NotRequired[
        TestHelperIssuingAuthorizationCreateBodyFleetReportedBreakdownNonFuel
    ]

    tax: typing_extensions.NotRequired[
        TestHelperIssuingAuthorizationCreateBodyFleetReportedBreakdownTax
    ]


class _SerializerTestHelperIssuingAuthorizationCreateBodyFleetReportedBreakdown(
    pydantic.BaseModel
):
    """
    Serializer for TestHelperIssuingAuthorizationCreateBodyFleetReportedBreakdown handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    fuel: typing.Optional[
        _SerializerTestHelperIssuingAuthorizationCreateBodyFleetReportedBreakdownFuel
    ] = pydantic.Field(alias="fuel", default=None)
    non_fuel: typing.Optional[
        _SerializerTestHelperIssuingAuthorizationCreateBodyFleetReportedBreakdownNonFuel
    ] = pydantic.Field(alias="non_fuel", default=None)
    tax: typing.Optional[
        _SerializerTestHelperIssuingAuthorizationCreateBodyFleetReportedBreakdownTax
    ] = pydantic.Field(alias="tax", default=None)
