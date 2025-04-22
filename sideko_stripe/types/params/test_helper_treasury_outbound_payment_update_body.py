import pydantic
import typing
import typing_extensions

from .test_helper_treasury_outbound_payment_update_body_tracking_details import (
    TestHelperTreasuryOutboundPaymentUpdateBodyTrackingDetails,
    _SerializerTestHelperTreasuryOutboundPaymentUpdateBodyTrackingDetails,
)


class TestHelperTreasuryOutboundPaymentUpdateBody(
    typing_extensions.TypedDict, total=False
):
    """
    TestHelperTreasuryOutboundPaymentUpdateBody
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """

    tracking_details: typing_extensions.Required[
        TestHelperTreasuryOutboundPaymentUpdateBodyTrackingDetails
    ]
    """
    Details about network-specific tracking information.
    """


class _SerializerTestHelperTreasuryOutboundPaymentUpdateBody(pydantic.BaseModel):
    """
    Serializer for TestHelperTreasuryOutboundPaymentUpdateBody handling case conversions
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
    tracking_details: _SerializerTestHelperTreasuryOutboundPaymentUpdateBodyTrackingDetails = pydantic.Field(
        alias="tracking_details",
    )
