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
from sideko_stripe.resources.product.feature import AsyncFeatureClient, FeatureClient
from sideko_stripe.types import models, params


class ProductClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        self.feature = FeatureClient(base_client=self._base_client)

    def delete(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.DeletedProduct:
        """
        Delete a product

        <p>Delete a product. Deleting a product is only possible if it has no prices associated with it. Additionally, deleting a product with <code>type=good</code> is only possible if it has no SKUs associated with it.</p>

        DELETE /v1/products/{id}

        Args:
            id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.product.delete(id="string")
        ```
        """
        return self._base_client.request(
            method="DELETE",
            path=f"/v1/products/{id}",
            auth_names=["basicAuth", "bearerAuth"],
            cast_to=models.DeletedProduct,
            request_options=request_options or default_request_options(),
        )

    def list(
        self,
        *,
        active: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        created: typing.Union[
            typing.Optional[typing.Union[params.ProductListCreatedObj0, int]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        ending_before: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        ids: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        limit: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        shippable: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        starting_after: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        url: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ProductListResponse:
        """
        List all products

        <p>Returns a list of your products. The products are returned sorted by creation date, with the most recently created products appearing first.</p>

        GET /v1/products

        Args:
            active: Only return products that are active or inactive (e.g., pass `false` to list all inactive products).
            created: Only return products that were created during the given date interval.
            ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            expand: Specifies which fields in the response should be expanded.
            ids: Only return products with the given IDs. Cannot be used with [starting_after](https://stripe.com/docs/api#list_products-starting_after) or [ending_before](https://stripe.com/docs/api#list_products-ending_before).
            limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            shippable: Only return products that can be shipped (i.e., physical, not digital products).
            starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
            url: Only return products with the given url.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.product.list()
        ```
        """
        models.ProductListResponse.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _query: QueryParams = {}
        if not isinstance(active, type_utils.NotGiven):
            encode_query_param(
                _query,
                "active",
                to_encodable(item=active, dump_with=bool),
                style="form",
                explode=True,
            )
        if not isinstance(created, type_utils.NotGiven):
            encode_query_param(
                _query,
                "created",
                to_encodable(
                    item=created,
                    dump_with=typing.Union[
                        params._SerializerProductListCreatedObj0, int
                    ],
                ),
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
        if not isinstance(ids, type_utils.NotGiven):
            encode_query_param(
                _query,
                "ids",
                to_encodable(item=ids, dump_with=typing.List[str]),
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
        if not isinstance(shippable, type_utils.NotGiven):
            encode_query_param(
                _query,
                "shippable",
                to_encodable(item=shippable, dump_with=bool),
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
        if not isinstance(url, type_utils.NotGiven):
            encode_query_param(
                _query,
                "url",
                to_encodable(item=url, dump_with=str),
                style="form",
                explode=True,
            )
        return self._base_client.request(
            method="GET",
            path="/v1/products",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.ProductListResponse,
            request_options=request_options or default_request_options(),
        )

    def search(
        self,
        *,
        query: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        limit: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        page: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ProductSearchResponse:
        """
        Search products

        <p>Search for products you’ve previously created using Stripe’s <a href="/docs/search#search-query-language">Search Query Language</a>.
        Don’t use search in read-after-write flows where strict consistency is necessary. Under normal operating
        conditions, data is searchable in less than a minute. Occasionally, propagation of new or updated data can be up
        to an hour behind during outages. Search functionality is not available to merchants in India.</p>

        GET /v1/products/search

        Args:
            expand: Specifies which fields in the response should be expanded.
            limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            page: A cursor for pagination across multiple pages of results. Don't include this parameter on the first call. Use the next_page value returned in a previous response to request subsequent results.
            query: The search query string. See [search query language](https://stripe.com/docs/search#search-query-language) and the list of supported [query fields for products](https://stripe.com/docs/search#query-fields-for-products).
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.product.search(query="string")
        ```
        """
        models.ProductSearchResponse.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _query: QueryParams = {}
        encode_query_param(
            _query,
            "query",
            to_encodable(item=query, dump_with=str),
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
        if not isinstance(page, type_utils.NotGiven):
            encode_query_param(
                _query,
                "page",
                to_encodable(item=page, dump_with=str),
                style="form",
                explode=True,
            )
        return self._base_client.request(
            method="GET",
            path="/v1/products/search",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.ProductSearchResponse,
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
    ) -> models.Product:
        """
        Retrieve a product

        <p>Retrieves the details of an existing product. Supply the unique product ID from either a product creation request or the product list, and Stripe will return the corresponding product information.</p>

        GET /v1/products/{id}

        Args:
            expand: Specifies which fields in the response should be expanded.
            id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.product.get(id="string")
        ```
        """
        models.Product.model_rebuild(_types_namespace=models._types_namespace)
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
            path=f"/v1/products/{id}",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.Product,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        name: str,
        active: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        default_price_data: typing.Union[
            typing.Optional[params.ProductCreateBodyDefaultPriceData],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        description: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        images: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        marketing_features: typing.Union[
            typing.Optional[typing.List[params.ProductCreateBodyMarketingFeaturesItem]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        metadata: typing.Union[
            typing.Optional[params.ProductCreateBodyMetadata], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        package_dimensions: typing.Union[
            typing.Optional[params.ProductCreateBodyPackageDimensions],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        shippable: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        statement_descriptor: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        tax_code: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        unit_label: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        url: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Product:
        """
        Create a product

        <p>Creates a new product object.</p>

        POST /v1/products

        Args:
            active: Whether the product is currently available for purchase. Defaults to `true`.
            default_price_data: Data used to generate a new [Price](https://stripe.com/docs/api/prices) object. This Price will be set as the default price for this product.
            description: The product's description, meant to be displayable to the customer. Use this field to optionally store a long form explanation of the product being sold for your own rendering purposes.
            expand: Specifies which fields in the response should be expanded.
            id: An identifier will be randomly generated by Stripe. You can optionally override this ID, but the ID must be unique across all products in your Stripe account.
            images: A list of up to 8 URLs of images for this product, meant to be displayable to the customer.
            marketing_features: A list of up to 15 marketing features for this product. These are displayed in [pricing tables](https://stripe.com/docs/payments/checkout/pricing-table).
            metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
            package_dimensions: The dimensions of this product for shipping purposes.
            shippable: Whether this product is shipped (i.e., physical goods).
            statement_descriptor: An arbitrary string to be displayed on your customer's credit card or bank statement. While most banks display this information consistently, some may display it incorrectly or not at all.

        This may be up to 22 characters. The statement description may not include `<`, `>`, `\`, `"`, `'` characters, and will appear on your customer's statement in capital letters. Non-ASCII characters are automatically stripped.
         It must contain at least one letter. Only used for subscription payments.
            tax_code: A [tax code](https://stripe.com/docs/tax/tax-categories) ID.
            unit_label: A label that represents units of this product. When set, this will be included in customers' receipts, invoices, Checkout, and the customer portal.
            url: A URL of a publicly-accessible webpage for this product.
            name: The product's name, meant to be displayable to the customer.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.product.create(name="string")
        ```
        """
        models.Product.model_rebuild(_types_namespace=models._types_namespace)
        _data = to_form_urlencoded(
            item={
                "active": active,
                "default_price_data": default_price_data,
                "description": description,
                "expand": expand,
                "id": id,
                "images": images,
                "marketing_features": marketing_features,
                "metadata": metadata,
                "package_dimensions": package_dimensions,
                "shippable": shippable,
                "statement_descriptor": statement_descriptor,
                "tax_code": tax_code,
                "unit_label": unit_label,
                "url": url,
                "name": name,
            },
            dump_with=params._SerializerProductCreateBody,
            style={
                "active": "form",
                "default_price_data": "deepObject",
                "description": "form",
                "expand": "deepObject",
                "id": "form",
                "images": "deepObject",
                "marketing_features": "deepObject",
                "metadata": "deepObject",
                "name": "form",
                "package_dimensions": "deepObject",
                "shippable": "form",
                "statement_descriptor": "form",
                "tax_code": "form",
                "unit_label": "form",
                "url": "form",
            },
            explode={
                "active": True,
                "default_price_data": True,
                "description": True,
                "expand": True,
                "id": True,
                "images": True,
                "marketing_features": True,
                "metadata": True,
                "name": True,
                "package_dimensions": True,
                "shippable": True,
                "statement_descriptor": True,
                "tax_code": True,
                "unit_label": True,
                "url": True,
            },
        )
        return self._base_client.request(
            method="POST",
            path="/v1/products",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.Product,
            request_options=request_options or default_request_options(),
        )

    def update(
        self,
        *,
        id: str,
        data: typing.Union[
            typing.Optional[params.ProductUpdateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Product:
        """
        Update a product

        <p>Updates the specific product by setting the values of the parameters passed. Any parameters not provided will be left unchanged.</p>

        POST /v1/products/{id}

        Args:
            data: ProductUpdateBody
            id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.product.update(id="string")
        ```
        """
        models.Product.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerProductUpdateBody,
                style={
                    "active": "form",
                    "default_price": "form",
                    "description": "deepObject",
                    "expand": "deepObject",
                    "images": "deepObject",
                    "marketing_features": "deepObject",
                    "metadata": "deepObject",
                    "name": "form",
                    "package_dimensions": "deepObject",
                    "shippable": "form",
                    "statement_descriptor": "form",
                    "tax_code": "deepObject",
                    "unit_label": "deepObject",
                    "url": "deepObject",
                },
                explode={
                    "active": True,
                    "default_price": True,
                    "description": True,
                    "expand": True,
                    "images": True,
                    "marketing_features": True,
                    "metadata": True,
                    "name": True,
                    "package_dimensions": True,
                    "shippable": True,
                    "statement_descriptor": True,
                    "tax_code": True,
                    "unit_label": True,
                    "url": True,
                },
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/products/{id}",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.Product,
            request_options=request_options or default_request_options(),
        )


class AsyncProductClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        self.feature = AsyncFeatureClient(base_client=self._base_client)

    async def delete(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.DeletedProduct:
        """
        Delete a product

        <p>Delete a product. Deleting a product is only possible if it has no prices associated with it. Additionally, deleting a product with <code>type=good</code> is only possible if it has no SKUs associated with it.</p>

        DELETE /v1/products/{id}

        Args:
            id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.product.delete(id="string")
        ```
        """
        return await self._base_client.request(
            method="DELETE",
            path=f"/v1/products/{id}",
            auth_names=["basicAuth", "bearerAuth"],
            cast_to=models.DeletedProduct,
            request_options=request_options or default_request_options(),
        )

    async def list(
        self,
        *,
        active: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        created: typing.Union[
            typing.Optional[typing.Union[params.ProductListCreatedObj0, int]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        ending_before: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        ids: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        limit: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        shippable: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        starting_after: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        url: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ProductListResponse:
        """
        List all products

        <p>Returns a list of your products. The products are returned sorted by creation date, with the most recently created products appearing first.</p>

        GET /v1/products

        Args:
            active: Only return products that are active or inactive (e.g., pass `false` to list all inactive products).
            created: Only return products that were created during the given date interval.
            ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            expand: Specifies which fields in the response should be expanded.
            ids: Only return products with the given IDs. Cannot be used with [starting_after](https://stripe.com/docs/api#list_products-starting_after) or [ending_before](https://stripe.com/docs/api#list_products-ending_before).
            limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            shippable: Only return products that can be shipped (i.e., physical, not digital products).
            starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
            url: Only return products with the given url.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.product.list()
        ```
        """
        models.ProductListResponse.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _query: QueryParams = {}
        if not isinstance(active, type_utils.NotGiven):
            encode_query_param(
                _query,
                "active",
                to_encodable(item=active, dump_with=bool),
                style="form",
                explode=True,
            )
        if not isinstance(created, type_utils.NotGiven):
            encode_query_param(
                _query,
                "created",
                to_encodable(
                    item=created,
                    dump_with=typing.Union[
                        params._SerializerProductListCreatedObj0, int
                    ],
                ),
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
        if not isinstance(ids, type_utils.NotGiven):
            encode_query_param(
                _query,
                "ids",
                to_encodable(item=ids, dump_with=typing.List[str]),
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
        if not isinstance(shippable, type_utils.NotGiven):
            encode_query_param(
                _query,
                "shippable",
                to_encodable(item=shippable, dump_with=bool),
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
        if not isinstance(url, type_utils.NotGiven):
            encode_query_param(
                _query,
                "url",
                to_encodable(item=url, dump_with=str),
                style="form",
                explode=True,
            )
        return await self._base_client.request(
            method="GET",
            path="/v1/products",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.ProductListResponse,
            request_options=request_options or default_request_options(),
        )

    async def search(
        self,
        *,
        query: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        limit: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        page: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ProductSearchResponse:
        """
        Search products

        <p>Search for products you’ve previously created using Stripe’s <a href="/docs/search#search-query-language">Search Query Language</a>.
        Don’t use search in read-after-write flows where strict consistency is necessary. Under normal operating
        conditions, data is searchable in less than a minute. Occasionally, propagation of new or updated data can be up
        to an hour behind during outages. Search functionality is not available to merchants in India.</p>

        GET /v1/products/search

        Args:
            expand: Specifies which fields in the response should be expanded.
            limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            page: A cursor for pagination across multiple pages of results. Don't include this parameter on the first call. Use the next_page value returned in a previous response to request subsequent results.
            query: The search query string. See [search query language](https://stripe.com/docs/search#search-query-language) and the list of supported [query fields for products](https://stripe.com/docs/search#query-fields-for-products).
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.product.search(query="string")
        ```
        """
        models.ProductSearchResponse.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _query: QueryParams = {}
        encode_query_param(
            _query,
            "query",
            to_encodable(item=query, dump_with=str),
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
        if not isinstance(page, type_utils.NotGiven):
            encode_query_param(
                _query,
                "page",
                to_encodable(item=page, dump_with=str),
                style="form",
                explode=True,
            )
        return await self._base_client.request(
            method="GET",
            path="/v1/products/search",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.ProductSearchResponse,
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
    ) -> models.Product:
        """
        Retrieve a product

        <p>Retrieves the details of an existing product. Supply the unique product ID from either a product creation request or the product list, and Stripe will return the corresponding product information.</p>

        GET /v1/products/{id}

        Args:
            expand: Specifies which fields in the response should be expanded.
            id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.product.get(id="string")
        ```
        """
        models.Product.model_rebuild(_types_namespace=models._types_namespace)
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
            path=f"/v1/products/{id}",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.Product,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        name: str,
        active: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        default_price_data: typing.Union[
            typing.Optional[params.ProductCreateBodyDefaultPriceData],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        description: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        images: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        marketing_features: typing.Union[
            typing.Optional[typing.List[params.ProductCreateBodyMarketingFeaturesItem]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        metadata: typing.Union[
            typing.Optional[params.ProductCreateBodyMetadata], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        package_dimensions: typing.Union[
            typing.Optional[params.ProductCreateBodyPackageDimensions],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        shippable: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        statement_descriptor: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        tax_code: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        unit_label: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        url: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Product:
        """
        Create a product

        <p>Creates a new product object.</p>

        POST /v1/products

        Args:
            active: Whether the product is currently available for purchase. Defaults to `true`.
            default_price_data: Data used to generate a new [Price](https://stripe.com/docs/api/prices) object. This Price will be set as the default price for this product.
            description: The product's description, meant to be displayable to the customer. Use this field to optionally store a long form explanation of the product being sold for your own rendering purposes.
            expand: Specifies which fields in the response should be expanded.
            id: An identifier will be randomly generated by Stripe. You can optionally override this ID, but the ID must be unique across all products in your Stripe account.
            images: A list of up to 8 URLs of images for this product, meant to be displayable to the customer.
            marketing_features: A list of up to 15 marketing features for this product. These are displayed in [pricing tables](https://stripe.com/docs/payments/checkout/pricing-table).
            metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
            package_dimensions: The dimensions of this product for shipping purposes.
            shippable: Whether this product is shipped (i.e., physical goods).
            statement_descriptor: An arbitrary string to be displayed on your customer's credit card or bank statement. While most banks display this information consistently, some may display it incorrectly or not at all.

        This may be up to 22 characters. The statement description may not include `<`, `>`, `\`, `"`, `'` characters, and will appear on your customer's statement in capital letters. Non-ASCII characters are automatically stripped.
         It must contain at least one letter. Only used for subscription payments.
            tax_code: A [tax code](https://stripe.com/docs/tax/tax-categories) ID.
            unit_label: A label that represents units of this product. When set, this will be included in customers' receipts, invoices, Checkout, and the customer portal.
            url: A URL of a publicly-accessible webpage for this product.
            name: The product's name, meant to be displayable to the customer.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.product.create(name="string")
        ```
        """
        models.Product.model_rebuild(_types_namespace=models._types_namespace)
        _data = to_form_urlencoded(
            item={
                "active": active,
                "default_price_data": default_price_data,
                "description": description,
                "expand": expand,
                "id": id,
                "images": images,
                "marketing_features": marketing_features,
                "metadata": metadata,
                "package_dimensions": package_dimensions,
                "shippable": shippable,
                "statement_descriptor": statement_descriptor,
                "tax_code": tax_code,
                "unit_label": unit_label,
                "url": url,
                "name": name,
            },
            dump_with=params._SerializerProductCreateBody,
            style={
                "active": "form",
                "default_price_data": "deepObject",
                "description": "form",
                "expand": "deepObject",
                "id": "form",
                "images": "deepObject",
                "marketing_features": "deepObject",
                "metadata": "deepObject",
                "name": "form",
                "package_dimensions": "deepObject",
                "shippable": "form",
                "statement_descriptor": "form",
                "tax_code": "form",
                "unit_label": "form",
                "url": "form",
            },
            explode={
                "active": True,
                "default_price_data": True,
                "description": True,
                "expand": True,
                "id": True,
                "images": True,
                "marketing_features": True,
                "metadata": True,
                "name": True,
                "package_dimensions": True,
                "shippable": True,
                "statement_descriptor": True,
                "tax_code": True,
                "unit_label": True,
                "url": True,
            },
        )
        return await self._base_client.request(
            method="POST",
            path="/v1/products",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.Product,
            request_options=request_options or default_request_options(),
        )

    async def update(
        self,
        *,
        id: str,
        data: typing.Union[
            typing.Optional[params.ProductUpdateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Product:
        """
        Update a product

        <p>Updates the specific product by setting the values of the parameters passed. Any parameters not provided will be left unchanged.</p>

        POST /v1/products/{id}

        Args:
            data: ProductUpdateBody
            id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.product.update(id="string")
        ```
        """
        models.Product.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerProductUpdateBody,
                style={
                    "active": "form",
                    "default_price": "form",
                    "description": "deepObject",
                    "expand": "deepObject",
                    "images": "deepObject",
                    "marketing_features": "deepObject",
                    "metadata": "deepObject",
                    "name": "form",
                    "package_dimensions": "deepObject",
                    "shippable": "form",
                    "statement_descriptor": "form",
                    "tax_code": "deepObject",
                    "unit_label": "deepObject",
                    "url": "deepObject",
                },
                explode={
                    "active": True,
                    "default_price": True,
                    "description": True,
                    "expand": True,
                    "images": True,
                    "marketing_features": True,
                    "metadata": True,
                    "name": True,
                    "package_dimensions": True,
                    "shippable": True,
                    "statement_descriptor": True,
                    "tax_code": True,
                    "unit_label": True,
                    "url": True,
                },
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/products/{id}",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.Product,
            request_options=request_options or default_request_options(),
        )
