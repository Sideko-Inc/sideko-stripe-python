import pydantic
import typing
import typing_extensions

from .test_helper_treasury_outbound_transfer_update_body_tracking_details import (
    TestHelperTreasuryOutboundTransferUpdateBodyTrackingDetails,
    _SerializerTestHelperTreasuryOutboundTransferUpdateBodyTrackingDetails,
)


class TestHelperTreasuryOutboundTransferUpdateBody(
    typing_extensions.TypedDict, total=False
):
    """
    TestHelperTreasuryOutboundTransferUpdateBody
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """

    tracking_details: typing_extensions.Required[
        TestHelperTreasuryOutboundTransferUpdateBodyTrackingDetails
    ]
    """
    Details about network-specific tracking information.
    """


class _SerializerTestHelperTreasuryOutboundTransferUpdateBody(pydantic.BaseModel):
    """
    Serializer for TestHelperTreasuryOutboundTransferUpdateBody handling case conversions
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
    tracking_details: _SerializerTestHelperTreasuryOutboundTransferUpdateBodyTrackingDetails = pydantic.Field(
        alias="tracking_details",
    )
