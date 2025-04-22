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


class FeatureClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def list(
        self,
        *,
        archived: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        ending_before: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        limit: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        lookup_key: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        starting_after: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.EntitlementFeatureListResponse:
        """
        List all features

        <p>Retrieve a list of features</p>

        GET /v1/entitlements/features

        Args:
            archived: If set, filter results to only include features with the given archive status.
            ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            expand: Specifies which fields in the response should be expanded.
            limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            lookup_key: If set, filter results to only include features with the given lookup_key.
            starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.entitlement.feature.list()
        ```
        """
        _query: QueryParams = {}
        if not isinstance(archived, type_utils.NotGiven):
            encode_query_param(
                _query,
                "archived",
                to_encodable(item=archived, dump_with=bool),
                style="form",
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
        if not isinstance(lookup_key, type_utils.NotGiven):
            encode_query_param(
                _query,
                "lookup_key",
                to_encodable(item=lookup_key, dump_with=str),
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
            path="/v1/entitlements/features",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.EntitlementFeatureListResponse,
            request_options=request_options or default_request_options(),
        )

    def get(
        self,
        *,
        id: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.EntitlementsFeature:
        """
        Retrieve a feature

        <p>Retrieves a feature</p>

        GET /v1/entitlements/features/{id}

        Args:
            expand: Specifies which fields in the response should be expanded.
            id: The ID of the feature.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.entitlement.feature.get(id="string")
        ```
        """
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
            path=f"/v1/entitlements/features/{id}",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.EntitlementsFeature,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        lookup_key: str,
        name: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        metadata: typing.Union[
            typing.Optional[params.EntitlementFeatureCreateBodyMetadata],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.EntitlementsFeature:
        """
        Create a feature

        <p>Creates a feature</p>

        POST /v1/entitlements/features

        Args:
            expand: Specifies which fields in the response should be expanded.
            metadata: Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
            lookup_key: A unique key you provide as your own system identifier. This may be up to 80 characters.
            name: The feature's name, for your own purpose, not meant to be displayable to the customer.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.entitlement.feature.create(lookup_key="string", name="string")
        ```
        """
        _data = to_form_urlencoded(
            item={
                "expand": expand,
                "metadata": metadata,
                "lookup_key": lookup_key,
                "name": name,
            },
            dump_with=params._SerializerEntitlementFeatureCreateBody,
            style={
                "expand": "deepObject",
                "lookup_key": "form",
                "metadata": "deepObject",
                "name": "form",
            },
            explode={
                "expand": True,
                "lookup_key": True,
                "metadata": True,
                "name": True,
            },
        )
        return self._base_client.request(
            method="POST",
            path="/v1/entitlements/features",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.EntitlementsFeature,
            request_options=request_options or default_request_options(),
        )

    def update(
        self,
        *,
        id: str,
        data: typing.Union[
            typing.Optional[params.EntitlementFeatureUpdateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.EntitlementsFeature:
        """
        Updates a feature

        <p>Update a feature’s metadata or permanently deactivate it.</p>

        POST /v1/entitlements/features/{id}

        Args:
            data: EntitlementFeatureUpdateBody
            id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.entitlement.feature.update(id="string")
        ```
        """
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerEntitlementFeatureUpdateBody,
                style={
                    "active": "form",
                    "expand": "deepObject",
                    "metadata": "deepObject",
                    "name": "form",
                },
                explode={
                    "active": True,
                    "expand": True,
                    "metadata": True,
                    "name": True,
                },
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/entitlements/features/{id}",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.EntitlementsFeature,
            request_options=request_options or default_request_options(),
        )


class AsyncFeatureClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def list(
        self,
        *,
        archived: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        ending_before: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        limit: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        lookup_key: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        starting_after: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.EntitlementFeatureListResponse:
        """
        List all features

        <p>Retrieve a list of features</p>

        GET /v1/entitlements/features

        Args:
            archived: If set, filter results to only include features with the given archive status.
            ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            expand: Specifies which fields in the response should be expanded.
            limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            lookup_key: If set, filter results to only include features with the given lookup_key.
            starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.entitlement.feature.list()
        ```
        """
        _query: QueryParams = {}
        if not isinstance(archived, type_utils.NotGiven):
            encode_query_param(
                _query,
                "archived",
                to_encodable(item=archived, dump_with=bool),
                style="form",
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
        if not isinstance(lookup_key, type_utils.NotGiven):
            encode_query_param(
                _query,
                "lookup_key",
                to_encodable(item=lookup_key, dump_with=str),
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
            path="/v1/entitlements/features",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.EntitlementFeatureListResponse,
            request_options=request_options or default_request_options(),
        )

    async def get(
        self,
        *,
        id: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.EntitlementsFeature:
        """
        Retrieve a feature

        <p>Retrieves a feature</p>

        GET /v1/entitlements/features/{id}

        Args:
            expand: Specifies which fields in the response should be expanded.
            id: The ID of the feature.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.entitlement.feature.get(id="string")
        ```
        """
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
            path=f"/v1/entitlements/features/{id}",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.EntitlementsFeature,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        lookup_key: str,
        name: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        metadata: typing.Union[
            typing.Optional[params.EntitlementFeatureCreateBodyMetadata],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.EntitlementsFeature:
        """
        Create a feature

        <p>Creates a feature</p>

        POST /v1/entitlements/features

        Args:
            expand: Specifies which fields in the response should be expanded.
            metadata: Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
            lookup_key: A unique key you provide as your own system identifier. This may be up to 80 characters.
            name: The feature's name, for your own purpose, not meant to be displayable to the customer.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.entitlement.feature.create(lookup_key="string", name="string")
        ```
        """
        _data = to_form_urlencoded(
            item={
                "expand": expand,
                "metadata": metadata,
                "lookup_key": lookup_key,
                "name": name,
            },
            dump_with=params._SerializerEntitlementFeatureCreateBody,
            style={
                "expand": "deepObject",
                "lookup_key": "form",
                "metadata": "deepObject",
                "name": "form",
            },
            explode={
                "expand": True,
                "lookup_key": True,
                "metadata": True,
                "name": True,
            },
        )
        return await self._base_client.request(
            method="POST",
            path="/v1/entitlements/features",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.EntitlementsFeature,
            request_options=request_options or default_request_options(),
        )

    async def update(
        self,
        *,
        id: str,
        data: typing.Union[
            typing.Optional[params.EntitlementFeatureUpdateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.EntitlementsFeature:
        """
        Updates a feature

        <p>Update a feature’s metadata or permanently deactivate it.</p>

        POST /v1/entitlements/features/{id}

        Args:
            data: EntitlementFeatureUpdateBody
            id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.entitlement.feature.update(id="string")
        ```
        """
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerEntitlementFeatureUpdateBody,
                style={
                    "active": "form",
                    "expand": "deepObject",
                    "metadata": "deepObject",
                    "name": "form",
                },
                explode={
                    "active": True,
                    "expand": True,
                    "metadata": True,
                    "name": True,
                },
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/entitlements/features/{id}",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.EntitlementsFeature,
            request_options=request_options or default_request_options(),
        )
