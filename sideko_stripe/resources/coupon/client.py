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


class CouponClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def delete(
        self, *, coupon: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.DeletedCoupon:
        """
        Delete a coupon

        <p>You can delete coupons via the <a href="https://dashboard.stripe.com/coupons">coupon management</a> page of the Stripe dashboard. However, deleting a coupon does not affect any customers who have already applied the coupon; it means that new customers can’t redeem the coupon. You can also delete coupons via the API.</p>

        DELETE /v1/coupons/{coupon}

        Args:
            coupon: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.coupon.delete(coupon="string")
        ```
        """
        return self._base_client.request(
            method="DELETE",
            path=f"/v1/coupons/{coupon}",
            auth_names=["bearerAuth"],
            cast_to=models.DeletedCoupon,
            request_options=request_options or default_request_options(),
        )

    def list(
        self,
        *,
        created: typing.Union[
            typing.Optional[typing.Union[params.CouponListCreatedObj0, int]],
            type_utils.NotGiven,
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
    ) -> models.CouponListResponse:
        """
        List all coupons

        <p>Returns a list of your coupons.</p>

        GET /v1/coupons

        Args:
            created: A filter on the list, based on the object `created` field. The value can be a string with an integer Unix timestamp, or it can be a dictionary with a number of different query options.
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
        client.coupon.list()
        ```
        """
        _query: QueryParams = {}
        if not isinstance(created, type_utils.NotGiven):
            encode_query_param(
                _query,
                "created",
                to_encodable(
                    item=created,
                    dump_with=typing.Union[
                        params._SerializerCouponListCreatedObj0, int
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
            path="/v1/coupons",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.CouponListResponse,
            request_options=request_options or default_request_options(),
        )

    def get(
        self,
        *,
        coupon: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Coupon:
        """
        Retrieve a coupon

        <p>Retrieves the coupon with the given ID.</p>

        GET /v1/coupons/{coupon}

        Args:
            expand: Specifies which fields in the response should be expanded.
            coupon: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.coupon.get(coupon="string")
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
            path=f"/v1/coupons/{coupon}",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.Coupon,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        data: typing.Union[
            typing.Optional[params.CouponCreateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Coupon:
        """
        Create a coupon

        <p>You can create coupons easily via the <a href="https://dashboard.stripe.com/coupons">coupon management</a> page of the Stripe dashboard. Coupon creation is also accessible via the API if you need to create coupons on the fly.</p>

        <p>A coupon has either a <code>percent_off</code> or an <code>amount_off</code> and <code>currency</code>. If you set an <code>amount_off</code>, that amount will be subtracted from any invoice’s subtotal. For example, an invoice with a subtotal of <currency>100</currency> will have a final total of <currency>0</currency> if a coupon with an <code>amount_off</code> of <amount>200</amount> is applied to it and an invoice with a subtotal of <currency>300</currency> will have a final total of <currency>100</currency> if a coupon with an <code>amount_off</code> of <amount>200</amount> is applied to it.</p>

        POST /v1/coupons

        Args:
            data: CouponCreateBody
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.coupon.create()
        ```
        """
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerCouponCreateBody,
                style={
                    "amount_off": "form",
                    "applies_to": "deepObject",
                    "currency": "form",
                    "currency_options": "deepObject",
                    "duration": "form",
                    "duration_in_months": "form",
                    "expand": "deepObject",
                    "id": "form",
                    "max_redemptions": "form",
                    "metadata": "deepObject",
                    "name": "form",
                    "percent_off": "form",
                    "redeem_by": "form",
                },
                explode={
                    "amount_off": True,
                    "applies_to": True,
                    "currency": True,
                    "currency_options": True,
                    "duration": True,
                    "duration_in_months": True,
                    "expand": True,
                    "id": True,
                    "max_redemptions": True,
                    "metadata": True,
                    "name": True,
                    "percent_off": True,
                    "redeem_by": True,
                },
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path="/v1/coupons",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.Coupon,
            request_options=request_options or default_request_options(),
        )

    def update(
        self,
        *,
        coupon: str,
        data: typing.Union[
            typing.Optional[params.CouponUpdateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Coupon:
        """
        Update a coupon

        <p>Updates the metadata of a coupon. Other coupon details (currency, duration, amount_off) are, by design, not editable.</p>

        POST /v1/coupons/{coupon}

        Args:
            data: CouponUpdateBody
            coupon: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.coupon.update(coupon="string")
        ```
        """
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerCouponUpdateBody,
                style={
                    "currency_options": "deepObject",
                    "expand": "deepObject",
                    "metadata": "deepObject",
                    "name": "form",
                },
                explode={
                    "currency_options": True,
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
            path=f"/v1/coupons/{coupon}",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.Coupon,
            request_options=request_options or default_request_options(),
        )


class AsyncCouponClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def delete(
        self, *, coupon: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.DeletedCoupon:
        """
        Delete a coupon

        <p>You can delete coupons via the <a href="https://dashboard.stripe.com/coupons">coupon management</a> page of the Stripe dashboard. However, deleting a coupon does not affect any customers who have already applied the coupon; it means that new customers can’t redeem the coupon. You can also delete coupons via the API.</p>

        DELETE /v1/coupons/{coupon}

        Args:
            coupon: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.coupon.delete(coupon="string")
        ```
        """
        return await self._base_client.request(
            method="DELETE",
            path=f"/v1/coupons/{coupon}",
            auth_names=["bearerAuth"],
            cast_to=models.DeletedCoupon,
            request_options=request_options or default_request_options(),
        )

    async def list(
        self,
        *,
        created: typing.Union[
            typing.Optional[typing.Union[params.CouponListCreatedObj0, int]],
            type_utils.NotGiven,
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
    ) -> models.CouponListResponse:
        """
        List all coupons

        <p>Returns a list of your coupons.</p>

        GET /v1/coupons

        Args:
            created: A filter on the list, based on the object `created` field. The value can be a string with an integer Unix timestamp, or it can be a dictionary with a number of different query options.
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
        await client.coupon.list()
        ```
        """
        _query: QueryParams = {}
        if not isinstance(created, type_utils.NotGiven):
            encode_query_param(
                _query,
                "created",
                to_encodable(
                    item=created,
                    dump_with=typing.Union[
                        params._SerializerCouponListCreatedObj0, int
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
            path="/v1/coupons",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.CouponListResponse,
            request_options=request_options or default_request_options(),
        )

    async def get(
        self,
        *,
        coupon: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Coupon:
        """
        Retrieve a coupon

        <p>Retrieves the coupon with the given ID.</p>

        GET /v1/coupons/{coupon}

        Args:
            expand: Specifies which fields in the response should be expanded.
            coupon: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.coupon.get(coupon="string")
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
            path=f"/v1/coupons/{coupon}",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.Coupon,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        data: typing.Union[
            typing.Optional[params.CouponCreateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Coupon:
        """
        Create a coupon

        <p>You can create coupons easily via the <a href="https://dashboard.stripe.com/coupons">coupon management</a> page of the Stripe dashboard. Coupon creation is also accessible via the API if you need to create coupons on the fly.</p>

        <p>A coupon has either a <code>percent_off</code> or an <code>amount_off</code> and <code>currency</code>. If you set an <code>amount_off</code>, that amount will be subtracted from any invoice’s subtotal. For example, an invoice with a subtotal of <currency>100</currency> will have a final total of <currency>0</currency> if a coupon with an <code>amount_off</code> of <amount>200</amount> is applied to it and an invoice with a subtotal of <currency>300</currency> will have a final total of <currency>100</currency> if a coupon with an <code>amount_off</code> of <amount>200</amount> is applied to it.</p>

        POST /v1/coupons

        Args:
            data: CouponCreateBody
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.coupon.create()
        ```
        """
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerCouponCreateBody,
                style={
                    "amount_off": "form",
                    "applies_to": "deepObject",
                    "currency": "form",
                    "currency_options": "deepObject",
                    "duration": "form",
                    "duration_in_months": "form",
                    "expand": "deepObject",
                    "id": "form",
                    "max_redemptions": "form",
                    "metadata": "deepObject",
                    "name": "form",
                    "percent_off": "form",
                    "redeem_by": "form",
                },
                explode={
                    "amount_off": True,
                    "applies_to": True,
                    "currency": True,
                    "currency_options": True,
                    "duration": True,
                    "duration_in_months": True,
                    "expand": True,
                    "id": True,
                    "max_redemptions": True,
                    "metadata": True,
                    "name": True,
                    "percent_off": True,
                    "redeem_by": True,
                },
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path="/v1/coupons",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.Coupon,
            request_options=request_options or default_request_options(),
        )

    async def update(
        self,
        *,
        coupon: str,
        data: typing.Union[
            typing.Optional[params.CouponUpdateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Coupon:
        """
        Update a coupon

        <p>Updates the metadata of a coupon. Other coupon details (currency, duration, amount_off) are, by design, not editable.</p>

        POST /v1/coupons/{coupon}

        Args:
            data: CouponUpdateBody
            coupon: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.coupon.update(coupon="string")
        ```
        """
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerCouponUpdateBody,
                style={
                    "currency_options": "deepObject",
                    "expand": "deepObject",
                    "metadata": "deepObject",
                    "name": "form",
                },
                explode={
                    "currency_options": True,
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
            path=f"/v1/coupons/{coupon}",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.Coupon,
            request_options=request_options or default_request_options(),
        )
