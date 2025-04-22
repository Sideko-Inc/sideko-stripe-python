import pydantic
import typing
import typing_extensions

from .checkout_session_create_body_after_expiration_recovery import (
    CheckoutSessionCreateBodyAfterExpirationRecovery,
    _SerializerCheckoutSessionCreateBodyAfterExpirationRecovery,
)


class CheckoutSessionCreateBodyAfterExpiration(typing_extensions.TypedDict):
    """
    Configure actions after a Checkout Session has expired.
    """

    recovery: typing_extensions.NotRequired[
        CheckoutSessionCreateBodyAfterExpirationRecovery
    ]


class _SerializerCheckoutSessionCreateBodyAfterExpiration(pydantic.BaseModel):
    """
    Serializer for CheckoutSessionCreateBodyAfterExpiration handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    recovery: typing.Optional[
        _SerializerCheckoutSessionCreateBodyAfterExpirationRecovery
    ] = pydantic.Field(alias="recovery", default=None)
