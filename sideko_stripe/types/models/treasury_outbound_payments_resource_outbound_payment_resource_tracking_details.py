import pydantic
import typing
import typing_extensions

from .treasury_outbound_payments_resource_ach_tracking_details import (
    TreasuryOutboundPaymentsResourceAchTrackingDetails,
)
from .treasury_outbound_payments_resource_us_domestic_wire_tracking_details import (
    TreasuryOutboundPaymentsResourceUsDomesticWireTrackingDetails,
)


class TreasuryOutboundPaymentsResourceOutboundPaymentResourceTrackingDetails(
    pydantic.BaseModel
):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    ach: typing.Optional[TreasuryOutboundPaymentsResourceAchTrackingDetails] = (
        pydantic.Field(alias="ach", default=None)
    )
    type_: typing_extensions.Literal["ach", "us_domestic_wire"] = pydantic.Field(
        alias="type",
    )
    """
    The US bank account network used to send funds.
    """
    us_domestic_wire: typing.Optional[
        TreasuryOutboundPaymentsResourceUsDomesticWireTrackingDetails
    ] = pydantic.Field(alias="us_domestic_wire", default=None)
