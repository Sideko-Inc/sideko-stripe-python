import pydantic
import typing
import typing_extensions

from .application import Application
from .deleted_customer import DeletedCustomer

if typing_extensions.TYPE_CHECKING:
    from .account import Account
    from .api_errors import ApiErrors
    from .customer import Customer
    from .payment_method import PaymentMethod
    from .setup_attempt_payment_method_details import SetupAttemptPaymentMethodDetails
    from .setup_intent import SetupIntent


class SetupAttempt(pydantic.BaseModel):
    """
    A SetupAttempt describes one attempted confirmation of a SetupIntent,
    whether that confirmation is successful or unsuccessful. You can use
    SetupAttempts to inspect details of a specific attempt at setting up a
    payment method using a SetupIntent.
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    application: typing.Optional[typing.Union[str, Application]] = pydantic.Field(
        alias="application", default=None
    )
    """
    The value of [application](https://stripe.com/docs/api/setup_intents/object#setup_intent_object-application) on the SetupIntent at the time of this confirmation.
    """
    attach_to_self: typing.Optional[bool] = pydantic.Field(
        alias="attach_to_self", default=None
    )
    """
    If present, the SetupIntent's payment method will be attached to the in-context Stripe Account.
    
    It can only be used for this Stripe Account’s own money movement flows like InboundTransfer and OutboundTransfers. It cannot be set to true when setting up a PaymentMethod for a Customer, and defaults to false when attaching a PaymentMethod to a Customer.
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
    The value of [customer](https://stripe.com/docs/api/setup_intents/object#setup_intent_object-customer) on the SetupIntent at the time of this confirmation.
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
    livemode: bool = pydantic.Field(
        alias="livemode",
    )
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    object: typing_extensions.Literal["setup_attempt"] = pydantic.Field(
        alias="object",
    )
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    on_behalf_of: typing.Optional[typing.Union[str, "Account"]] = pydantic.Field(
        alias="on_behalf_of", default=None
    )
    """
    The value of [on_behalf_of](https://stripe.com/docs/api/setup_intents/object#setup_intent_object-on_behalf_of) on the SetupIntent at the time of this confirmation.
    """
    payment_method: typing.Union[str, "PaymentMethod"] = pydantic.Field(
        alias="payment_method",
    )
    """
    ID of the payment method used with this SetupAttempt.
    """
    payment_method_details: "SetupAttemptPaymentMethodDetails" = pydantic.Field(
        alias="payment_method_details",
    )
    setup_error: typing.Optional["ApiErrors"] = pydantic.Field(
        alias="setup_error", default=None
    )
    setup_intent: typing.Union[str, "SetupIntent"] = pydantic.Field(
        alias="setup_intent",
    )
    """
    ID of the SetupIntent that this attempt belongs to.
    """
    status: str = pydantic.Field(
        alias="status",
    )
    """
    Status of this SetupAttempt, one of `requires_confirmation`, `requires_action`, `processing`, `succeeded`, `failed`, or `abandoned`.
    """
    usage: str = pydantic.Field(
        alias="usage",
    )
    """
    The value of [usage](https://stripe.com/docs/api/setup_intents/object#setup_intent_object-usage) on the SetupIntent at the time of this confirmation, one of `off_session` or `on_session`.
    """
