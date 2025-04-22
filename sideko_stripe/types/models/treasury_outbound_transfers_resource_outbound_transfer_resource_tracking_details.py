import pydantic
import typing
import typing_extensions

from .treasury_outbound_transfers_resource_ach_tracking_details import (
    TreasuryOutboundTransfersResourceAchTrackingDetails,
)
from .treasury_outbound_transfers_resource_us_domestic_wire_tracking_details import (
    TreasuryOutboundTransfersResourceUsDomesticWireTrackingDetails,
)


class TreasuryOutboundTransfersResourceOutboundTransferResourceTrackingDetails(
    pydantic.BaseModel
):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    ach: typing.Optional[TreasuryOutboundTransfersResourceAchTrackingDetails] = (
        pydantic.Field(alias="ach", default=None)
    )
    type_: typing_extensions.Literal["ach", "us_domestic_wire"] = pydantic.Field(
        alias="type",
    )
    """
    The US bank account network used to send funds.
    """
    us_domestic_wire: typing.Optional[
        TreasuryOutboundTransfersResourceUsDomesticWireTrackingDetails
    ] = pydantic.Field(alias="us_domestic_wire", default=None)
