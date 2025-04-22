import pydantic
import typing
import typing_extensions


class TestHelperIssuingTransactionRefundBody(typing_extensions.TypedDict, total=False):
    """
    TestHelperIssuingTransactionRefundBody
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """

    refund_amount: typing_extensions.NotRequired[int]
    """
    The total amount to attempt to refund. This amount is in the provided currency, or defaults to the cards currency, and in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal).
    """


class _SerializerTestHelperIssuingTransactionRefundBody(pydantic.BaseModel):
    """
    Serializer for TestHelperIssuingTransactionRefundBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    expand: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="expand", default=None
    )
    refund_amount: typing.Optional[int] = pydantic.Field(
        alias="refund_amount", default=None
    )
