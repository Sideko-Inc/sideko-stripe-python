import typing

from sideko_stripe.core import (
    AsyncBaseClient,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
    to_form_urlencoded,
    type_utils,
)
from sideko_stripe.types import models, params


class AccountSessionsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def create(
        self,
        *,
        account: str,
        components: params.AccountSessionsCreateBodyComponents,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.AccountSession:
        """
        Create an Account Session

        <p>Creates a AccountSession object that includes a single-use token that the platform can use on their front-end to grant client-side API access.</p>

        POST /v1/account_sessions

        Args:
            expand: Specifies which fields in the response should be expanded.
            account: The identifier of the account to create an Account Session for.
            components: Each key of the dictionary represents an embedded component, and each embedded component maps to its configuration (e.g. whether it has been enabled or not).
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.account_sessions.create(account="string", components={})
        ```
        """
        _data = to_form_urlencoded(
            item={"expand": expand, "account": account, "components": components},
            dump_with=params._SerializerAccountSessionsCreateBody,
            style={
                "account": "form",
                "components": "deepObject",
                "expand": "deepObject",
            },
            explode={"account": True, "components": True, "expand": True},
        )
        return self._base_client.request(
            method="POST",
            path="/v1/account_sessions",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.AccountSession,
            request_options=request_options or default_request_options(),
        )


class AsyncAccountSessionsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def create(
        self,
        *,
        account: str,
        components: params.AccountSessionsCreateBodyComponents,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.AccountSession:
        """
        Create an Account Session

        <p>Creates a AccountSession object that includes a single-use token that the platform can use on their front-end to grant client-side API access.</p>

        POST /v1/account_sessions

        Args:
            expand: Specifies which fields in the response should be expanded.
            account: The identifier of the account to create an Account Session for.
            components: Each key of the dictionary represents an embedded component, and each embedded component maps to its configuration (e.g. whether it has been enabled or not).
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.account_sessions.create(account="string", components={})
        ```
        """
        _data = to_form_urlencoded(
            item={"expand": expand, "account": account, "components": components},
            dump_with=params._SerializerAccountSessionsCreateBody,
            style={
                "account": "form",
                "components": "deepObject",
                "expand": "deepObject",
            },
            explode={"account": True, "components": True, "expand": True},
        )
        return await self._base_client.request(
            method="POST",
            path="/v1/account_sessions",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.AccountSession,
            request_options=request_options or default_request_options(),
        )
