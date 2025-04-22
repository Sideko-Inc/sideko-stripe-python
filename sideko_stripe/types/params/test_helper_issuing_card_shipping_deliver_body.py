import pydantic
import typing
import typing_extensions


class TestHelperIssuingCardShippingDeliverBody(
    typing_extensions.TypedDict, total=False
):
    """
    TestHelperIssuingCardShippingDeliverBody
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """


class _SerializerTestHelperIssuingCardShippingDeliverBody(pydantic.BaseModel):
    """
    Serializer for TestHelperIssuingCardShippingDeliverBody handling case conversions
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
