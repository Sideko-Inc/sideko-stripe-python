import pydantic
import typing
import typing_extensions

from .billing_portal_session_create_body_flow_data import (
    BillingPortalSessionCreateBodyFlowData,
    _SerializerBillingPortalSessionCreateBodyFlowData,
)


class BillingPortalSessionCreateBody(typing_extensions.TypedDict, total=False):
    """
    BillingPortalSessionCreateBody
    """

    configuration: typing_extensions.NotRequired[str]
    """
    The ID of an existing [configuration](https://stripe.com/docs/api/customer_portal/configuration) to use for this session, describing its functionality and features. If not specified, the session uses the default configuration.
    """

    customer: typing_extensions.Required[str]
    """
    The ID of an existing customer.
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """

    flow_data: typing_extensions.NotRequired[BillingPortalSessionCreateBodyFlowData]
    """
    Information about a specific flow for the customer to go through. See the [docs](https://stripe.com/docs/customer-management/portal-deep-links) to learn more about using customer portal deep links and flows.
    """

    locale: typing_extensions.NotRequired[
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
    ]
    """
    The IETF language tag of the locale customer portal is displayed in. If blank or auto, the customer’s `preferred_locales` or browser’s locale is used.
    """

    on_behalf_of: typing_extensions.NotRequired[str]
    """
    The `on_behalf_of` account to use for this session. When specified, only subscriptions and invoices with this `on_behalf_of` account appear in the portal. For more information, see the [docs](https://stripe.com/docs/connect/separate-charges-and-transfers#settlement-merchant). Use the [Accounts API](https://stripe.com/docs/api/accounts/object#account_object-settings-branding) to modify the `on_behalf_of` account's branding settings, which the portal displays.
    """

    return_url: typing_extensions.NotRequired[str]
    """
    The default URL to redirect customers to when they click on the portal's link to return to your website.
    """


class _SerializerBillingPortalSessionCreateBody(pydantic.BaseModel):
    """
    Serializer for BillingPortalSessionCreateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    configuration: typing.Optional[str] = pydantic.Field(
        alias="configuration", default=None
    )
    customer: str = pydantic.Field(
        alias="customer",
    )
    expand: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="expand", default=None
    )
    flow_data: typing.Optional[_SerializerBillingPortalSessionCreateBodyFlowData] = (
        pydantic.Field(alias="flow_data", default=None)
    )
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
    on_behalf_of: typing.Optional[str] = pydantic.Field(
        alias="on_behalf_of", default=None
    )
    return_url: typing.Optional[str] = pydantic.Field(alias="return_url", default=None)
