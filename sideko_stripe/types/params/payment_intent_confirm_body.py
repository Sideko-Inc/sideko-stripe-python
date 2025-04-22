import pydantic
import typing
import typing_extensions

from .payment_intent_confirm_body_mandate_data_obj0 import (
    PaymentIntentConfirmBodyMandateDataObj0,
    _SerializerPaymentIntentConfirmBodyMandateDataObj0,
)
from .payment_intent_confirm_body_mandate_data_obj2 import (
    PaymentIntentConfirmBodyMandateDataObj2,
    _SerializerPaymentIntentConfirmBodyMandateDataObj2,
)
from .payment_intent_confirm_body_payment_method_data import (
    PaymentIntentConfirmBodyPaymentMethodData,
    _SerializerPaymentIntentConfirmBodyPaymentMethodData,
)
from .payment_intent_confirm_body_payment_method_options import (
    PaymentIntentConfirmBodyPaymentMethodOptions,
    _SerializerPaymentIntentConfirmBodyPaymentMethodOptions,
)
from .payment_intent_confirm_body_radar_options import (
    PaymentIntentConfirmBodyRadarOptions,
    _SerializerPaymentIntentConfirmBodyRadarOptions,
)
from .payment_intent_confirm_body_shipping_obj0 import (
    PaymentIntentConfirmBodyShippingObj0,
    _SerializerPaymentIntentConfirmBodyShippingObj0,
)


class PaymentIntentConfirmBody(typing_extensions.TypedDict, total=False):
    """
    PaymentIntentConfirmBody
    """

    capture_method: typing_extensions.NotRequired[
        typing_extensions.Literal["automatic", "automatic_async", "manual"]
    ]
    """
    Controls when the funds will be captured from the customer's account.
    """

    client_secret: typing_extensions.NotRequired[str]
    """
    The client secret of the PaymentIntent.
    """

    confirmation_token: typing_extensions.NotRequired[str]
    """
    ID of the ConfirmationToken used to confirm this PaymentIntent.
    
    If the provided ConfirmationToken contains properties that are also being provided in this request, such as `payment_method`, then the values in this request will take precedence.
    """

    error_on_requires_action: typing_extensions.NotRequired[bool]
    """
    Set to `true` to fail the payment attempt if the PaymentIntent transitions into `requires_action`. This parameter is intended for simpler integrations that do not handle customer actions, like [saving cards without authentication](https://stripe.com/docs/payments/save-card-without-authentication).
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """

    mandate: typing_extensions.NotRequired[str]
    """
    ID of the mandate that's used for this payment.
    """

    mandate_data: typing_extensions.NotRequired[
        typing.Union[
            PaymentIntentConfirmBodyMandateDataObj0,
            str,
            PaymentIntentConfirmBodyMandateDataObj2,
        ]
    ]

    off_session: typing_extensions.NotRequired[
        typing.Union[bool, typing_extensions.Literal["one_off", "recurring"]]
    ]
    """
    Set to `true` to indicate that the customer isn't in your checkout flow during this payment attempt and can't authenticate. Use this parameter in scenarios where you collect card details and [charge them later](https://stripe.com/docs/payments/cards/charging-saved-cards).
    """

    payment_method: typing_extensions.NotRequired[str]
    """
    ID of the payment method (a PaymentMethod, Card, or [compatible Source](https://stripe.com/docs/payments/payment-methods/transitioning#compatibility) object) to attach to this PaymentIntent.
    """

    payment_method_data: typing_extensions.NotRequired[
        PaymentIntentConfirmBodyPaymentMethodData
    ]
    """
    If provided, this hash will be used to create a PaymentMethod. The new PaymentMethod will appear
    in the [payment_method](https://stripe.com/docs/api/payment_intents/object#payment_intent_object-payment_method)
    property on the PaymentIntent.
    """

    payment_method_options: typing_extensions.NotRequired[
        PaymentIntentConfirmBodyPaymentMethodOptions
    ]
    """
    Payment method-specific configuration for this PaymentIntent.
    """

    payment_method_types: typing_extensions.NotRequired[typing.List[str]]
    """
    The list of payment method types (for example, a card) that this PaymentIntent can use. Use `automatic_payment_methods` to manage payment methods from the [Stripe Dashboard](https://dashboard.stripe.com/settings/payment_methods).
    """

    radar_options: typing_extensions.NotRequired[PaymentIntentConfirmBodyRadarOptions]
    """
    Options to configure Radar. Learn more about [Radar Sessions](https://stripe.com/docs/radar/radar-session).
    """

    receipt_email: typing_extensions.NotRequired[typing.Union[str, str]]
    """
    Email address that the receipt for the resulting payment will be sent to. If `receipt_email` is specified for a payment in live mode, a receipt will be sent regardless of your [email settings](https://dashboard.stripe.com/account/emails).
    """

    return_url: typing_extensions.NotRequired[str]
    """
    The URL to redirect your customer back to after they authenticate or cancel their payment on the payment method's app or site.
    If you'd prefer to redirect to a mobile application, you can alternatively supply an application URI scheme.
    This parameter is only used for cards and other redirect-based payment methods.
    """

    setup_future_usage: typing_extensions.NotRequired[
        typing_extensions.Literal["off_session", "on_session"]
    ]
    """
    Indicates that you intend to make future payments with this PaymentIntent's payment method.
    
    If you provide a Customer with the PaymentIntent, you can use this parameter to [attach the payment method](/payments/save-during-payment) to the Customer after the PaymentIntent is confirmed and the customer completes any required actions. If you don't provide a Customer, you can still [attach](/api/payment_methods/attach) the payment method to a Customer after the transaction completes.
    
    If the payment method is `card_present` and isn't a digital wallet, Stripe creates and attaches a [generated_card](/api/charges/object#charge_object-payment_method_details-card_present-generated_card) payment method representing the card to the Customer instead.
    
    When processing card payments, Stripe uses `setup_future_usage` to help you comply with regional legislation and network rules, such as [SCA](/strong-customer-authentication).
    
    If you've already set `setup_future_usage` and you're performing a request using a publishable key, you can only update the value from `on_session` to `off_session`.
    """

    shipping: typing_extensions.NotRequired[
        typing.Union[PaymentIntentConfirmBodyShippingObj0, str]
    ]
    """
    Shipping information for this PaymentIntent.
    """

    use_stripe_sdk: typing_extensions.NotRequired[bool]
    """
    Set to `true` when confirming server-side and using Stripe.js, iOS, or Android client-side SDKs to handle the next actions.
    """


