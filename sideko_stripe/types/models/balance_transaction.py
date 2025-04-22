import pydantic
import typing
import typing_extensions

from .fee import Fee
from .reserve_transaction import ReserveTransaction
from .tax_deducted_at_source import TaxDeductedAtSource

if typing_extensions.TYPE_CHECKING:
    from .application_fee import ApplicationFee
    from .charge import Charge
    from .connect_collection_transfer import ConnectCollectionTransfer
    from .customer_cash_balance_transaction import CustomerCashBalanceTransaction
    from .dispute import Dispute
    from .fee_refund import FeeRefund
    from .issuing_authorization import IssuingAuthorization
    from .issuing_dispute import IssuingDispute
    from .issuing_transaction import IssuingTransaction
    from .payout import Payout
    from .refund import Refund
    from .topup import Topup
    from .transfer import Transfer
    from .transfer_reversal import TransferReversal


class BalanceTransaction(pydantic.BaseModel):
    """
    Balance transactions represent funds moving through your Stripe account.
    Stripe creates them for every type of transaction that enters or leaves your Stripe account balance.

    Related guide: [Balance transaction types](https://stripe.com/docs/reports/balance-transaction-types)
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    amount: int = pydantic.Field(
        alias="amount",
    )
    """
    Gross amount of this transaction (in cents (or local equivalent)). A positive value represents funds charged to another party, and a negative value represents funds sent to another party.
    """
    available_on: int = pydantic.Field(
        alias="available_on",
    )
    """
    The date that the transaction's net funds become available in the Stripe balance.
    """
    created: int = pydantic.Field(
        alias="created",
    )
    """
    Time at which the object was created. Measured in seconds since the Unix epoch.
    """
    currency: str = pydantic.Field(
        alias="currency",
    )
    """
    Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    """
    description: typing.Optional[str] = pydantic.Field(
        alias="description", default=None
    )
    """
    An arbitrary string attached to the object. Often useful for displaying to users.
    """
    exchange_rate: typing.Optional[float] = pydantic.Field(
        alias="exchange_rate", default=None
    )
    """
    If applicable, this transaction uses an exchange rate. If money converts from currency A to currency B, then the `amount` in currency A, multipled by the `exchange_rate`, equals the `amount` in currency B. For example, if you charge a customer 10.00 EUR, the PaymentIntent's `amount` is `1000` and `currency` is `eur`. If this converts to 12.34 USD in your Stripe account, the BalanceTransaction's `amount` is `1234`, its `currency` is `usd`, and the `exchange_rate` is `1.234`.
    """
    fee: int = pydantic.Field(
        alias="fee",
    )
    """
    Fees (in cents (or local equivalent)) paid for this transaction. Represented as a positive integer when assessed.
    """
    fee_details: typing.List[Fee] = pydantic.Field(
        alias="fee_details",
    )
    """
    Detailed breakdown of fees (in cents (or local equivalent)) paid for this transaction.
    """
    id: str = pydantic.Field(
        alias="id",
    )
    """
    Unique identifier for the object.
    """
    net: int = pydantic.Field(
        alias="net",
    )
    """
    Net impact to a Stripe balance (in cents (or local equivalent)). A positive value represents incrementing a Stripe balance, and a negative value decrementing a Stripe balance. You can calculate the net impact of a transaction on a balance by `amount` - `fee`
    """
    object: typing_extensions.Literal["balance_transaction"] = pydantic.Field(
        alias="object",
    )
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    reporting_category: str = pydantic.Field(
        alias="reporting_category",
    )
    """
    Learn more about how [reporting categories](https://stripe.com/docs/reports/reporting-categories) can help you understand balance transactions from an accounting perspective.
    """
    source: typing.Optional[
        typing.Union[
            str,
            "ApplicationFee",
            "Charge",
            "ConnectCollectionTransfer",
            "CustomerCashBalanceTransaction",
            "Dispute",
            "FeeRefund",
            "IssuingAuthorization",
            "IssuingDispute",
            "IssuingTransaction",
            "Payout",
            "Refund",
            ReserveTransaction,
            TaxDeductedAtSource,
            "Topup",
            "Transfer",
            "TransferReversal",
        ]
    ] = pydantic.Field(alias="source", default=None)
    """
    This transaction relates to the Stripe object.
    """
    status: str = pydantic.Field(
        alias="status",
    )
    """
    The transaction's net funds status in the Stripe balance, which are either `available` or `pending`.
    """
    type_: typing_extensions.Literal[
        "adjustment",
        "advance",
        "advance_funding",
        "anticipation_repayment",
        "application_fee",
        "application_fee_refund",
        "charge",
        "climate_order_purchase",
        "climate_order_refund",
        "connect_collection_transfer",
        "contribution",
        "issuing_authorization_hold",
        "issuing_authorization_release",
        "issuing_dispute",
        "issuing_transaction",
        "obligation_outbound",
        "obligation_reversal_inbound",
        "payment",
        "payment_failure_refund",
        "payment_network_reserve_hold",
        "payment_network_reserve_release",
        "payment_refund",
        "payment_reversal",
        "payment_unreconciled",
        "payout",
        "payout_cancel",
        "payout_failure",
        "payout_minimum_balance_hold",
        "payout_minimum_balance_release",
        "refund",
        "refund_failure",
        "reserve_transaction",
        "reserved_funds",
        "stripe_balance_payment_debit",
        "stripe_balance_payment_debit_reversal",
        "stripe_fee",
        "stripe_fx_fee",
        "tax_fee",
        "topup",
        "topup_reversal",
        "transfer",
        "transfer_cancel",
        "transfer_failure",
        "transfer_refund",
    ] = pydantic.Field(
        alias="type",
    )
    """
    Transaction type: `adjustment`, `advance`, `advance_funding`, `anticipation_repayment`, `application_fee`, `application_fee_refund`, `charge`, `climate_order_purchase`, `climate_order_refund`, `connect_collection_transfer`, `contribution`, `issuing_authorization_hold`, `issuing_authorization_release`, `issuing_dispute`, `issuing_transaction`, `obligation_outbound`, `obligation_reversal_inbound`, `payment`, `payment_failure_refund`, `payment_network_reserve_hold`, `payment_network_reserve_release`, `payment_refund`, `payment_reversal`, `payment_unreconciled`, `payout`, `payout_cancel`, `payout_failure`, `payout_minimum_balance_hold`, `payout_minimum_balance_release`, `refund`, `refund_failure`, `reserve_transaction`, `reserved_funds`, `stripe_fee`, `stripe_fx_fee`, `stripe_balance_payment_debit`, `stripe_balance_payment_debit_reversal`, `tax_fee`, `topup`, `topup_reversal`, `transfer`, `transfer_cancel`, `transfer_failure`, or `transfer_refund`. Learn more about [balance transaction types and what they represent](https://stripe.com/docs/reports/balance-transaction-types). To classify transactions for accounting purposes, consider `reporting_category` instead.
    """
