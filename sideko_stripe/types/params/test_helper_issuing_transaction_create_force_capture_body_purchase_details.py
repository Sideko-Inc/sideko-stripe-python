import pydantic
import typing
import typing_extensions

from .test_helper_issuing_transaction_create_force_capture_body_purchase_details_fleet import (
    TestHelperIssuingTransactionCreateForceCaptureBodyPurchaseDetailsFleet,
    _SerializerTestHelperIssuingTransactionCreateForceCaptureBodyPurchaseDetailsFleet,
)
from .test_helper_issuing_transaction_create_force_capture_body_purchase_details_flight import (
    TestHelperIssuingTransactionCreateForceCaptureBodyPurchaseDetailsFlight,
    _SerializerTestHelperIssuingTransactionCreateForceCaptureBodyPurchaseDetailsFlight,
)
from .test_helper_issuing_transaction_create_force_capture_body_purchase_details_fuel import (
    TestHelperIssuingTransactionCreateForceCaptureBodyPurchaseDetailsFuel,
    _SerializerTestHelperIssuingTransactionCreateForceCaptureBodyPurchaseDetailsFuel,
)
from .test_helper_issuing_transaction_create_force_capture_body_purchase_details_lodging import (
    TestHelperIssuingTransactionCreateForceCaptureBodyPurchaseDetailsLodging,
    _SerializerTestHelperIssuingTransactionCreateForceCaptureBodyPurchaseDetailsLodging,
)
from .test_helper_issuing_transaction_create_force_capture_body_purchase_details_receipt_item import (
    TestHelperIssuingTransactionCreateForceCaptureBodyPurchaseDetailsReceiptItem,
    _SerializerTestHelperIssuingTransactionCreateForceCaptureBodyPurchaseDetailsReceiptItem,
)


class TestHelperIssuingTransactionCreateForceCaptureBodyPurchaseDetails(
    typing_extensions.TypedDict
):
    """
    Additional purchase information that is optionally provided by the merchant.
    """

    fleet: typing_extensions.NotRequired[
        TestHelperIssuingTransactionCreateForceCaptureBodyPurchaseDetailsFleet
    ]

    flight: typing_extensions.NotRequired[
        TestHelperIssuingTransactionCreateForceCaptureBodyPurchaseDetailsFlight
    ]

    fuel: typing_extensions.NotRequired[
        TestHelperIssuingTransactionCreateForceCaptureBodyPurchaseDetailsFuel
    ]

    lodging: typing_extensions.NotRequired[
        TestHelperIssuingTransactionCreateForceCaptureBodyPurchaseDetailsLodging
    ]

    receipt: typing_extensions.NotRequired[
        typing.List[
            TestHelperIssuingTransactionCreateForceCaptureBodyPurchaseDetailsReceiptItem
        ]
    ]

    reference: typing_extensions.NotRequired[str]


class _SerializerTestHelperIssuingTransactionCreateForceCaptureBodyPurchaseDetails(
    pydantic.BaseModel
):
    """
    Serializer for TestHelperIssuingTransactionCreateForceCaptureBodyPurchaseDetails handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    fleet: typing.Optional[
        _SerializerTestHelperIssuingTransactionCreateForceCaptureBodyPurchaseDetailsFleet
    ] = pydantic.Field(alias="fleet", default=None)
    flight: typing.Optional[
        _SerializerTestHelperIssuingTransactionCreateForceCaptureBodyPurchaseDetailsFlight
    ] = pydantic.Field(alias="flight", default=None)
    fuel: typing.Optional[
        _SerializerTestHelperIssuingTransactionCreateForceCaptureBodyPurchaseDetailsFuel
    ] = pydantic.Field(alias="fuel", default=None)
    lodging: typing.Optional[
        _SerializerTestHelperIssuingTransactionCreateForceCaptureBodyPurchaseDetailsLodging
    ] = pydantic.Field(alias="lodging", default=None)
    receipt: typing.Optional[
        typing.List[
            _SerializerTestHelperIssuingTransactionCreateForceCaptureBodyPurchaseDetailsReceiptItem
        ]
    ] = pydantic.Field(alias="receipt", default=None)
    reference: typing.Optional[str] = pydantic.Field(alias="reference", default=None)
