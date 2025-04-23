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


class AccountLinkClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def create(
        self,
        *,
        account: str,
        type_: typing_extensions.Literal["account_onboarding", "account_update"],
        collect: typing.Union[
            typing.Optional[
                typing_extensions.Literal["currently_due", "eventually_due"]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        collection_options: typing.Union[
            typing.Optional[params.AccountLinkCreateBodyCollectionOptions],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        refresh_url: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        return_url: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.AccountLink:
        """
        Create an account link

        <p>Creates an AccountLink object that includes a single-use Stripe URL that the platform can redirect their user to in order to take them through the Connect Onboarding flow.</p>

        POST /v1/account_links

        Args:
            collect: The collect parameter is deprecated. Use `collection_options` instead.
            collection_options: Specifies the requirements that Stripe collects from connected accounts in the Connect Onboarding flow.
            expand: Specifies which fields in the response should be expanded.
            refresh_url: The URL the user will be redirected to if the account link is expired, has been previously-visited, or is otherwise invalid. The URL you specify should attempt to generate a new account link with the same parameters used to create the original account link, then redirect the user to the new account link's URL so they can continue with Connect Onboarding. If a new account link cannot be generated or the redirect fails you should display a useful error to the user.
            return_url: The URL that the user will be redirected to upon leaving or completing the linked flow.
            account: The identifier of the account to create an account link for.
            type: The type of account link the user is requesting. Possible values are `account_onboarding` or `account_update`.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.account_link.create(account="string", type_="account_onboarding")
        ```
        """
        _data = to_form_urlencoded(
            item={
                "collect": collect,
                "collection_options": collection_options,
                "expand": expand,
                "refresh_url": refresh_url,
                "return_url": return_url,
                "account": account,
                "type_": type_,
            },
            dump_with=params._SerializerAccountLinkCreateBody,
            style={
                "account": "form",
                "collect": "form",
                "collection_options": "deepObject",
                "expand": "deepObject",
                "refresh_url": "form",
                "return_url": "form",
                "type": "form",
            },
            explode={
                "account": True,
                "collect": True,
                "collection_options": True,
                "expand": True,
                "refresh_url": True,
                "return_url": True,
                "type": True,
            },
        )
        return self._base_client.request(
            method="POST",
            path="/v1/account_links",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.AccountLink,
            request_options=request_options or default_request_options(),
        )


class AsyncAccountLinkClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def create(
        self,
        *,
        account: str,
        type_: typing_extensions.Literal["account_onboarding", "account_update"],
        collect: typing.Union[
            typing.Optional[
                typing_extensions.Literal["currently_due", "eventually_due"]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        collection_options: typing.Union[
            typing.Optional[params.AccountLinkCreateBodyCollectionOptions],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        refresh_url: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        return_url: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.AccountLink:
        """
        Create an account link

        <p>Creates an AccountLink object that includes a single-use Stripe URL that the platform can redirect their user to in order to take them through the Connect Onboarding flow.</p>

        POST /v1/account_links

        Args:
            collect: The collect parameter is deprecated. Use `collection_options` instead.
            collection_options: Specifies the requirements that Stripe collects from connected accounts in the Connect Onboarding flow.
            expand: Specifies which fields in the response should be expanded.
            refresh_url: The URL the user will be redirected to if the account link is expired, has been previously-visited, or is otherwise invalid. The URL you specify should attempt to generate a new account link with the same parameters used to create the original account link, then redirect the user to the new account link's URL so they can continue with Connect Onboarding. If a new account link cannot be generated or the redirect fails you should display a useful error to the user.
            return_url: The URL that the user will be redirected to upon leaving or completing the linked flow.
            account: The identifier of the account to create an account link for.
            type: The type of account link the user is requesting. Possible values are `account_onboarding` or `account_update`.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.account_link.create(account="string", type_="account_onboarding")
        ```
        """
        _data = to_form_urlencoded(
            item={
                "collect": collect,
                "collection_options": collection_options,
                "expand": expand,
                "refresh_url": refresh_url,
                "return_url": return_url,
                "account": account,
                "type_": type_,
            },
            dump_with=params._SerializerAccountLinkCreateBody,
            style={
                "account": "form",
                "collect": "form",
                "collection_options": "deepObject",
                "expand": "deepObject",
                "refresh_url": "form",
                "return_url": "form",
                "type": "form",
            },
            explode={
                "account": True,
                "collect": True,
                "collection_options": True,
                "expand": True,
                "refresh_url": True,
                "return_url": True,
                "type": True,
            },
        )
        return await self._base_client.request(
            method="POST",
            path="/v1/account_links",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.AccountLink,
            request_options=request_options or default_request_options(),
        )
