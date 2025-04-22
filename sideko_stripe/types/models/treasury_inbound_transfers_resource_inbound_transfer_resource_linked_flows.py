import pydantic
import typing


class TreasuryInboundTransfersResourceInboundTransferResourceLinkedFlows(
    pydantic.BaseModel
):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    received_debit: typing.Optional[str] = pydantic.Field(
        alias="received_debit", default=None
    )
    """
    If funds for this flow were returned after the flow went to the `succeeded` state, this field contains a reference to the ReceivedDebit return.
    """
