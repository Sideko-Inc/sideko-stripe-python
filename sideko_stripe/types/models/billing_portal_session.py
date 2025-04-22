import pydantic
import typing
import typing_extensions

from .billing_portal_configuration import BillingPortalConfiguration
from .portal_flows_flow import PortalFlowsFlow


class BillingPortalSession(pydantic.BaseModel):
    """
    The Billing customer portal is a Stripe-hosted UI for subscription and
    billing management.

    A portal configuration describes the functionality and features that you
    want to provide to your customers through the portal.

    A portal session describes the instantiation of the customer portal for
    a particular customer. By visiting the session's URL, the customer
    can manage their subscriptions and billing details. For security reasons,
    sessions are short-lived and will expire if the customer does not visit the URL.
    Create sessions on-demand when customers intend to manage their subscriptions
    and billing details.

    Related guide: [Customer management](/customer-management)
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    configuration: typing.Union[str, BillingPortalConfiguration] = pydantic.Field(
        alias="configuration",
    )
    """
    The configuration used by this session, describing the features available.
    """
    created: int = pydantic.Field(
        alias="created",
    )
    """
    Time at which the object was created. Measured in seconds since the Unix epoch.
    """
    customer: str = pydantic.Field(
        alias="customer",
    )
    """
    The ID of the customer for this session.
    """
    flow: typing.Optional[PortalFlowsFlow] = pydantic.Field(alias="flow", default=None)
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
    locale: typing.Optional[
        typing_extensions.Literal[
            "auto",
            "bg",
            "cs",
            "da",
            "de",
            "el",
            "en",
            "en-AU",
            "en-CA",
            "en-GB",
            "en-IE",
            "en-IN",
            "en-NZ",
            "en-SG",
            "es",
            "es-419",
            "et",
            "fi",
            "fil",
            "fr",
            "fr-CA",
            "hr",
            "hu",
            "id",
            "it",
            "ja",
            "ko",
            "lt",
            "lv",
            "ms",
            "mt",
            "nb",
            "nl",
            "pl",
            "pt",
            "pt-BR",
            "ro",
            "ru",
            "sk",
            "sl",
            "sv",
            "th",
            "tr",
            "vi",
            "zh",
            "zh-HK",
            "zh-TW",
        ]
    ] = pydantic.Field(alias="locale", default=None)
    """
    The IETF language tag of the locale Customer Portal is displayed in. If blank or auto, the customer’s `preferred_locales` or browser’s locale is used.
    """
    object: typing_extensions.Literal["billing_portal.session"] = pydantic.Field(
        alias="object",
    )
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    on_behalf_of: typing.Optional[str] = pydantic.Field(
        alias="on_behalf_of", default=None
    )
    """
    The account for which the session was created on behalf of. When specified, only subscriptions and invoices with this `on_behalf_of` account appear in the portal. For more information, see the [docs](https://stripe.com/docs/connect/separate-charges-and-transfers#settlement-merchant). Use the [Accounts API](https://stripe.com/docs/api/accounts/object#account_object-settings-branding) to modify the `on_behalf_of` account's branding settings, which the portal displays.
    """
    return_url: typing.Optional[str] = pydantic.Field(alias="return_url", default=None)
    """
    The URL to redirect customers to when they click on the portal's link to return to your website.
    """
    url: str = pydantic.Field(
        alias="url",
    )
    """
    The short-lived URL of the session that gives customers access to the customer portal.
    """
