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

    def delete(
        self,
        *,
        id: str,
        product: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.DeletedProductFeature:
        """
        Remove a feature from a product

        <p>Deletes the feature attachment to a product</p>

        DELETE /v1/products/{product}/features/{id}

        Args:
            id: str
            product: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.product.feature.delete(id="string", product="string")
        ```
        """
        return self._base_client.request(
            method="DELETE",
            path=f"/v1/products/{product}/features/{id}",
            auth_names=["bearerAuth"],
            cast_to=models.DeletedProductFeature,
            request_options=request_options or default_request_options(),
        )

    def list(
        self,
        *,
        product: str,
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
    ) -> models.ProductFeatureListResponse:
        """
        List all features attached to a product

        <p>Retrieve a list of features for a product</p>

        GET /v1/products/{product}/features

        Args:
            ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            expand: Specifies which fields in the response should be expanded.
            limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
            product: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.product.feature.list(product="string")
        ```
        """
        _query: QueryParams = {}
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
            path=f"/v1/products/{product}/features",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.ProductFeatureListResponse,
            request_options=request_options or default_request_options(),
        )

    def get(
        self,
        *,
        id: str,
        product: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ProductFeature:
        """
        Retrieve a product_feature

        <p>Retrieves a product_feature, which represents a feature attachment to a product</p>

        GET /v1/products/{product}/features/{id}

        Args:
            expand: Specifies which fields in the response should be expanded.
            id: The ID of the product_feature.
            product: The ID of the product.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.product.feature.get(id="string", product="string")
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
            path=f"/v1/products/{product}/features/{id}",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.ProductFeature,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        entitlement_feature: str,
        product: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ProductFeature:
        """
        Attach a feature to a product

        <p>Creates a product_feature, which represents a feature attachment to a product</p>

        POST /v1/products/{product}/features

        Args:
            expand: Specifies which fields in the response should be expanded.
            entitlement_feature: The ID of the [Feature](https://stripe.com/docs/api/entitlements/feature) object attached to this product.
            product: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.product.feature.create(entitlement_feature="string", product="string")
        ```
        """
        _data = to_form_urlencoded(
            item={"expand": expand, "entitlement_feature": entitlement_feature},
            dump_with=params._SerializerProductFeatureCreateBody,
            style={"entitlement_feature": "form", "expand": "deepObject"},
            explode={"entitlement_feature": True, "expand": True},
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/products/{product}/features",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.ProductFeature,
            request_options=request_options or default_request_options(),
        )


class AsyncFeatureClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def delete(
        self,
        *,
        id: str,
        product: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.DeletedProductFeature:
        """
        Remove a feature from a product

        <p>Deletes the feature attachment to a product</p>

        DELETE /v1/products/{product}/features/{id}

        Args:
            id: str
            product: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.product.feature.delete(id="string", product="string")
        ```
        """
        return await self._base_client.request(
            method="DELETE",
            path=f"/v1/products/{product}/features/{id}",
            auth_names=["bearerAuth"],
            cast_to=models.DeletedProductFeature,
            request_options=request_options or default_request_options(),
        )

    async def list(
        self,
        *,
        product: str,
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
    ) -> models.ProductFeatureListResponse:
        """
        List all features attached to a product

        <p>Retrieve a list of features for a product</p>

        GET /v1/products/{product}/features

        Args:
            ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            expand: Specifies which fields in the response should be expanded.
            limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
            product: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.product.feature.list(product="string")
        ```
        """
        _query: QueryParams = {}
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
            path=f"/v1/products/{product}/features",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.ProductFeatureListResponse,
            request_options=request_options or default_request_options(),
        )

    async def get(
        self,
        *,
        id: str,
        product: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ProductFeature:
        """
        Retrieve a product_feature

        <p>Retrieves a product_feature, which represents a feature attachment to a product</p>

        GET /v1/products/{product}/features/{id}

        Args:
            expand: Specifies which fields in the response should be expanded.
            id: The ID of the product_feature.
            product: The ID of the product.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.product.feature.get(id="string", product="string")
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
            path=f"/v1/products/{product}/features/{id}",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.ProductFeature,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        entitlement_feature: str,
        product: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ProductFeature:
        """
        Attach a feature to a product

        <p>Creates a product_feature, which represents a feature attachment to a product</p>

        POST /v1/products/{product}/features

        Args:
            expand: Specifies which fields in the response should be expanded.
            entitlement_feature: The ID of the [Feature](https://stripe.com/docs/api/entitlements/feature) object attached to this product.
            product: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.product.feature.create(
            entitlement_feature="string", product="string"
        )
        ```
        """
        _data = to_form_urlencoded(
            item={"expand": expand, "entitlement_feature": entitlement_feature},
            dump_with=params._SerializerProductFeatureCreateBody,
            style={"entitlement_feature": "form", "expand": "deepObject"},
            explode={"entitlement_feature": True, "expand": True},
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/products/{product}/features",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.ProductFeature,
            request_options=request_options or default_request_options(),
        )
