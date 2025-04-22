import pydantic
import typing
import typing_extensions


class TestHelperIssuingAuthorizationFraudChallengesRespondBody(
    typing_extensions.TypedDict, total=False
):
    """
    TestHelperIssuingAuthorizationFraudChallengesRespondBody
    """

    confirmed: typing_extensions.Required[bool]
    """
    Whether to simulate the user confirming that the transaction was legitimate (true) or telling Stripe that it was fraudulent (false).
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """


class _SerializerTestHelperIssuingAuthorizationFraudChallengesRespondBody(
    pydantic.BaseModel
):
    """
    Serializer for TestHelperIssuingAuthorizationFraudChallengesRespondBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    confirmed: bool = pydantic.Field(
        alias="confirmed",
    )
    expand: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="expand", default=None
    )
