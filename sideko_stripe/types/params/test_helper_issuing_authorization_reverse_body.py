import pydantic
import typing
import typing_extensions


class TestHelperIssuingAuthorizationReverseBody(
    typing_extensions.TypedDict, total=False
):
    """
    TestHelperIssuingAuthorizationReverseBody
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """

    reverse_amount: typing_extensions.NotRequired[int]
    """
    The amount to reverse from the authorization. If not provided, the full amount of the authorization will be reversed. This amount is in the authorization currency and in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal).
    """


class _SerializerTestHelperIssuingAuthorizationReverseBody(pydantic.BaseModel):
    """
    Serializer for TestHelperIssuingAuthorizationReverseBody handling case conversions
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
    reverse_amount: typing.Optional[int] = pydantic.Field(
        alias="reverse_amount", default=None
    )
