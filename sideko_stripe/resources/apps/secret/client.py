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


class SecretClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def list(
        self,
        *,
        scope: params.AppsSecretListScope,
        ending_before: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        limit: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        starting_after: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.AppsSecretListResponse:
        """
        List secrets

        <p>List all secrets stored on the given scope.</p>

        GET /v1/apps/secrets

        Args:
            ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            expand: Specifies which fields in the response should be expanded.
            limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
            scope: Specifies the scoping of the secret. Requests originating from UI extensions can only access account-scoped secrets or secrets scoped to their own user.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.apps.secret.list(scope={"type_": "account"})
        ```
        """
        _query: QueryParams = {}
        encode_query_param(
            _query,
            "scope",
            to_encodable(item=scope, dump_with=params._SerializerAppsSecretListScope),
            style="deepObject",
            explode=True,
        )
        if not isinstance(ending_before, type_utils.NotGiven):
            encode_query_param(
                _query,
                "ending_before",
                to_encodable(item=ending_before, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(expand, type_utils.NotGiven):
            encode_query_param(
                _query,
                "expand",
                to_encodable(item=expand, dump_with=typing.List[str]),
                style="deepObject",
                explode=True,
            )
        if not isinstance(limit, type_utils.NotGiven):
            encode_query_param(
                _query,
                "limit",
                to_encodable(item=limit, dump_with=int),
                style="form",
                explode=True,
            )
        if not isinstance(starting_after, type_utils.NotGiven):
            encode_query_param(
                _query,
                "starting_after",
                to_encodable(item=starting_after, dump_with=str),
                style="form",
                explode=True,
            )
        return self._base_client.request(
            method="GET",
            path="/v1/apps/secrets",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.AppsSecretListResponse,
            request_options=request_options or default_request_options(),
        )

    def find(
        self,
        *,
        name: str,
        scope: params.AppsSecretFindScope,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.AppsSecret:
        """
        Find a Secret

        <p>Finds a secret in the secret store by name and scope.</p>

        GET /v1/apps/secrets/find

        Args:
            expand: Specifies which fields in the response should be expanded.
            name: A name for the secret that's unique within the scope.
            scope: Specifies the scoping of the secret. Requests originating from UI extensions can only access account-scoped secrets or secrets scoped to their own user.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.apps.secret.find(name="string", scope={"type_": "account"})
        ```
        """
        _query: QueryParams = {}
        encode_query_param(
            _query,
            "name",
            to_encodable(item=name, dump_with=str),
            style="form",
            explode=True,
        )
        encode_query_param(
            _query,
            "scope",
            to_encodable(item=scope, dump_with=params._SerializerAppsSecretFindScope),
            style="deepObject",
            explode=True,
        )
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
            path="/v1/apps/secrets/find",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.AppsSecret,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        name: str,
        payload: str,
        scope: params.AppsSecretCreateBodyScope,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        expires_at: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.AppsSecret:
        """
        Set a Secret

        <p>Create or replace a secret in the secret store.</p>

        POST /v1/apps/secrets

        Args:
            expand: Specifies which fields in the response should be expanded.
            expires_at: The Unix timestamp for the expiry time of the secret, after which the secret deletes.
            name: A name for the secret that's unique within the scope.
            payload: The plaintext secret value to be stored.
            scope: Specifies the scoping of the secret. Requests originating from UI extensions can only access account-scoped secrets or secrets scoped to their own user.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.apps.secret.create(
            name="string", payload="string", scope={"type_": "account"}
        )
        ```
        """
        _data = to_form_urlencoded(
            item={
                "expand": expand,
                "expires_at": expires_at,
                "name": name,
                "payload": payload,
                "scope": scope,
            },
            dump_with=params._SerializerAppsSecretCreateBody,
            style={
                "expand": "deepObject",
                "expires_at": "form",
                "name": "form",
                "payload": "form",
                "scope": "deepObject",
            },
            explode={
                "expand": True,
                "expires_at": True,
                "name": True,
                "payload": True,
                "scope": True,
            },
        )
        return self._base_client.request(
            method="POST",
            path="/v1/apps/secrets",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.AppsSecret,
            request_options=request_options or default_request_options(),
        )

    def delete(
        self,
        *,
        name: str,
        scope: params.AppsSecretDeleteBodyScope,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.AppsSecret:
        """
        Delete a Secret

        <p>Deletes a secret from the secret store by name and scope.</p>

        POST /v1/apps/secrets/delete

        Args:
            expand: Specifies which fields in the response should be expanded.
            name: A name for the secret that's unique within the scope.
            scope: Specifies the scoping of the secret. Requests originating from UI extensions can only access account-scoped secrets or secrets scoped to their own user.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.apps.secret.delete(name="string", scope={"type_": "account"})
        ```
        """
        _data = to_form_urlencoded(
            item={"expand": expand, "name": name, "scope": scope},
            dump_with=params._SerializerAppsSecretDeleteBody,
            style={"expand": "deepObject", "name": "form", "scope": "deepObject"},
            explode={"expand": True, "name": True, "scope": True},
        )
        return self._base_client.request(
            method="POST",
            path="/v1/apps/secrets/delete",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.AppsSecret,
            request_options=request_options or default_request_options(),
        )


class AsyncSecretClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def list(
        self,
        *,
        scope: params.AppsSecretListScope,
        ending_before: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        limit: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        starting_after: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.AppsSecretListResponse:
        """
        List secrets

        <p>List all secrets stored on the given scope.</p>

        GET /v1/apps/secrets

        Args:
            ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            expand: Specifies which fields in the response should be expanded.
            limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
            scope: Specifies the scoping of the secret. Requests originating from UI extensions can only access account-scoped secrets or secrets scoped to their own user.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.apps.secret.list(scope={"type_": "account"})
        ```
        """
        _query: QueryParams = {}
        encode_query_param(
            _query,
            "scope",
            to_encodable(item=scope, dump_with=params._SerializerAppsSecretListScope),
            style="deepObject",
            explode=True,
        )
        if not isinstance(ending_before, type_utils.NotGiven):
            encode_query_param(
                _query,
                "ending_before",
                to_encodable(item=ending_before, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(expand, type_utils.NotGiven):
            encode_query_param(
                _query,
                "expand",
                to_encodable(item=expand, dump_with=typing.List[str]),
                style="deepObject",
                explode=True,
            )
        if not isinstance(limit, type_utils.NotGiven):
            encode_query_param(
                _query,
                "limit",
                to_encodable(item=limit, dump_with=int),
                style="form",
                explode=True,
            )
        if not isinstance(starting_after, type_utils.NotGiven):
            encode_query_param(
                _query,
                "starting_after",
                to_encodable(item=starting_after, dump_with=str),
                style="form",
                explode=True,
            )
        return await self._base_client.request(
            method="GET",
            path="/v1/apps/secrets",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.AppsSecretListResponse,
            request_options=request_options or default_request_options(),
        )

    async def find(
        self,
        *,
        name: str,
        scope: params.AppsSecretFindScope,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.AppsSecret:
        """
        Find a Secret

        <p>Finds a secret in the secret store by name and scope.</p>

        GET /v1/apps/secrets/find

        Args:
            expand: Specifies which fields in the response should be expanded.
            name: A name for the secret that's unique within the scope.
            scope: Specifies the scoping of the secret. Requests originating from UI extensions can only access account-scoped secrets or secrets scoped to their own user.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.apps.secret.find(name="string", scope={"type_": "account"})
        ```
        """
        _query: QueryParams = {}
        encode_query_param(
            _query,
            "name",
            to_encodable(item=name, dump_with=str),
            style="form",
            explode=True,
        )
        encode_query_param(
            _query,
            "scope",
            to_encodable(item=scope, dump_with=params._SerializerAppsSecretFindScope),
            style="deepObject",
            explode=True,
        )
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
            path="/v1/apps/secrets/find",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.AppsSecret,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        name: str,
        payload: str,
        scope: params.AppsSecretCreateBodyScope,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        expires_at: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.AppsSecret:
        """
        Set a Secret

        <p>Create or replace a secret in the secret store.</p>

        POST /v1/apps/secrets

        Args:
            expand: Specifies which fields in the response should be expanded.
            expires_at: The Unix timestamp for the expiry time of the secret, after which the secret deletes.
            name: A name for the secret that's unique within the scope.
            payload: The plaintext secret value to be stored.
            scope: Specifies the scoping of the secret. Requests originating from UI extensions can only access account-scoped secrets or secrets scoped to their own user.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.apps.secret.create(
            name="string", payload="string", scope={"type_": "account"}
        )
        ```
        """
        _data = to_form_urlencoded(
            item={
                "expand": expand,
                "expires_at": expires_at,
                "name": name,
                "payload": payload,
                "scope": scope,
            },
            dump_with=params._SerializerAppsSecretCreateBody,
            style={
                "expand": "deepObject",
                "expires_at": "form",
                "name": "form",
                "payload": "form",
                "scope": "deepObject",
            },
            explode={
                "expand": True,
                "expires_at": True,
                "name": True,
                "payload": True,
                "scope": True,
            },
        )
        return await self._base_client.request(
            method="POST",
            path="/v1/apps/secrets",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.AppsSecret,
            request_options=request_options or default_request_options(),
        )

    async def delete(
        self,
        *,
        name: str,
        scope: params.AppsSecretDeleteBodyScope,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.AppsSecret:
        """
        Delete a Secret

        <p>Deletes a secret from the secret store by name and scope.</p>

        POST /v1/apps/secrets/delete

        Args:
            expand: Specifies which fields in the response should be expanded.
            name: A name for the secret that's unique within the scope.
            scope: Specifies the scoping of the secret. Requests originating from UI extensions can only access account-scoped secrets or secrets scoped to their own user.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.apps.secret.delete(name="string", scope={"type_": "account"})
        ```
        """
        _data = to_form_urlencoded(
            item={"expand": expand, "name": name, "scope": scope},
            dump_with=params._SerializerAppsSecretDeleteBody,
            style={"expand": "deepObject", "name": "form", "scope": "deepObject"},
            explode={"expand": True, "name": True, "scope": True},
        )
        return await self._base_client.request(
            method="POST",
            path="/v1/apps/secrets/delete",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.AppsSecret,
            request_options=request_options or default_request_options(),
        )
