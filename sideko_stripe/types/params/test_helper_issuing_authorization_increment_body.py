import pydantic
import typing
import typing_extensions


class TestHelperIssuingAuthorizationIncrementBody(
    typing_extensions.TypedDict, total=False
):
    """
    TestHelperIssuingAuthorizationIncrementBody
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """

    increment_amount: typing_extensions.Required[int]
    """
    The amount to increment the authorization by. This amount is in the authorization currency and in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal).
    """

    is_amount_controllable: typing_extensions.NotRequired[bool]
    """
    If set `true`, you may provide [amount](https://stripe.com/docs/api/issuing/authorizations/approve#approve_issuing_authorization-amount) to control how much to hold for the authorization.
    """


class _SerializerTestHelperIssuingAuthorizationIncrementBody(pydantic.BaseModel):
    """
    Serializer for TestHelperIssuingAuthorizationIncrementBody handling case conversions
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
    increment_amount: int = pydantic.Field(
        alias="increment_amount",
    )
    is_amount_controllable: typing.Optional[bool] = pydantic.Field(
        alias="is_amount_controllable", default=None
    )
