import pydantic
import typing
import typing_extensions

from .test_helper_issuing_transaction_create_force_capture_body_merchant_data import (
    TestHelperIssuingTransactionCreateForceCaptureBodyMerchantData,
    _SerializerTestHelperIssuingTransactionCreateForceCaptureBodyMerchantData,
)
from .test_helper_issuing_transaction_create_force_capture_body_purchase_details import (
    TestHelperIssuingTransactionCreateForceCaptureBodyPurchaseDetails,
    _SerializerTestHelperIssuingTransactionCreateForceCaptureBodyPurchaseDetails,
)


class TestHelperIssuingTransactionCreateForceCaptureBody(
    typing_extensions.TypedDict, total=False
):
    """
    TestHelperIssuingTransactionCreateForceCaptureBody
    """

    amount: typing_extensions.Required[int]
    """
    The total amount to attempt to capture. This amount is in the provided currency, or defaults to the cards currency, and in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal).
    """

    card: typing_extensions.Required[str]
    """
    Card associated with this transaction.
    """

    currency: typing_extensions.NotRequired[str]
    """
    The currency of the capture. If not provided, defaults to the currency of the card. Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """

    merchant_data: typing_extensions.NotRequired[
        TestHelperIssuingTransactionCreateForceCaptureBodyMerchantData
    ]
    """
    Details about the seller (grocery store, e-commerce website, etc.) where the card authorization happened.
    """

    purchase_details: typing_extensions.NotRequired[
        TestHelperIssuingTransactionCreateForceCaptureBodyPurchaseDetails
    ]
    """
    Additional purchase information that is optionally provided by the merchant.
    """


class _SerializerTestHelperIssuingTransactionCreateForceCaptureBody(pydantic.BaseModel):
    """
    Serializer for TestHelperIssuingTransactionCreateForceCaptureBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    amount: int = pydantic.Field(
        alias="amount",
    )
    card: str = pydantic.Field(
        alias="card",
    )
    currency: typing.Optional[str] = pydantic.Field(alias="currency", default=None)
    expand: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="expand", default=None
    )
    merchant_data: typing.Optional[
        _SerializerTestHelperIssuingTransactionCreateForceCaptureBodyMerchantData
    ] = pydantic.Field(alias="merchant_data", default=None)
    purchase_details: typing.Optional[
        _SerializerTestHelperIssuingTransactionCreateForceCaptureBodyPurchaseDetails
    ] = pydantic.Field(alias="purchase_details", default=None)
