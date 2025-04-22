import pydantic
import typing
import typing_extensions

from .application import Application
from .billing_portal_configuration_metadata import BillingPortalConfigurationMetadata
from .deleted_application import DeletedApplication
from .portal_business_profile import PortalBusinessProfile
from .portal_features import PortalFeatures
from .portal_login_page import PortalLoginPage


class BillingPortalConfiguration(pydantic.BaseModel):
    """
    A portal configuration describes the functionality and behavior of a portal session.
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    active: bool = pydantic.Field(
        alias="active",
    )
    """
    Whether the configuration is active and can be used to create portal sessions.
    """
    application: typing.Optional[typing.Union[str, Application, DeletedApplication]] = (
        pydantic.Field(alias="application", default=None)
    )
    """
    ID of the Connect Application that created the configuration.
    """
    business_profile: PortalBusinessProfile = pydantic.Field(
        alias="business_profile",
    )
    created: int = pydantic.Field(
        alias="created",
    )
    """
    Time at which the object was created. Measured in seconds since the Unix epoch.
    """
    default_return_url: typing.Optional[str] = pydantic.Field(
        alias="default_return_url", default=None
    )
    """
    The default URL to redirect customers to when they click on the portal's link to return to your website. This can be [overriden](https://stripe.com/docs/api/customer_portal/sessions/create#create_portal_session-return_url) when creating the session.
    """
    features: PortalFeatures = pydantic.Field(
        alias="features",
    )
    id: str = pydantic.Field(
        alias="id",
    )
    """
    Unique identifier for the object.
    """
    is_default: bool = pydantic.Field(
        alias="is_default",
    )
    """
    Whether the configuration is the default. If `true`, this configuration can be managed in the Dashboard and portal sessions will use this configuration unless it is overriden when creating the session.
    """
    livemode: bool = pydantic.Field(
        alias="livemode",
    )
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    login_page: PortalLoginPage = pydantic.Field(
        alias="login_page",
    )
    metadata: typing.Optional[BillingPortalConfigurationMetadata] = pydantic.Field(
        alias="metadata", default=None
    )
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    object: typing_extensions.Literal["billing_portal.configuration"] = pydantic.Field(
        alias="object",
    )
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    updated: int = pydantic.Field(
        alias="updated",
    )
    """
    Time at which the object was last updated. Measured in seconds since the Unix epoch.
    """
