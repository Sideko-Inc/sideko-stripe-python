import pydantic
import typing
import typing_extensions

from .test_helper_issuing_transaction_create_force_capture_body_purchase_details_flight_segments_item import (
    TestHelperIssuingTransactionCreateForceCaptureBodyPurchaseDetailsFlightSegmentsItem,
    _SerializerTestHelperIssuingTransactionCreateForceCaptureBodyPurchaseDetailsFlightSegmentsItem,
)


class TestHelperIssuingTransactionCreateForceCaptureBodyPurchaseDetailsFlight(
    typing_extensions.TypedDict
):
    """
    TestHelperIssuingTransactionCreateForceCaptureBodyPurchaseDetailsFlight
    """

    departure_at: typing_extensions.NotRequired[int]

    passenger_name: typing_extensions.NotRequired[str]

    refundable: typing_extensions.NotRequired[bool]

    segments: typing_extensions.NotRequired[
        typing.List[
            TestHelperIssuingTransactionCreateForceCaptureBodyPurchaseDetailsFlightSegmentsItem
        ]
    ]

    travel_agency: typing_extensions.NotRequired[str]


class _SerializerTestHelperIssuingTransactionCreateForceCaptureBodyPurchaseDetailsFlight(
    pydantic.BaseModel
):
    """
    Serializer for TestHelperIssuingTransactionCreateForceCaptureBodyPurchaseDetailsFlight handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    departure_at: typing.Optional[int] = pydantic.Field(
        alias="departure_at", default=None
    )
    passenger_name: typing.Optional[str] = pydantic.Field(
        alias="passenger_name", default=None
    )
    refundable: typing.Optional[bool] = pydantic.Field(alias="refundable", default=None)
    segments: typing.Optional[
        typing.List[
            _SerializerTestHelperIssuingTransactionCreateForceCaptureBodyPurchaseDetailsFlightSegmentsItem
        ]
    ] = pydantic.Field(alias="segments", default=None)
    travel_agency: typing.Optional[str] = pydantic.Field(
        alias="travel_agency", default=None
    )
