import pydantic
import typing
import typing_extensions

from .confirmation_tokens_resource_mandate_data import (
    ConfirmationTokensResourceMandateData,
)
from .confirmation_tokens_resource_payment_method_options import (
    ConfirmationTokensResourcePaymentMethodOptions,
)
from .confirmation_tokens_resource_shipping import ConfirmationTokensResourceShipping

if typing_extensions.TYPE_CHECKING:
    from .confirmation_tokens_resource_payment_method_preview import (
        ConfirmationTokensResourcePaymentMethodPreview,
    )


class ConfirmationToken(pydantic.BaseModel):
    """
    ConfirmationTokens help transport client side data collected by Stripe JS over
    to your server for confirming a PaymentIntent or SetupIntent. If the confirmation
    is successful, values present on the ConfirmationToken are written onto the Intent.

    To learn more about how to use ConfirmationToken, visit the related guides:
    - [Finalize payments on the server](https://stripe.com/docs/payments/finalize-payments-on-the-server)
    - [Build two-step confirmation](https://stripe.com/docs/payments/build-a-two-step-confirmation).
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    created: int = pydantic.Field(
        alias="created",
    )
    """
    Time at which the object was created. Measured in seconds since the Unix epoch.
    """
    expires_at: typing.Optional[int] = pydantic.Field(alias="expires_at", default=None)
    """
    Time at which this ConfirmationToken expires and can no longer be used to confirm a PaymentIntent or SetupIntent.
    """
    id: str = pydantic.Field(
        alias="id",
    )
    """
    Unique identifier for the object.
    """
    livemode: bool = pydantic.Field(
        alias="livemode",
    )
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    mandate_data: typing.Optional[ConfirmationTokensResourceMandateData] = (
        pydantic.Field(alias="mandate_data", default=None)
    )
    """
    Data used for generating a Mandate.
    """
    object: typing_extensions.Literal["confirmation_token"] = pydantic.Field(
        alias="object",
    )
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    payment_intent: typing.Optional[str] = pydantic.Field(
        alias="payment_intent", default=None
    )
    """
    ID of the PaymentIntent that this ConfirmationToken was used to confirm, or null if this ConfirmationToken has not yet been used.
    """
    payment_method_options: typing.Optional[
        ConfirmationTokensResourcePaymentMethodOptions
    ] = pydantic.Field(alias="payment_method_options", default=None)
    """
    Payment-method-specific configuration
    """
    payment_method_preview: typing.Optional[
        "ConfirmationTokensResourcePaymentMethodPreview"
    ] = pydantic.Field(alias="payment_method_preview", default=None)
    """
    Details of the PaymentMethod collected by Payment Element
    """
    return_url: typing.Optional[str] = pydantic.Field(alias="return_url", default=None)
    """
    Return URL used to confirm the Intent.
    """
    setup_future_usage: typing.Optional[
        typing_extensions.Literal["off_session", "on_session"]
    ] = pydantic.Field(alias="setup_future_usage", default=None)
    """
    Indicates that you intend to make future payments with this ConfirmationToken's payment method.
    
    The presence of this property will [attach the payment method](https://stripe.com/docs/payments/save-during-payment) to the PaymentIntent's Customer, if present, after the PaymentIntent is confirmed and any required actions from the user are complete.
    """
    setup_intent: typing.Optional[str] = pydantic.Field(
        alias="setup_intent", default=None
    )
    """
    ID of the SetupIntent that this ConfirmationToken was used to confirm, or null if this ConfirmationToken has not yet been used.
    """
    shipping: typing.Optional[ConfirmationTokensResourceShipping] = pydantic.Field(
        alias="shipping", default=None
    )
    use_stripe_sdk: bool = pydantic.Field(
        alias="use_stripe_sdk",
    )
    """
    Indicates whether the Stripe SDK is used to handle confirmation flow. Defaults to `true` on ConfirmationToken.
    """
