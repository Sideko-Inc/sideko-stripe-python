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


class RefundClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def list(
        self,
        *,
        charge: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        created: typing.Union[
            typing.Optional[typing.Union[params.RefundListCreatedObj0, int]],
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
        payment_intent: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        starting_after: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.RefundListResponse:
        """
        List all refunds

        <p>Returns a list of all refunds you created. We return the refunds in sorted order, with the most recent refunds appearing first. The 10 most recent refunds are always available by default on the Charge object.</p>

        GET /v1/refunds

        Args:
            charge: Only return refunds for the charge specified by this charge ID.
            created: Only return refunds that were created during the given date interval.
            ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            expand: Specifies which fields in the response should be expanded.
            limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            payment_intent: Only return refunds for the PaymentIntent specified by this ID.
            starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.refund.list()
        ```
        """
        models.RefundListResponse.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _query: QueryParams = {}
        if not isinstance(charge, type_utils.NotGiven):
            encode_query_param(
                _query,
                "charge",
                to_encodable(item=charge, dump_with=str),
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
                        params._SerializerRefundListCreatedObj0, int
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
        if not isinstance(payment_intent, type_utils.NotGiven):
            encode_query_param(
                _query,
                "payment_intent",
                to_encodable(item=payment_intent, dump_with=str),
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
            path="/v1/refunds",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.RefundListResponse,
            request_options=request_options or default_request_options(),
        )

    def get(
        self,
        *,
        refund: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Refund:
        """
        Retrieve a refund

        <p>Retrieves the details of an existing refund.</p>

        GET /v1/refunds/{refund}

        Args:
            expand: Specifies which fields in the response should be expanded.
            refund: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.refund.get(refund="string")
        ```
        """
        models.Refund.model_rebuild(_types_namespace=models._types_namespace)
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
            path=f"/v1/refunds/{refund}",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.Refund,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        data: typing.Union[
            typing.Optional[params.RefundCreateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Refund:
        """
        Create customer balance refund

        <p>When you create a new refund, you must specify a Charge or a PaymentIntent object on which to create it.</p>

        <p>Creating a new refund will refund a charge that has previously been created but not yet refunded.
        Funds will be refunded to the credit or debit card that was originally charged.</p>

        <p>You can optionally refund only part of a charge.
        You can do so multiple times, until the entire charge has been refunded.</p>

        <p>Once entirely refunded, a charge can’t be refunded again.
        This method will raise an error when called on an already-refunded charge,
        or when trying to refund more money than is left on a charge.</p>

        POST /v1/refunds

        Args:
            data: RefundCreateBody
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.refund.create()
        ```
        """
        models.Refund.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerRefundCreateBody,
                style={
                    "amount": "form",
                    "charge": "form",
                    "currency": "form",
                    "customer": "form",
                    "expand": "deepObject",
                    "instructions_email": "form",
                    "metadata": "deepObject",
                    "origin": "form",
                    "payment_intent": "form",
                    "reason": "form",
                    "refund_application_fee": "form",
                    "reverse_transfer": "form",
                },
                explode={
                    "amount": True,
                    "charge": True,
                    "currency": True,
                    "customer": True,
                    "expand": True,
                    "instructions_email": True,
                    "metadata": True,
                    "origin": True,
                    "payment_intent": True,
                    "reason": True,
                    "refund_application_fee": True,
                    "reverse_transfer": True,
                },
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path="/v1/refunds",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.Refund,
            request_options=request_options or default_request_options(),
        )

    def update(
        self,
        *,
        refund: str,
        data: typing.Union[
            typing.Optional[params.RefundUpdateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Refund:
        """
        Update a refund

        <p>Updates the refund that you specify by setting the values of the passed parameters. Any parameters that you don’t provide remain unchanged.</p>

        <p>This request only accepts <code>metadata</code> as an argument.</p>

        POST /v1/refunds/{refund}

        Args:
            data: RefundUpdateBody
            refund: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.refund.update(refund="string")
        ```
        """
        models.Refund.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerRefundUpdateBody,
                style={"expand": "deepObject", "metadata": "deepObject"},
                explode={"expand": True, "metadata": True},
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/refunds/{refund}",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.Refund,
            request_options=request_options or default_request_options(),
        )

    def cancel(
        self,
        *,
        refund: str,
        data: typing.Union[
            typing.Optional[params.RefundCancelBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Refund:
        """
        Cancel a refund

        <p>Cancels a refund with a status of <code>requires_action</code>.</p>

        <p>You can’t cancel refunds in other states. Only refunds for payment methods that require customer action can enter the <code>requires_action</code> state.</p>

        POST /v1/refunds/{refund}/cancel

        Args:
            data: RefundCancelBody
            refund: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.refund.cancel(refund="string")
        ```
        """
        models.Refund.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerRefundCancelBody,
                style={"expand": "deepObject"},
                explode={"expand": True},
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/refunds/{refund}/cancel",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.Refund,
            request_options=request_options or default_request_options(),
        )


class AsyncRefundClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def list(
        self,
        *,
        charge: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        created: typing.Union[
            typing.Optional[typing.Union[params.RefundListCreatedObj0, int]],
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
        payment_intent: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        starting_after: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.RefundListResponse:
        """
        List all refunds

        <p>Returns a list of all refunds you created. We return the refunds in sorted order, with the most recent refunds appearing first. The 10 most recent refunds are always available by default on the Charge object.</p>

        GET /v1/refunds

        Args:
            charge: Only return refunds for the charge specified by this charge ID.
            created: Only return refunds that were created during the given date interval.
            ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            expand: Specifies which fields in the response should be expanded.
            limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            payment_intent: Only return refunds for the PaymentIntent specified by this ID.
            starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.refund.list()
        ```
        """
        models.RefundListResponse.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _query: QueryParams = {}
        if not isinstance(charge, type_utils.NotGiven):
            encode_query_param(
                _query,
                "charge",
                to_encodable(item=charge, dump_with=str),
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
                        params._SerializerRefundListCreatedObj0, int
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
        if not isinstance(payment_intent, type_utils.NotGiven):
            encode_query_param(
                _query,
                "payment_intent",
                to_encodable(item=payment_intent, dump_with=str),
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
            path="/v1/refunds",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.RefundListResponse,
            request_options=request_options or default_request_options(),
        )

    async def get(
        self,
        *,
        refund: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Refund:
        """
        Retrieve a refund

        <p>Retrieves the details of an existing refund.</p>

        GET /v1/refunds/{refund}

        Args:
            expand: Specifies which fields in the response should be expanded.
            refund: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.refund.get(refund="string")
        ```
        """
        models.Refund.model_rebuild(_types_namespace=models._types_namespace)
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
            path=f"/v1/refunds/{refund}",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.Refund,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        data: typing.Union[
            typing.Optional[params.RefundCreateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Refund:
        """
        Create customer balance refund

        <p>When you create a new refund, you must specify a Charge or a PaymentIntent object on which to create it.</p>

        <p>Creating a new refund will refund a charge that has previously been created but not yet refunded.
        Funds will be refunded to the credit or debit card that was originally charged.</p>

        <p>You can optionally refund only part of a charge.
        You can do so multiple times, until the entire charge has been refunded.</p>

        <p>Once entirely refunded, a charge can’t be refunded again.
        This method will raise an error when called on an already-refunded charge,
        or when trying to refund more money than is left on a charge.</p>

        POST /v1/refunds

        Args:
            data: RefundCreateBody
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.refund.create()
        ```
        """
        models.Refund.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerRefundCreateBody,
                style={
                    "amount": "form",
                    "charge": "form",
                    "currency": "form",
                    "customer": "form",
                    "expand": "deepObject",
                    "instructions_email": "form",
                    "metadata": "deepObject",
                    "origin": "form",
                    "payment_intent": "form",
                    "reason": "form",
                    "refund_application_fee": "form",
                    "reverse_transfer": "form",
                },
                explode={
                    "amount": True,
                    "charge": True,
                    "currency": True,
                    "customer": True,
                    "expand": True,
                    "instructions_email": True,
                    "metadata": True,
                    "origin": True,
                    "payment_intent": True,
                    "reason": True,
                    "refund_application_fee": True,
                    "reverse_transfer": True,
                },
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path="/v1/refunds",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.Refund,
            request_options=request_options or default_request_options(),
        )

    async def update(
        self,
        *,
        refund: str,
        data: typing.Union[
            typing.Optional[params.RefundUpdateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Refund:
        """
        Update a refund

        <p>Updates the refund that you specify by setting the values of the passed parameters. Any parameters that you don’t provide remain unchanged.</p>

        <p>This request only accepts <code>metadata</code> as an argument.</p>

        POST /v1/refunds/{refund}

        Args:
            data: RefundUpdateBody
            refund: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.refund.update(refund="string")
        ```
        """
        models.Refund.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerRefundUpdateBody,
                style={"expand": "deepObject", "metadata": "deepObject"},
                explode={"expand": True, "metadata": True},
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/refunds/{refund}",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.Refund,
            request_options=request_options or default_request_options(),
        )

    async def cancel(
        self,
        *,
        refund: str,
        data: typing.Union[
            typing.Optional[params.RefundCancelBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Refund:
        """
        Cancel a refund

        <p>Cancels a refund with a status of <code>requires_action</code>.</p>

        <p>You can’t cancel refunds in other states. Only refunds for payment methods that require customer action can enter the <code>requires_action</code> state.</p>

        POST /v1/refunds/{refund}/cancel

        Args:
            data: RefundCancelBody
            refund: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.refund.cancel(refund="string")
        ```
        """
        models.Refund.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerRefundCancelBody,
                style={"expand": "deepObject"},
                explode={"expand": True},
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/refunds/{refund}/cancel",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.Refund,
            request_options=request_options or default_request_options(),
        )
