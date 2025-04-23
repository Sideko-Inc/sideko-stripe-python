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


class ConnectionTokenClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def create(
        self,
        *,
        data: typing.Union[
            typing.Optional[params.TerminalConnectionTokenCreateBody],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TerminalConnectionToken:
        """
        Create a Connection Token

        <p>To connect to a reader the Stripe Terminal SDK needs to retrieve a short-lived connection token from Stripe, proxied through your server. On your backend, add an endpoint that creates and returns a connection token.</p>

        POST /v1/terminal/connection_tokens

        Args:
            data: TerminalConnectionTokenCreateBody
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.terminal.connection_token.create()
        ```
        """
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerTerminalConnectionTokenCreateBody,
                style={"expand": "deepObject", "location": "form"},
                explode={"expand": True, "location": True},
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path="/v1/terminal/connection_tokens",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.TerminalConnectionToken,
            request_options=request_options or default_request_options(),
        )


class AsyncConnectionTokenClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def create(
        self,
        *,
        data: typing.Union[
            typing.Optional[params.TerminalConnectionTokenCreateBody],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TerminalConnectionToken:
        """
        Create a Connection Token

        <p>To connect to a reader the Stripe Terminal SDK needs to retrieve a short-lived connection token from Stripe, proxied through your server. On your backend, add an endpoint that creates and returns a connection token.</p>

        POST /v1/terminal/connection_tokens

        Args:
            data: TerminalConnectionTokenCreateBody
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.terminal.connection_token.create()
        ```
        """
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerTerminalConnectionTokenCreateBody,
                style={"expand": "deepObject", "location": "form"},
                explode={"expand": True, "location": True},
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path="/v1/terminal/connection_tokens",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.TerminalConnectionToken,
            request_options=request_options or default_request_options(),
        )
