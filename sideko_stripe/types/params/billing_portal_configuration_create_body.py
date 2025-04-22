import pydantic
import typing
import typing_extensions

from .billing_portal_configuration_create_body_business_profile import (
    BillingPortalConfigurationCreateBodyBusinessProfile,
    _SerializerBillingPortalConfigurationCreateBodyBusinessProfile,
)
from .billing_portal_configuration_create_body_features import (
    BillingPortalConfigurationCreateBodyFeatures,
    _SerializerBillingPortalConfigurationCreateBodyFeatures,
)
from .billing_portal_configuration_create_body_login_page import (
    BillingPortalConfigurationCreateBodyLoginPage,
    _SerializerBillingPortalConfigurationCreateBodyLoginPage,
)
from .billing_portal_configuration_create_body_metadata import (
    BillingPortalConfigurationCreateBodyMetadata,
    _SerializerBillingPortalConfigurationCreateBodyMetadata,
)


class BillingPortalConfigurationCreateBody(typing_extensions.TypedDict, total=False):
    """
    BillingPortalConfigurationCreateBody
    """

    business_profile: typing_extensions.NotRequired[
        BillingPortalConfigurationCreateBodyBusinessProfile
    ]
    """
    The business information shown to customers in the portal.
    """

    default_return_url: typing_extensions.NotRequired[typing.Union[str, str]]
    """
    The default URL to redirect customers to when they click on the portal's link to return to your website. This can be [overriden](https://stripe.com/docs/api/customer_portal/sessions/create#create_portal_session-return_url) when creating the session.
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """

    features: typing_extensions.Required[BillingPortalConfigurationCreateBodyFeatures]
    """
    Information about the features available in the portal.
    """

    login_page: typing_extensions.NotRequired[
        BillingPortalConfigurationCreateBodyLoginPage
    ]
    """
    The hosted login page for this configuration. Learn more about the portal login page in our [integration docs](https://stripe.com/docs/billing/subscriptions/integrating-customer-portal#share).
    """

    metadata: typing_extensions.NotRequired[
        BillingPortalConfigurationCreateBodyMetadata
    ]
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    """


class _SerializerBillingPortalConfigurationCreateBody(pydantic.BaseModel):
    """
    Serializer for BillingPortalConfigurationCreateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    business_profile: typing.Optional[
        _SerializerBillingPortalConfigurationCreateBodyBusinessProfile
    ] = pydantic.Field(alias="business_profile", default=None)
    default_return_url: typing.Optional[typing.Union[str, str]] = pydantic.Field(
        alias="default_return_url", default=None
    )
    expand: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="expand", default=None
    )
    features: _SerializerBillingPortalConfigurationCreateBodyFeatures = pydantic.Field(
        alias="features",
    )
    login_page: typing.Optional[
        _SerializerBillingPortalConfigurationCreateBodyLoginPage
    ] = pydantic.Field(alias="login_page", default=None)
    metadata: typing.Optional[
        _SerializerBillingPortalConfigurationCreateBodyMetadata
    ] = pydantic.Field(alias="metadata", default=None)
