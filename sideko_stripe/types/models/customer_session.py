import pydantic
import typing
import typing_extensions

from .customer_session_resource_components import CustomerSessionResourceComponents

if typing_extensions.TYPE_CHECKING:
    from .customer import Customer


class CustomerSession(pydantic.BaseModel):
    """
    A Customer Session allows you to grant Stripe's frontend SDKs (like Stripe.js) client-side access
    control over a Customer.

    Related guides: [Customer Session with the Payment Element](/payments/accept-a-payment-deferred?platform=web&type=payment#save-payment-methods),
    [Customer Session with the Pricing Table](/payments/checkout/pricing-table#customer-session),
    [Customer Session with the Buy Button](/payment-links/buy-button#pass-an-existing-customer).
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    client_secret: str = pydantic.Field(
        alias="client_secret",
    )
    """
    The client secret of this Customer Session. Used on the client to set up secure access to the given `customer`.
    
    The client secret can be used to provide access to `customer` from your frontend. It should not be stored, logged, or exposed to anyone other than the relevant customer. Make sure that you have TLS enabled on any page that includes the client secret.
    """
    components: typing.Optional[CustomerSessionResourceComponents] = pydantic.Field(
        alias="components", default=None
    )
    """
    Configuration for the components supported by this Customer Session.
    """
    created: int = pydantic.Field(
        alias="created",
    )
    """
    Time at which the object was created. Measured in seconds since the Unix epoch.
    """
    customer: typing.Union[str, "Customer"] = pydantic.Field(
        alias="customer",
    )
    """
    The Customer the Customer Session was created for.
    """
    expires_at: int = pydantic.Field(
        alias="expires_at",
    )
    """
    The timestamp at which this Customer Session will expire.
    """
    livemode: bool = pydantic.Field(
        alias="livemode",
    )
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    object: typing_extensions.Literal["customer_session"] = pydantic.Field(
        alias="object",
    )
    """
    String representing the object's type. Objects of the same type share the same value.
    """
