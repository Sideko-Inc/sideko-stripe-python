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


class EphemeralKeyClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def delete(
        self,
        *,
        key: str,
        data: typing.Union[
            typing.Optional[params.EphemeralKeyDeleteBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.EphemeralKey:
        """
        Immediately invalidate an ephemeral key

        <p>Invalidates a short-lived API key for a given resource.</p>

        DELETE /v1/ephemeral_keys/{key}

        Args:
            data: EphemeralKeyDeleteBody
            key: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.ephemeral_key.delete(key="string")
        ```
        """
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerEphemeralKeyDeleteBody,
                style={"expand": "deepObject"},
                explode={"expand": True},
            )
            if data
            else None
        )
        return self._base_client.request(
            method="DELETE",
            path=f"/v1/ephemeral_keys/{key}",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.EphemeralKey,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        data: typing.Union[
            typing.Optional[params.EphemeralKeyCreateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.EphemeralKey:
        """
        Create an ephemeral key

        <p>Creates a short-lived API key for a given resource.</p>

        POST /v1/ephemeral_keys

        Args:
            data: EphemeralKeyCreateBody
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.ephemeral_key.create()
        ```
        """
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerEphemeralKeyCreateBody,
                style={
                    "customer": "form",
                    "expand": "deepObject",
                    "issuing_card": "form",
                    "nonce": "form",
                    "verification_session": "form",
                },
                explode={
                    "customer": True,
                    "expand": True,
                    "issuing_card": True,
                    "nonce": True,
                    "verification_session": True,
                },
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path="/v1/ephemeral_keys",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.EphemeralKey,
            request_options=request_options or default_request_options(),
        )


class AsyncEphemeralKeyClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def delete(
        self,
        *,
        key: str,
        data: typing.Union[
            typing.Optional[params.EphemeralKeyDeleteBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.EphemeralKey:
        """
        Immediately invalidate an ephemeral key

        <p>Invalidates a short-lived API key for a given resource.</p>

        DELETE /v1/ephemeral_keys/{key}

        Args:
            data: EphemeralKeyDeleteBody
            key: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.ephemeral_key.delete(key="string")
        ```
        """
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerEphemeralKeyDeleteBody,
                style={"expand": "deepObject"},
                explode={"expand": True},
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="DELETE",
            path=f"/v1/ephemeral_keys/{key}",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.EphemeralKey,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        data: typing.Union[
            typing.Optional[params.EphemeralKeyCreateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.EphemeralKey:
        """
        Create an ephemeral key

        <p>Creates a short-lived API key for a given resource.</p>

        POST /v1/ephemeral_keys

        Args:
            data: EphemeralKeyCreateBody
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.ephemeral_key.create()
        ```
        """
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerEphemeralKeyCreateBody,
                style={
                    "customer": "form",
                    "expand": "deepObject",
                    "issuing_card": "form",
                    "nonce": "form",
                    "verification_session": "form",
                },
                explode={
                    "customer": True,
                    "expand": True,
                    "issuing_card": True,
                    "nonce": True,
                    "verification_session": True,
                },
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path="/v1/ephemeral_keys",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.EphemeralKey,
            request_options=request_options or default_request_options(),
        )
