import pydantic
import typing
import typing_extensions

from .source import Source

if typing_extensions.TYPE_CHECKING:
    from .bank_account import BankAccount
    from .card import Card
    from .payment_intent import PaymentIntent
    from .setup_intent import SetupIntent


class ApiErrors(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    advice_code: typing.Optional[str] = pydantic.Field(
        alias="advice_code", default=None
    )
    """
    For card errors resulting from a card issuer decline, a short string indicating [how to proceed with an error](https://stripe.com/docs/declines#retrying-issuer-declines) if they provide one.
    """
    charge: typing.Optional[str] = pydantic.Field(alias="charge", default=None)
    """
    For card errors, the ID of the failed charge.
    """
    code: typing.Optional[str] = pydantic.Field(alias="code", default=None)
    """
    For some errors that could be handled programmatically, a short string indicating the [error code](https://stripe.com/docs/error-codes) reported.
    """
    decline_code: typing.Optional[str] = pydantic.Field(
        alias="decline_code", default=None
    )
    """
    For card errors resulting from a card issuer decline, a short string indicating the [card issuer's reason for the decline](https://stripe.com/docs/declines#issuer-declines) if they provide one.
    """
    doc_url: typing.Optional[str] = pydantic.Field(alias="doc_url", default=None)
    """
    A URL to more information about the [error code](https://stripe.com/docs/error-codes) reported.
    """
    message: typing.Optional[str] = pydantic.Field(alias="message", default=None)
    """
    A human-readable message providing more details about the error. For card errors, these messages can be shown to your users.
    """
    network_advice_code: typing.Optional[str] = pydantic.Field(
        alias="network_advice_code", default=None
    )
    """
    For card errors resulting from a card issuer decline, a 2 digit code which indicates the advice given to merchant by the card network on how to proceed with an error.
    """
    network_decline_code: typing.Optional[str] = pydantic.Field(
        alias="network_decline_code", default=None
    )
    """
    For card errors resulting from a card issuer decline, a brand specific 2, 3, or 4 digit code which indicates the reason the authorization failed.
    """
    param: typing.Optional[str] = pydantic.Field(alias="param", default=None)
    """
    If the error is parameter-specific, the parameter related to the error. For example, you can use this to display a message near the correct form field.
    """
    payment_intent: typing.Optional["PaymentIntent"] = pydantic.Field(
        alias="payment_intent", default=None
    )
    """
    A PaymentIntent guides you through the process of collecting a payment from your customer.
    We recommend that you create exactly one PaymentIntent for each order or
    customer session in your system. You can reference the PaymentIntent later to
    see the history of payment attempts for a particular session.
    
    A PaymentIntent transitions through
    [multiple statuses](https://stripe.com/docs/payments/intents#intent-statuses)
    throughout its lifetime as it interfaces with Stripe.js to perform
    authentication flows and ultimately creates at most one successful charge.
    
    Related guide: [Payment Intents API](https://stripe.com/docs/payments/payment-intents)
    """
    payment_method_type: typing.Optional[str] = pydantic.Field(
        alias="payment_method_type", default=None
    )
    """
    If the error is specific to the type of payment method, the payment method type that had a problem. This field is only populated for invoice-related errors.
    """
    request_log_url: typing.Optional[str] = pydantic.Field(
        alias="request_log_url", default=None
    )
    """
    A URL to the request log entry in your dashboard.
    """
    setup_intent: typing.Optional["SetupIntent"] = pydantic.Field(
        alias="setup_intent", default=None
    )
    """
    A SetupIntent guides you through the process of setting up and saving a customer's payment credentials for future payments.
    For example, you can use a SetupIntent to set up and save your customer's card without immediately collecting a payment.
    Later, you can use [PaymentIntents](https://stripe.com/docs/api#payment_intents) to drive the payment flow.
    
    Create a SetupIntent when you're ready to collect your customer's payment credentials.
    Don't maintain long-lived, unconfirmed SetupIntents because they might not be valid.
    The SetupIntent transitions through multiple [statuses](https://docs.stripe.com/payments/intents#intent-statuses) as it guides
    you through the setup process.
    
    Successful SetupIntents result in payment credentials that are optimized for future payments.
    For example, cardholders in [certain regions](https://stripe.com/guides/strong-customer-authentication) might need to be run through
    [Strong Customer Authentication](https://docs.stripe.com/strong-customer-authentication) during payment method collection
    to streamline later [off-session payments](https://docs.stripe.com/payments/setup-intents).
    If you use the SetupIntent with a [Customer](https://stripe.com/docs/api#setup_intent_object-customer),
    it automatically attaches the resulting payment method to that Customer after successful setup.
    We recommend using SetupIntents or [setup_future_usage](https://stripe.com/docs/api#payment_intent_object-setup_future_usage) on
    PaymentIntents to save payment methods to prevent saving invalid or unoptimized payment methods.
    
    By using SetupIntents, you can reduce friction for your customers, even as regulations change over time.
    
    Related guide: [Setup Intents API](https://docs.stripe.com/payments/setup-intents)
    """
    source: typing.Optional[typing.Union["BankAccount", "Card", Source]] = (
        pydantic.Field(alias="source", default=None)
    )
    """
    The [source object](https://stripe.com/docs/api/sources/object) for errors returned on a request involving a source.
    """
    type_: typing_extensions.Literal[
        "api_error", "card_error", "idempotency_error", "invalid_request_error"
    ] = pydantic.Field(
        alias="type",
    )
    """
    The type of error returned. One of `api_error`, `card_error`, `idempotency_error`, or `invalid_request_error`
    """
