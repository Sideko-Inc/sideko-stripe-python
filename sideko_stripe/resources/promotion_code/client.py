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


class PromotionCodeClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def list(
        self,
        *,
        active: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        code: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        coupon: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        created: typing.Union[
            typing.Optional[typing.Union[params.PromotionCodeListCreatedObj0, int]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        customer: typing.Union[
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
    ) -> models.PromotionCodeListResponse:
        """
        List all promotion codes

        <p>Returns a list of your promotion codes.</p>

        GET /v1/promotion_codes

        Args:
            active: Filter promotion codes by whether they are active.
            code: Only return promotion codes that have this case-insensitive code.
            coupon: Only return promotion codes for this coupon.
            created: A filter on the list, based on the object `created` field. The value can be a string with an integer Unix timestamp, or it can be a dictionary with a number of different query options.
            customer: Only return promotion codes that are restricted to this customer.
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
        client.promotion_code.list()
        ```
        """
        models.PromotionCodeListResponse.model_rebuild(
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
        if not isinstance(code, type_utils.NotGiven):
            encode_query_param(
                _query,
                "code",
                to_encodable(item=code, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(coupon, type_utils.NotGiven):
            encode_query_param(
                _query,
                "coupon",
                to_encodable(item=coupon, dump_with=str),
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
                        params._SerializerPromotionCodeListCreatedObj0, int
                    ],
                ),
                style="deepObject",
                explode=True,
            )
        if not isinstance(customer, type_utils.NotGiven):
            encode_query_param(
                _query,
                "customer",
                to_encodable(item=customer, dump_with=str),
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
            path="/v1/promotion_codes",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.PromotionCodeListResponse,
            request_options=request_options or default_request_options(),
        )

    def get(
        self,
        *,
        promotion_code: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PromotionCode:
        """
        Retrieve a promotion code

        <p>Retrieves the promotion code with the given ID. In order to retrieve a promotion code by the customer-facing <code>code</code> use <a href="/docs/api/promotion_codes/list">list</a> with the desired <code>code</code>.</p>

        GET /v1/promotion_codes/{promotion_code}

        Args:
            expand: Specifies which fields in the response should be expanded.
            promotion_code: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.promotion_code.get(promotion_code="string")
        ```
        """
        models.PromotionCode.model_rebuild(_types_namespace=models._types_namespace)
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
            path=f"/v1/promotion_codes/{promotion_code}",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.PromotionCode,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        coupon: str,
        active: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        code: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        customer: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        expires_at: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        max_redemptions: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        metadata: typing.Union[
            typing.Optional[params.PromotionCodeCreateBodyMetadata], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        restrictions: typing.Union[
            typing.Optional[params.PromotionCodeCreateBodyRestrictions],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PromotionCode:
        """
        Create a promotion code

        <p>A promotion code points to a coupon. You can optionally restrict the code to a specific customer, redemption limit, and expiration date.</p>

        POST /v1/promotion_codes

        Args:
            active: Whether the promotion code is currently active.
            code: The customer-facing code. Regardless of case, this code must be unique across all active promotion codes for a specific customer. Valid characters are lower case letters (a-z), upper case letters (A-Z), and digits (0-9).

        If left blank, we will generate one automatically.
            customer: The customer that this promotion code can be used by. If not set, the promotion code can be used by all customers.
            expand: Specifies which fields in the response should be expanded.
            expires_at: The timestamp at which this promotion code will expire. If the coupon has specified a `redeems_by`, then this value cannot be after the coupon's `redeems_by`.
            max_redemptions: A positive integer specifying the number of times the promotion code can be redeemed. If the coupon has specified a `max_redemptions`, then this value cannot be greater than the coupon's `max_redemptions`.
            metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
            restrictions: Settings that restrict the redemption of the promotion code.
            coupon: The coupon for this promotion code.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.promotion_code.create(coupon="string")
        ```
        """
        models.PromotionCode.model_rebuild(_types_namespace=models._types_namespace)
        _data = to_form_urlencoded(
            item={
                "active": active,
                "code": code,
                "customer": customer,
                "expand": expand,
                "expires_at": expires_at,
                "max_redemptions": max_redemptions,
                "metadata": metadata,
                "restrictions": restrictions,
                "coupon": coupon,
            },
            dump_with=params._SerializerPromotionCodeCreateBody,
            style={
                "active": "form",
                "code": "form",
                "coupon": "form",
                "customer": "form",
                "expand": "deepObject",
                "expires_at": "form",
                "max_redemptions": "form",
                "metadata": "deepObject",
                "restrictions": "deepObject",
            },
            explode={
                "active": True,
                "code": True,
                "coupon": True,
                "customer": True,
                "expand": True,
                "expires_at": True,
                "max_redemptions": True,
                "metadata": True,
                "restrictions": True,
            },
        )
        return self._base_client.request(
            method="POST",
            path="/v1/promotion_codes",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.PromotionCode,
            request_options=request_options or default_request_options(),
        )

    def update(
        self,
        *,
        promotion_code: str,
        data: typing.Union[
            typing.Optional[params.PromotionCodeUpdateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PromotionCode:
        """
        Update a promotion code

        <p>Updates the specified promotion code by setting the values of the parameters passed. Most fields are, by design, not editable.</p>

        POST /v1/promotion_codes/{promotion_code}

        Args:
            data: PromotionCodeUpdateBody
            promotion_code: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.promotion_code.update(promotion_code="string")
        ```
        """
        models.PromotionCode.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerPromotionCodeUpdateBody,
                style={
                    "active": "form",
                    "expand": "deepObject",
                    "metadata": "deepObject",
                    "restrictions": "deepObject",
                },
                explode={
                    "active": True,
                    "expand": True,
                    "metadata": True,
                    "restrictions": True,
                },
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/promotion_codes/{promotion_code}",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.PromotionCode,
            request_options=request_options or default_request_options(),
        )


class AsyncPromotionCodeClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def list(
        self,
        *,
        active: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        code: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        coupon: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        created: typing.Union[
            typing.Optional[typing.Union[params.PromotionCodeListCreatedObj0, int]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        customer: typing.Union[
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
    ) -> models.PromotionCodeListResponse:
        """
        List all promotion codes

        <p>Returns a list of your promotion codes.</p>

        GET /v1/promotion_codes

        Args:
            active: Filter promotion codes by whether they are active.
            code: Only return promotion codes that have this case-insensitive code.
            coupon: Only return promotion codes for this coupon.
            created: A filter on the list, based on the object `created` field. The value can be a string with an integer Unix timestamp, or it can be a dictionary with a number of different query options.
            customer: Only return promotion codes that are restricted to this customer.
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
        await client.promotion_code.list()
        ```
        """
        models.PromotionCodeListResponse.model_rebuild(
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
        if not isinstance(code, type_utils.NotGiven):
            encode_query_param(
                _query,
                "code",
                to_encodable(item=code, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(coupon, type_utils.NotGiven):
            encode_query_param(
                _query,
                "coupon",
                to_encodable(item=coupon, dump_with=str),
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
                        params._SerializerPromotionCodeListCreatedObj0, int
                    ],
                ),
                style="deepObject",
                explode=True,
            )
        if not isinstance(customer, type_utils.NotGiven):
            encode_query_param(
                _query,
                "customer",
                to_encodable(item=customer, dump_with=str),
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
            path="/v1/promotion_codes",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.PromotionCodeListResponse,
            request_options=request_options or default_request_options(),
        )

    async def get(
        self,
        *,
        promotion_code: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PromotionCode:
        """
        Retrieve a promotion code

        <p>Retrieves the promotion code with the given ID. In order to retrieve a promotion code by the customer-facing <code>code</code> use <a href="/docs/api/promotion_codes/list">list</a> with the desired <code>code</code>.</p>

        GET /v1/promotion_codes/{promotion_code}

        Args:
            expand: Specifies which fields in the response should be expanded.
            promotion_code: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.promotion_code.get(promotion_code="string")
        ```
        """
        models.PromotionCode.model_rebuild(_types_namespace=models._types_namespace)
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
            path=f"/v1/promotion_codes/{promotion_code}",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.PromotionCode,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        coupon: str,
        active: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        code: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        customer: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        expires_at: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        max_redemptions: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        metadata: typing.Union[
            typing.Optional[params.PromotionCodeCreateBodyMetadata], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        restrictions: typing.Union[
            typing.Optional[params.PromotionCodeCreateBodyRestrictions],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PromotionCode:
        """
        Create a promotion code

        <p>A promotion code points to a coupon. You can optionally restrict the code to a specific customer, redemption limit, and expiration date.</p>

        POST /v1/promotion_codes

        Args:
            active: Whether the promotion code is currently active.
            code: The customer-facing code. Regardless of case, this code must be unique across all active promotion codes for a specific customer. Valid characters are lower case letters (a-z), upper case letters (A-Z), and digits (0-9).

        If left blank, we will generate one automatically.
            customer: The customer that this promotion code can be used by. If not set, the promotion code can be used by all customers.
            expand: Specifies which fields in the response should be expanded.
            expires_at: The timestamp at which this promotion code will expire. If the coupon has specified a `redeems_by`, then this value cannot be after the coupon's `redeems_by`.
            max_redemptions: A positive integer specifying the number of times the promotion code can be redeemed. If the coupon has specified a `max_redemptions`, then this value cannot be greater than the coupon's `max_redemptions`.
            metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
            restrictions: Settings that restrict the redemption of the promotion code.
            coupon: The coupon for this promotion code.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.promotion_code.create(coupon="string")
        ```
        """
        models.PromotionCode.model_rebuild(_types_namespace=models._types_namespace)
        _data = to_form_urlencoded(
            item={
                "active": active,
                "code": code,
                "customer": customer,
                "expand": expand,
                "expires_at": expires_at,
                "max_redemptions": max_redemptions,
                "metadata": metadata,
                "restrictions": restrictions,
                "coupon": coupon,
            },
            dump_with=params._SerializerPromotionCodeCreateBody,
            style={
                "active": "form",
                "code": "form",
                "coupon": "form",
                "customer": "form",
                "expand": "deepObject",
                "expires_at": "form",
                "max_redemptions": "form",
                "metadata": "deepObject",
                "restrictions": "deepObject",
            },
            explode={
                "active": True,
                "code": True,
                "coupon": True,
                "customer": True,
                "expand": True,
                "expires_at": True,
                "max_redemptions": True,
                "metadata": True,
                "restrictions": True,
            },
        )
        return await self._base_client.request(
            method="POST",
            path="/v1/promotion_codes",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.PromotionCode,
            request_options=request_options or default_request_options(),
        )

    async def update(
        self,
        *,
        promotion_code: str,
        data: typing.Union[
            typing.Optional[params.PromotionCodeUpdateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PromotionCode:
        """
        Update a promotion code

        <p>Updates the specified promotion code by setting the values of the parameters passed. Most fields are, by design, not editable.</p>

        POST /v1/promotion_codes/{promotion_code}

        Args:
            data: PromotionCodeUpdateBody
            promotion_code: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.promotion_code.update(promotion_code="string")
        ```
        """
        models.PromotionCode.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerPromotionCodeUpdateBody,
                style={
                    "active": "form",
                    "expand": "deepObject",
                    "metadata": "deepObject",
                    "restrictions": "deepObject",
                },
                explode={
                    "active": True,
                    "expand": True,
                    "metadata": True,
                    "restrictions": True,
                },
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/promotion_codes/{promotion_code}",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.PromotionCode,
            request_options=request_options or default_request_options(),
        )
