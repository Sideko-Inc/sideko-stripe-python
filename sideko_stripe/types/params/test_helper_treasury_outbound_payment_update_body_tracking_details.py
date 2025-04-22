import pydantic
import typing
import typing_extensions

from .test_helper_treasury_outbound_payment_update_body_tracking_details_ach import (
    TestHelperTreasuryOutboundPaymentUpdateBodyTrackingDetailsAch,
    _SerializerTestHelperTreasuryOutboundPaymentUpdateBodyTrackingDetailsAch,
)
from .test_helper_treasury_outbound_payment_update_body_tracking_details_us_domestic_wire import (
    TestHelperTreasuryOutboundPaymentUpdateBodyTrackingDetailsUsDomesticWire,
    _SerializerTestHelperTreasuryOutboundPaymentUpdateBodyTrackingDetailsUsDomesticWire,
)


class TestHelperTreasuryOutboundPaymentUpdateBodyTrackingDetails(
    typing_extensions.TypedDict
):
    """
    Details about network-specific tracking information.
    """

    ach: typing_extensions.NotRequired[
        TestHelperTreasuryOutboundPaymentUpdateBodyTrackingDetailsAch
    ]

    type_: typing_extensions.Required[
        typing_extensions.Literal["ach", "us_domestic_wire"]
    ]

    us_domestic_wire: typing_extensions.NotRequired[
        TestHelperTreasuryOutboundPaymentUpdateBodyTrackingDetailsUsDomesticWire
    ]


class _SerializerTestHelperTreasuryOutboundPaymentUpdateBodyTrackingDetails(
    pydantic.BaseModel
):
    """
    Serializer for TestHelperTreasuryOutboundPaymentUpdateBodyTrackingDetails handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    ach: typing.Optional[
        _SerializerTestHelperTreasuryOutboundPaymentUpdateBodyTrackingDetailsAch
    ] = pydantic.Field(alias="ach", default=None)
    type_: typing_extensions.Literal["ach", "us_domestic_wire"] = pydantic.Field(
        alias="type",
    )
    us_domestic_wire: typing.Optional[
        _SerializerTestHelperTreasuryOutboundPaymentUpdateBodyTrackingDetailsUsDomesticWire
    ] = pydantic.Field(alias="us_domestic_wire", default=None)
