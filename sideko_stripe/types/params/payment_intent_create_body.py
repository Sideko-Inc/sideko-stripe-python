import pydantic
import typing
import typing_extensions

from .payment_intent_create_body_automatic_payment_methods import (
    PaymentIntentCreateBodyAutomaticPaymentMethods,
    _SerializerPaymentIntentCreateBodyAutomaticPaymentMethods,
)
from .payment_intent_create_body_mandate_data_obj0 import (
    PaymentIntentCreateBodyMandateDataObj0,
    _SerializerPaymentIntentCreateBodyMandateDataObj0,
)
from .payment_intent_create_body_metadata import (
    PaymentIntentCreateBodyMetadata,
    _SerializerPaymentIntentCreateBodyMetadata,
)
from .payment_intent_create_body_payment_method_data import (
    PaymentIntentCreateBodyPaymentMethodData,
    _SerializerPaymentIntentCreateBodyPaymentMethodData,
)
from .payment_intent_create_body_payment_method_options import (
    PaymentIntentCreateBodyPaymentMethodOptions,
    _SerializerPaymentIntentCreateBodyPaymentMethodOptions,
)
from .payment_intent_create_body_radar_options import (
    PaymentIntentCreateBodyRadarOptions,
    _SerializerPaymentIntentCreateBodyRadarOptions,
)
from .payment_intent_create_body_shipping import (
    PaymentIntentCreateBodyShipping,
    _SerializerPaymentIntentCreateBodyShipping,
)
from .payment_intent_create_body_transfer_data import (
    PaymentIntentCreateBodyTransferData,
    _SerializerPaymentIntentCreateBodyTransferData,
)


