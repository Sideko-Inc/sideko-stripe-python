import pydantic
import typing_extensions


class TestHelperIssuingAuthorizationCreateBodyVerificationDataThreeDSecure(
    typing_extensions.TypedDict
):
    """
    TestHelperIssuingAuthorizationCreateBodyVerificationDataThreeDSecure
    """

    result: typing_extensions.Required[
        typing_extensions.Literal[
            "attempt_acknowledged", "authenticated", "failed", "required"
        ]
    ]


class _SerializerTestHelperIssuingAuthorizationCreateBodyVerificationDataThreeDSecure(
    pydantic.BaseModel
):
    """
    Serializer for TestHelperIssuingAuthorizationCreateBodyVerificationDataThreeDSecure handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    result: typing_extensions.Literal[
        "attempt_acknowledged", "authenticated", "failed", "required"
    ] = pydantic.Field(
        alias="result",
    )
