import pydantic
import typing

from .issuing_authorization_amount_details import IssuingAuthorizationAmountDetails


class IssuingAuthorizationPendingRequest(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    amount: int = pydantic.Field(
        alias="amount",
    )
    """
    The additional amount Stripe will hold if the authorization is approved, in the card's [currency](https://stripe.com/docs/api#issuing_authorization_object-pending-request-currency) and in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal).
    """
    amount_details: typing.Optional[IssuingAuthorizationAmountDetails] = pydantic.Field(
        alias="amount_details", default=None
    )
    currency: str = pydantic.Field(
        alias="currency",
    )
    """
    Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    """
    is_amount_controllable: bool = pydantic.Field(
        alias="is_amount_controllable",
    )
    """
    If set `true`, you may provide [amount](https://stripe.com/docs/api/issuing/authorizations/approve#approve_issuing_authorization-amount) to control how much to hold for the authorization.
    """
    merchant_amount: int = pydantic.Field(
        alias="merchant_amount",
    )
    """
    The amount the merchant is requesting to be authorized in the `merchant_currency`. The amount is in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal).
    """
    merchant_currency: str = pydantic.Field(
        alias="merchant_currency",
    )
    """
    The local currency the merchant is requesting to authorize.
    """
    network_risk_score: typing.Optional[int] = pydantic.Field(
        alias="network_risk_score", default=None
    )
    """
    The card network's estimate of the likelihood that an authorization is fraudulent. Takes on values between 1 and 99.
    """
