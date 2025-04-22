import pydantic
import typing
import typing_extensions

from .test_helper_issuing_authorization_capture_body_purchase_details_fleet import (
    TestHelperIssuingAuthorizationCaptureBodyPurchaseDetailsFleet,
    _SerializerTestHelperIssuingAuthorizationCaptureBodyPurchaseDetailsFleet,
)
from .test_helper_issuing_authorization_capture_body_purchase_details_flight import (
    TestHelperIssuingAuthorizationCaptureBodyPurchaseDetailsFlight,
    _SerializerTestHelperIssuingAuthorizationCaptureBodyPurchaseDetailsFlight,
)
from .test_helper_issuing_authorization_capture_body_purchase_details_fuel import (
    TestHelperIssuingAuthorizationCaptureBodyPurchaseDetailsFuel,
    _SerializerTestHelperIssuingAuthorizationCaptureBodyPurchaseDetailsFuel,
)
from .test_helper_issuing_authorization_capture_body_purchase_details_lodging import (
    TestHelperIssuingAuthorizationCaptureBodyPurchaseDetailsLodging,
    _SerializerTestHelperIssuingAuthorizationCaptureBodyPurchaseDetailsLodging,
)
from .test_helper_issuing_authorization_capture_body_purchase_details_receipt_item import (
    TestHelperIssuingAuthorizationCaptureBodyPurchaseDetailsReceiptItem,
    _SerializerTestHelperIssuingAuthorizationCaptureBodyPurchaseDetailsReceiptItem,
)


class TestHelperIssuingAuthorizationCaptureBodyPurchaseDetails(
    typing_extensions.TypedDict
):
    """
    Additional purchase information that is optionally provided by the merchant.
    """

    fleet: typing_extensions.NotRequired[
        TestHelperIssuingAuthorizationCaptureBodyPurchaseDetailsFleet
    ]

    flight: typing_extensions.NotRequired[
        TestHelperIssuingAuthorizationCaptureBodyPurchaseDetailsFlight
    ]

    fuel: typing_extensions.NotRequired[
        TestHelperIssuingAuthorizationCaptureBodyPurchaseDetailsFuel
    ]

    lodging: typing_extensions.NotRequired[
        TestHelperIssuingAuthorizationCaptureBodyPurchaseDetailsLodging
    ]

    receipt: typing_extensions.NotRequired[
        typing.List[TestHelperIssuingAuthorizationCaptureBodyPurchaseDetailsReceiptItem]
    ]

    reference: typing_extensions.NotRequired[str]


class _SerializerTestHelperIssuingAuthorizationCaptureBodyPurchaseDetails(
    pydantic.BaseModel
):
    """
    Serializer for TestHelperIssuingAuthorizationCaptureBodyPurchaseDetails handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    fleet: typing.Optional[
        _SerializerTestHelperIssuingAuthorizationCaptureBodyPurchaseDetailsFleet
    ] = pydantic.Field(alias="fleet", default=None)
    flight: typing.Optional[
        _SerializerTestHelperIssuingAuthorizationCaptureBodyPurchaseDetailsFlight
    ] = pydantic.Field(alias="flight", default=None)
    fuel: typing.Optional[
        _SerializerTestHelperIssuingAuthorizationCaptureBodyPurchaseDetailsFuel
    ] = pydantic.Field(alias="fuel", default=None)
    lodging: typing.Optional[
        _SerializerTestHelperIssuingAuthorizationCaptureBodyPurchaseDetailsLodging
    ] = pydantic.Field(alias="lodging", default=None)
    receipt: typing.Optional[
        typing.List[
            _SerializerTestHelperIssuingAuthorizationCaptureBodyPurchaseDetailsReceiptItem
        ]
    ] = pydantic.Field(alias="receipt", default=None)
    reference: typing.Optional[str] = pydantic.Field(alias="reference", default=None)
