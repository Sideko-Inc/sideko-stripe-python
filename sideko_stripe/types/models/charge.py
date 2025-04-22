import pydantic
import typing
import typing_extensions

from .application import Application
from .billing_details import BillingDetails
from .charge_fraud_details import ChargeFraudDetails
from .charge_metadata import ChargeMetadata
from .charge_outcome import ChargeOutcome
from .deleted_customer import DeletedCustomer
from .payment_flows_payment_intent_presentment_details import (
    PaymentFlowsPaymentIntentPresentmentDetails,
)
from .radar_radar_options import RadarRadarOptions
from .shipping import Shipping

if typing_extensions.TYPE_CHECKING:
    from .account import Account
    from .application_fee import ApplicationFee
    from .balance_transaction import BalanceTransaction
    from .charge_refunds import ChargeRefunds
    from .charge_transfer_data import ChargeTransferData
    from .customer import Customer
    from .payment_intent import PaymentIntent
    from .payment_method_details import PaymentMethodDetails
    from .review import Review
    from .transfer import Transfer


class Charge(pydantic.BaseModel):
    """
    The `Charge` object represents a single attempt to move money into your Stripe account.
    PaymentIntent confirmation is the most common way to create Charges, but transferring
    money to a different Stripe account through Connect also creates Charges.
    Some legacy payment flows create Charges directly, which is not recommended for new integrations.
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    amount: int = pydantic.Field(
        alias="amount",
    )
    """
    Amount intended to be collected by this payment. A positive integer representing how much to charge in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal) (e.g., 100 cents to charge $1.00 or 100 to charge ¥100, a zero-decimal currency). The minimum amount is $0.50 US or [equivalent in charge currency](https://stripe.com/docs/currencies#minimum-and-maximum-charge-amounts). The amount value supports up to eight digits (e.g., a value of 99999999 for a USD charge of $999,999.99).
    """
    amount_captured: int = pydantic.Field(
        alias="amount_captured",
    )
    """
    Amount in cents (or local equivalent) captured (can be less than the amount attribute on the charge if a partial capture was made).
    """
    amount_refunded: int = pydantic.Field(
        alias="amount_refunded",
    )
    """
    Amount in cents (or local equivalent) refunded (can be less than the amount attribute on the charge if a partial refund was issued).
    """
    application: typing.Optional[typing.Union[str, Application]] = pydantic.Field(
        alias="application", default=None
    )
    """
    ID of the Connect application that created the charge.
    """
    application_fee: typing.Optional[typing.Union[str, "ApplicationFee"]] = (
        pydantic.Field(alias="application_fee", default=None)
    )
    """
    The application fee (if any) for the charge. [See the Connect documentation](https://stripe.com/docs/connect/direct-charges#collect-fees) for details.
    """
    application_fee_amount: typing.Optional[int] = pydantic.Field(
        alias="application_fee_amount", default=None
    )
    """
    The amount of the application fee (if any) requested for the charge. [See the Connect documentation](https://stripe.com/docs/connect/direct-charges#collect-fees) for details.
    """
    balance_transaction: typing.Optional[typing.Union[str, "BalanceTransaction"]] = (
        pydantic.Field(alias="balance_transaction", default=None)
    )
    """
    ID of the balance transaction that describes the impact of this charge on your account balance (not including refunds or disputes).
    """
    billing_details: BillingDetails = pydantic.Field(
        alias="billing_details",
    )
    calculated_statement_descriptor: typing.Optional[str] = pydantic.Field(
        alias="calculated_statement_descriptor", default=None
    )
    """
    The full statement descriptor that is passed to card networks, and that is displayed on your customers' credit card and bank statements. Allows you to see what the statement descriptor looks like after the static and dynamic portions are combined. This value only exists for card payments.
    """
    captured: bool = pydantic.Field(
        alias="captured",
    )
    """
    If the charge was created without capturing, this Boolean represents whether it is still uncaptured or has since been captured.
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
    customer: typing.Optional[typing.Union[str, "Customer", DeletedCustomer]] = (
        pydantic.Field(alias="customer", default=None)
    )
    """
    ID of the customer this charge is for if one exists.
    """
    description: typing.Optional[str] = pydantic.Field(
        alias="description", default=None
    )
    """
    An arbitrary string attached to the object. Often useful for displaying to users.
    """
    disputed: bool = pydantic.Field(
        alias="disputed",
    )
    """
    Whether the charge has been disputed.
    """
    failure_balance_transaction: typing.Optional[
        typing.Union[str, "BalanceTransaction"]
    ] = pydantic.Field(alias="failure_balance_transaction", default=None)
    """
    ID of the balance transaction that describes the reversal of the balance on your account due to payment failure.
    """
    failure_code: typing.Optional[str] = pydantic.Field(
        alias="failure_code", default=None
    )
    """
    Error code explaining reason for charge failure if available (see [the errors section](https://stripe.com/docs/error-codes) for a list of codes).
    """
    failure_message: typing.Optional[str] = pydantic.Field(
        alias="failure_message", default=None
    )
    """
    Message to user further explaining reason for charge failure if available.
    """
    fraud_details: typing.Optional[ChargeFraudDetails] = pydantic.Field(
        alias="fraud_details", default=None
    )
    id: str = pydantic.Field(
        alias="id",
    )
    """
    Unique identifier for the object.
    """
    livemode: bool = pydantic.Field(
        alias="livemode",
    )
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    metadata: ChargeMetadata = pydantic.Field(
        alias="metadata",
    )
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    object: typing_extensions.Literal["charge"] = pydantic.Field(
        alias="object",
    )
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    on_behalf_of: typing.Optional[typing.Union[str, "Account"]] = pydantic.Field(
        alias="on_behalf_of", default=None
    )
    """
    The account (if any) the charge was made on behalf of without triggering an automatic transfer. See the [Connect documentation](https://stripe.com/docs/connect/separate-charges-and-transfers) for details.
    """
    outcome: typing.Optional[ChargeOutcome] = pydantic.Field(
        alias="outcome", default=None
    )
    paid: bool = pydantic.Field(
        alias="paid",
    )
    """
    `true` if the charge succeeded, or was successfully authorized for later capture.
    """
    payment_intent: typing.Optional[typing.Union[str, "PaymentIntent"]] = (
        pydantic.Field(alias="payment_intent", default=None)
    )
    """
    ID of the PaymentIntent associated with this charge, if one exists.
    """
    payment_method: typing.Optional[str] = pydantic.Field(
        alias="payment_method", default=None
    )
    """
    ID of the payment method used in this charge.
    """
    payment_method_details: typing.Optional["PaymentMethodDetails"] = pydantic.Field(
        alias="payment_method_details", default=None
    )
    presentment_details: typing.Optional[
        PaymentFlowsPaymentIntentPresentmentDetails
    ] = pydantic.Field(alias="presentment_details", default=None)
    radar_options: typing.Optional[RadarRadarOptions] = pydantic.Field(
        alias="radar_options", default=None
    )
    """
    Options to configure Radar. See [Radar Session](https://stripe.com/docs/radar/radar-session) for more information.
    """
    receipt_email: typing.Optional[str] = pydantic.Field(
        alias="receipt_email", default=None
    )
    """
    This is the email address that the receipt for this charge was sent to.
    """
    receipt_number: typing.Optional[str] = pydantic.Field(
        alias="receipt_number", default=None
    )
    """
    This is the transaction number that appears on email receipts sent for this charge. This attribute will be `null` until a receipt has been sent.
    """
    receipt_url: typing.Optional[str] = pydantic.Field(
        alias="receipt_url", default=None
    )
    """
    This is the URL to view the receipt for this charge. The receipt is kept up-to-date to the latest state of the charge, including any refunds. If the charge is for an Invoice, the receipt will be stylized as an Invoice receipt.
    """
    refunded: bool = pydantic.Field(
        alias="refunded",
    )
    """
    Whether the charge has been fully refunded. If the charge is only partially refunded, this attribute will still be false.
    """
    refunds: typing.Optional["ChargeRefunds"] = pydantic.Field(
        alias="refunds", default=None
    )
    """
    A list of refunds that have been applied to the charge.
    """
    review: typing.Optional[typing.Union[str, "Review"]] = pydantic.Field(
        alias="review", default=None
    )
    """
    ID of the review associated with this charge if one exists.
    """
    shipping: typing.Optional[Shipping] = pydantic.Field(alias="shipping", default=None)
    source_transfer: typing.Optional[typing.Union[str, "Transfer"]] = pydantic.Field(
        alias="source_transfer", default=None
    )
    """
    The transfer ID which created this charge. Only present if the charge came from another Stripe account. [See the Connect documentation](https://docs.stripe.com/connect/destination-charges) for details.
    """
    statement_descriptor: typing.Optional[str] = pydantic.Field(
        alias="statement_descriptor", default=None
    )
    """
    For a non-card charge, text that appears on the customer's statement as the statement descriptor. This value overrides the account's default statement descriptor. For information about requirements, including the 22-character limit, see [the Statement Descriptor docs](https://docs.stripe.com/get-started/account/statement-descriptors).
    
    For a card charge, this value is ignored unless you don't specify a `statement_descriptor_suffix`, in which case this value is used as the suffix.
    """
    statement_descriptor_suffix: typing.Optional[str] = pydantic.Field(
        alias="statement_descriptor_suffix", default=None
    )
    """
    Provides information about a card charge. Concatenated to the account's [statement descriptor prefix](https://docs.stripe.com/get-started/account/statement-descriptors#static) to form the complete statement descriptor that appears on the customer's statement. If the account has no prefix value, the suffix is concatenated to the account's statement descriptor.
    """
    status: typing_extensions.Literal["failed", "pending", "succeeded"] = (
        pydantic.Field(
            alias="status",
        )
    )
    """
    The status of the payment is either `succeeded`, `pending`, or `failed`.
    """
    transfer: typing.Optional[typing.Union[str, "Transfer"]] = pydantic.Field(
        alias="transfer", default=None
    )
    """
    ID of the transfer to the `destination` account (only applicable if the charge was created using the `destination` parameter).
    """
    transfer_data: typing.Optional["ChargeTransferData"] = pydantic.Field(
        alias="transfer_data", default=None
    )
    transfer_group: typing.Optional[str] = pydantic.Field(
        alias="transfer_group", default=None
    )
    """
    A string that identifies this transaction as part of a group. See the [Connect documentation](https://stripe.com/docs/connect/separate-charges-and-transfers#transfer-options) for details.
    """
