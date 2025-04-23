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


class ConfirmationTokenClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def create(
        self,
        *,
        data: typing.Union[
            typing.Optional[params.TestHelperConfirmationTokenCreateBody],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ConfirmationToken:
        """
        Create a test Confirmation Token

        <p>Creates a test mode Confirmation Token server side for your integration tests.</p>

        POST /v1/test_helpers/confirmation_tokens

        Args:
            data: TestHelperConfirmationTokenCreateBody
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.test_helper.confirmation_token.create()
        ```
        """
        models.ConfirmationToken.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerTestHelperConfirmationTokenCreateBody,
                style={
                    "expand": "deepObject",
                    "payment_method": "form",
                    "payment_method_data": "deepObject",
                    "return_url": "form",
                    "setup_future_usage": "form",
                    "shipping": "deepObject",
                },
                explode={
                    "expand": True,
                    "payment_method": True,
                    "payment_method_data": True,
                    "return_url": True,
                    "setup_future_usage": True,
                    "shipping": True,
                },
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path="/v1/test_helpers/confirmation_tokens",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.ConfirmationToken,
            request_options=request_options or default_request_options(),
        )


class AsyncConfirmationTokenClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def create(
        self,
        *,
        data: typing.Union[
            typing.Optional[params.TestHelperConfirmationTokenCreateBody],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ConfirmationToken:
        """
        Create a test Confirmation Token

        <p>Creates a test mode Confirmation Token server side for your integration tests.</p>

        POST /v1/test_helpers/confirmation_tokens

        Args:
            data: TestHelperConfirmationTokenCreateBody
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.test_helper.confirmation_token.create()
        ```
        """
        models.ConfirmationToken.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerTestHelperConfirmationTokenCreateBody,
                style={
                    "expand": "deepObject",
                    "payment_method": "form",
                    "payment_method_data": "deepObject",
                    "return_url": "form",
                    "setup_future_usage": "form",
                    "shipping": "deepObject",
                },
                explode={
                    "expand": True,
                    "payment_method": True,
                    "payment_method_data": True,
                    "return_url": True,
                    "setup_future_usage": True,
                    "shipping": True,
                },
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path="/v1/test_helpers/confirmation_tokens",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.ConfirmationToken,
            request_options=request_options or default_request_options(),
        )