class _SerializerPaymentIntentConfirmBody(pydantic.BaseModel):
    """
    Serializer for PaymentIntentConfirmBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    capture_method: typing.Optional[
        typing_extensions.Literal["automatic", "automatic_async", "manual"]
    ] = pydantic.Field(alias="capture_method", default=None)
    client_secret: typing.Optional[str] = pydantic.Field(
        alias="client_secret", default=None
    )
    confirmation_token: typing.Optional[str] = pydantic.Field(
        alias="confirmation_token", default=None
    )
    error_on_requires_action: typing.Optional[bool] = pydantic.Field(
        alias="error_on_requires_action", default=None
    )
    expand: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="expand", default=None
    )
    mandate: typing.Optional[str] = pydantic.Field(alias="mandate", default=None)
    mandate_data: typing.Optional[
        typing.Union[
            _SerializerPaymentIntentConfirmBodyMandateDataObj0,
            str,
            _SerializerPaymentIntentConfirmBodyMandateDataObj2,
        ]
    ] = pydantic.Field(alias="mandate_data", default=None)
    off_session: typing.Optional[
        typing.Union[bool, typing_extensions.Literal["one_off", "recurring"]]
    ] = pydantic.Field(alias="off_session", default=None)
    payment_method: typing.Optional[str] = pydantic.Field(
        alias="payment_method", default=None
    )
    payment_method_data: typing.Optional[
        _SerializerPaymentIntentConfirmBodyPaymentMethodData
    ] = pydantic.Field(alias="payment_method_data", default=None)
    payment_method_options: typing.Optional[
        _SerializerPaymentIntentConfirmBodyPaymentMethodOptions
    ] = pydantic.Field(alias="payment_method_options", default=None)
    payment_method_types: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="payment_method_types", default=None
    )
    radar_options: typing.Optional[_SerializerPaymentIntentConfirmBodyRadarOptions] = (
        pydantic.Field(alias="radar_options", default=None)
    )
    receipt_email: typing.Optional[typing.Union[str, str]] = pydantic.Field(
        alias="receipt_email", default=None
    )
    return_url: typing.Optional[str] = pydantic.Field(alias="return_url", default=None)
    setup_future_usage: typing.Optional[
        typing_extensions.Literal["off_session", "on_session"]
    ] = pydantic.Field(alias="setup_future_usage", default=None)
    shipping: typing.Optional[
        typing.Union[_SerializerPaymentIntentConfirmBodyShippingObj0, str]
    ] = pydantic.Field(alias="shipping", default=None)
    use_stripe_sdk: typing.Optional[bool] = pydantic.Field(
        alias="use_stripe_sdk", default=None
    )
