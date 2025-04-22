import pydantic
import typing_extensions


class TestHelperIssuingAuthorizationCreateBodyVerificationDataAuthenticationExemption(
    typing_extensions.TypedDict
):
    """
    TestHelperIssuingAuthorizationCreateBodyVerificationDataAuthenticationExemption
    """

    claimed_by: typing_extensions.Required[
        typing_extensions.Literal["acquirer", "issuer"]
    ]

    type_: typing_extensions.Required[
        typing_extensions.Literal[
            "low_value_transaction", "transaction_risk_analysis", "unknown"
        ]
    ]


class _SerializerTestHelperIssuingAuthorizationCreateBodyVerificationDataAuthenticationExemption(
    pydantic.BaseModel
):
    """
    Serializer for TestHelperIssuingAuthorizationCreateBodyVerificationDataAuthenticationExemption handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    claimed_by: typing_extensions.Literal["acquirer", "issuer"] = pydantic.Field(
        alias="claimed_by",
    )
    type_: typing_extensions.Literal[
        "low_value_transaction", "transaction_risk_analysis", "unknown"
    ] = pydantic.Field(
        alias="type",
    )
