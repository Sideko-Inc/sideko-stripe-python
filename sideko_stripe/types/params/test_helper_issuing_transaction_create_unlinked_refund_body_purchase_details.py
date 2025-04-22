import pydantic
import typing
import typing_extensions

from .test_helper_issuing_transaction_create_unlinked_refund_body_purchase_details_fleet import (
    TestHelperIssuingTransactionCreateUnlinkedRefundBodyPurchaseDetailsFleet,
    _SerializerTestHelperIssuingTransactionCreateUnlinkedRefundBodyPurchaseDetailsFleet,
)
from .test_helper_issuing_transaction_create_unlinked_refund_body_purchase_details_flight import (
    TestHelperIssuingTransactionCreateUnlinkedRefundBodyPurchaseDetailsFlight,
    _SerializerTestHelperIssuingTransactionCreateUnlinkedRefundBodyPurchaseDetailsFlight,
)
from .test_helper_issuing_transaction_create_unlinked_refund_body_purchase_details_fuel import (
    TestHelperIssuingTransactionCreateUnlinkedRefundBodyPurchaseDetailsFuel,
    _SerializerTestHelperIssuingTransactionCreateUnlinkedRefundBodyPurchaseDetailsFuel,
)
from .test_helper_issuing_transaction_create_unlinked_refund_body_purchase_details_lodging import (
    TestHelperIssuingTransactionCreateUnlinkedRefundBodyPurchaseDetailsLodging,
    _SerializerTestHelperIssuingTransactionCreateUnlinkedRefundBodyPurchaseDetailsLodging,
)
from .test_helper_issuing_transaction_create_unlinked_refund_body_purchase_details_receipt_item import (
    TestHelperIssuingTransactionCreateUnlinkedRefundBodyPurchaseDetailsReceiptItem,
    _SerializerTestHelperIssuingTransactionCreateUnlinkedRefundBodyPurchaseDetailsReceiptItem,
)


class TestHelperIssuingTransactionCreateUnlinkedRefundBodyPurchaseDetails(
    typing_extensions.TypedDict
):
    """
    Additional purchase information that is optionally provided by the merchant.
    """

    fleet: typing_extensions.NotRequired[
        TestHelperIssuingTransactionCreateUnlinkedRefundBodyPurchaseDetailsFleet
    ]

    flight: typing_extensions.NotRequired[
        TestHelperIssuingTransactionCreateUnlinkedRefundBodyPurchaseDetailsFlight
    ]

    fuel: typing_extensions.NotRequired[
        TestHelperIssuingTransactionCreateUnlinkedRefundBodyPurchaseDetailsFuel
    ]

    lodging: typing_extensions.NotRequired[
        TestHelperIssuingTransactionCreateUnlinkedRefundBodyPurchaseDetailsLodging
    ]

    receipt: typing_extensions.NotRequired[
        typing.List[
            TestHelperIssuingTransactionCreateUnlinkedRefundBodyPurchaseDetailsReceiptItem
        ]
    ]

    reference: typing_extensions.NotRequired[str]


class _SerializerTestHelperIssuingTransactionCreateUnlinkedRefundBodyPurchaseDetails(
    pydantic.BaseModel
):
    """
    Serializer for TestHelperIssuingTransactionCreateUnlinkedRefundBodyPurchaseDetails handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    fleet: typing.Optional[
        _SerializerTestHelperIssuingTransactionCreateUnlinkedRefundBodyPurchaseDetailsFleet
    ] = pydantic.Field(alias="fleet", default=None)
    flight: typing.Optional[
        _SerializerTestHelperIssuingTransactionCreateUnlinkedRefundBodyPurchaseDetailsFlight
    ] = pydantic.Field(alias="flight", default=None)
    fuel: typing.Optional[
        _SerializerTestHelperIssuingTransactionCreateUnlinkedRefundBodyPurchaseDetailsFuel
    ] = pydantic.Field(alias="fuel", default=None)
    lodging: typing.Optional[
        _SerializerTestHelperIssuingTransactionCreateUnlinkedRefundBodyPurchaseDetailsLodging
    ] = pydantic.Field(alias="lodging", default=None)
    receipt: typing.Optional[
        typing.List[
            _SerializerTestHelperIssuingTransactionCreateUnlinkedRefundBodyPurchaseDetailsReceiptItem
        ]
    ] = pydantic.Field(alias="receipt", default=None)
    reference: typing.Optional[str] = pydantic.Field(alias="reference", default=None)
