import typing
import typing_extensions

from sideko_stripe.core import (
    AsyncBaseClient,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
    to_form_urlencoded,
    type_utils,
)
from sideko_stripe.types import models, params


class SessionClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def create(
        self,
        *,
        customer: str,
        configuration: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        flow_data: typing.Union[
            typing.Optional[params.BillingPortalSessionCreateBodyFlowData],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        locale: typing.Union[
            typing.Optional[
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
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        on_behalf_of: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        return_url: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.BillingPortalSession:
        """
        Create a portal session

        <p>Creates a session of the customer portal.</p>

        POST /v1/billing_portal/sessions

        Args:
            configuration: The ID of an existing [configuration](https://stripe.com/docs/api/customer_portal/configuration) to use for this session, describing its functionality and features. If not specified, the session uses the default configuration.
            expand: Specifies which fields in the response should be expanded.
            flow_data: Information about a specific flow for the customer to go through. See the [docs](https://stripe.com/docs/customer-management/portal-deep-links) to learn more about using customer portal deep links and flows.
            locale: The IETF language tag of the locale customer portal is displayed in. If blank or auto, the customer’s `preferred_locales` or browser’s locale is used.
            on_behalf_of: The `on_behalf_of` account to use for this session. When specified, only subscriptions and invoices with this `on_behalf_of` account appear in the portal. For more information, see the [docs](https://stripe.com/docs/connect/separate-charges-and-transfers#settlement-merchant). Use the [Accounts API](https://stripe.com/docs/api/accounts/object#account_object-settings-branding) to modify the `on_behalf_of` account's branding settings, which the portal displays.
            return_url: The default URL to redirect customers to when they click on the portal's link to return to your website.
            customer: The ID of an existing customer.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.billing_portal.session.create(customer="string")
        ```
        """
        _data = to_form_urlencoded(
            item={
                "configuration": configuration,
                "expand": expand,
                "flow_data": flow_data,
                "locale": locale,
                "on_behalf_of": on_behalf_of,
                "return_url": return_url,
                "customer": customer,
            },
            dump_with=params._SerializerBillingPortalSessionCreateBody,
            style={
                "configuration": "form",
                "customer": "form",
                "expand": "deepObject",
                "flow_data": "deepObject",
                "locale": "form",
                "on_behalf_of": "form",
                "return_url": "form",
            },
            explode={
                "configuration": True,
                "customer": True,
                "expand": True,
                "flow_data": True,
                "locale": True,
                "on_behalf_of": True,
                "return_url": True,
            },
        )
        return self._base_client.request(
            method="POST",
            path="/v1/billing_portal/sessions",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.BillingPortalSession,
            request_options=request_options or default_request_options(),
        )


class AsyncSessionClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def create(
        self,
        *,
        customer: str,
        configuration: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        flow_data: typing.Union[
            typing.Optional[params.BillingPortalSessionCreateBodyFlowData],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        locale: typing.Union[
            typing.Optional[
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
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        on_behalf_of: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        return_url: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.BillingPortalSession:
        """
        Create a portal session

        <p>Creates a session of the customer portal.</p>

        POST /v1/billing_portal/sessions

        Args:
            configuration: The ID of an existing [configuration](https://stripe.com/docs/api/customer_portal/configuration) to use for this session, describing its functionality and features. If not specified, the session uses the default configuration.
            expand: Specifies which fields in the response should be expanded.
            flow_data: Information about a specific flow for the customer to go through. See the [docs](https://stripe.com/docs/customer-management/portal-deep-links) to learn more about using customer portal deep links and flows.
            locale: The IETF language tag of the locale customer portal is displayed in. If blank or auto, the customer’s `preferred_locales` or browser’s locale is used.
            on_behalf_of: The `on_behalf_of` account to use for this session. When specified, only subscriptions and invoices with this `on_behalf_of` account appear in the portal. For more information, see the [docs](https://stripe.com/docs/connect/separate-charges-and-transfers#settlement-merchant). Use the [Accounts API](https://stripe.com/docs/api/accounts/object#account_object-settings-branding) to modify the `on_behalf_of` account's branding settings, which the portal displays.
            return_url: The default URL to redirect customers to when they click on the portal's link to return to your website.
            customer: The ID of an existing customer.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.billing_portal.session.create(customer="string")
        ```
        """
        _data = to_form_urlencoded(
            item={
                "configuration": configuration,
                "expand": expand,
                "flow_data": flow_data,
                "locale": locale,
                "on_behalf_of": on_behalf_of,
                "return_url": return_url,
                "customer": customer,
            },
            dump_with=params._SerializerBillingPortalSessionCreateBody,
            style={
                "configuration": "form",
                "customer": "form",
                "expand": "deepObject",
                "flow_data": "deepObject",
                "locale": "form",
                "on_behalf_of": "form",
                "return_url": "form",
            },
            explode={
                "configuration": True,
                "customer": True,
                "expand": True,
                "flow_data": True,
                "locale": True,
                "on_behalf_of": True,
                "return_url": True,
            },
        )
        return await self._base_client.request(
            method="POST",
            path="/v1/billing_portal/sessions",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.BillingPortalSession,
            request_options=request_options or default_request_options(),
        )
