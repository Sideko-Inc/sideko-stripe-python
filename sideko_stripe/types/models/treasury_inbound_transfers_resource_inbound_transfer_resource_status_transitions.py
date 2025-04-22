import pydantic
import typing


class TreasuryInboundTransfersResourceInboundTransferResourceStatusTransitions(
    pydantic.BaseModel
):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    canceled_at: typing.Optional[int] = pydantic.Field(
        alias="canceled_at", default=None
    )
    """
    Timestamp describing when an InboundTransfer changed status to `canceled`.
    """
    failed_at: typing.Optional[int] = pydantic.Field(alias="failed_at", default=None)
    """
    Timestamp describing when an InboundTransfer changed status to `failed`.
    """
    succeeded_at: typing.Optional[int] = pydantic.Field(
        alias="succeeded_at", default=None
    )
    """
    Timestamp describing when an InboundTransfer changed status to `succeeded`.
    """
