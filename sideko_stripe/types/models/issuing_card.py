import pydantic
import typing
import typing_extensions

from .issuing_card_authorization_controls import IssuingCardAuthorizationControls
from .issuing_card_metadata import IssuingCardMetadata
from .issuing_card_shipping import IssuingCardShipping
from .issuing_card_wallets import IssuingCardWallets

if typing_extensions.TYPE_CHECKING:
    from .issuing_cardholder import IssuingCardholder
    from .issuing_personalization_design import IssuingPersonalizationDesign


class IssuingCard(pydantic.BaseModel):
    """
    You can [create physical or virtual cards](https://stripe.com/docs/issuing) that are issued to cardholders.
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    brand: str = pydantic.Field(
        alias="brand",
    )
    """
    The brand of the card.
    """
    cancellation_reason: typing.Optional[
        typing_extensions.Literal["design_rejected", "lost", "stolen"]
    ] = pydantic.Field(alias="cancellation_reason", default=None)
    """
    The reason why the card was canceled.
    """
    cardholder: "IssuingCardholder" = pydantic.Field(
        alias="cardholder",
    )
    """
    An Issuing `Cardholder` object represents an individual or business entity who is [issued](https://stripe.com/docs/issuing) cards.
    
    Related guide: [How to create a cardholder](https://stripe.com/docs/issuing/cards/virtual/issue-cards#create-cardholder)
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
    Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Supported currencies are `usd` in the US, `eur` in the EU, and `gbp` in the UK.
    """
    cvc: typing.Optional[str] = pydantic.Field(alias="cvc", default=None)
    """
    The card's CVC. For security reasons, this is only available for virtual cards, and will be omitted unless you explicitly request it with [the `expand` parameter](https://stripe.com/docs/api/expanding_objects). Additionally, it's only available via the ["Retrieve a card" endpoint](https://stripe.com/docs/api/issuing/cards/retrieve), not via "List all cards" or any other endpoint.
    """
    exp_month: int = pydantic.Field(
        alias="exp_month",
    )
    """
    The expiration month of the card.
    """
    exp_year: int = pydantic.Field(
        alias="exp_year",
    )
    """
    The expiration year of the card.
    """
    financial_account: typing.Optional[str] = pydantic.Field(
        alias="financial_account", default=None
    )
    """
    The financial account this card is attached to.
    """
    id: str = pydantic.Field(
        alias="id",
    )
    """
    Unique identifier for the object.
    """
    last4: str = pydantic.Field(
        alias="last4",
    )
    """
    The last 4 digits of the card number.
    """
    livemode: bool = pydantic.Field(
        alias="livemode",
    )
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    metadata: IssuingCardMetadata = pydantic.Field(
        alias="metadata",
    )
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    number: typing.Optional[str] = pydantic.Field(alias="number", default=None)
    """
    The full unredacted card number. For security reasons, this is only available for virtual cards, and will be omitted unless you explicitly request it with [the `expand` parameter](https://stripe.com/docs/api/expanding_objects). Additionally, it's only available via the ["Retrieve a card" endpoint](https://stripe.com/docs/api/issuing/cards/retrieve), not via "List all cards" or any other endpoint.
    """
    object: typing_extensions.Literal["issuing.card"] = pydantic.Field(
        alias="object",
    )
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    personalization_design: typing.Optional[
        typing.Union[str, "IssuingPersonalizationDesign"]
    ] = pydantic.Field(alias="personalization_design", default=None)
    """
    The personalization design object belonging to this card.
    """
    replaced_by: typing.Optional[typing.Union[str, "IssuingCard"]] = pydantic.Field(
        alias="replaced_by", default=None
    )
    """
    The latest card that replaces this card, if any.
    """
    replacement_for: typing.Optional[typing.Union[str, "IssuingCard"]] = pydantic.Field(
        alias="replacement_for", default=None
    )
    """
    The card this card replaces, if any.
    """
    replacement_reason: typing.Optional[
        typing_extensions.Literal["damaged", "expired", "lost", "stolen"]
    ] = pydantic.Field(alias="replacement_reason", default=None)
    """
    The reason why the previous card needed to be replaced.
    """
    shipping: typing.Optional[IssuingCardShipping] = pydantic.Field(
        alias="shipping", default=None
    )
    spending_controls: IssuingCardAuthorizationControls = pydantic.Field(
        alias="spending_controls",
    )
    status: typing_extensions.Literal["active", "canceled", "inactive"] = (
        pydantic.Field(
            alias="status",
        )
    )
    """
    Whether authorizations can be approved on this card. May be blocked from activating cards depending on past-due Cardholder requirements. Defaults to `inactive`.
    """
    type_: typing_extensions.Literal["physical", "virtual"] = pydantic.Field(
        alias="type",
    )
    """
    The type of the card.
    """
    wallets: typing.Optional[IssuingCardWallets] = pydantic.Field(
        alias="wallets", default=None
    )
