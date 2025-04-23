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

    def get(
        self,
        *,
        fee: str,
        id: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.FeeRefund:
        """
        Retrieve an application fee refund

        <p>By default, you can see the 10 most recent refunds stored directly on the application fee object, but you can also retrieve details about a specific refund stored on the application fee.</p>

        GET /v1/application_fees/{fee}/refunds/{id}

        Args:
            expand: Specifies which fields in the response should be expanded.
            fee: str
            id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.application_fee.refund.get(fee="string", id="string")
        ```
        """
        models.FeeRefund.model_rebuild(_types_namespace=models._types_namespace)
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
            path=f"/v1/application_fees/{fee}/refunds/{id}",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.FeeRefund,
            request_options=request_options or default_request_options(),
        )

    def list(
        self,
        *,
        id: str,
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
    ) -> models.ApplicationFeeRefundListResponse:
        """
        List all application fee refunds

        <p>You can see a list of the refunds belonging to a specific application fee. Note that the 10 most recent refunds are always available by default on the application fee object. If you need more than those 10, you can use this API method and the <code>limit</code> and <code>starting_after</code> parameters to page through additional refunds.</p>

        GET /v1/application_fees/{id}/refunds

        Args:
            ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            expand: Specifies which fields in the response should be expanded.
            limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
            id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.application_fee.refund.list(id="string")
        ```
        """
        models.ApplicationFeeRefundListResponse.model_rebuild(
            _types_namespace=models._types_namespace
        )
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
            path=f"/v1/application_fees/{id}/refunds",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.ApplicationFeeRefundListResponse,
            request_options=request_options or default_request_options(),
        )

    def update(
        self,
        *,
        fee: str,
        id: str,
        data: typing.Union[
            typing.Optional[params.ApplicationFeeRefundUpdateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.FeeRefund:
        """
        Update an application fee refund

        <p>Updates the specified application fee refund by setting the values of the parameters passed. Any parameters not provided will be left unchanged.</p>

        <p>This request only accepts metadata as an argument.</p>

        POST /v1/application_fees/{fee}/refunds/{id}

        Args:
            data: ApplicationFeeRefundUpdateBody
            fee: str
            id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.application_fee.refund.update(fee="string", id="string")
        ```
        """
        models.FeeRefund.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerApplicationFeeRefundUpdateBody,
                style={"expand": "deepObject", "metadata": "deepObject"},
                explode={"expand": True, "metadata": True},
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/application_fees/{fee}/refunds/{id}",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.FeeRefund,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        id: str,
        data: typing.Union[
            typing.Optional[params.ApplicationFeeRefundCreateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ApplicationFee:
        """


        POST /v1/application_fees/{id}/refund

        Args:
            data: ApplicationFeeRefundCreateBody
            id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.application_fee.refund.create(id="string")
        ```
        """
        models.ApplicationFee.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerApplicationFeeRefundCreateBody,
                style={"amount": "form", "directive": "form", "expand": "deepObject"},
                explode={"amount": True, "directive": True, "expand": True},
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/application_fees/{id}/refund",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.ApplicationFee,
            request_options=request_options or default_request_options(),
        )

    def create_many(
        self,
        *,
        id: str,
        data: typing.Union[
            typing.Optional[params.ApplicationFeeRefundCreateManyBody],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.FeeRefund:
        """
        Create an application fee refund

        <p>Refunds an application fee that has previously been collected but not yet refunded.
        Funds will be refunded to the Stripe account from which the fee was originally collected.</p>

        <p>You can optionally refund only part of an application fee.
        You can do so multiple times, until the entire fee has been refunded.</p>

        <p>Once entirely refunded, an application fee can’t be refunded again.
        This method will raise an error when called on an already-refunded application fee,
        or when trying to refund more money than is left on an application fee.</p>

        POST /v1/application_fees/{id}/refunds

        Args:
            data: ApplicationFeeRefundCreateManyBody
            id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.application_fee.refund.create_many(id="string")
        ```
        """
        models.FeeRefund.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerApplicationFeeRefundCreateManyBody,
                style={
                    "amount": "form",
                    "expand": "deepObject",
                    "metadata": "deepObject",
                },
                explode={"amount": True, "expand": True, "metadata": True},
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/application_fees/{id}/refunds",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.FeeRefund,
            request_options=request_options or default_request_options(),
        )


class AsyncRefundClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def get(
        self,
        *,
        fee: str,
        id: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.FeeRefund:
        """
        Retrieve an application fee refund

        <p>By default, you can see the 10 most recent refunds stored directly on the application fee object, but you can also retrieve details about a specific refund stored on the application fee.</p>

        GET /v1/application_fees/{fee}/refunds/{id}

        Args:
            expand: Specifies which fields in the response should be expanded.
            fee: str
            id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.application_fee.refund.get(fee="string", id="string")
        ```
        """
        models.FeeRefund.model_rebuild(_types_namespace=models._types_namespace)
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
            path=f"/v1/application_fees/{fee}/refunds/{id}",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.FeeRefund,
            request_options=request_options or default_request_options(),
        )

    async def list(
        self,
        *,
        id: str,
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
    ) -> models.ApplicationFeeRefundListResponse:
        """
        List all application fee refunds

        <p>You can see a list of the refunds belonging to a specific application fee. Note that the 10 most recent refunds are always available by default on the application fee object. If you need more than those 10, you can use this API method and the <code>limit</code> and <code>starting_after</code> parameters to page through additional refunds.</p>

        GET /v1/application_fees/{id}/refunds

        Args:
            ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            expand: Specifies which fields in the response should be expanded.
            limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
            id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.application_fee.refund.list(id="string")
        ```
        """
        models.ApplicationFeeRefundListResponse.model_rebuild(
            _types_namespace=models._types_namespace
        )
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
            path=f"/v1/application_fees/{id}/refunds",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.ApplicationFeeRefundListResponse,
            request_options=request_options or default_request_options(),
        )

    async def update(
        self,
        *,
        fee: str,
        id: str,
        data: typing.Union[
            typing.Optional[params.ApplicationFeeRefundUpdateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.FeeRefund:
        """
        Update an application fee refund

        <p>Updates the specified application fee refund by setting the values of the parameters passed. Any parameters not provided will be left unchanged.</p>

        <p>This request only accepts metadata as an argument.</p>

        POST /v1/application_fees/{fee}/refunds/{id}

        Args:
            data: ApplicationFeeRefundUpdateBody
            fee: str
            id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.application_fee.refund.update(fee="string", id="string")
        ```
        """
        models.FeeRefund.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerApplicationFeeRefundUpdateBody,
                style={"expand": "deepObject", "metadata": "deepObject"},
                explode={"expand": True, "metadata": True},
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/application_fees/{fee}/refunds/{id}",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.FeeRefund,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        id: str,
        data: typing.Union[
            typing.Optional[params.ApplicationFeeRefundCreateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ApplicationFee:
        """


        POST /v1/application_fees/{id}/refund

        Args:
            data: ApplicationFeeRefundCreateBody
            id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.application_fee.refund.create(id="string")
        ```
        """
        models.ApplicationFee.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerApplicationFeeRefundCreateBody,
                style={"amount": "form", "directive": "form", "expand": "deepObject"},
                explode={"amount": True, "directive": True, "expand": True},
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/application_fees/{id}/refund",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.ApplicationFee,
            request_options=request_options or default_request_options(),
        )

    async def create_many(
        self,
        *,
        id: str,
        data: typing.Union[
            typing.Optional[params.ApplicationFeeRefundCreateManyBody],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.FeeRefund:
        """
        Create an application fee refund

        <p>Refunds an application fee that has previously been collected but not yet refunded.
        Funds will be refunded to the Stripe account from which the fee was originally collected.</p>

        <p>You can optionally refund only part of an application fee.
        You can do so multiple times, until the entire fee has been refunded.</p>

        <p>Once entirely refunded, an application fee can’t be refunded again.
        This method will raise an error when called on an already-refunded application fee,
        or when trying to refund more money than is left on an application fee.</p>

        POST /v1/application_fees/{id}/refunds

        Args:
            data: ApplicationFeeRefundCreateManyBody
            id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.application_fee.refund.create_many(id="string")
        ```
        """
        models.FeeRefund.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerApplicationFeeRefundCreateManyBody,
                style={
                    "amount": "form",
                    "expand": "deepObject",
                    "metadata": "deepObject",
                },
                explode={"amount": True, "expand": True, "metadata": True},
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/application_fees/{id}/refunds",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.FeeRefund,
            request_options=request_options or default_request_options(),
        )
