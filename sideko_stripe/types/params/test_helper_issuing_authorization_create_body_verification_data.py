import pydantic
import typing
import typing_extensions

from .test_helper_issuing_authorization_create_body_verification_data_authentication_exemption import (
    TestHelperIssuingAuthorizationCreateBodyVerificationDataAuthenticationExemption,
    _SerializerTestHelperIssuingAuthorizationCreateBodyVerificationDataAuthenticationExemption,
)
from .test_helper_issuing_authorization_create_body_verification_data_three_d_secure import (
    TestHelperIssuingAuthorizationCreateBodyVerificationDataThreeDSecure,
    _SerializerTestHelperIssuingAuthorizationCreateBodyVerificationDataThreeDSecure,
)


class TestHelperIssuingAuthorizationCreateBodyVerificationData(
    typing_extensions.TypedDict
):
    """
    Verifications that Stripe performed on information that the cardholder provided to the merchant.
    """

    address_line1_check: typing_extensions.NotRequired[
        typing_extensions.Literal["match", "mismatch", "not_provided"]
    ]

    address_postal_code_check: typing_extensions.NotRequired[
        typing_extensions.Literal["match", "mismatch", "not_provided"]
    ]

    authentication_exemption: typing_extensions.NotRequired[
        TestHelperIssuingAuthorizationCreateBodyVerificationDataAuthenticationExemption
    ]

    cvc_check: typing_extensions.NotRequired[
        typing_extensions.Literal["match", "mismatch", "not_provided"]
    ]

    expiry_check: typing_extensions.NotRequired[
        typing_extensions.Literal["match", "mismatch", "not_provided"]
    ]

    three_d_secure: typing_extensions.NotRequired[
        TestHelperIssuingAuthorizationCreateBodyVerificationDataThreeDSecure
    ]


class _SerializerTestHelperIssuingAuthorizationCreateBodyVerificationData(
    pydantic.BaseModel
):
    """
    Serializer for TestHelperIssuingAuthorizationCreateBodyVerificationData handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    address_line1_check: typing.Optional[
        typing_extensions.Literal["match", "mismatch", "not_provided"]
    ] = pydantic.Field(alias="address_line1_check", default=None)
    address_postal_code_check: typing.Optional[
        typing_extensions.Literal["match", "mismatch", "not_provided"]
    ] = pydantic.Field(alias="address_postal_code_check", default=None)
    authentication_exemption: typing.Optional[
        _SerializerTestHelperIssuingAuthorizationCreateBodyVerificationDataAuthenticationExemption
    ] = pydantic.Field(alias="authentication_exemption", default=None)
    cvc_check: typing.Optional[
        typing_extensions.Literal["match", "mismatch", "not_provided"]
    ] = pydantic.Field(alias="cvc_check", default=None)
    expiry_check: typing.Optional[
        typing_extensions.Literal["match", "mismatch", "not_provided"]
    ] = pydantic.Field(alias="expiry_check", default=None)
    three_d_secure: typing.Optional[
        _SerializerTestHelperIssuingAuthorizationCreateBodyVerificationDataThreeDSecure
    ] = pydantic.Field(alias="three_d_secure", default=None)
