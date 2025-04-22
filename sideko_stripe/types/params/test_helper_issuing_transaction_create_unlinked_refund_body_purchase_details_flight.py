import pydantic
import typing
import typing_extensions

from .test_helper_issuing_transaction_create_unlinked_refund_body_purchase_details_flight_segments_item import (
    TestHelperIssuingTransactionCreateUnlinkedRefundBodyPurchaseDetailsFlightSegmentsItem,
    _SerializerTestHelperIssuingTransactionCreateUnlinkedRefundBodyPurchaseDetailsFlightSegmentsItem,
)


class TestHelperIssuingTransactionCreateUnlinkedRefundBodyPurchaseDetailsFlight(
    typing_extensions.TypedDict
):
    """
    TestHelperIssuingTransactionCreateUnlinkedRefundBodyPurchaseDetailsFlight
    """

    departure_at: typing_extensions.NotRequired[int]

    passenger_name: typing_extensions.NotRequired[str]

    refundable: typing_extensions.NotRequired[bool]

    segments: typing_extensions.NotRequired[
        typing.List[
            TestHelperIssuingTransactionCreateUnlinkedRefundBodyPurchaseDetailsFlightSegmentsItem
        ]
    ]

    travel_agency: typing_extensions.NotRequired[str]


class _SerializerTestHelperIssuingTransactionCreateUnlinkedRefundBodyPurchaseDetailsFlight(
    pydantic.BaseModel
):
    """
    Serializer for TestHelperIssuingTransactionCreateUnlinkedRefundBodyPurchaseDetailsFlight handling case conversions
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
            _SerializerTestHelperIssuingTransactionCreateUnlinkedRefundBodyPurchaseDetailsFlightSegmentsItem
        ]
    ] = pydantic.Field(alias="segments", default=None)
    travel_agency: typing.Optional[str] = pydantic.Field(
        alias="travel_agency", default=None
    )
