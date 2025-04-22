import pydantic
import typing
import typing_extensions

from .issuing_authorization_merchant_data import IssuingAuthorizationMerchantData
from .issuing_transaction_amount_details import IssuingTransactionAmountDetails
from .issuing_transaction_metadata import IssuingTransactionMetadata
from .issuing_transaction_network_data import IssuingTransactionNetworkData
from .issuing_transaction_purchase_details import IssuingTransactionPurchaseDetails
from .issuing_transaction_treasury import IssuingTransactionTreasury

if typing_extensions.TYPE_CHECKING:
    from .balance_transaction import BalanceTransaction
    from .issuing_authorization import IssuingAuthorization
    from .issuing_card import IssuingCard
    from .issuing_cardholder import IssuingCardholder
    from .issuing_dispute import IssuingDispute
    from .issuing_token import IssuingToken


class IssuingTransaction(pydantic.BaseModel):
    """
    Any use of an [issued card](https://stripe.com/docs/issuing) that results in funds entering or leaving
    your Stripe account, such as a completed purchase or refund, is represented by an Issuing
    `Transaction` object.

    Related guide: [Issued card transactions](https://stripe.com/docs/issuing/purchases/transactions)
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    amount: int = pydantic.Field(
        alias="amount",
    )
    """
    The transaction amount, which will be reflected in your balance. This amount is in your currency and in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal).
    """
    amount_details: typing.Optional[IssuingTransactionAmountDetails] = pydantic.Field(
        alias="amount_details", default=None
    )
    authorization: typing.Optional[typing.Union[str, "IssuingAuthorization"]] = (
        pydantic.Field(alias="authorization", default=None)
    )
    """
    The `Authorization` object that led to this transaction.
    """
    balance_transaction: typing.Optional[typing.Union[str, "BalanceTransaction"]] = (
        pydantic.Field(alias="balance_transaction", default=None)
    )
    """
    ID of the [balance transaction](https://stripe.com/docs/api/balance_transactions) associated with this transaction.
    """
    card: typing.Union[str, "IssuingCard"] = pydantic.Field(
        alias="card",
    )
    """
    The card used to make this transaction.
    """
    cardholder: typing.Optional[typing.Union[str, "IssuingCardholder"]] = (
        pydantic.Field(alias="cardholder", default=None)
    )
    """
    The cardholder to whom this transaction belongs.
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
    dispute: typing.Optional[typing.Union[str, "IssuingDispute"]] = pydantic.Field(
        alias="dispute", default=None
    )
    """
    If you've disputed the transaction, the ID of the dispute.
    """
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
    merchant_amount: int = pydantic.Field(
        alias="merchant_amount",
    )
    """
    The amount that the merchant will receive, denominated in `merchant_currency` and in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal). It will be different from `amount` if the merchant is taking payment in a different currency.
    """
    merchant_currency: str = pydantic.Field(
        alias="merchant_currency",
    )
    """
    The currency with which the merchant is taking payment.
    """
    merchant_data: IssuingAuthorizationMerchantData = pydantic.Field(
        alias="merchant_data",
    )
    metadata: IssuingTransactionMetadata = pydantic.Field(
        alias="metadata",
    )
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    network_data: typing.Optional[IssuingTransactionNetworkData] = pydantic.Field(
        alias="network_data", default=None
    )
    object: typing_extensions.Literal["issuing.transaction"] = pydantic.Field(
        alias="object",
    )
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    purchase_details: typing.Optional[IssuingTransactionPurchaseDetails] = (
        pydantic.Field(alias="purchase_details", default=None)
    )
    token: typing.Optional[typing.Union[str, "IssuingToken"]] = pydantic.Field(
        alias="token", default=None
    )
    """
    [Token](https://stripe.com/docs/api/issuing/tokens/object) object used for this transaction. If a network token was not used for this transaction, this field will be null.
    """
    treasury: typing.Optional[IssuingTransactionTreasury] = pydantic.Field(
        alias="treasury", default=None
    )
    type_: typing_extensions.Literal["capture", "refund"] = pydantic.Field(
        alias="type",
    )
    """
    The nature of the transaction.
    """
    wallet: typing.Optional[
        typing_extensions.Literal["apple_pay", "google_pay", "samsung_pay"]
    ] = pydantic.Field(alias="wallet", default=None)
    """
    The digital wallet used for this transaction. One of `apple_pay`, `google_pay`, or `samsung_pay`.
    """
