import pydantic
import typing
import typing_extensions

from .issuing_network_token_network_data import IssuingNetworkTokenNetworkData

if typing_extensions.TYPE_CHECKING:
    from .issuing_card import IssuingCard


class IssuingToken(pydantic.BaseModel):
    """
    An issuing token object is created when an issued card is added to a digital wallet. As a [card issuer](https://stripe.com/docs/issuing), you can [view and manage these tokens](https://stripe.com/docs/issuing/controls/token-management) through Stripe.
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    card: typing.Union[str, "IssuingCard"] = pydantic.Field(
        alias="card",
    )
    """
    Card associated with this token.
    """
    created: int = pydantic.Field(
        alias="created",
    )
    """
    Time at which the object was created. Measured in seconds since the Unix epoch.
    """
    device_fingerprint: typing.Optional[str] = pydantic.Field(
        alias="device_fingerprint", default=None
    )
    """
    The hashed ID derived from the device ID from the card network associated with the token.
    """
    id: str = pydantic.Field(
        alias="id",
    )
    """
    Unique identifier for the object.
    """
    last4: typing.Optional[str] = pydantic.Field(alias="last4", default=None)
    """
    The last four digits of the token.
    """
    livemode: bool = pydantic.Field(
        alias="livemode",
    )
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    network: typing_extensions.Literal["mastercard", "visa"] = pydantic.Field(
        alias="network",
    )
    """
    The token service provider / card network associated with the token.
    """
    network_data: typing.Optional[IssuingNetworkTokenNetworkData] = pydantic.Field(
        alias="network_data", default=None
    )
    network_updated_at: int = pydantic.Field(
        alias="network_updated_at",
    )
    """
    Time at which the token was last updated by the card network. Measured in seconds since the Unix epoch.
    """
    object: typing_extensions.Literal["issuing.token"] = pydantic.Field(
        alias="object",
    )
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    status: typing_extensions.Literal["active", "deleted", "requested", "suspended"] = (
        pydantic.Field(
            alias="status",
        )
    )
    """
    The usage state of the token.
    """
    wallet_provider: typing.Optional[
        typing_extensions.Literal["apple_pay", "google_pay", "samsung_pay"]
    ] = pydantic.Field(alias="wallet_provider", default=None)
    """
    The digital wallet for this token, if one was used.
    """
