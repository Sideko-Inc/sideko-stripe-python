import pydantic
import typing
import typing_extensions

from .application import Application
from .deleted_customer import DeletedCustomer
from .payment_flows_automatic_payment_methods_setup_intent import (
    PaymentFlowsAutomaticPaymentMethodsSetupIntent,
)
from .payment_method_config_biz_payment_method_configuration_details import (
    PaymentMethodConfigBizPaymentMethodConfigurationDetails,
)
from .setup_intent_metadata import SetupIntentMetadata
from .setup_intent_next_action import SetupIntentNextAction
from .setup_intent_payment_method_options import SetupIntentPaymentMethodOptions

if typing_extensions.TYPE_CHECKING:
    from .account import Account
    from .api_errors import ApiErrors
    from .customer import Customer
    from .mandate import Mandate
    from .payment_method import PaymentMethod
    from .setup_attempt import SetupAttempt


class SetupIntent(pydantic.BaseModel):
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

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    application: typing.Optional[typing.Union[str, Application]] = pydantic.Field(
        alias="application", default=None
    )
    """
    ID of the Connect application that created the SetupIntent.
    """
    attach_to_self: typing.Optional[bool] = pydantic.Field(
        alias="attach_to_self", default=None
    )
    """
    If present, the SetupIntent's payment method will be attached to the in-context Stripe Account.
    
    It can only be used for this Stripe Account’s own money movement flows like InboundTransfer and OutboundTransfers. It cannot be set to true when setting up a PaymentMethod for a Customer, and defaults to false when attaching a PaymentMethod to a Customer.
    """
    automatic_payment_methods: typing.Optional[
        PaymentFlowsAutomaticPaymentMethodsSetupIntent
    ] = pydantic.Field(alias="automatic_payment_methods", default=None)
    cancellation_reason: typing.Optional[
        typing_extensions.Literal["abandoned", "duplicate", "requested_by_customer"]
    ] = pydantic.Field(alias="cancellation_reason", default=None)
    """
    Reason for cancellation of this SetupIntent, one of `abandoned`, `requested_by_customer`, or `duplicate`.
    """
    client_secret: typing.Optional[str] = pydantic.Field(
        alias="client_secret", default=None
    )
    """
    The client secret of this SetupIntent. Used for client-side retrieval using a publishable key.
    
    The client secret can be used to complete payment setup from your frontend. It should not be stored, logged, or exposed to anyone other than the customer. Make sure that you have TLS enabled on any page that includes the client secret.
    """
    created: int = pydantic.Field(
        alias="created",
    )
    """
    Time at which the object was created. Measured in seconds since the Unix epoch.
    """
    customer: typing.Optional[typing.Union[str, "Customer", DeletedCustomer]] = (
        pydantic.Field(alias="customer", default=None)
    )
    """
    ID of the Customer this SetupIntent belongs to, if one exists.
    
    If present, the SetupIntent's payment method will be attached to the Customer on successful setup. Payment methods attached to other Customers cannot be used with this SetupIntent.
    """
    description: typing.Optional[str] = pydantic.Field(
        alias="description", default=None
    )
    """
    An arbitrary string attached to the object. Often useful for displaying to users.
    """
    flow_directions: typing.Optional[
        typing.List[typing_extensions.Literal["inbound", "outbound"]]
    ] = pydantic.Field(alias="flow_directions", default=None)
    """
    Indicates the directions of money movement for which this payment method is intended to be used.
    
    Include `inbound` if you intend to use the payment method as the origin to pull funds from. Include `outbound` if you intend to use the payment method as the destination to send funds to. You can include both if you intend to use the payment method for both purposes.
    """
    id: str = pydantic.Field(
        alias="id",
    )
    """
    Unique identifier for the object.
    """
    last_setup_error: typing.Optional["ApiErrors"] = pydantic.Field(
        alias="last_setup_error", default=None
    )
    latest_attempt: typing.Optional[typing.Union[str, "SetupAttempt"]] = pydantic.Field(
        alias="latest_attempt", default=None
    )
    """
    The most recent SetupAttempt for this SetupIntent.
    """
    livemode: bool = pydantic.Field(
        alias="livemode",
    )
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    mandate: typing.Optional[typing.Union[str, "Mandate"]] = pydantic.Field(
        alias="mandate", default=None
    )
    """
    ID of the multi use Mandate generated by the SetupIntent.
    """
    metadata: typing.Optional[SetupIntentMetadata] = pydantic.Field(
        alias="metadata", default=None
    )
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    next_action: typing.Optional[SetupIntentNextAction] = pydantic.Field(
        alias="next_action", default=None
    )
    object: typing_extensions.Literal["setup_intent"] = pydantic.Field(
        alias="object",
    )
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    on_behalf_of: typing.Optional[typing.Union[str, "Account"]] = pydantic.Field(
        alias="on_behalf_of", default=None
    )
    """
    The account (if any) for which the setup is intended.
    """
    payment_method: typing.Optional[typing.Union[str, "PaymentMethod"]] = (
        pydantic.Field(alias="payment_method", default=None)
    )
    """
    ID of the payment method used with this SetupIntent. If the payment method is `card_present` and isn't a digital wallet, then the [generated_card](https://docs.stripe.com/api/setup_attempts/object#setup_attempt_object-payment_method_details-card_present-generated_card) associated with the `latest_attempt` is attached to the Customer instead.
    """
    payment_method_configuration_details: typing.Optional[
        PaymentMethodConfigBizPaymentMethodConfigurationDetails
    ] = pydantic.Field(alias="payment_method_configuration_details", default=None)
    payment_method_options: typing.Optional[SetupIntentPaymentMethodOptions] = (
        pydantic.Field(alias="payment_method_options", default=None)
    )
    payment_method_types: typing.List[str] = pydantic.Field(
        alias="payment_method_types",
    )
    """
    The list of payment method types (e.g. card) that this SetupIntent is allowed to set up.
    """
    single_use_mandate: typing.Optional[typing.Union[str, "Mandate"]] = pydantic.Field(
        alias="single_use_mandate", default=None
    )
    """
    ID of the single_use Mandate generated by the SetupIntent.
    """
    status: typing_extensions.Literal[
        "canceled",
        "processing",
        "requires_action",
        "requires_confirmation",
        "requires_payment_method",
        "succeeded",
    ] = pydantic.Field(
        alias="status",
    )
    """
    [Status](https://stripe.com/docs/payments/intents#intent-statuses) of this SetupIntent, one of `requires_payment_method`, `requires_confirmation`, `requires_action`, `processing`, `canceled`, or `succeeded`.
    """
    usage: str = pydantic.Field(
        alias="usage",
    )
    """
    Indicates how the payment method is intended to be used in the future.
    
    Use `on_session` if you intend to only reuse the payment method when the customer is in your checkout flow. Use `off_session` if your customer may or may not be in your checkout flow. If not provided, this value defaults to `off_session`.
    """
