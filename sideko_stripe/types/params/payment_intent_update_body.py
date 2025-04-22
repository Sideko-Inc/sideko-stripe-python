import pydantic
import typing
import typing_extensions

from .payment_intent_update_body_metadata_obj0 import (
    PaymentIntentUpdateBodyMetadataObj0,
    _SerializerPaymentIntentUpdateBodyMetadataObj0,
)
from .payment_intent_update_body_payment_method_data import (
    PaymentIntentUpdateBodyPaymentMethodData,
    _SerializerPaymentIntentUpdateBodyPaymentMethodData,
)
from .payment_intent_update_body_payment_method_options import (
    PaymentIntentUpdateBodyPaymentMethodOptions,
    _SerializerPaymentIntentUpdateBodyPaymentMethodOptions,
)
from .payment_intent_update_body_shipping_obj0 import (
    PaymentIntentUpdateBodyShippingObj0,
    _SerializerPaymentIntentUpdateBodyShippingObj0,
)
from .payment_intent_update_body_transfer_data import (
    PaymentIntentUpdateBodyTransferData,
    _SerializerPaymentIntentUpdateBodyTransferData,
)


class PaymentIntentUpdateBody(typing_extensions.TypedDict, total=False):
    """
    PaymentIntentUpdateBody
    """

    amount: typing_extensions.NotRequired[int]
    """
    Amount intended to be collected by this PaymentIntent. A positive integer representing how much to charge in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal) (e.g., 100 cents to charge $1.00 or 100 to charge ¥100, a zero-decimal currency). The minimum amount is $0.50 US or [equivalent in charge currency](https://stripe.com/docs/currencies#minimum-and-maximum-charge-amounts). The amount value supports up to eight digits (e.g., a value of 99999999 for a USD charge of $999,999.99).
    """

    application_fee_amount: typing_extensions.NotRequired[typing.Union[int, str]]
    """
    The amount of the application fee (if any) that will be requested to be applied to the payment and transferred to the application owner's Stripe account. The amount of the application fee collected will be capped at the total amount captured. For more information, see the PaymentIntents [use case for connected accounts](https://stripe.com/docs/payments/connected-accounts).
    """

    capture_method: typing_extensions.NotRequired[
        typing_extensions.Literal["automatic", "automatic_async", "manual"]
    ]
    """
    Controls when the funds will be captured from the customer's account.
    """

    currency: typing_extensions.NotRequired[str]
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

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """

    metadata: typing_extensions.NotRequired[
        typing.Union[PaymentIntentUpdateBodyMetadataObj0, str]
    ]
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    """

    payment_method: typing_extensions.NotRequired[str]
    """
    ID of the payment method (a PaymentMethod, Card, or [compatible Source](https://stripe.com/docs/payments/payment-methods/transitioning#compatibility) object) to attach to this PaymentIntent. To unset this field to null, pass in an empty string.
    """

    payment_method_configuration: typing_extensions.NotRequired[str]
    """
    The ID of the [payment method configuration](https://stripe.com/docs/api/payment_method_configurations) to use with this PaymentIntent.
    """

    payment_method_data: typing_extensions.NotRequired[
        PaymentIntentUpdateBodyPaymentMethodData
    ]
    """
    If provided, this hash will be used to create a PaymentMethod. The new PaymentMethod will appear
    in the [payment_method](https://stripe.com/docs/api/payment_intents/object#payment_intent_object-payment_method)
    property on the PaymentIntent.
    """

    payment_method_options: typing_extensions.NotRequired[
        PaymentIntentUpdateBodyPaymentMethodOptions
    ]
    """
    Payment-method-specific configuration for this PaymentIntent.
    """

    payment_method_types: typing_extensions.NotRequired[typing.List[str]]
    """
    The list of payment method types (for example, card) that this PaymentIntent can use. Use `automatic_payment_methods` to manage payment methods from the [Stripe Dashboard](https://dashboard.stripe.com/settings/payment_methods).
    """

    receipt_email: typing_extensions.NotRequired[typing.Union[str, str]]
    """
    Email address that the receipt for the resulting payment will be sent to. If `receipt_email` is specified for a payment in live mode, a receipt will be sent regardless of your [email settings](https://dashboard.stripe.com/account/emails).
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
        typing.Union[PaymentIntentUpdateBodyShippingObj0, str]
    ]
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

    transfer_data: typing_extensions.NotRequired[PaymentIntentUpdateBodyTransferData]
    """
    Use this parameter to automatically create a Transfer when the payment succeeds. Learn more about the [use case for connected accounts](https://stripe.com/docs/payments/connected-accounts).
    """

    transfer_group: typing_extensions.NotRequired[str]
    """
    A string that identifies the resulting payment as part of a group. You can only provide `transfer_group` if it hasn't been set. Learn more about the [use case for connected accounts](https://stripe.com/docs/payments/connected-accounts).
    """


class _SerializerPaymentIntentUpdateBody(pydantic.BaseModel):
    """
    Serializer for PaymentIntentUpdateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    amount: typing.Optional[int] = pydantic.Field(alias="amount", default=None)
    application_fee_amount: typing.Optional[typing.Union[int, str]] = pydantic.Field(
        alias="application_fee_amount", default=None
    )
    capture_method: typing.Optional[
        typing_extensions.Literal["automatic", "automatic_async", "manual"]
    ] = pydantic.Field(alias="capture_method", default=None)
    currency: typing.Optional[str] = pydantic.Field(alias="currency", default=None)
    customer: typing.Optional[str] = pydantic.Field(alias="customer", default=None)
    description: typing.Optional[str] = pydantic.Field(
        alias="description", default=None
    )
    expand: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="expand", default=None
    )
    metadata: typing.Optional[
        typing.Union[_SerializerPaymentIntentUpdateBodyMetadataObj0, str]
    ] = pydantic.Field(alias="metadata", default=None)
    payment_method: typing.Optional[str] = pydantic.Field(
        alias="payment_method", default=None
    )
    payment_method_configuration: typing.Optional[str] = pydantic.Field(
        alias="payment_method_configuration", default=None
    )
    payment_method_data: typing.Optional[
        _SerializerPaymentIntentUpdateBodyPaymentMethodData
    ] = pydantic.Field(alias="payment_method_data", default=None)
    payment_method_options: typing.Optional[
        _SerializerPaymentIntentUpdateBodyPaymentMethodOptions
    ] = pydantic.Field(alias="payment_method_options", default=None)
    payment_method_types: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="payment_method_types", default=None
    )
    receipt_email: typing.Optional[typing.Union[str, str]] = pydantic.Field(
        alias="receipt_email", default=None
    )
    setup_future_usage: typing.Optional[
        typing_extensions.Literal["off_session", "on_session"]
    ] = pydantic.Field(alias="setup_future_usage", default=None)
    shipping: typing.Optional[
        typing.Union[_SerializerPaymentIntentUpdateBodyShippingObj0, str]
    ] = pydantic.Field(alias="shipping", default=None)
    statement_descriptor: typing.Optional[str] = pydantic.Field(
        alias="statement_descriptor", default=None
    )
    statement_descriptor_suffix: typing.Optional[str] = pydantic.Field(
        alias="statement_descriptor_suffix", default=None
    )
    transfer_data: typing.Optional[_SerializerPaymentIntentUpdateBodyTransferData] = (
        pydantic.Field(alias="transfer_data", default=None)
    )
    transfer_group: typing.Optional[str] = pydantic.Field(
        alias="transfer_group", default=None
    )
