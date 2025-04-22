import pydantic
import typing
import typing_extensions


class PaymentFlowsAutomaticPaymentMethodsPaymentIntent(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    allow_redirects: typing.Optional[typing_extensions.Literal["always", "never"]] = (
        pydantic.Field(alias="allow_redirects", default=None)
    )
    """
    Controls whether this PaymentIntent will accept redirect-based payment methods.
    
    Redirect-based payment methods may require your customer to be redirected to a payment method's app or site for authentication or additional steps. To [confirm](https://stripe.com/docs/api/payment_intents/confirm) this PaymentIntent, you may be required to provide a `return_url` to redirect customers back to your site after they authenticate or complete the payment.
    """
    enabled: bool = pydantic.Field(
        alias="enabled",
    )
    """
    Automatically calculates compatible payment methods
    """
