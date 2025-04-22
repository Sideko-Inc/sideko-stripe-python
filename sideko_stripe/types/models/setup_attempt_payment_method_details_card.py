import pydantic
import typing

from .setup_attempt_payment_method_details_card_checks import (
    SetupAttemptPaymentMethodDetailsCardChecks,
)
from .setup_attempt_payment_method_details_card_wallet import (
    SetupAttemptPaymentMethodDetailsCardWallet,
)
from .three_d_secure_details import ThreeDSecureDetails


class SetupAttemptPaymentMethodDetailsCard(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    brand: typing.Optional[str] = pydantic.Field(alias="brand", default=None)
    """
    Card brand. Can be `amex`, `diners`, `discover`, `eftpos_au`, `jcb`, `link`, `mastercard`, `unionpay`, `visa`, or `unknown`.
    """
    checks: typing.Optional[SetupAttemptPaymentMethodDetailsCardChecks] = (
        pydantic.Field(alias="checks", default=None)
    )
    country: typing.Optional[str] = pydantic.Field(alias="country", default=None)
    """
    Two-letter ISO code representing the country of the card. You could use this attribute to get a sense of the international breakdown of cards you've collected.
    """
    exp_month: typing.Optional[int] = pydantic.Field(alias="exp_month", default=None)
    """
    Two-digit number representing the card's expiration month.
    """
    exp_year: typing.Optional[int] = pydantic.Field(alias="exp_year", default=None)
    """
    Four-digit number representing the card's expiration year.
    """
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
    last4: typing.Optional[str] = pydantic.Field(alias="last4", default=None)
    """
    The last four digits of the card.
    """
    network: typing.Optional[str] = pydantic.Field(alias="network", default=None)
    """
    Identifies which network this charge was processed on. Can be `amex`, `cartes_bancaires`, `diners`, `discover`, `eftpos_au`, `interac`, `jcb`, `link`, `mastercard`, `unionpay`, `visa`, or `unknown`.
    """
    three_d_secure: typing.Optional[ThreeDSecureDetails] = pydantic.Field(
        alias="three_d_secure", default=None
    )
    wallet: typing.Optional[SetupAttemptPaymentMethodDetailsCardWallet] = (
        pydantic.Field(alias="wallet", default=None)
    )
