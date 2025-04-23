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


class ShippingRateClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def list(
        self,
        *,
        active: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        created: typing.Union[
            typing.Optional[typing.Union[params.ShippingRateListCreatedObj0, int]],
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
        starting_after: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ShippingRateListResponse:
        """
        List all shipping rates

        <p>Returns a list of your shipping rates.</p>

        GET /v1/shipping_rates

        Args:
            active: Only return shipping rates that are active or inactive.
            created: A filter on the list, based on the object `created` field. The value can be a string with an integer Unix timestamp, or it can be a dictionary with a number of different query options.
            currency: Only return shipping rates for the given currency.
            ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            expand: Specifies which fields in the response should be expanded.
            limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.shipping_rate.list()
        ```
        """
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
                        params._SerializerShippingRateListCreatedObj0, int
                    ],
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
            path="/v1/shipping_rates",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.ShippingRateListResponse,
            request_options=request_options or default_request_options(),
        )

    def get(
        self,
        *,
        shipping_rate_token: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ShippingRate:
        """
        Retrieve a shipping rate

        <p>Returns the shipping rate object with the given ID.</p>

        GET /v1/shipping_rates/{shipping_rate_token}

        Args:
            expand: Specifies which fields in the response should be expanded.
            shipping_rate_token: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.shipping_rate.get(shipping_rate_token="string")
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
            path=f"/v1/shipping_rates/{shipping_rate_token}",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.ShippingRate,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        display_name: str,
        delivery_estimate: typing.Union[
            typing.Optional[params.ShippingRateCreateBodyDeliveryEstimate],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        fixed_amount: typing.Union[
            typing.Optional[params.ShippingRateCreateBodyFixedAmount],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        metadata: typing.Union[
            typing.Optional[params.ShippingRateCreateBodyMetadata], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        tax_behavior: typing.Union[
            typing.Optional[
                typing_extensions.Literal["exclusive", "inclusive", "unspecified"]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        tax_code: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        type_: typing.Union[
            typing.Optional[typing_extensions.Literal["fixed_amount"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ShippingRate:
        """
        Create a shipping rate

        <p>Creates a new shipping rate object.</p>

        POST /v1/shipping_rates

        Args:
            delivery_estimate: The estimated range for how long shipping will take, meant to be displayable to the customer. This will appear on CheckoutSessions.
            expand: Specifies which fields in the response should be expanded.
            fixed_amount: Describes a fixed amount to charge for shipping. Must be present if type is `fixed_amount`.
            metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
            tax_behavior: Specifies whether the rate is considered inclusive of taxes or exclusive of taxes. One of `inclusive`, `exclusive`, or `unspecified`.
            tax_code: A [tax code](https://stripe.com/docs/tax/tax-categories) ID. The Shipping tax code is `txcd_92010001`.
            type: The type of calculation to use on the shipping rate.
            display_name: The name of the shipping rate, meant to be displayable to the customer. This will appear on CheckoutSessions.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.shipping_rate.create(display_name="string")
        ```
        """
        _data = to_form_urlencoded(
            item={
                "delivery_estimate": delivery_estimate,
                "expand": expand,
                "fixed_amount": fixed_amount,
                "metadata": metadata,
                "tax_behavior": tax_behavior,
                "tax_code": tax_code,
                "type_": type_,
                "display_name": display_name,
            },
            dump_with=params._SerializerShippingRateCreateBody,
            style={
                "delivery_estimate": "deepObject",
                "display_name": "form",
                "expand": "deepObject",
                "fixed_amount": "deepObject",
                "metadata": "deepObject",
                "tax_behavior": "form",
                "tax_code": "form",
                "type": "form",
            },
            explode={
                "delivery_estimate": True,
                "display_name": True,
                "expand": True,
                "fixed_amount": True,
                "metadata": True,
                "tax_behavior": True,
                "tax_code": True,
                "type": True,
            },
        )
        return self._base_client.request(
            method="POST",
            path="/v1/shipping_rates",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.ShippingRate,
            request_options=request_options or default_request_options(),
        )

    def update(
        self,
        *,
        shipping_rate_token: str,
        data: typing.Union[
            typing.Optional[params.ShippingRateUpdateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ShippingRate:
        """
        Update a shipping rate

        <p>Updates an existing shipping rate object.</p>

        POST /v1/shipping_rates/{shipping_rate_token}

        Args:
            data: ShippingRateUpdateBody
            shipping_rate_token: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.shipping_rate.update(shipping_rate_token="string")
        ```
        """
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerShippingRateUpdateBody,
                style={
                    "active": "form",
                    "expand": "deepObject",
                    "fixed_amount": "deepObject",
                    "metadata": "deepObject",
                    "tax_behavior": "form",
                },
                explode={
                    "active": True,
                    "expand": True,
                    "fixed_amount": True,
                    "metadata": True,
                    "tax_behavior": True,
                },
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/shipping_rates/{shipping_rate_token}",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.ShippingRate,
            request_options=request_options or default_request_options(),
        )


class AsyncShippingRateClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def list(
        self,
        *,
        active: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        created: typing.Union[
            typing.Optional[typing.Union[params.ShippingRateListCreatedObj0, int]],
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
        starting_after: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ShippingRateListResponse:
        """
        List all shipping rates

        <p>Returns a list of your shipping rates.</p>

        GET /v1/shipping_rates

        Args:
            active: Only return shipping rates that are active or inactive.
            created: A filter on the list, based on the object `created` field. The value can be a string with an integer Unix timestamp, or it can be a dictionary with a number of different query options.
            currency: Only return shipping rates for the given currency.
            ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            expand: Specifies which fields in the response should be expanded.
            limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.shipping_rate.list()
        ```
        """
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
                        params._SerializerShippingRateListCreatedObj0, int
                    ],
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
            path="/v1/shipping_rates",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.ShippingRateListResponse,
            request_options=request_options or default_request_options(),
        )

    async def get(
        self,
        *,
        shipping_rate_token: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ShippingRate:
        """
        Retrieve a shipping rate

        <p>Returns the shipping rate object with the given ID.</p>

        GET /v1/shipping_rates/{shipping_rate_token}

        Args:
            expand: Specifies which fields in the response should be expanded.
            shipping_rate_token: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.shipping_rate.get(shipping_rate_token="string")
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
            path=f"/v1/shipping_rates/{shipping_rate_token}",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.ShippingRate,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        display_name: str,
        delivery_estimate: typing.Union[
            typing.Optional[params.ShippingRateCreateBodyDeliveryEstimate],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        fixed_amount: typing.Union[
            typing.Optional[params.ShippingRateCreateBodyFixedAmount],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        metadata: typing.Union[
            typing.Optional[params.ShippingRateCreateBodyMetadata], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        tax_behavior: typing.Union[
            typing.Optional[
                typing_extensions.Literal["exclusive", "inclusive", "unspecified"]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        tax_code: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        type_: typing.Union[
            typing.Optional[typing_extensions.Literal["fixed_amount"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ShippingRate:
        """
        Create a shipping rate

        <p>Creates a new shipping rate object.</p>

        POST /v1/shipping_rates

        Args:
            delivery_estimate: The estimated range for how long shipping will take, meant to be displayable to the customer. This will appear on CheckoutSessions.
            expand: Specifies which fields in the response should be expanded.
            fixed_amount: Describes a fixed amount to charge for shipping. Must be present if type is `fixed_amount`.
            metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
            tax_behavior: Specifies whether the rate is considered inclusive of taxes or exclusive of taxes. One of `inclusive`, `exclusive`, or `unspecified`.
            tax_code: A [tax code](https://stripe.com/docs/tax/tax-categories) ID. The Shipping tax code is `txcd_92010001`.
            type: The type of calculation to use on the shipping rate.
            display_name: The name of the shipping rate, meant to be displayable to the customer. This will appear on CheckoutSessions.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.shipping_rate.create(display_name="string")
        ```
        """
        _data = to_form_urlencoded(
            item={
                "delivery_estimate": delivery_estimate,
                "expand": expand,
                "fixed_amount": fixed_amount,
                "metadata": metadata,
                "tax_behavior": tax_behavior,
                "tax_code": tax_code,
                "type_": type_,
                "display_name": display_name,
            },
            dump_with=params._SerializerShippingRateCreateBody,
            style={
                "delivery_estimate": "deepObject",
                "display_name": "form",
                "expand": "deepObject",
                "fixed_amount": "deepObject",
                "metadata": "deepObject",
                "tax_behavior": "form",
                "tax_code": "form",
                "type": "form",
            },
            explode={
                "delivery_estimate": True,
                "display_name": True,
                "expand": True,
                "fixed_amount": True,
                "metadata": True,
                "tax_behavior": True,
                "tax_code": True,
                "type": True,
            },
        )
        return await self._base_client.request(
            method="POST",
            path="/v1/shipping_rates",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.ShippingRate,
            request_options=request_options or default_request_options(),
        )

    async def update(
        self,
        *,
        shipping_rate_token: str,
        data: typing.Union[
            typing.Optional[params.ShippingRateUpdateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ShippingRate:
        """
        Update a shipping rate

        <p>Updates an existing shipping rate object.</p>

        POST /v1/shipping_rates/{shipping_rate_token}

        Args:
            data: ShippingRateUpdateBody
            shipping_rate_token: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.shipping_rate.update(shipping_rate_token="string")
        ```
        """
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerShippingRateUpdateBody,
                style={
                    "active": "form",
                    "expand": "deepObject",
                    "fixed_amount": "deepObject",
                    "metadata": "deepObject",
                    "tax_behavior": "form",
                },
                explode={
                    "active": True,
                    "expand": True,
                    "fixed_amount": True,
                    "metadata": True,
                    "tax_behavior": True,
                },
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/shipping_rates/{shipping_rate_token}",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.ShippingRate,
            request_options=request_options or default_request_options(),
        )
