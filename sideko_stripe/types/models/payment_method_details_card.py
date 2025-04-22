import pydantic
import typing
import typing_extensions

from .payment_flows_private_payment_methods_card_details_api_resource_enterprise_features_extended_authorization_extended_authorization import (
    PaymentFlowsPrivatePaymentMethodsCardDetailsApiResourceEnterpriseFeaturesExtendedAuthorizationExtendedAuthorization,
)
from .payment_flows_private_payment_methods_card_details_api_resource_enterprise_features_incremental_authorization_incremental_authorization import (
    PaymentFlowsPrivatePaymentMethodsCardDetailsApiResourceEnterpriseFeaturesIncrementalAuthorizationIncrementalAuthorization,
)
from .payment_flows_private_payment_methods_card_details_api_resource_enterprise_features_overcapture_overcapture import (
    PaymentFlowsPrivatePaymentMethodsCardDetailsApiResourceEnterpriseFeaturesOvercaptureOvercapture,
)
from .payment_flows_private_payment_methods_card_details_api_resource_multicapture import (
    PaymentFlowsPrivatePaymentMethodsCardDetailsApiResourceMulticapture,
)
from .payment_method_details_card_checks import PaymentMethodDetailsCardChecks
from .payment_method_details_card_installments import (
    PaymentMethodDetailsCardInstallments,
)
from .payment_method_details_card_network_token import (
    PaymentMethodDetailsCardNetworkToken,
)
from .payment_method_details_card_wallet import PaymentMethodDetailsCardWallet
from .three_d_secure_details_charge import ThreeDSecureDetailsCharge


class PaymentMethodDetailsCard(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    amount_authorized: typing.Optional[int] = pydantic.Field(
        alias="amount_authorized", default=None
    )
    """
    The authorized amount.
    """
    authorization_code: typing.Optional[str] = pydantic.Field(
        alias="authorization_code", default=None
    )
    """
    Authorization code on the charge.
    """
    brand: typing.Optional[str] = pydantic.Field(alias="brand", default=None)
    """
    Card brand. Can be `amex`, `diners`, `discover`, `eftpos_au`, `jcb`, `link`, `mastercard`, `unionpay`, `visa`, or `unknown`.
    """
    capture_before: typing.Optional[int] = pydantic.Field(
        alias="capture_before", default=None
    )
    """
    When using manual capture, a future timestamp at which the charge will be automatically refunded if uncaptured.
    """
    checks: typing.Optional[PaymentMethodDetailsCardChecks] = pydantic.Field(
        alias="checks", default=None
    )
    country: typing.Optional[str] = pydantic.Field(alias="country", default=None)
    """
    Two-letter ISO code representing the country of the card. You could use this attribute to get a sense of the international breakdown of cards you've collected.
    """
    exp_month: int = pydantic.Field(
        alias="exp_month",
    )
    """
    Two-digit number representing the card's expiration month.
    """
    exp_year: int = pydantic.Field(
        alias="exp_year",
    )
    """
    Four-digit number representing the card's expiration year.
    """
    extended_authorization: typing.Optional[
        PaymentFlowsPrivatePaymentMethodsCardDetailsApiResourceEnterpriseFeaturesExtendedAuthorizationExtendedAuthorization
    ] = pydantic.Field(alias="extended_authorization", default=None)
    fingerprint: typing.Optional[str] = pydantic.Field(
        alias="fingerprint", default=None
    )
    """
    Uniquely identifies this particular card number. You can use this attribute to check whether two customers who’ve signed up with you are using the same card number, for example. For payment methods that tokenize card information (Apple Pay, Google Pay), the tokenized number might be provided instead of the underlying card number.
    
    *As of May 1, 2021, card fingerprint in India for Connect changed to allow two fingerprints for the same card---one for India and one for the rest of the world.*
    """
    funding: typing.Optional[str] = pydantic.Field(alias="funding", default=None)
    """
    Card funding type. Can be `credit`, `debit`, `prepaid`, or `unknown`.
    """
    incremental_authorization: typing.Optional[
        PaymentFlowsPrivatePaymentMethodsCardDetailsApiResourceEnterpriseFeaturesIncrementalAuthorizationIncrementalAuthorization
    ] = pydantic.Field(alias="incremental_authorization", default=None)
    installments: typing.Optional[PaymentMethodDetailsCardInstallments] = (
        pydantic.Field(alias="installments", default=None)
    )
    last4: typing.Optional[str] = pydantic.Field(alias="last4", default=None)
    """
    The last four digits of the card.
    """
    mandate: typing.Optional[str] = pydantic.Field(alias="mandate", default=None)
    """
    ID of the mandate used to make this payment or created by it.
    """
    multicapture: typing.Optional[
        PaymentFlowsPrivatePaymentMethodsCardDetailsApiResourceMulticapture
    ] = pydantic.Field(alias="multicapture", default=None)
    network: typing.Optional[str] = pydantic.Field(alias="network", default=None)
    """
    Identifies which network this charge was processed on. Can be `amex`, `cartes_bancaires`, `diners`, `discover`, `eftpos_au`, `interac`, `jcb`, `link`, `mastercard`, `unionpay`, `visa`, or `unknown`.
    """
    network_token: typing.Optional[PaymentMethodDetailsCardNetworkToken] = (
        pydantic.Field(alias="network_token", default=None)
    )
    network_transaction_id: typing.Optional[str] = pydantic.Field(
        alias="network_transaction_id", default=None
    )
    """
    This is used by the financial networks to identify a transaction. Visa calls this the Transaction ID, Mastercard calls this the Trace ID, and American Express calls this the Acquirer Reference Data. This value will be present if it is returned by the financial network in the authorization response, and null otherwise.
    """
    overcapture: typing.Optional[
        PaymentFlowsPrivatePaymentMethodsCardDetailsApiResourceEnterpriseFeaturesOvercaptureOvercapture
    ] = pydantic.Field(alias="overcapture", default=None)
    regulated_status: typing.Optional[
        typing_extensions.Literal["regulated", "unregulated"]
    ] = pydantic.Field(alias="regulated_status", default=None)
    """
    Status of a card based on the card issuer.
    """
    three_d_secure: typing.Optional[ThreeDSecureDetailsCharge] = pydantic.Field(
        alias="three_d_secure", default=None
    )
    wallet: typing.Optional[PaymentMethodDetailsCardWallet] = pydantic.Field(
        alias="wallet", default=None
    )
