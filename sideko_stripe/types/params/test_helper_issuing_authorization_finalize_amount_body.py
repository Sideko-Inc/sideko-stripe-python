import pydantic
import typing
import typing_extensions

from .test_helper_issuing_authorization_finalize_amount_body_fleet import (
    TestHelperIssuingAuthorizationFinalizeAmountBodyFleet,
    _SerializerTestHelperIssuingAuthorizationFinalizeAmountBodyFleet,
)
from .test_helper_issuing_authorization_finalize_amount_body_fuel import (
    TestHelperIssuingAuthorizationFinalizeAmountBodyFuel,
    _SerializerTestHelperIssuingAuthorizationFinalizeAmountBodyFuel,
)


class TestHelperIssuingAuthorizationFinalizeAmountBody(
    typing_extensions.TypedDict, total=False
):
    """
    TestHelperIssuingAuthorizationFinalizeAmountBody
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """

    final_amount: typing_extensions.Required[int]
    """
    The final authorization amount that will be captured by the merchant. This amount is in the authorization currency and in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal).
    """

    fleet: typing_extensions.NotRequired[
        TestHelperIssuingAuthorizationFinalizeAmountBodyFleet
    ]
    """
    Fleet-specific information for authorizations using Fleet cards.
    """

    fuel: typing_extensions.NotRequired[
        TestHelperIssuingAuthorizationFinalizeAmountBodyFuel
    ]
    """
    Information about fuel that was purchased with this transaction.
    """


class _SerializerTestHelperIssuingAuthorizationFinalizeAmountBody(pydantic.BaseModel):
    """
    Serializer for TestHelperIssuingAuthorizationFinalizeAmountBody handling case conversions
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
    final_amount: int = pydantic.Field(
        alias="final_amount",
    )
    fleet: typing.Optional[
        _SerializerTestHelperIssuingAuthorizationFinalizeAmountBodyFleet
    ] = pydantic.Field(alias="fleet", default=None)
    fuel: typing.Optional[
        _SerializerTestHelperIssuingAuthorizationFinalizeAmountBodyFuel
    ] = pydantic.Field(alias="fuel", default=None)
