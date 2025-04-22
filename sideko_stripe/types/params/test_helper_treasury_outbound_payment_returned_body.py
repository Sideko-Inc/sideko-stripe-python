import pydantic
import typing
import typing_extensions

from .test_helper_treasury_outbound_payment_returned_body_returned_details import (
    TestHelperTreasuryOutboundPaymentReturnedBodyReturnedDetails,
    _SerializerTestHelperTreasuryOutboundPaymentReturnedBodyReturnedDetails,
)


class TestHelperTreasuryOutboundPaymentReturnedBody(
    typing_extensions.TypedDict, total=False
):
    """
    TestHelperTreasuryOutboundPaymentReturnedBody
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """

    returned_details: typing_extensions.NotRequired[
        TestHelperTreasuryOutboundPaymentReturnedBodyReturnedDetails
    ]
    """
    Optional hash to set the return code.
    """


class _SerializerTestHelperTreasuryOutboundPaymentReturnedBody(pydantic.BaseModel):
    """
    Serializer for TestHelperTreasuryOutboundPaymentReturnedBody handling case conversions
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
    returned_details: typing.Optional[
        _SerializerTestHelperTreasuryOutboundPaymentReturnedBodyReturnedDetails
    ] = pydantic.Field(alias="returned_details", default=None)
