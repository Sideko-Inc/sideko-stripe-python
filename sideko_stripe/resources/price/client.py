import typing
import typing_extensions

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


class PriceClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def list(
        self,
        *,
        active: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        created: typing.Union[
            typing.Optional[typing.Union[params.PriceListCreatedObj0, int]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        currency: typing.Union[
            typing.Optional[str], type_utils.NotGiven
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
        lookup_keys: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        product: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        recurring: typing.Union[
            typing.Optional[params.PriceListRecurring], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        starting_after: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        type_: typing.Union[
            typing.Optional[typing_extensions.Literal["one_time", "recurring"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PriceListResponse:
        """
        List all prices

        <p>Returns a list of your active prices, excluding <a href="/docs/products-prices/pricing-models#inline-pricing">inline prices</a>. For the list of inactive prices, set <code>active</code> to false.</p>

        GET /v1/prices

        Args:
            active: Only return prices that are active or inactive (e.g., pass `false` to list all inactive prices).
            created: A filter on the list, based on the object `created` field. The value can be a string with an integer Unix timestamp, or it can be a dictionary with a number of different query options.
            currency: Only return prices for the given currency.
            ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            expand: Specifies which fields in the response should be expanded.
            limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            lookup_keys: Only return the price with these lookup_keys, if any exist. You can specify up to 10 lookup_keys.
            product: Only return prices for the given product.
            recurring: Only return prices with these recurring fields.
            starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
            type: Only return prices of type `recurring` or `one_time`.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.price.list()
        ```
        """
        models.PriceListResponse.model_rebuild(_types_namespace=models._types_namespace)
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
                    dump_with=typing.Union[params._SerializerPriceListCreatedObj0, int],
                ),
                style="deepObject",
                explode=True,
            )
        if not isinstance(currency, type_utils.NotGiven):
            encode_query_param(
                _query,
                "currency",
                to_encodable(item=currency, dump_with=str),
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
        if not isinstance(lookup_keys, type_utils.NotGiven):
            encode_query_param(
                _query,
                "lookup_keys",
                to_encodable(item=lookup_keys, dump_with=typing.List[str]),
                style="deepObject",
                explode=True,
            )
        if not isinstance(product, type_utils.NotGiven):
            encode_query_param(
                _query,
                "product",
                to_encodable(item=product, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(recurring, type_utils.NotGiven):
            encode_query_param(
                _query,
                "recurring",
                to_encodable(
                    item=recurring, dump_with=params._SerializerPriceListRecurring
                ),
                style="deepObject",
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
        if not isinstance(type_, type_utils.NotGiven):
            encode_query_param(
                _query,
                "type",
                to_encodable(
                    item=type_,
                    dump_with=typing_extensions.Literal["one_time", "recurring"],
                ),
                style="form",
                explode=True,
            )
        return self._base_client.request(
            method="GET",
            path="/v1/prices",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.PriceListResponse,
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
    ) -> models.PriceSearchResponse:
        """
        Search prices

        <p>Search for prices you’ve previously created using Stripe’s <a href="/docs/search#search-query-language">Search Query Language</a>.
        Don’t use search in read-after-write flows where strict consistency is necessary. Under normal operating
        conditions, data is searchable in less than a minute. Occasionally, propagation of new or updated data can be up
        to an hour behind during outages. Search functionality is not available to merchants in India.</p>

        GET /v1/prices/search

        Args:
            expand: Specifies which fields in the response should be expanded.
            limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            page: A cursor for pagination across multiple pages of results. Don't include this parameter on the first call. Use the next_page value returned in a previous response to request subsequent results.
            query: The search query string. See [search query language](https://stripe.com/docs/search#search-query-language) and the list of supported [query fields for prices](https://stripe.com/docs/search#query-fields-for-prices).
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.price.search(query="string")
        ```
        """
        models.PriceSearchResponse.model_rebuild(
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
            path="/v1/prices/search",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.PriceSearchResponse,
            request_options=request_options or default_request_options(),
        )

    def get(
        self,
        *,
        price: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Price:
        """
        Retrieve a price

        <p>Retrieves the price with the given ID.</p>

        GET /v1/prices/{price}

        Args:
            expand: Specifies which fields in the response should be expanded.
            price: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.price.get(price="string")
        ```
        """
        models.Price.model_rebuild(_types_namespace=models._types_namespace)
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
            path=f"/v1/prices/{price}",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.Price,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        currency: str,
        active: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        billing_scheme: typing.Union[
            typing.Optional[typing_extensions.Literal["per_unit", "tiered"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        currency_options: typing.Union[
            typing.Optional[params.PriceCreateBodyCurrencyOptions], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        custom_unit_amount: typing.Union[
            typing.Optional[params.PriceCreateBodyCustomUnitAmount], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        lookup_key: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        metadata: typing.Union[
            typing.Optional[params.PriceCreateBodyMetadata], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        nickname: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        product: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        product_data: typing.Union[
            typing.Optional[params.PriceCreateBodyProductData], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        recurring: typing.Union[
            typing.Optional[params.PriceCreateBodyRecurring], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        tax_behavior: typing.Union[
            typing.Optional[
                typing_extensions.Literal["exclusive", "inclusive", "unspecified"]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        tiers: typing.Union[
            typing.Optional[typing.List[params.PriceCreateBodyTiersItem]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        tiers_mode: typing.Union[
            typing.Optional[typing_extensions.Literal["graduated", "volume"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        transfer_lookup_key: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        transform_quantity: typing.Union[
            typing.Optional[params.PriceCreateBodyTransformQuantity],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        unit_amount: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        unit_amount_decimal: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Price:
        """
        Create a price

        <p>Creates a new <a href="https://docs.stripe.com/api/prices">Price</a> for an existing <a href="https://docs.stripe.com/api/products">Product</a>. The Price can be recurring or one-time.</p>

        POST /v1/prices

        Args:
            active: Whether the price can be used for new purchases. Defaults to `true`.
            billing_scheme: Describes how to compute the price per period. Either `per_unit` or `tiered`. `per_unit` indicates that the fixed amount (specified in `unit_amount` or `unit_amount_decimal`) will be charged per unit in `quantity` (for prices with `usage_type=licensed`), or per unit of total usage (for prices with `usage_type=metered`). `tiered` indicates that the unit pricing will be computed using a tiering strategy as defined using the `tiers` and `tiers_mode` attributes.
            currency_options: Prices defined in each available currency option. Each key must be a three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html) and a [supported currency](https://stripe.com/docs/currencies).
            custom_unit_amount: When set, provides configuration for the amount to be adjusted by the customer during Checkout Sessions and Payment Links.
            expand: Specifies which fields in the response should be expanded.
            lookup_key: A lookup key used to retrieve prices dynamically from a static string. This may be up to 200 characters.
            metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
            nickname: A brief description of the price, hidden from customers.
            product: The ID of the [Product](https://docs.stripe.com/api/products) that this [Price](https://docs.stripe.com/api/prices) will belong to.
            product_data: These fields can be used to create a new product that this price will belong to.
            recurring: The recurring components of a price such as `interval` and `usage_type`.
            tax_behavior: Only required if a [default tax behavior](https://stripe.com/docs/tax/products-prices-tax-categories-tax-behavior#setting-a-default-tax-behavior-(recommended)) was not provided in the Stripe Tax settings. Specifies whether the price is considered inclusive of taxes or exclusive of taxes. One of `inclusive`, `exclusive`, or `unspecified`. Once specified as either `inclusive` or `exclusive`, it cannot be changed.
            tiers: Each element represents a pricing tier. This parameter requires `billing_scheme` to be set to `tiered`. See also the documentation for `billing_scheme`.
            tiers_mode: Defines if the tiering price should be `graduated` or `volume` based. In `volume`-based tiering, the maximum quantity within a period determines the per unit price, in `graduated` tiering pricing can successively change as the quantity grows.
            transfer_lookup_key: If set to true, will atomically remove the lookup key from the existing price, and assign it to this price.
            transform_quantity: Apply a transformation to the reported usage or set quantity before computing the billed price. Cannot be combined with `tiers`.
            unit_amount: A positive integer in cents (or local equivalent) (or 0 for a free price) representing how much to charge. One of `unit_amount`, `unit_amount_decimal`, or `custom_unit_amount` is required, unless `billing_scheme=tiered`.
            unit_amount_decimal: Same as `unit_amount`, but accepts a decimal value in cents (or local equivalent) with at most 12 decimal places. Only one of `unit_amount` and `unit_amount_decimal` can be set.
            currency: Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.price.create(currency="string")
        ```
        """
        models.Price.model_rebuild(_types_namespace=models._types_namespace)
        _data = to_form_urlencoded(
            item={
                "active": active,
                "billing_scheme": billing_scheme,
                "currency_options": currency_options,
                "custom_unit_amount": custom_unit_amount,
                "expand": expand,
                "lookup_key": lookup_key,
                "metadata": metadata,
                "nickname": nickname,
                "product": product,
                "product_data": product_data,
                "recurring": recurring,
                "tax_behavior": tax_behavior,
                "tiers": tiers,
                "tiers_mode": tiers_mode,
                "transfer_lookup_key": transfer_lookup_key,
                "transform_quantity": transform_quantity,
                "unit_amount": unit_amount,
                "unit_amount_decimal": unit_amount_decimal,
                "currency": currency,
            },
            dump_with=params._SerializerPriceCreateBody,
            style={
                "active": "form",
                "billing_scheme": "form",
                "currency": "form",
                "currency_options": "deepObject",
                "custom_unit_amount": "deepObject",
                "expand": "deepObject",
                "lookup_key": "form",
                "metadata": "deepObject",
                "nickname": "form",
                "product": "form",
                "product_data": "deepObject",
                "recurring": "deepObject",
                "tax_behavior": "form",
                "tiers": "deepObject",
                "tiers_mode": "form",
                "transfer_lookup_key": "form",
                "transform_quantity": "deepObject",
                "unit_amount": "form",
                "unit_amount_decimal": "form",
            },
            explode={
                "active": True,
                "billing_scheme": True,
                "currency": True,
                "currency_options": True,
                "custom_unit_amount": True,
                "expand": True,
                "lookup_key": True,
                "metadata": True,
                "nickname": True,
                "product": True,
                "product_data": True,
                "recurring": True,
                "tax_behavior": True,
                "tiers": True,
                "tiers_mode": True,
                "transfer_lookup_key": True,
                "transform_quantity": True,
                "unit_amount": True,
                "unit_amount_decimal": True,
            },
        )
        return self._base_client.request(
            method="POST",
            path="/v1/prices",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.Price,
            request_options=request_options or default_request_options(),
        )

    def update(
        self,
        *,
        price: str,
        data: typing.Union[
            typing.Optional[params.PriceUpdateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Price:
        """
        Update a price

        <p>Updates the specified price by setting the values of the parameters passed. Any parameters not provided are left unchanged.</p>

        POST /v1/prices/{price}

        Args:
            data: PriceUpdateBody
            price: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.price.update(price="string")
        ```
        """
        models.Price.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerPriceUpdateBody,
                style={
                    "active": "form",
                    "currency_options": "deepObject",
                    "expand": "deepObject",
                    "lookup_key": "form",
                    "metadata": "deepObject",
                    "nickname": "form",
                    "tax_behavior": "form",
                    "transfer_lookup_key": "form",
                },
                explode={
                    "active": True,
                    "currency_options": True,
                    "expand": True,
                    "lookup_key": True,
                    "metadata": True,
                    "nickname": True,
                    "tax_behavior": True,
                    "transfer_lookup_key": True,
                },
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/prices/{price}",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.Price,
            request_options=request_options or default_request_options(),
        )


class AsyncPriceClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def list(
        self,
        *,
        active: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        created: typing.Union[
            typing.Optional[typing.Union[params.PriceListCreatedObj0, int]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        currency: typing.Union[
            typing.Optional[str], type_utils.NotGiven
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
        lookup_keys: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        product: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        recurring: typing.Union[
            typing.Optional[params.PriceListRecurring], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        starting_after: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        type_: typing.Union[
            typing.Optional[typing_extensions.Literal["one_time", "recurring"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PriceListResponse:
        """
        List all prices

        <p>Returns a list of your active prices, excluding <a href="/docs/products-prices/pricing-models#inline-pricing">inline prices</a>. For the list of inactive prices, set <code>active</code> to false.</p>

        GET /v1/prices

        Args:
            active: Only return prices that are active or inactive (e.g., pass `false` to list all inactive prices).
            created: A filter on the list, based on the object `created` field. The value can be a string with an integer Unix timestamp, or it can be a dictionary with a number of different query options.
            currency: Only return prices for the given currency.
            ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            expand: Specifies which fields in the response should be expanded.
            limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            lookup_keys: Only return the price with these lookup_keys, if any exist. You can specify up to 10 lookup_keys.
            product: Only return prices for the given product.
            recurring: Only return prices with these recurring fields.
            starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
            type: Only return prices of type `recurring` or `one_time`.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.price.list()
        ```
        """
        models.PriceListResponse.model_rebuild(_types_namespace=models._types_namespace)
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
                    dump_with=typing.Union[params._SerializerPriceListCreatedObj0, int],
                ),
                style="deepObject",
                explode=True,
            )
        if not isinstance(currency, type_utils.NotGiven):
            encode_query_param(
                _query,
                "currency",
                to_encodable(item=currency, dump_with=str),
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
        if not isinstance(lookup_keys, type_utils.NotGiven):
            encode_query_param(
                _query,
                "lookup_keys",
                to_encodable(item=lookup_keys, dump_with=typing.List[str]),
                style="deepObject",
                explode=True,
            )
        if not isinstance(product, type_utils.NotGiven):
            encode_query_param(
                _query,
                "product",
                to_encodable(item=product, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(recurring, type_utils.NotGiven):
            encode_query_param(
                _query,
                "recurring",
                to_encodable(
                    item=recurring, dump_with=params._SerializerPriceListRecurring
                ),
                style="deepObject",
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
        if not isinstance(type_, type_utils.NotGiven):
            encode_query_param(
                _query,
                "type",
                to_encodable(
                    item=type_,
                    dump_with=typing_extensions.Literal["one_time", "recurring"],
                ),
                style="form",
                explode=True,
            )
        return await self._base_client.request(
            method="GET",
            path="/v1/prices",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.PriceListResponse,
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
    ) -> models.PriceSearchResponse:
        """
        Search prices

        <p>Search for prices you’ve previously created using Stripe’s <a href="/docs/search#search-query-language">Search Query Language</a>.
        Don’t use search in read-after-write flows where strict consistency is necessary. Under normal operating
        conditions, data is searchable in less than a minute. Occasionally, propagation of new or updated data can be up
        to an hour behind during outages. Search functionality is not available to merchants in India.</p>

        GET /v1/prices/search

        Args:
            expand: Specifies which fields in the response should be expanded.
            limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            page: A cursor for pagination across multiple pages of results. Don't include this parameter on the first call. Use the next_page value returned in a previous response to request subsequent results.
            query: The search query string. See [search query language](https://stripe.com/docs/search#search-query-language) and the list of supported [query fields for prices](https://stripe.com/docs/search#query-fields-for-prices).
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.price.search(query="string")
        ```
        """
        models.PriceSearchResponse.model_rebuild(
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
            path="/v1/prices/search",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.PriceSearchResponse,
            request_options=request_options or default_request_options(),
        )

    async def get(
        self,
        *,
        price: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Price:
        """
        Retrieve a price

        <p>Retrieves the price with the given ID.</p>

        GET /v1/prices/{price}

        Args:
            expand: Specifies which fields in the response should be expanded.
            price: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.price.get(price="string")
        ```
        """
        models.Price.model_rebuild(_types_namespace=models._types_namespace)
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
            path=f"/v1/prices/{price}",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.Price,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        currency: str,
        active: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        billing_scheme: typing.Union[
            typing.Optional[typing_extensions.Literal["per_unit", "tiered"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        currency_options: typing.Union[
            typing.Optional[params.PriceCreateBodyCurrencyOptions], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        custom_unit_amount: typing.Union[
            typing.Optional[params.PriceCreateBodyCustomUnitAmount], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        lookup_key: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        metadata: typing.Union[
            typing.Optional[params.PriceCreateBodyMetadata], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        nickname: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        product: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        product_data: typing.Union[
            typing.Optional[params.PriceCreateBodyProductData], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        recurring: typing.Union[
            typing.Optional[params.PriceCreateBodyRecurring], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        tax_behavior: typing.Union[
            typing.Optional[
                typing_extensions.Literal["exclusive", "inclusive", "unspecified"]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        tiers: typing.Union[
            typing.Optional[typing.List[params.PriceCreateBodyTiersItem]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        tiers_mode: typing.Union[
            typing.Optional[typing_extensions.Literal["graduated", "volume"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        transfer_lookup_key: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        transform_quantity: typing.Union[
            typing.Optional[params.PriceCreateBodyTransformQuantity],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        unit_amount: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        unit_amount_decimal: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Price:
        """
        Create a price

        <p>Creates a new <a href="https://docs.stripe.com/api/prices">Price</a> for an existing <a href="https://docs.stripe.com/api/products">Product</a>. The Price can be recurring or one-time.</p>

        POST /v1/prices

        Args:
            active: Whether the price can be used for new purchases. Defaults to `true`.
            billing_scheme: Describes how to compute the price per period. Either `per_unit` or `tiered`. `per_unit` indicates that the fixed amount (specified in `unit_amount` or `unit_amount_decimal`) will be charged per unit in `quantity` (for prices with `usage_type=licensed`), or per unit of total usage (for prices with `usage_type=metered`). `tiered` indicates that the unit pricing will be computed using a tiering strategy as defined using the `tiers` and `tiers_mode` attributes.
            currency_options: Prices defined in each available currency option. Each key must be a three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html) and a [supported currency](https://stripe.com/docs/currencies).
            custom_unit_amount: When set, provides configuration for the amount to be adjusted by the customer during Checkout Sessions and Payment Links.
            expand: Specifies which fields in the response should be expanded.
            lookup_key: A lookup key used to retrieve prices dynamically from a static string. This may be up to 200 characters.
            metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
            nickname: A brief description of the price, hidden from customers.
            product: The ID of the [Product](https://docs.stripe.com/api/products) that this [Price](https://docs.stripe.com/api/prices) will belong to.
            product_data: These fields can be used to create a new product that this price will belong to.
            recurring: The recurring components of a price such as `interval` and `usage_type`.
            tax_behavior: Only required if a [default tax behavior](https://stripe.com/docs/tax/products-prices-tax-categories-tax-behavior#setting-a-default-tax-behavior-(recommended)) was not provided in the Stripe Tax settings. Specifies whether the price is considered inclusive of taxes or exclusive of taxes. One of `inclusive`, `exclusive`, or `unspecified`. Once specified as either `inclusive` or `exclusive`, it cannot be changed.
            tiers: Each element represents a pricing tier. This parameter requires `billing_scheme` to be set to `tiered`. See also the documentation for `billing_scheme`.
            tiers_mode: Defines if the tiering price should be `graduated` or `volume` based. In `volume`-based tiering, the maximum quantity within a period determines the per unit price, in `graduated` tiering pricing can successively change as the quantity grows.
            transfer_lookup_key: If set to true, will atomically remove the lookup key from the existing price, and assign it to this price.
            transform_quantity: Apply a transformation to the reported usage or set quantity before computing the billed price. Cannot be combined with `tiers`.
            unit_amount: A positive integer in cents (or local equivalent) (or 0 for a free price) representing how much to charge. One of `unit_amount`, `unit_amount_decimal`, or `custom_unit_amount` is required, unless `billing_scheme=tiered`.
            unit_amount_decimal: Same as `unit_amount`, but accepts a decimal value in cents (or local equivalent) with at most 12 decimal places. Only one of `unit_amount` and `unit_amount_decimal` can be set.
            currency: Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.price.create(currency="string")
        ```
        """
        models.Price.model_rebuild(_types_namespace=models._types_namespace)
        _data = to_form_urlencoded(
            item={
                "active": active,
                "billing_scheme": billing_scheme,
                "currency_options": currency_options,
                "custom_unit_amount": custom_unit_amount,
                "expand": expand,
                "lookup_key": lookup_key,
                "metadata": metadata,
                "nickname": nickname,
                "product": product,
                "product_data": product_data,
                "recurring": recurring,
                "tax_behavior": tax_behavior,
                "tiers": tiers,
                "tiers_mode": tiers_mode,
                "transfer_lookup_key": transfer_lookup_key,
                "transform_quantity": transform_quantity,
                "unit_amount": unit_amount,
                "unit_amount_decimal": unit_amount_decimal,
                "currency": currency,
            },
            dump_with=params._SerializerPriceCreateBody,
            style={
                "active": "form",
                "billing_scheme": "form",
                "currency": "form",
                "currency_options": "deepObject",
                "custom_unit_amount": "deepObject",
                "expand": "deepObject",
                "lookup_key": "form",
                "metadata": "deepObject",
                "nickname": "form",
                "product": "form",
                "product_data": "deepObject",
                "recurring": "deepObject",
                "tax_behavior": "form",
                "tiers": "deepObject",
                "tiers_mode": "form",
                "transfer_lookup_key": "form",
                "transform_quantity": "deepObject",
                "unit_amount": "form",
                "unit_amount_decimal": "form",
            },
            explode={
                "active": True,
                "billing_scheme": True,
                "currency": True,
                "currency_options": True,
                "custom_unit_amount": True,
                "expand": True,
                "lookup_key": True,
                "metadata": True,
                "nickname": True,
                "product": True,
                "product_data": True,
                "recurring": True,
                "tax_behavior": True,
                "tiers": True,
                "tiers_mode": True,
                "transfer_lookup_key": True,
                "transform_quantity": True,
                "unit_amount": True,
                "unit_amount_decimal": True,
            },
        )
        return await self._base_client.request(
            method="POST",
            path="/v1/prices",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.Price,
            request_options=request_options or default_request_options(),
        )

    async def update(
        self,
        *,
        price: str,
        data: typing.Union[
            typing.Optional[params.PriceUpdateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Price:
        """
        Update a price

        <p>Updates the specified price by setting the values of the parameters passed. Any parameters not provided are left unchanged.</p>

        POST /v1/prices/{price}

        Args:
            data: PriceUpdateBody
            price: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.price.update(price="string")
        ```
        """
        models.Price.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerPriceUpdateBody,
                style={
                    "active": "form",
                    "currency_options": "deepObject",
                    "expand": "deepObject",
                    "lookup_key": "form",
                    "metadata": "deepObject",
                    "nickname": "form",
                    "tax_behavior": "form",
                    "transfer_lookup_key": "form",
                },
                explode={
                    "active": True,
                    "currency_options": True,
                    "expand": True,
                    "lookup_key": True,
                    "metadata": True,
                    "nickname": True,
                    "tax_behavior": True,
                    "transfer_lookup_key": True,
                },
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/prices/{price}",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.Price,
            request_options=request_options or default_request_options(),
        )
