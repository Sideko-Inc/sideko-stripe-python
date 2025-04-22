import typing

from sideko_stripe.core import (
    AsyncBaseClient,
    QueryParams,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
    encode_query_param,
    to_encodable,
    type_utils,
)
from sideko_stripe.types import models


class ConfirmationTokenClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def get(
        self,
        *,
        confirmation_token: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ConfirmationToken:
        """
        Retrieve a ConfirmationToken

        <p>Retrieves an existing ConfirmationToken object</p>

        GET /v1/confirmation_tokens/{confirmation_token}

        Args:
            expand: Specifies which fields in the response should be expanded.
            confirmation_token: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.confirmation_token.get(confirmation_token="string")
        ```
        """
        models.ConfirmationToken.model_rebuild(_types_namespace=models._types_namespace)
        _query: QueryParams = {}
        if not isinstance(expand, type_utils.NotGiven):
            encode_query_param(
                _query,
                "expand",
                to_encodable(item=expand, dump_with=typing.List[str]),
                style="deepObject",
                explode=True,
            )
        return self._base_client.request(
            method="GET",
            path=f"/v1/confirmation_tokens/{confirmation_token}",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.ConfirmationToken,
            request_options=request_options or default_request_options(),
        )


class AsyncConfirmationTokenClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def get(
        self,
        *,
        confirmation_token: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ConfirmationToken:
        """
        Retrieve a ConfirmationToken

        <p>Retrieves an existing ConfirmationToken object</p>

        GET /v1/confirmation_tokens/{confirmation_token}

        Args:
            expand: Specifies which fields in the response should be expanded.
            confirmation_token: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.confirmation_token.get(confirmation_token="string")
        ```
        """
        models.ConfirmationToken.model_rebuild(_types_namespace=models._types_namespace)
        _query: QueryParams = {}
        if not isinstance(expand, type_utils.NotGiven):
            encode_query_param(
                _query,
                "expand",
                to_encodable(item=expand, dump_with=typing.List[str]),
                style="deepObject",
                explode=True,
            )
        return await self._base_client.request(
            method="GET",
            path=f"/v1/confirmation_tokens/{confirmation_token}",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.ConfirmationToken,
            request_options=request_options or default_request_options(),
        )
