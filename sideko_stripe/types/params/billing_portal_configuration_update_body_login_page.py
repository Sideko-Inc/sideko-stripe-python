import pydantic
import typing_extensions


class BillingPortalConfigurationUpdateBodyLoginPage(typing_extensions.TypedDict):
    """
    The hosted login page for this configuration. Learn more about the portal login page in our [integration docs](https://stripe.com/docs/billing/subscriptions/integrating-customer-portal#share).
    """

    enabled: typing_extensions.Required[bool]


class _SerializerBillingPortalConfigurationUpdateBodyLoginPage(pydantic.BaseModel):
    """
    Serializer for BillingPortalConfigurationUpdateBodyLoginPage handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    enabled: bool = pydantic.Field(
        alias="enabled",
    )
