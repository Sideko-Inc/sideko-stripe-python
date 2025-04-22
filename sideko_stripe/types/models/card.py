import pydantic
import typing
import typing_extensions

from .card_metadata import CardMetadata
from .deleted_customer import DeletedCustomer
from .token_card_networks import TokenCardNetworks

if typing_extensions.TYPE_CHECKING:
    from .account import Account
    from .customer import Customer


class Card(pydantic.BaseModel):
    """
    You can store multiple cards on a customer in order to charge the customer
    later. You can also store multiple debit cards on a recipient in order to
    transfer to those cards later.

    Related guide: [Card payments with Sources](https://stripe.com/docs/sources/cards)
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    account: typing.Optional[typing.Union[str, "Account"]] = pydantic.Field(
        alias="account", default=None
    )
    address_city: typing.Optional[str] = pydantic.Field(
        alias="address_city", default=None
    )
    """
    City/District/Suburb/Town/Village.
    """
    address_country: typing.Optional[str] = pydantic.Field(
        alias="address_country", default=None
    )
    """
    Billing address country, if provided when creating card.
    """
    address_line1: typing.Optional[str] = pydantic.Field(
        alias="address_line1", default=None
    )
    """
    Address line 1 (Street address/PO Box/Company name).
    """
    address_line1_check: typing.Optional[str] = pydantic.Field(
        alias="address_line1_check", default=None
    )
    """
    If `address_line1` was provided, results of the check: `pass`, `fail`, `unavailable`, or `unchecked`.
    """
    address_line2: typing.Optional[str] = pydantic.Field(
        alias="address_line2", default=None
    )
    """
    Address line 2 (Apartment/Suite/Unit/Building).
    """
    address_state: typing.Optional[str] = pydantic.Field(
        alias="address_state", default=None
    )
    """
    State/County/Province/Region.
    """
    address_zip: typing.Optional[str] = pydantic.Field(
        alias="address_zip", default=None
    )
    """
    ZIP or postal code.
    """
    address_zip_check: typing.Optional[str] = pydantic.Field(
        alias="address_zip_check", default=None
    )
    """
    If `address_zip` was provided, results of the check: `pass`, `fail`, `unavailable`, or `unchecked`.
    """
    allow_redisplay: typing.Optional[
        typing_extensions.Literal["always", "limited", "unspecified"]
    ] = pydantic.Field(alias="allow_redisplay", default=None)
    """
    This field indicates whether this payment method can be shown again to its customer in a checkout flow. Stripe products such as Checkout and Elements use this field to determine whether a payment method can be shown as a saved payment method in a checkout flow. The field defaults to “unspecified”.
    """
    available_payout_methods: typing.Optional[
        typing.List[typing_extensions.Literal["instant", "standard"]]
    ] = pydantic.Field(alias="available_payout_methods", default=None)
    """
    A set of available payout methods for this card. Only values from this set should be passed as the `method` when creating a payout.
    """
    brand: str = pydantic.Field(
        alias="brand",
    )
    """
    Card brand. Can be `American Express`, `Diners Club`, `Discover`, `Eftpos Australia`, `Girocard`, `JCB`, `MasterCard`, `UnionPay`, `Visa`, or `Unknown`.
    """
    country: typing.Optional[str] = pydantic.Field(alias="country", default=None)
    """
    Two-letter ISO code representing the country of the card. You could use this attribute to get a sense of the international breakdown of cards you've collected.
    """
    currency: typing.Optional[str] = pydantic.Field(alias="currency", default=None)
    """
    Three-letter [ISO code for currency](https://www.iso.org/iso-4217-currency-codes.html) in lowercase. Must be a [supported currency](https://docs.stripe.com/currencies). Only applicable on accounts (not customers or recipients). The card can be used as a transfer destination for funds in this currency. This property is only available when returned as an [External Account](/api/external_account_cards/object) where [controller.is_controller](/api/accounts/object#account_object-controller-is_controller) is `true`.
    """
    customer: typing.Optional[typing.Union[str, "Customer", DeletedCustomer]] = (
        pydantic.Field(alias="customer", default=None)
    )
    """
    The customer that this card belongs to. This attribute will not be in the card object if the card belongs to an account or recipient instead.
    """
    cvc_check: typing.Optional[str] = pydantic.Field(alias="cvc_check", default=None)
    """
    If a CVC was provided, results of the check: `pass`, `fail`, `unavailable`, or `unchecked`. A result of unchecked indicates that CVC was provided but hasn't been checked yet. Checks are typically performed when attaching a card to a Customer object, or when creating a charge. For more details, see [Check if a card is valid without a charge](https://support.stripe.com/questions/check-if-a-card-is-valid-without-a-charge).
    """
    default_for_currency: typing.Optional[bool] = pydantic.Field(
        alias="default_for_currency", default=None
    )
    """
    Whether this card is the default external account for its currency. This property is only available for accounts where [controller.requirement_collection](/api/accounts/object#account_object-controller-requirement_collection) is `application`, which includes Custom accounts.
    """
    dynamic_last4: typing.Optional[str] = pydantic.Field(
        alias="dynamic_last4", default=None
    )
    """
    (For tokenized numbers only.) The last four digits of the device account number.
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
    id: str = pydantic.Field(
        alias="id",
    )
    """
    Unique identifier for the object.
    """
    iin: typing.Optional[str] = pydantic.Field(alias="iin", default=None)
    """
    Issuer identification number of the card.
    """
    last4: str = pydantic.Field(
        alias="last4",
    )
    """
    The last four digits of the card.
    """
    metadata: typing.Optional[CardMetadata] = pydantic.Field(
        alias="metadata", default=None
    )
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    """
    Cardholder name.
    """
    networks: typing.Optional[TokenCardNetworks] = pydantic.Field(
        alias="networks", default=None
    )
    object: typing_extensions.Literal["card"] = pydantic.Field(
        alias="object",
    )
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    regulated_status: typing.Optional[
        typing_extensions.Literal["regulated", "unregulated"]
    ] = pydantic.Field(alias="regulated_status", default=None)
    """
    Status of a card based on the card issuer.
    """
    status: typing.Optional[str] = pydantic.Field(alias="status", default=None)
    """
    For external accounts that are cards, possible values are `new` and `errored`. If a payout fails, the status is set to `errored` and [scheduled payouts](https://stripe.com/docs/payouts#payout-schedule) are stopped until account details are updated.
    """
    tokenization_method: typing.Optional[str] = pydantic.Field(
        alias="tokenization_method", default=None
    )
    """
    If the card number is tokenized, this is the method that was used. Can be `android_pay` (includes Google Pay), `apple_pay`, `masterpass`, `visa_checkout`, or null.
    """
