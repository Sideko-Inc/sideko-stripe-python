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


class OrderClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def list(
        self,
        *,
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
    ) -> models.ClimateOrderListResponse:
        """
        List orders

        <p>Lists all Climate order objects. The orders are returned sorted by creation date, with the
        most recently created orders appearing first.</p>

        GET /v1/climate/orders

        Args:
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
        client.climate.order.list()
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
            path="/v1/climate/orders",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.ClimateOrderListResponse,
            request_options=request_options or default_request_options(),
        )

    def get(
        self,
        *,
        order: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ClimateOrder:
        """
        Retrieve an order

        <p>Retrieves the details of a Climate order object with the given ID.</p>

        GET /v1/climate/orders/{order}

        Args:
            expand: Specifies which fields in the response should be expanded.
            order: Unique identifier of the order.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.climate.order.get(order="string")
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
            path=f"/v1/climate/orders/{order}",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.ClimateOrder,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        product: str,
        amount: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        beneficiary: typing.Union[
            typing.Optional[params.ClimateOrderCreateBodyBeneficiary],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        currency: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        metadata: typing.Union[
            typing.Optional[params.ClimateOrderCreateBodyMetadata], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        metric_tons: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ClimateOrder:
        """
        Create an order

        <p>Creates a Climate order object for a given Climate product. The order will be processed immediately
        after creation and payment will be deducted your Stripe balance.</p>

        POST /v1/climate/orders

        Args:
            amount: Requested amount of carbon removal units. Either this or `metric_tons` must be specified.
            beneficiary: Publicly sharable reference for the end beneficiary of carbon removal. Assumed to be the Stripe account if not set.
            currency: Request currency for the order as a three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a supported [settlement currency for your account](https://stripe.com/docs/currencies). If omitted, the account's default currency will be used.
            expand: Specifies which fields in the response should be expanded.
            metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
            metric_tons: Requested number of tons for the order. Either this or `amount` must be specified.
            product: Unique identifier of the Climate product.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.climate.order.create(product="string")
        ```
        """
        _data = to_form_urlencoded(
            item={
                "amount": amount,
                "beneficiary": beneficiary,
                "currency": currency,
                "expand": expand,
                "metadata": metadata,
                "metric_tons": metric_tons,
                "product": product,
            },
            dump_with=params._SerializerClimateOrderCreateBody,
            style={
                "amount": "form",
                "beneficiary": "deepObject",
                "currency": "form",
                "expand": "deepObject",
                "metadata": "deepObject",
                "metric_tons": "form",
                "product": "form",
            },
            explode={
                "amount": True,
                "beneficiary": True,
                "currency": True,
                "expand": True,
                "metadata": True,
                "metric_tons": True,
                "product": True,
            },
        )
        return self._base_client.request(
            method="POST",
            path="/v1/climate/orders",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.ClimateOrder,
            request_options=request_options or default_request_options(),
        )

    def update(
        self,
        *,
        order: str,
        data: typing.Union[
            typing.Optional[params.ClimateOrderUpdateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ClimateOrder:
        """
        Update an order

        <p>Updates the specified order by setting the values of the parameters passed.</p>

        POST /v1/climate/orders/{order}

        Args:
            data: ClimateOrderUpdateBody
            order: Unique identifier of the order.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.climate.order.update(order="string")
        ```
        """
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerClimateOrderUpdateBody,
                style={
                    "beneficiary": "deepObject",
                    "expand": "deepObject",
                    "metadata": "deepObject",
                },
                explode={"beneficiary": True, "expand": True, "metadata": True},
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/climate/orders/{order}",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.ClimateOrder,
            request_options=request_options or default_request_options(),
        )

    def cancel(
        self,
        *,
        order: str,
        data: typing.Union[
            typing.Optional[params.ClimateOrderCancelBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ClimateOrder:
        """
        Cancel an order

        <p>Cancels a Climate order. You can cancel an order within 24 hours of creation. Stripe refunds the
        reservation <code>amount_subtotal</code>, but not the <code>amount_fees</code> for user-triggered cancellations. Frontier
        might cancel reservations if suppliers fail to deliver. If Frontier cancels the reservation, Stripe
        provides 90 days advance notice and refunds the <code>amount_total</code>.</p>

        POST /v1/climate/orders/{order}/cancel

        Args:
            data: ClimateOrderCancelBody
            order: Unique identifier of the order.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.climate.order.cancel(order="string")
        ```
        """
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerClimateOrderCancelBody,
                style={"expand": "deepObject"},
                explode={"expand": True},
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/climate/orders/{order}/cancel",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.ClimateOrder,
            request_options=request_options or default_request_options(),
        )


class AsyncOrderClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def list(
        self,
        *,
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
    ) -> models.ClimateOrderListResponse:
        """
        List orders

        <p>Lists all Climate order objects. The orders are returned sorted by creation date, with the
        most recently created orders appearing first.</p>

        GET /v1/climate/orders

        Args:
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
        await client.climate.order.list()
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
            path="/v1/climate/orders",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.ClimateOrderListResponse,
            request_options=request_options or default_request_options(),
        )

    async def get(
        self,
        *,
        order: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ClimateOrder:
        """
        Retrieve an order

        <p>Retrieves the details of a Climate order object with the given ID.</p>

        GET /v1/climate/orders/{order}

        Args:
            expand: Specifies which fields in the response should be expanded.
            order: Unique identifier of the order.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.climate.order.get(order="string")
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
            path=f"/v1/climate/orders/{order}",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.ClimateOrder,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        product: str,
        amount: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        beneficiary: typing.Union[
            typing.Optional[params.ClimateOrderCreateBodyBeneficiary],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        currency: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        metadata: typing.Union[
            typing.Optional[params.ClimateOrderCreateBodyMetadata], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        metric_tons: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ClimateOrder:
        """
        Create an order

        <p>Creates a Climate order object for a given Climate product. The order will be processed immediately
        after creation and payment will be deducted your Stripe balance.</p>

        POST /v1/climate/orders

        Args:
            amount: Requested amount of carbon removal units. Either this or `metric_tons` must be specified.
            beneficiary: Publicly sharable reference for the end beneficiary of carbon removal. Assumed to be the Stripe account if not set.
            currency: Request currency for the order as a three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a supported [settlement currency for your account](https://stripe.com/docs/currencies). If omitted, the account's default currency will be used.
            expand: Specifies which fields in the response should be expanded.
            metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
            metric_tons: Requested number of tons for the order. Either this or `amount` must be specified.
            product: Unique identifier of the Climate product.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.climate.order.create(product="string")
        ```
        """
        _data = to_form_urlencoded(
            item={
                "amount": amount,
                "beneficiary": beneficiary,
                "currency": currency,
                "expand": expand,
                "metadata": metadata,
                "metric_tons": metric_tons,
                "product": product,
            },
            dump_with=params._SerializerClimateOrderCreateBody,
            style={
                "amount": "form",
                "beneficiary": "deepObject",
                "currency": "form",
                "expand": "deepObject",
                "metadata": "deepObject",
                "metric_tons": "form",
                "product": "form",
            },
            explode={
                "amount": True,
                "beneficiary": True,
                "currency": True,
                "expand": True,
                "metadata": True,
                "metric_tons": True,
                "product": True,
            },
        )
        return await self._base_client.request(
            method="POST",
            path="/v1/climate/orders",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.ClimateOrder,
            request_options=request_options or default_request_options(),
        )

    async def update(
        self,
        *,
        order: str,
        data: typing.Union[
            typing.Optional[params.ClimateOrderUpdateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ClimateOrder:
        """
        Update an order

        <p>Updates the specified order by setting the values of the parameters passed.</p>

        POST /v1/climate/orders/{order}

        Args:
            data: ClimateOrderUpdateBody
            order: Unique identifier of the order.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.climate.order.update(order="string")
        ```
        """
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerClimateOrderUpdateBody,
                style={
                    "beneficiary": "deepObject",
                    "expand": "deepObject",
                    "metadata": "deepObject",
                },
                explode={"beneficiary": True, "expand": True, "metadata": True},
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/climate/orders/{order}",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.ClimateOrder,
            request_options=request_options or default_request_options(),
        )

    async def cancel(
        self,
        *,
        order: str,
        data: typing.Union[
            typing.Optional[params.ClimateOrderCancelBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ClimateOrder:
        """
        Cancel an order

        <p>Cancels a Climate order. You can cancel an order within 24 hours of creation. Stripe refunds the
        reservation <code>amount_subtotal</code>, but not the <code>amount_fees</code> for user-triggered cancellations. Frontier
        might cancel reservations if suppliers fail to deliver. If Frontier cancels the reservation, Stripe
        provides 90 days advance notice and refunds the <code>amount_total</code>.</p>

        POST /v1/climate/orders/{order}/cancel

        Args:
            data: ClimateOrderCancelBody
            order: Unique identifier of the order.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.climate.order.cancel(order="string")
        ```
        """
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerClimateOrderCancelBody,
                style={"expand": "deepObject"},
                explode={"expand": True},
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/climate/orders/{order}/cancel",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.ClimateOrder,
            request_options=request_options or default_request_options(),
        )
