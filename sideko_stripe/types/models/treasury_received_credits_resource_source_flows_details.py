import pydantic
import typing
import typing_extensions


if typing_extensions.TYPE_CHECKING:
    from .payout import Payout
    from .treasury_credit_reversal import TreasuryCreditReversal
    from .treasury_outbound_payment import TreasuryOutboundPayment
    from .treasury_outbound_transfer import TreasuryOutboundTransfer


class TreasuryReceivedCreditsResourceSourceFlowsDetails(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    credit_reversal: typing.Optional["TreasuryCreditReversal"] = pydantic.Field(
        alias="credit_reversal", default=None
    )
    """
    You can reverse some [ReceivedCredits](https://stripe.com/docs/api#received_credits) depending on their network and source flow. Reversing a ReceivedCredit leads to the creation of a new object known as a CreditReversal.
    """
    outbound_payment: typing.Optional["TreasuryOutboundPayment"] = pydantic.Field(
        alias="outbound_payment", default=None
    )
    """
    Use [OutboundPayments](https://docs.stripe.com/docs/treasury/moving-money/financial-accounts/out-of/outbound-payments) to send funds to another party's external bank account or [FinancialAccount](https://stripe.com/docs/api#financial_accounts). To send money to an account belonging to the same user, use an [OutboundTransfer](https://stripe.com/docs/api#outbound_transfers).
    
    Simulate OutboundPayment state changes with the `/v1/test_helpers/treasury/outbound_payments` endpoints. These methods can only be called on test mode objects.
    
    Related guide: [Moving money with Treasury using OutboundPayment objects](https://docs.stripe.com/docs/treasury/moving-money/financial-accounts/out-of/outbound-payments)
    """
    outbound_transfer: typing.Optional["TreasuryOutboundTransfer"] = pydantic.Field(
        alias="outbound_transfer", default=None
    )
    """
    Use [OutboundTransfers](https://docs.stripe.com/docs/treasury/moving-money/financial-accounts/out-of/outbound-transfers) to transfer funds from a [FinancialAccount](https://stripe.com/docs/api#financial_accounts) to a PaymentMethod belonging to the same entity. To send funds to a different party, use [OutboundPayments](https://stripe.com/docs/api#outbound_payments) instead. You can send funds over ACH rails or through a domestic wire transfer to a user's own external bank account.
    
    Simulate OutboundTransfer state changes with the `/v1/test_helpers/treasury/outbound_transfers` endpoints. These methods can only be called on test mode objects.
    
    Related guide: [Moving money with Treasury using OutboundTransfer objects](https://docs.stripe.com/docs/treasury/moving-money/financial-accounts/out-of/outbound-transfers)
    """
    payout: typing.Optional["Payout"] = pydantic.Field(alias="payout", default=None)
    """
    A `Payout` object is created when you receive funds from Stripe, or when you
    initiate a payout to either a bank account or debit card of a [connected
    Stripe account](/docs/connect/bank-debit-card-payouts). You can retrieve individual payouts,
    and list all payouts. Payouts are made on [varying
    schedules](/docs/connect/manage-payout-schedule), depending on your country and
    industry.
    
    Related guide: [Receiving payouts](https://stripe.com/docs/payouts)
    """
    type_: typing_extensions.Literal[
        "credit_reversal", "other", "outbound_payment", "outbound_transfer", "payout"
    ] = pydantic.Field(
        alias="type",
    )
    """
    The type of the source flow that originated the ReceivedCredit.
    """
