import pydantic
import typing
import typing_extensions


class TestHelperIssuingTransactionCreateUnlinkedRefundBodyPurchaseDetailsReceiptItem(
    typing_extensions.TypedDict
):
    """
    TestHelperIssuingTransactionCreateUnlinkedRefundBodyPurchaseDetailsReceiptItem
    """

    description: typing_extensions.NotRequired[str]

    quantity: typing_extensions.NotRequired[str]

    total: typing_extensions.NotRequired[int]

    unit_cost: typing_extensions.NotRequired[int]


class _SerializerTestHelperIssuingTransactionCreateUnlinkedRefundBodyPurchaseDetailsReceiptItem(
    pydantic.BaseModel
):
    """
    Serializer for TestHelperIssuingTransactionCreateUnlinkedRefundBodyPurchaseDetailsReceiptItem handling case conversions
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
