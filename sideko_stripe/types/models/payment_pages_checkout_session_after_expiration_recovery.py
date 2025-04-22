import pydantic
import typing


class PaymentPagesCheckoutSessionAfterExpirationRecovery(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    allow_promotion_codes: bool = pydantic.Field(
        alias="allow_promotion_codes",
    )
    """
    Enables user redeemable promotion codes on the recovered Checkout Sessions. Defaults to `false`
    """
    enabled: bool = pydantic.Field(
        alias="enabled",
    )
    """
    If `true`, a recovery url will be generated to recover this Checkout Session if it
    expires before a transaction is completed. It will be attached to the
    Checkout Session object upon expiration.
    """
    expires_at: typing.Optional[int] = pydantic.Field(alias="expires_at", default=None)
    """
    The timestamp at which the recovery URL will expire.
    """
    url: typing.Optional[str] = pydantic.Field(alias="url", default=None)
    """
    URL that creates a new Checkout Session when clicked that is a copy of this expired Checkout Session
    """
