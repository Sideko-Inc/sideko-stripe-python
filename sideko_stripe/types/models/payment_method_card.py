import pydantic
import typing
import typing_extensions

from .networks import Networks
from .payment_method_card_checks import PaymentMethodCardChecks
from .payment_method_card_wallet import PaymentMethodCardWallet
from .three_d_secure_usage import ThreeDSecureUsage

if typing_extensions.TYPE_CHECKING:
    from .payment_method_card_generated_card import PaymentMethodCardGeneratedCard


class PaymentMethodCard(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    brand: str = pydantic.Field(
        alias="brand",
    )
    """
    Card brand. Can be `amex`, `diners`, `discover`, `eftpos_au`, `jcb`, `link`, `mastercard`, `unionpay`, `visa`, or `unknown`.
    """
    checks: typing.Optional[PaymentMethodCardChecks] = pydantic.Field(
        alias="checks", default=None
    )
    country: typing.Optional[str] = pydantic.Field(alias="country", default=None)
    """
    Two-letter ISO code representing the country of the card. You could use this attribute to get a sense of the international breakdown of cards you've collected.
    """
    display_brand: typing.Optional[str] = pydantic.Field(
        alias="display_brand", default=None
    )
    """
    The brand to use when displaying the card, this accounts for customer's brand choice on dual-branded cards. Can be `american_express`, `cartes_bancaires`, `diners_club`, `discover`, `eftpos_australia`, `interac`, `jcb`, `mastercard`, `union_pay`, `visa`, or `other` and may contain more values in the future.
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
    fingerprint: typing.Optional[str] = pydantic.Field(
        alias="fingerprint", default=None
    )
    """
    Uniquely identifies this particular card number. You can use this attribute to check whether two customers who’ve signed up with you are using the same card number, for example. For payment methods that tokenize card information (Apple Pay, Google Pay), the tokenized number might be provided instead of the underlying card number.
    
    *As of May 1, 2021, card fingerprint in India for Connect changed to allow two fingerprints for the same card---one for India and one for the rest of the world.*
    """
    funding: str = pydantic.Field(
        alias="funding",
    )
    """
    Card funding type. Can be `credit`, `debit`, `prepaid`, or `unknown`.
    """
    generated_from: typing.Optional["PaymentMethodCardGeneratedCard"] = pydantic.Field(
        alias="generated_from", default=None
    )
    last4: str = pydantic.Field(
        alias="last4",
    )
    """
    The last four digits of the card.
    """
    networks: typing.Optional[Networks] = pydantic.Field(alias="networks", default=None)
    regulated_status: typing.Optional[
        typing_extensions.Literal["regulated", "unregulated"]
    ] = pydantic.Field(alias="regulated_status", default=None)
    """
    Status of a card based on the card issuer.
    """
    three_d_secure_usage: typing.Optional[ThreeDSecureUsage] = pydantic.Field(
        alias="three_d_secure_usage", default=None
    )
    wallet: typing.Optional[PaymentMethodCardWallet] = pydantic.Field(
        alias="wallet", default=None
    )