class PaymentIntentCreateBody(typing_extensions.TypedDict, total=False):
    """
    PaymentIntentCreateBody
    """

    amount: typing_extensions.Required[int]
    """
    Amount intended to be collected by this PaymentIntent. A positive integer representing how much to charge in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal) (e.g., 100 cents to charge $1.00 or 100 to charge ¥100, a zero-decimal currency). The minimum amount is $0.50 US or [equivalent in charge currency](https://stripe.com/docs/currencies#minimum-and-maximum-charge-amounts). The amount value supports up to eight digits (e.g., a value of 99999999 for a USD charge of $999,999.99).
    """

    application_fee_amount: typing_extensions.NotRequired[int]
    """
    The amount of the application fee (if any) that will be requested to be applied to the payment and transferred to the application owner's Stripe account. The amount of the application fee collected will be capped at the total amount captured. For more information, see the PaymentIntents [use case for connected accounts](https://stripe.com/docs/payments/connected-accounts).
    """

    automatic_payment_methods: typing_extensions.NotRequired[
        PaymentIntentCreateBodyAutomaticPaymentMethods
    ]
    """
    When you enable this parameter, this PaymentIntent accepts payment methods that you enable in the Dashboard and that are compatible with this PaymentIntent's other parameters.
    """

    capture_method: typing_extensions.NotRequired[
        typing_extensions.Literal["automatic", "automatic_async", "manual"]
    ]
    """
    Controls when the funds will be captured from the customer's account.
    """

    confirm: typing_extensions.NotRequired[bool]
    """
    Set to `true` to attempt to [confirm this PaymentIntent](https://stripe.com/docs/api/payment_intents/confirm) immediately. This parameter defaults to `false`. When creating and confirming a PaymentIntent at the same time, you can also provide the parameters available in the [Confirm API](https://stripe.com/docs/api/payment_intents/confirm).
    """

    confirmation_method: typing_extensions.NotRequired[
        typing_extensions.Literal["automatic", "manual"]
    ]
    """
    Describes whether we can confirm this PaymentIntent automatically, or if it requires customer action to confirm the payment.
    """

    confirmation_token: typing_extensions.NotRequired[str]
    """
    ID of the ConfirmationToken used to confirm this PaymentIntent.
    
    If the provided ConfirmationToken contains properties that are also being provided in this request, such as `payment_method`, then the values in this request will take precedence.
    """

    currency: typing_extensions.Required[str]
    """
    Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    """

    customer: typing_extensions.NotRequired[str]
    """
    ID of the Customer this PaymentIntent belongs to, if one exists.
    
    Payment methods attached to other Customers cannot be used with this PaymentIntent.
    
    If [setup_future_usage](https://stripe.com/docs/api#payment_intent_object-setup_future_usage) is set and this PaymentIntent's payment method is not `card_present`, then the payment method attaches to the Customer after the PaymentIntent has been confirmed and any required actions from the user are complete. If the payment method is `card_present` and isn't a digital wallet, then a [generated_card](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-card_present-generated_card) payment method representing the card is created and attached to the Customer instead.
    """

    description: typing_extensions.NotRequired[str]
    """
    An arbitrary string attached to the object. Often useful for displaying to users.
    """

    error_on_requires_action: typing_extensions.NotRequired[bool]
    """
    Set to `true` to fail the payment attempt if the PaymentIntent transitions into `requires_action`. Use this parameter for simpler integrations that don't handle customer actions, such as [saving cards without authentication](https://stripe.com/docs/payments/save-card-without-authentication). This parameter can only be used with [`confirm=true`](https://stripe.com/docs/api/payment_intents/create#create_payment_intent-confirm).
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """

    mandate: typing_extensions.NotRequired[str]
    """
    ID of the mandate that's used for this payment. This parameter can only be used with [`confirm=true`](https://stripe.com/docs/api/payment_intents/create#create_payment_intent-confirm).
    """

    mandate_data: typing_extensions.NotRequired[
        typing.Union[PaymentIntentCreateBodyMandateDataObj0, str]
    ]
    """
    This hash contains details about the Mandate to create. This parameter can only be used with [`confirm=true`](https://stripe.com/docs/api/payment_intents/create#create_payment_intent-confirm).
    """

    metadata: typing_extensions.NotRequired[PaymentIntentCreateBodyMetadata]
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    """

    off_session: typing_extensions.NotRequired[
        typing.Union[bool, typing_extensions.Literal["one_off", "recurring"]]
    ]
    """
    Set to `true` to indicate that the customer isn't in your checkout flow during this payment attempt and can't authenticate. Use this parameter in scenarios where you collect card details and [charge them later](https://stripe.com/docs/payments/cards/charging-saved-cards). This parameter can only be used with [`confirm=true`](https://stripe.com/docs/api/payment_intents/create#create_payment_intent-confirm).
    """

    on_behalf_of: typing_extensions.NotRequired[str]
    """
    The Stripe account ID that these funds are intended for. Learn more about the [use case for connected accounts](https://stripe.com/docs/payments/connected-accounts).
    """

    payment_method: typing_extensions.NotRequired[str]
    """
    ID of the payment method (a PaymentMethod, Card, or [compatible Source](https://stripe.com/docs/payments/payment-methods/transitioning#compatibility) object) to attach to this PaymentIntent.
    
    If you omit this parameter with `confirm=true`, `customer.default_source` attaches as this PaymentIntent's payment instrument to improve migration for users of the Charges API. We recommend that you explicitly provide the `payment_method` moving forward.
    """

    payment_method_configuration: typing_extensions.NotRequired[str]
    """
    The ID of the [payment method configuration](https://stripe.com/docs/api/payment_method_configurations) to use with this PaymentIntent.
    """

    payment_method_data: typing_extensions.NotRequired[
        PaymentIntentCreateBodyPaymentMethodData
    ]
    """
    If provided, this hash will be used to create a PaymentMethod. The new PaymentMethod will appear
    in the [payment_method](https://stripe.com/docs/api/payment_intents/object#payment_intent_object-payment_method)
    property on the PaymentIntent.
    """

    payment_method_options: typing_extensions.NotRequired[
        PaymentIntentCreateBodyPaymentMethodOptions
    ]
    """
    Payment method-specific configuration for this PaymentIntent.
    """

    payment_method_types: typing_extensions.NotRequired[typing.List[str]]
    """
    The list of payment method types (for example, a card) that this PaymentIntent can use. If you don't provide this, Stripe will dynamically show relevant payment methods from your [payment method settings](https://dashboard.stripe.com/settings/payment_methods).
    """

    radar_options: typing_extensions.NotRequired[PaymentIntentCreateBodyRadarOptions]
    """
    Options to configure Radar. Learn more about [Radar Sessions](https://stripe.com/docs/radar/radar-session).
    """

    receipt_email: typing_extensions.NotRequired[str]
    """
    Email address to send the receipt to. If you specify `receipt_email` for a payment in live mode, you send a receipt regardless of your [email settings](https://dashboard.stripe.com/account/emails).
    """

    return_url: typing_extensions.NotRequired[str]
    """
    The URL to redirect your customer back to after they authenticate or cancel their payment on the payment method's app or site. If you'd prefer to redirect to a mobile application, you can alternatively supply an application URI scheme. This parameter can only be used with [`confirm=true`](https://stripe.com/docs/api/payment_intents/create#create_payment_intent-confirm).
    """

    setup_future_usage: typing_extensions.NotRequired[
        typing_extensions.Literal["off_session", "on_session"]
    ]
    """
    Indicates that you intend to make future payments with this PaymentIntent's payment method.
    
    If you provide a Customer with the PaymentIntent, you can use this parameter to [attach the payment method](/payments/save-during-payment) to the Customer after the PaymentIntent is confirmed and the customer completes any required actions. If you don't provide a Customer, you can still [attach](/api/payment_methods/attach) the payment method to a Customer after the transaction completes.
    
    If the payment method is `card_present` and isn't a digital wallet, Stripe creates and attaches a [generated_card](/api/charges/object#charge_object-payment_method_details-card_present-generated_card) payment method representing the card to the Customer instead.
    
    When processing card payments, Stripe uses `setup_future_usage` to help you comply with regional legislation and network rules, such as [SCA](/strong-customer-authentication).
    """

    shipping: typing_extensions.NotRequired[PaymentIntentCreateBodyShipping]
    """
    Shipping information for this PaymentIntent.
    """

    statement_descriptor: typing_extensions.NotRequired[str]
    """
    Text that appears on the customer's statement as the statement descriptor for a non-card charge. This value overrides the account's default statement descriptor. For information about requirements, including the 22-character limit, see [the Statement Descriptor docs](https://docs.stripe.com/get-started/account/statement-descriptors).
    
    Setting this value for a card charge returns an error. For card charges, set the [statement_descriptor_suffix](https://docs.stripe.com/get-started/account/statement-descriptors#dynamic) instead.
    """

    statement_descriptor_suffix: typing_extensions.NotRequired[str]
    """
    Provides information about a card charge. Concatenated to the account's [statement descriptor prefix](https://docs.stripe.com/get-started/account/statement-descriptors#static) to form the complete statement descriptor that appears on the customer's statement.
    """

    transfer_data: typing_extensions.NotRequired[PaymentIntentCreateBodyTransferData]
    """
    The parameters that you can use to automatically create a Transfer.
    Learn more about the [use case for connected accounts](https://stripe.com/docs/payments/connected-accounts).
    """

    transfer_group: typing_extensions.NotRequired[str]
    """
    A string that identifies the resulting payment as part of a group. Learn more about the [use case for connected accounts](https://stripe.com/docs/connect/separate-charges-and-transfers).
    """

    use_stripe_sdk: typing_extensions.NotRequired[bool]
    """
    Set to `true` when confirming server-side and using Stripe.js, iOS, or Android client-side SDKs to handle the next actions.
    """


class _SerializerPaymentIntentCreateBody(pydantic.BaseModel):
    """
    Serializer for PaymentIntentCreateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    amount: int = pydantic.Field(
        alias="amount",
    )
    application_fee_amount: typing.Optional[int] = pydantic.Field(
        alias="application_fee_amount", default=None
    )
    automatic_payment_methods: typing.Optional[
        _SerializerPaymentIntentCreateBodyAutomaticPaymentMethods
    ] = pydantic.Field(alias="automatic_payment_methods", default=None)
    capture_method: typing.Optional[
        typing_extensions.Literal["automatic", "automatic_async", "manual"]
    ] = pydantic.Field(alias="capture_method", default=None)
    confirm: typing.Optional[bool] = pydantic.Field(alias="confirm", default=None)
    confirmation_method: typing.Optional[
        typing_extensions.Literal["automatic", "manual"]
    ] = pydantic.Field(alias="confirmation_method", default=None)
    confirmation_token: typing.Optional[str] = pydantic.Field(
        alias="confirmation_token", default=None
    )
    currency: str = pydantic.Field(
        alias="currency",
    )
    customer: typing.Optional[str] = pydantic.Field(alias="customer", default=None)
    description: typing.Optional[str] = pydantic.Field(
        alias="description", default=None
    )
    error_on_requires_action: typing.Optional[bool] = pydantic.Field(
        alias="error_on_requires_action", default=None
    )
    expand: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="expand", default=None
    )
    mandate: typing.Optional[str] = pydantic.Field(alias="mandate", default=None)
    mandate_data: typing.Optional[
        typing.Union[_SerializerPaymentIntentCreateBodyMandateDataObj0, str]
    ] = pydantic.Field(alias="mandate_data", default=None)
    metadata: typing.Optional[_SerializerPaymentIntentCreateBodyMetadata] = (
        pydantic.Field(alias="metadata", default=None)
    )
    off_session: typing.Optional[
        typing.Union[bool, typing_extensions.Literal["one_off", "recurring"]]
    ] = pydantic.Field(alias="off_session", default=None)
    on_behalf_of: typing.Optional[str] = pydantic.Field(
        alias="on_behalf_of", default=None
    )
    payment_method: typing.Optional[str] = pydantic.Field(
        alias="payment_method", default=None
    )
    payment_method_configuration: typing.Optional[str] = pydantic.Field(
        alias="payment_method_configuration", default=None
    )
    payment_method_data: typing.Optional[
        _SerializerPaymentIntentCreateBodyPaymentMethodData
    ] = pydantic.Field(alias="payment_method_data", default=None)
    payment_method_options: typing.Optional[
        _SerializerPaymentIntentCreateBodyPaymentMethodOptions
    ] = pydantic.Field(alias="payment_method_options", default=None)
    payment_method_types: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="payment_method_types", default=None
    )
    radar_options: typing.Optional[_SerializerPaymentIntentCreateBodyRadarOptions] = (
        pydantic.Field(alias="radar_options", default=None)
    )
    receipt_email: typing.Optional[str] = pydantic.Field(
        alias="receipt_email", default=None
    )
    return_url: typing.Optional[str] = pydantic.Field(alias="return_url", default=None)
    setup_future_usage: typing.Optional[
        typing_extensions.Literal["off_session", "on_session"]
    ] = pydantic.Field(alias="setup_future_usage", default=None)
    shipping: typing.Optional[_SerializerPaymentIntentCreateBodyShipping] = (
        pydantic.Field(alias="shipping", default=None)
    )
    statement_descriptor: typing.Optional[str] = pydantic.Field(
        alias="statement_descriptor", default=None
    )
    statement_descriptor_suffix: typing.Optional[str] = pydantic.Field(
        alias="statement_descriptor_suffix", default=None
    )
    transfer_data: typing.Optional[_SerializerPaymentIntentCreateBodyTransferData] = (
        pydantic.Field(alias="transfer_data", default=None)
    )
    transfer_group: typing.Optional[str] = pydantic.Field(
        alias="transfer_group", default=None
    )
    use_stripe_sdk: typing.Optional[bool] = pydantic.Field(
        alias="use_stripe_sdk", default=None
    )
