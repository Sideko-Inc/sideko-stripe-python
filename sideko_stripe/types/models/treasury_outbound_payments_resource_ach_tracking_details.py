import pydantic


class TreasuryOutboundPaymentsResourceAchTrackingDetails(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    trace_id: str = pydantic.Field(
        alias="trace_id",
    )
    """
    ACH trace ID of the OutboundPayment for payments sent over the `ach` network.
    """
