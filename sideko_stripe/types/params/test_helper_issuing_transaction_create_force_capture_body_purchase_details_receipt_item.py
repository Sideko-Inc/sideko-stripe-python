import pydantic
import typing
import typing_extensions


class TestHelperIssuingTransactionCreateForceCaptureBodyPurchaseDetailsReceiptItem(
    typing_extensions.TypedDict
):
    """
    TestHelperIssuingTransactionCreateForceCaptureBodyPurchaseDetailsReceiptItem
    """

    description: typing_extensions.NotRequired[str]

    quantity: typing_extensions.NotRequired[str]

    total: typing_extensions.NotRequired[int]

    unit_cost: typing_extensions.NotRequired[int]


class _SerializerTestHelperIssuingTransactionCreateForceCaptureBodyPurchaseDetailsReceiptItem(
    pydantic.BaseModel
):
    """
    Serializer for TestHelperIssuingTransactionCreateForceCaptureBodyPurchaseDetailsReceiptItem handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    description: typing.Optional[str] = pydantic.Field(
        alias="description", default=None
    )
    quantity: typing.Optional[str] = pydantic.Field(alias="quantity", default=None)
    total: typing.Optional[int] = pydantic.Field(alias="total", default=None)
    unit_cost: typing.Optional[int] = pydantic.Field(alias="unit_cost", default=None)
