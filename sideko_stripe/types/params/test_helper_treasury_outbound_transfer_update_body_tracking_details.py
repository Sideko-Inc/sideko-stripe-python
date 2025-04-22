import pydantic
import typing
import typing_extensions

from .test_helper_treasury_outbound_transfer_update_body_tracking_details_ach import (
    TestHelperTreasuryOutboundTransferUpdateBodyTrackingDetailsAch,
    _SerializerTestHelperTreasuryOutboundTransferUpdateBodyTrackingDetailsAch,
)
from .test_helper_treasury_outbound_transfer_update_body_tracking_details_us_domestic_wire import (
    TestHelperTreasuryOutboundTransferUpdateBodyTrackingDetailsUsDomesticWire,
    _SerializerTestHelperTreasuryOutboundTransferUpdateBodyTrackingDetailsUsDomesticWire,
)


class TestHelperTreasuryOutboundTransferUpdateBodyTrackingDetails(
    typing_extensions.TypedDict
):
    """
    Details about network-specific tracking information.
    """

    ach: typing_extensions.NotRequired[
        TestHelperTreasuryOutboundTransferUpdateBodyTrackingDetailsAch
    ]

    type_: typing_extensions.Required[
        typing_extensions.Literal["ach", "us_domestic_wire"]
    ]

    us_domestic_wire: typing_extensions.NotRequired[
        TestHelperTreasuryOutboundTransferUpdateBodyTrackingDetailsUsDomesticWire
    ]


class _SerializerTestHelperTreasuryOutboundTransferUpdateBodyTrackingDetails(
    pydantic.BaseModel
):
    """
    Serializer for TestHelperTreasuryOutboundTransferUpdateBodyTrackingDetails handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    ach: typing.Optional[
        _SerializerTestHelperTreasuryOutboundTransferUpdateBodyTrackingDetailsAch
    ] = pydantic.Field(alias="ach", default=None)
    type_: typing_extensions.Literal["ach", "us_domestic_wire"] = pydantic.Field(
        alias="type",
    )
    us_domestic_wire: typing.Optional[
        _SerializerTestHelperTreasuryOutboundTransferUpdateBodyTrackingDetailsUsDomesticWire
    ] = pydantic.Field(alias="us_domestic_wire", default=None)
