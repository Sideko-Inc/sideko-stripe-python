import pydantic
import typing


class TreasuryReceivedDebitsResourceLinkedFlows(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    debit_reversal: typing.Optional[str] = pydantic.Field(
        alias="debit_reversal", default=None
    )
    """
    The DebitReversal created as a result of this ReceivedDebit being reversed.
    """
    inbound_transfer: typing.Optional[str] = pydantic.Field(
        alias="inbound_transfer", default=None
    )
    """
    Set if the ReceivedDebit is associated with an InboundTransfer's return of funds.
    """
    issuing_authorization: typing.Optional[str] = pydantic.Field(
        alias="issuing_authorization", default=None
    )
    """
    Set if the ReceivedDebit was created due to an [Issuing Authorization](https://stripe.com/docs/api#issuing_authorizations) object.
    """
    issuing_transaction: typing.Optional[str] = pydantic.Field(
        alias="issuing_transaction", default=None
    )
    """
    Set if the ReceivedDebit is also viewable as an [Issuing Dispute](https://stripe.com/docs/api#issuing_disputes) object.
    """
    payout: typing.Optional[str] = pydantic.Field(alias="payout", default=None)
    """
    Set if the ReceivedDebit was created due to a [Payout](https://stripe.com/docs/api#payouts) object.
    """
