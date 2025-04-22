import pydantic
import typing
import typing_extensions


if typing_extensions.TYPE_CHECKING:
    from .issuing_authorization import IssuingAuthorization
    from .treasury_credit_reversal import TreasuryCreditReversal
    from .treasury_debit_reversal import TreasuryDebitReversal
    from .treasury_inbound_transfer import TreasuryInboundTransfer
    from .treasury_outbound_payment import TreasuryOutboundPayment
    from .treasury_outbound_transfer import TreasuryOutboundTransfer
    from .treasury_received_credit import TreasuryReceivedCredit
    from .treasury_received_debit import TreasuryReceivedDebit


class TreasuryTransactionsResourceFlowDetails(pydantic.BaseModel):
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
    debit_reversal: typing.Optional["TreasuryDebitReversal"] = pydantic.Field(
        alias="debit_reversal", default=None
    )
    """
    You can reverse some [ReceivedDebits](https://stripe.com/docs/api#received_debits) depending on their network and source flow. Reversing a ReceivedDebit leads to the creation of a new object known as a DebitReversal.
    """
    inbound_transfer: typing.Optional["TreasuryInboundTransfer"] = pydantic.Field(
        alias="inbound_transfer", default=None
    )
    """
    Use [InboundTransfers](https://docs.stripe.com/docs/treasury/moving-money/financial-accounts/into/inbound-transfers) to add funds to your [FinancialAccount](https://stripe.com/docs/api#financial_accounts) via a PaymentMethod that is owned by you. The funds will be transferred via an ACH debit.
    
    Related guide: [Moving money with Treasury using InboundTransfer objects](https://docs.stripe.com/docs/treasury/moving-money/financial-accounts/into/inbound-transfers)
    """
    issuing_authorization: typing.Optional["IssuingAuthorization"] = pydantic.Field(
        alias="issuing_authorization", default=None
    )
    """
    When an [issued card](https://stripe.com/docs/issuing) is used to make a purchase, an Issuing `Authorization`
    object is created. [Authorizations](https://stripe.com/docs/issuing/purchases/authorizations) must be approved for the
    purchase to be completed successfully.
    
    Related guide: [Issued card authorizations](https://stripe.com/docs/issuing/purchases/authorizations)
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
    received_credit: typing.Optional["TreasuryReceivedCredit"] = pydantic.Field(
        alias="received_credit", default=None
    )
    """
    ReceivedCredits represent funds sent to a [FinancialAccount](https://stripe.com/docs/api#financial_accounts) (for example, via ACH or wire). These money movements are not initiated from the FinancialAccount.
    """
    received_debit: typing.Optional["TreasuryReceivedDebit"] = pydantic.Field(
        alias="received_debit", default=None
    )
    """
    ReceivedDebits represent funds pulled from a [FinancialAccount](https://stripe.com/docs/api#financial_accounts). These are not initiated from the FinancialAccount.
    """
    type_: typing_extensions.Literal[
        "credit_reversal",
        "debit_reversal",
        "inbound_transfer",
        "issuing_authorization",
        "other",
        "outbound_payment",
        "outbound_transfer",
        "received_credit",
        "received_debit",
    ] = pydantic.Field(
        alias="type",
    )
    """
    Type of the flow that created the Transaction. Set to the same value as `flow_type`.
    """
