import pydantic
import typing
import typing_extensions

from .setup_intent_create_body_automatic_payment_methods import (
    SetupIntentCreateBodyAutomaticPaymentMethods,
    _SerializerSetupIntentCreateBodyAutomaticPaymentMethods,
)
from .setup_intent_create_body_mandate_data_obj0 import (
    SetupIntentCreateBodyMandateDataObj0,
    _SerializerSetupIntentCreateBodyMandateDataObj0,
)
from .setup_intent_create_body_metadata import (
    SetupIntentCreateBodyMetadata,
    _SerializerSetupIntentCreateBodyMetadata,
)
from .setup_intent_create_body_payment_method_data import (
    SetupIntentCreateBodyPaymentMethodData,
    _SerializerSetupIntentCreateBodyPaymentMethodData,
)
from .setup_intent_create_body_payment_method_options import (
    SetupIntentCreateBodyPaymentMethodOptions,
    _SerializerSetupIntentCreateBodyPaymentMethodOptions,
)
from .setup_intent_create_body_single_use import (
    SetupIntentCreateBodySingleUse,
    _SerializerSetupIntentCreateBodySingleUse,
)


class SetupIntentCreateBody(typing_extensions.TypedDict, total=False):
    """
    SetupIntentCreateBody
    """

    attach_to_self: typing_extensions.NotRequired[bool]
    """
    If present, the SetupIntent's payment method will be attached to the in-context Stripe Account.
    
    It can only be used for this Stripe Account’s own money movement flows like InboundTransfer and OutboundTransfers. It cannot be set to true when setting up a PaymentMethod for a Customer, and defaults to false when attaching a PaymentMethod to a Customer.
    """

    automatic_payment_methods: typing_extensions.NotRequired[
        SetupIntentCreateBodyAutomaticPaymentMethods
    ]
    """
    When you enable this parameter, this SetupIntent accepts payment methods that you enable in the Dashboard and that are compatible with its other parameters.
    """

    confirm: typing_extensions.NotRequired[bool]
    """
    Set to `true` to attempt to confirm this SetupIntent immediately. This parameter defaults to `false`. If a card is the attached payment method, you can provide a `return_url` in case further authentication is necessary.
    """

    confirmation_token: typing_extensions.NotRequired[str]
    """
    ID of the ConfirmationToken used to confirm this SetupIntent.
    
    If the provided ConfirmationToken contains properties that are also being provided in this request, such as `payment_method`, then the values in this request will take precedence.
    """

    customer: typing_extensions.NotRequired[str]
    """
    ID of the Customer this SetupIntent belongs to, if one exists.
    
    If present, the SetupIntent's payment method will be attached to the Customer on successful setup. Payment methods attached to other Customers cannot be used with this SetupIntent.
    """

    description: typing_extensions.NotRequired[str]
    """
    An arbitrary string attached to the object. Often useful for displaying to users.
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """

    flow_directions: typing_extensions.NotRequired[
        typing.List[typing_extensions.Literal["inbound", "outbound"]]
    ]
    """
    Indicates the directions of money movement for which this payment method is intended to be used.
    
    Include `inbound` if you intend to use the payment method as the origin to pull funds from. Include `outbound` if you intend to use the payment method as the destination to send funds to. You can include both if you intend to use the payment method for both purposes.
    """

    mandate_data: typing_extensions.NotRequired[
        typing.Union[SetupIntentCreateBodyMandateDataObj0, str]
    ]
    """
    This hash contains details about the mandate to create. This parameter can only be used with [`confirm=true`](https://stripe.com/docs/api/setup_intents/create#create_setup_intent-confirm).
    """

    metadata: typing_extensions.NotRequired[SetupIntentCreateBodyMetadata]
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    """

    on_behalf_of: typing_extensions.NotRequired[str]
    """
    The Stripe account ID created for this SetupIntent.
    """

    payment_method: typing_extensions.NotRequired[str]
    """
    ID of the payment method (a PaymentMethod, Card, or saved Source object) to attach to this SetupIntent.
    """

    payment_method_configuration: typing_extensions.NotRequired[str]
    """
    The ID of the [payment method configuration](https://stripe.com/docs/api/payment_method_configurations) to use with this SetupIntent.
    """

    payment_method_data: typing_extensions.NotRequired[
        SetupIntentCreateBodyPaymentMethodData
    ]
    """
    When included, this hash creates a PaymentMethod that is set as the [`payment_method`](https://stripe.com/docs/api/setup_intents/object#setup_intent_object-payment_method)
    value in the SetupIntent.
    """

    payment_method_options: typing_extensions.NotRequired[
        SetupIntentCreateBodyPaymentMethodOptions
    ]
    """
    Payment method-specific configuration for this SetupIntent.
    """

    payment_method_types: typing_extensions.NotRequired[typing.List[str]]
    """
    The list of payment method types (for example, card) that this SetupIntent can use. If you don't provide this, Stripe will dynamically show relevant payment methods from your [payment method settings](https://dashboard.stripe.com/settings/payment_methods).
    """

    return_url: typing_extensions.NotRequired[str]
    """
    The URL to redirect your customer back to after they authenticate or cancel their payment on the payment method's app or site. To redirect to a mobile application, you can alternatively supply an application URI scheme. This parameter can only be used with [`confirm=true`](https://stripe.com/docs/api/setup_intents/create#create_setup_intent-confirm).
    """

    single_use: typing_extensions.NotRequired[SetupIntentCreateBodySingleUse]
    """
    If you populate this hash, this SetupIntent generates a `single_use` mandate after successful completion.
    
    Single-use mandates are only valid for the following payment methods: `acss_debit`, `alipay`, `au_becs_debit`, `bacs_debit`, `bancontact`, `boleto`, `ideal`, `link`, `sepa_debit`, and `us_bank_account`.
    """

    usage: typing_extensions.NotRequired[
        typing_extensions.Literal["off_session", "on_session"]
    ]
    """
    Indicates how the payment method is intended to be used in the future. If not provided, this value defaults to `off_session`.
    """

    use_stripe_sdk: typing_extensions.NotRequired[bool]
    """
    Set to `true` when confirming server-side and using Stripe.js, iOS, or Android client-side SDKs to handle the next actions.
    """


class _SerializerSetupIntentCreateBody(pydantic.BaseModel):
    """
    Serializer for SetupIntentCreateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    attach_to_self: typing.Optional[bool] = pydantic.Field(
        alias="attach_to_self", default=None
    )
    automatic_payment_methods: typing.Optional[
        _SerializerSetupIntentCreateBodyAutomaticPaymentMethods
    ] = pydantic.Field(alias="automatic_payment_methods", default=None)
    confirm: typing.Optional[bool] = pydantic.Field(alias="confirm", default=None)
    confirmation_token: typing.Optional[str] = pydantic.Field(
        alias="confirmation_token", default=None
    )
    customer: typing.Optional[str] = pydantic.Field(alias="customer", default=None)
    description: typing.Optional[str] = pydantic.Field(
        alias="description", default=None
    )
    expand: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="expand", default=None
    )
    flow_directions: typing.Optional[
        typing.List[typing_extensions.Literal["inbound", "outbound"]]
    ] = pydantic.Field(alias="flow_directions", default=None)
    mandate_data: typing.Optional[
        typing.Union[_SerializerSetupIntentCreateBodyMandateDataObj0, str]
    ] = pydantic.Field(alias="mandate_data", default=None)
    metadata: typing.Optional[_SerializerSetupIntentCreateBodyMetadata] = (
        pydantic.Field(alias="metadata", default=None)
    )
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
        _SerializerSetupIntentCreateBodyPaymentMethodData
    ] = pydantic.Field(alias="payment_method_data", default=None)
    payment_method_options: typing.Optional[
        _SerializerSetupIntentCreateBodyPaymentMethodOptions
    ] = pydantic.Field(alias="payment_method_options", default=None)
    payment_method_types: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="payment_method_types", default=None
    )
    return_url: typing.Optional[str] = pydantic.Field(alias="return_url", default=None)
    single_use: typing.Optional[_SerializerSetupIntentCreateBodySingleUse] = (
        pydantic.Field(alias="single_use", default=None)
    )
    usage: typing.Optional[typing_extensions.Literal["off_session", "on_session"]] = (
        pydantic.Field(alias="usage", default=None)
    )
    use_stripe_sdk: typing.Optional[bool] = pydantic.Field(
        alias="use_stripe_sdk", default=None
    )
