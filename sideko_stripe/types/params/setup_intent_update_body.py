import pydantic
import typing
import typing_extensions

from .setup_intent_update_body_metadata_obj0 import (
    SetupIntentUpdateBodyMetadataObj0,
    _SerializerSetupIntentUpdateBodyMetadataObj0,
)
from .setup_intent_update_body_payment_method_data import (
    SetupIntentUpdateBodyPaymentMethodData,
    _SerializerSetupIntentUpdateBodyPaymentMethodData,
)
from .setup_intent_update_body_payment_method_options import (
    SetupIntentUpdateBodyPaymentMethodOptions,
    _SerializerSetupIntentUpdateBodyPaymentMethodOptions,
)


class SetupIntentUpdateBody(typing_extensions.TypedDict, total=False):
    """
    SetupIntentUpdateBody
    """

    attach_to_self: typing_extensions.NotRequired[bool]
    """
    If present, the SetupIntent's payment method will be attached to the in-context Stripe Account.
    
    It can only be used for this Stripe Account’s own money movement flows like InboundTransfer and OutboundTransfers. It cannot be set to true when setting up a PaymentMethod for a Customer, and defaults to false when attaching a PaymentMethod to a Customer.
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

    metadata: typing_extensions.NotRequired[
        typing.Union[SetupIntentUpdateBodyMetadataObj0, str]
    ]
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    """

    payment_method: typing_extensions.NotRequired[str]
    """
    ID of the payment method (a PaymentMethod, Card, or saved Source object) to attach to this SetupIntent. To unset this field to null, pass in an empty string.
    """

    payment_method_configuration: typing_extensions.NotRequired[str]
    """
    The ID of the [payment method configuration](https://stripe.com/docs/api/payment_method_configurations) to use with this SetupIntent.
    """

    payment_method_data: typing_extensions.NotRequired[
        SetupIntentUpdateBodyPaymentMethodData
    ]
    """
    When included, this hash creates a PaymentMethod that is set as the [`payment_method`](https://stripe.com/docs/api/setup_intents/object#setup_intent_object-payment_method)
    value in the SetupIntent.
    """

    payment_method_options: typing_extensions.NotRequired[
        SetupIntentUpdateBodyPaymentMethodOptions
    ]
    """
    Payment method-specific configuration for this SetupIntent.
    """

    payment_method_types: typing_extensions.NotRequired[typing.List[str]]
    """
    The list of payment method types (for example, card) that this SetupIntent can set up. If you don't provide this, Stripe will dynamically show relevant payment methods from your [payment method settings](https://dashboard.stripe.com/settings/payment_methods).
    """


class _SerializerSetupIntentUpdateBody(pydantic.BaseModel):
    """
    Serializer for SetupIntentUpdateBody handling case conversions
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
    metadata: typing.Optional[
        typing.Union[_SerializerSetupIntentUpdateBodyMetadataObj0, str]
    ] = pydantic.Field(alias="metadata", default=None)
    payment_method: typing.Optional[str] = pydantic.Field(
        alias="payment_method", default=None
    )
    payment_method_configuration: typing.Optional[str] = pydantic.Field(
        alias="payment_method_configuration", default=None
    )
    payment_method_data: typing.Optional[
        _SerializerSetupIntentUpdateBodyPaymentMethodData
    ] = pydantic.Field(alias="payment_method_data", default=None)
    payment_method_options: typing.Optional[
        _SerializerSetupIntentUpdateBodyPaymentMethodOptions
    ] = pydantic.Field(alias="payment_method_options", default=None)
    payment_method_types: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="payment_method_types", default=None
    )
