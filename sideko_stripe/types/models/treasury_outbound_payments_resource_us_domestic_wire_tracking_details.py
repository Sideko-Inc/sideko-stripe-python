import pydantic
import typing


class TreasuryOutboundPaymentsResourceUsDomesticWireTrackingDetails(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    chips: typing.Optional[str] = pydantic.Field(alias="chips", default=None)
    """
    CHIPS System Sequence Number (SSN) of the OutboundPayment for payments sent over the `us_domestic_wire` network.
    """
    imad: typing.Optional[str] = pydantic.Field(alias="imad", default=None)
    """
    IMAD of the OutboundPayment for payments sent over the `us_domestic_wire` network.
    """
    omad: typing.Optional[str] = pydantic.Field(alias="omad", default=None)
    """
    OMAD of the OutboundPayment for payments sent over the `us_domestic_wire` network.
    """
