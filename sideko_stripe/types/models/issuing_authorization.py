import pydantic
import typing
import typing_extensions

from .issuing_authorization_amount_details import IssuingAuthorizationAmountDetails
from .issuing_authorization_fleet_data import IssuingAuthorizationFleetData
from .issuing_authorization_fraud_challenge import IssuingAuthorizationFraudChallenge
from .issuing_authorization_fuel_data import IssuingAuthorizationFuelData
from .issuing_authorization_merchant_data import IssuingAuthorizationMerchantData
from .issuing_authorization_metadata import IssuingAuthorizationMetadata
from .issuing_authorization_network_data import IssuingAuthorizationNetworkData
from .issuing_authorization_pending_request import IssuingAuthorizationPendingRequest
from .issuing_authorization_request import IssuingAuthorizationRequest
from .issuing_authorization_treasury import IssuingAuthorizationTreasury
from .issuing_authorization_verification_data import (
    IssuingAuthorizationVerificationData,
)

if typing_extensions.TYPE_CHECKING:
    from .balance_transaction import BalanceTransaction
    from .issuing_card import IssuingCard
    from .issuing_cardholder import IssuingCardholder
    from .issuing_token import IssuingToken
    from .issuing_transaction import IssuingTransaction


class IssuingAuthorization(pydantic.BaseModel):
    """
    When an [issued card](https://stripe.com/docs/issuing) is used to make a purchase, an Issuing `Authorization`
    object is created. [Authorizations](https://stripe.com/docs/issuing/purchases/authorizations) must be approved for the
    purchase to be completed successfully.

    Related guide: [Issued card authorizations](https://stripe.com/docs/issuing/purchases/authorizations)
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    amount: int = pydantic.Field(
        alias="amount",
    )
    """
    The total amount that was authorized or rejected. This amount is in `currency` and in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal). `amount` should be the same as `merchant_amount`, unless `currency` and `merchant_currency` are different.
    """
    amount_details: typing.Optional[IssuingAuthorizationAmountDetails] = pydantic.Field(
        alias="amount_details", default=None
    )
    approved: bool = pydantic.Field(
        alias="approved",
    )
    """
    Whether the authorization has been approved.
    """
    authorization_method: typing_extensions.Literal[
        "chip", "contactless", "keyed_in", "online", "swipe"
    ] = pydantic.Field(
        alias="authorization_method",
    )
    """
    How the card details were provided.
    """
    balance_transactions: typing.List["BalanceTransaction"] = pydantic.Field(
        alias="balance_transactions",
    )
    """
    List of balance transactions associated with this authorization.
    """
    card: "IssuingCard" = pydantic.Field(
        alias="card",
    )
    """
    You can [create physical or virtual cards](https://stripe.com/docs/issuing) that are issued to cardholders.
    """
    cardholder: typing.Optional[typing.Union[str, "IssuingCardholder"]] = (
        pydantic.Field(alias="cardholder", default=None)
    )
    """
    The cardholder to whom this authorization belongs.
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
    The currency of the cardholder. This currency can be different from the currency presented at authorization and the `merchant_currency` field on this authorization. Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    """
    fleet: typing.Optional[IssuingAuthorizationFleetData] = pydantic.Field(
        alias="fleet", default=None
    )
    fraud_challenges: typing.Optional[
        typing.List[IssuingAuthorizationFraudChallenge]
    ] = pydantic.Field(alias="fraud_challenges", default=None)
    """
    Fraud challenges sent to the cardholder, if this authorization was declined for fraud risk reasons.
    """
    fuel: typing.Optional[IssuingAuthorizationFuelData] = pydantic.Field(
        alias="fuel", default=None
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
    merchant_amount: int = pydantic.Field(
        alias="merchant_amount",
    )
    """
    The total amount that was authorized or rejected. This amount is in the `merchant_currency` and in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal). `merchant_amount` should be the same as `amount`, unless `merchant_currency` and `currency` are different.
    """
    merchant_currency: str = pydantic.Field(
        alias="merchant_currency",
    )
    """
    The local currency that was presented to the cardholder for the authorization. This currency can be different from the cardholder currency and the `currency` field on this authorization. Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    """
    merchant_data: IssuingAuthorizationMerchantData = pydantic.Field(
        alias="merchant_data",
    )
    metadata: IssuingAuthorizationMetadata = pydantic.Field(
        alias="metadata",
    )
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    network_data: typing.Optional[IssuingAuthorizationNetworkData] = pydantic.Field(
        alias="network_data", default=None
    )
    object: typing_extensions.Literal["issuing.authorization"] = pydantic.Field(
        alias="object",
    )
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    pending_request: typing.Optional[IssuingAuthorizationPendingRequest] = (
        pydantic.Field(alias="pending_request", default=None)
    )
    request_history: typing.List[IssuingAuthorizationRequest] = pydantic.Field(
        alias="request_history",
    )
    """
    History of every time a `pending_request` authorization was approved/declined, either by you directly or by Stripe (e.g. based on your spending_controls). If the merchant changes the authorization by performing an incremental authorization, you can look at this field to see the previous requests for the authorization. This field can be helpful in determining why a given authorization was approved/declined.
    """
    status: typing_extensions.Literal["closed", "expired", "pending", "reversed"] = (
        pydantic.Field(
            alias="status",
        )
    )
    """
    The current status of the authorization in its lifecycle.
    """
    token: typing.Optional[typing.Union[str, "IssuingToken"]] = pydantic.Field(
        alias="token", default=None
    )
    """
    [Token](https://stripe.com/docs/api/issuing/tokens/object) object used for this authorization. If a network token was not used for this authorization, this field will be null.
    """
    transactions: typing.List["IssuingTransaction"] = pydantic.Field(
        alias="transactions",
    )
    """
    List of [transactions](https://stripe.com/docs/api/issuing/transactions) associated with this authorization.
    """
    treasury: typing.Optional[IssuingAuthorizationTreasury] = pydantic.Field(
        alias="treasury", default=None
    )
    verification_data: IssuingAuthorizationVerificationData = pydantic.Field(
        alias="verification_data",
    )
    verified_by_fraud_challenge: typing.Optional[bool] = pydantic.Field(
        alias="verified_by_fraud_challenge", default=None
    )
    """
    Whether the authorization bypassed fraud risk checks because the cardholder has previously completed a fraud challenge on a similar high-risk authorization from the same merchant.
    """
    wallet: typing.Optional[str] = pydantic.Field(alias="wallet", default=None)
    """
    The digital wallet used for this transaction. One of `apple_pay`, `google_pay`, or `samsung_pay`. Will populate as `null` when no digital wallet was utilized.
    """
