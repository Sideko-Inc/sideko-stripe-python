import typing

from sideko_stripe.core import (
    AsyncBaseClient,
    QueryParams,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
    encode_query_param,
    to_encodable,
    to_form_urlencoded,
    type_utils,
)
from sideko_stripe.types import models, params


class TokenClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def get(
        self,
        *,
        token: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Token:
        """
        Retrieve a token

        <p>Retrieves the token with the given ID.</p>

        GET /v1/tokens/{token}

        Args:
            expand: Specifies which fields in the response should be expanded.
            token: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.token.get(token="string")
        ```
        """
        models.Token.model_rebuild(_types_namespace=models._types_namespace)
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
            path=f"/v1/tokens/{token}",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.Token,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        data: typing.Union[
            typing.Optional[params.TokenCreateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Token:
        """
        Create a CVC update token

        <p>Creates a single-use token that represents a bank account’s details.
        You can use this token with any v1 API method in place of a bank account dictionary. You can only use this token once. To do so, attach it to a <a href="#accounts">connected account</a> where <a href="/api/accounts/object#account_object-controller-requirement_collection">controller.requirement_collection</a> is <code>application</code>, which includes Custom accounts.</p>

        POST /v1/tokens

        Args:
            data: TokenCreateBody
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.token.create()
        ```
        """
        models.Token.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerTokenCreateBody,
                style={
                    "account": "deepObject",
                    "bank_account": "deepObject",
                    "card": "deepObject",
                    "customer": "form",
                    "cvc_update": "deepObject",
                    "expand": "deepObject",
                    "person": "deepObject",
                    "pii": "deepObject",
                },
                explode={
                    "account": True,
                    "bank_account": True,
                    "card": True,
                    "customer": True,
                    "cvc_update": True,
                    "expand": True,
                    "person": True,
                    "pii": True,
                },
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path="/v1/tokens",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.Token,
            request_options=request_options or default_request_options(),
        )


class AsyncTokenClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def get(
        self,
        *,
        token: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Token:
        """
        Retrieve a token

        <p>Retrieves the token with the given ID.</p>

        GET /v1/tokens/{token}

        Args:
            expand: Specifies which fields in the response should be expanded.
            token: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.token.get(token="string")
        ```
        """
        models.Token.model_rebuild(_types_namespace=models._types_namespace)
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
            path=f"/v1/tokens/{token}",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.Token,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        data: typing.Union[
            typing.Optional[params.TokenCreateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Token:
        """
        Create a CVC update token

        <p>Creates a single-use token that represents a bank account’s details.
        You can use this token with any v1 API method in place of a bank account dictionary. You can only use this token once. To do so, attach it to a <a href="#accounts">connected account</a> where <a href="/api/accounts/object#account_object-controller-requirement_collection">controller.requirement_collection</a> is <code>application</code>, which includes Custom accounts.</p>

        POST /v1/tokens

        Args:
            data: TokenCreateBody
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.token.create()
        ```
        """
        models.Token.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerTokenCreateBody,
                style={
                    "account": "deepObject",
                    "bank_account": "deepObject",
                    "card": "deepObject",
                    "customer": "form",
                    "cvc_update": "deepObject",
                    "expand": "deepObject",
                    "person": "deepObject",
                    "pii": "deepObject",
                },
                explode={
                    "account": True,
                    "bank_account": True,
                    "card": True,
                    "customer": True,
                    "cvc_update": True,
                    "expand": True,
                    "person": True,
                    "pii": True,
                },
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path="/v1/tokens",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.Token,
            request_options=request_options or default_request_options(),
        )
