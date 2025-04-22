import pydantic
import typing
import typing_extensions

from .payment_flows_private_payment_methods_card_present_common_wallet import (
    PaymentFlowsPrivatePaymentMethodsCardPresentCommonWallet,
)
from .payment_method_card_present_networks import PaymentMethodCardPresentNetworks
from .payment_method_details_card_present_offline import (
    PaymentMethodDetailsCardPresentOffline,
)


class PaymentMethodCardPresent(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    brand: typing.Optional[str] = pydantic.Field(alias="brand", default=None)
    """
    Card brand. Can be `amex`, `diners`, `discover`, `eftpos_au`, `jcb`, `link`, `mastercard`, `unionpay`, `visa`, or `unknown`.
    """
    brand_product: typing.Optional[str] = pydantic.Field(
        alias="brand_product", default=None
    )
    """
    The [product code](https://stripe.com/docs/card-product-codes) that identifies the specific program or product associated with a card.
    """
    cardholder_name: typing.Optional[str] = pydantic.Field(
        alias="cardholder_name", default=None
    )
    """
    The cardholder name as read from the card, in [ISO 7813](https://en.wikipedia.org/wiki/ISO/IEC_7813) format. May include alphanumeric characters, special characters and first/last name separator (`/`). In some cases, the cardholder name may not be available depending on how the issuer has configured the card. Cardholder name is typically not available on swipe or contactless payments, such as those made with Apple Pay and Google Pay.
    """
    country: typing.Optional[str] = pydantic.Field(alias="country", default=None)
    """
    Two-letter ISO code representing the country of the card. You could use this attribute to get a sense of the international breakdown of cards you've collected.
    """
    description: typing.Optional[str] = pydantic.Field(
        alias="description", default=None
    )
    """
    A high-level description of the type of cards issued in this range.
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
    funding: typing.Optional[str] = pydantic.Field(alias="funding", default=None)
    """
    Card funding type. Can be `credit`, `debit`, `prepaid`, or `unknown`.
    """
    issuer: typing.Optional[str] = pydantic.Field(alias="issuer", default=None)
    """
    The name of the card's issuing bank.
    """
    last4: typing.Optional[str] = pydantic.Field(alias="last4", default=None)
    """
    The last four digits of the card.
    """
    networks: typing.Optional[PaymentMethodCardPresentNetworks] = pydantic.Field(
        alias="networks", default=None
    )
    offline: typing.Optional[PaymentMethodDetailsCardPresentOffline] = pydantic.Field(
        alias="offline", default=None
    )
    preferred_locales: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="preferred_locales", default=None
    )
    """
    EMV tag 5F2D. Preferred languages specified by the integrated circuit chip.
    """
    read_method: typing.Optional[
        typing_extensions.Literal[
            "contact_emv",
            "contactless_emv",
            "contactless_magstripe_mode",
            "magnetic_stripe_fallback",
            "magnetic_stripe_track2",
        ]
    ] = pydantic.Field(alias="read_method", default=None)
    """
    How card details were read in this transaction.
    """
    wallet: typing.Optional[
        PaymentFlowsPrivatePaymentMethodsCardPresentCommonWallet
    ] = pydantic.Field(alias="wallet", default=None)
