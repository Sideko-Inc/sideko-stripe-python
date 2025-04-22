import pydantic
import typing
import typing_extensions

from .test_helper_issuing_authorization_capture_body_purchase_details import (
    TestHelperIssuingAuthorizationCaptureBodyPurchaseDetails,
    _SerializerTestHelperIssuingAuthorizationCaptureBodyPurchaseDetails,
)


class TestHelperIssuingAuthorizationCaptureBody(
    typing_extensions.TypedDict, total=False
):
    """
    TestHelperIssuingAuthorizationCaptureBody
    """

    capture_amount: typing_extensions.NotRequired[int]
    """
    The amount to capture from the authorization. If not provided, the full amount of the authorization will be captured. This amount is in the authorization currency and in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal).
    """

    close_authorization: typing_extensions.NotRequired[bool]
    """
    Whether to close the authorization after capture. Defaults to true. Set to false to enable multi-capture flows.
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """

    purchase_details: typing_extensions.NotRequired[
        TestHelperIssuingAuthorizationCaptureBodyPurchaseDetails
    ]
    """
    Additional purchase information that is optionally provided by the merchant.
    """


class _SerializerTestHelperIssuingAuthorizationCaptureBody(pydantic.BaseModel):
    """
    Serializer for TestHelperIssuingAuthorizationCaptureBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    capture_amount: typing.Optional[int] = pydantic.Field(
        alias="capture_amount", default=None
    )
    close_authorization: typing.Optional[bool] = pydantic.Field(
        alias="close_authorization", default=None
    )
    expand: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="expand", default=None
    )
    purchase_details: typing.Optional[
        _SerializerTestHelperIssuingAuthorizationCaptureBodyPurchaseDetails
    ] = pydantic.Field(alias="purchase_details", default=None)
