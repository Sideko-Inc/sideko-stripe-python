import pydantic
import typing
import typing_extensions


class TestHelperIssuingTransactionCreateUnlinkedRefundBodyPurchaseDetailsLodging(
    typing_extensions.TypedDict
):
    """
    TestHelperIssuingTransactionCreateUnlinkedRefundBodyPurchaseDetailsLodging
    """

    check_in_at: typing_extensions.NotRequired[int]

    nights: typing_extensions.NotRequired[int]


class _SerializerTestHelperIssuingTransactionCreateUnlinkedRefundBodyPurchaseDetailsLodging(
    pydantic.BaseModel
):
    """
    Serializer for TestHelperIssuingTransactionCreateUnlinkedRefundBodyPurchaseDetailsLodging handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    check_in_at: typing.Optional[int] = pydantic.Field(
        alias="check_in_at", default=None
    )
    nights: typing.Optional[int] = pydantic.Field(alias="nights", default=None)
