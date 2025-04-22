import pydantic
import typing
import typing_extensions


if typing_extensions.TYPE_CHECKING:
    from .treasury_received_credits_resource_source_flows_details import (
        TreasuryReceivedCreditsResourceSourceFlowsDetails,
    )


class TreasuryReceivedCreditsResourceLinkedFlows(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    credit_reversal: typing.Optional[str] = pydantic.Field(
        alias="credit_reversal", default=None
    )
    """
    The CreditReversal created as a result of this ReceivedCredit being reversed.
    """
    issuing_authorization: typing.Optional[str] = pydantic.Field(
        alias="issuing_authorization", default=None
    )
    """
    Set if the ReceivedCredit was created due to an [Issuing Authorization](https://stripe.com/docs/api#issuing_authorizations) object.
    """
    issuing_transaction: typing.Optional[str] = pydantic.Field(
        alias="issuing_transaction", default=None
    )
    """
    Set if the ReceivedCredit is also viewable as an [Issuing transaction](https://stripe.com/docs/api#issuing_transactions) object.
    """
    source_flow: typing.Optional[str] = pydantic.Field(
        alias="source_flow", default=None
    )
    """
    ID of the source flow. Set if `network` is `stripe` and the source flow is visible to the user. Examples of source flows include OutboundPayments, payouts, or CreditReversals.
    """
    source_flow_details: typing.Optional[
        "TreasuryReceivedCreditsResourceSourceFlowsDetails"
    ] = pydantic.Field(alias="source_flow_details", default=None)
    source_flow_type: typing.Optional[str] = pydantic.Field(
        alias="source_flow_type", default=None
    )
    """
    The type of flow that originated the ReceivedCredit (for example, `outbound_payment`).
    """
