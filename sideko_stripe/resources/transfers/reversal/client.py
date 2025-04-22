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


class ReversalClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

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
    ) -> models.TransfersReversalListResponse:
        """
        List all reversals

        <p>You can see a list of the reversals belonging to a specific transfer. Note that the 10 most recent reversals are always available by default on the transfer object. If you need more than those 10, you can use this API method and the <code>limit</code> and <code>starting_after</code> parameters to page through additional reversals.</p>

        GET /v1/transfers/{id}/reversals

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
        client.transfers.reversal.list(id="string")
        ```
        """
        models.TransfersReversalListResponse.model_rebuild(
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
            path=f"/v1/transfers/{id}/reversals",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.TransfersReversalListResponse,
            request_options=request_options or default_request_options(),
        )

    def get(
        self,
        *,
        id: str,
        transfer: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TransferReversal:
        """
        Retrieve a reversal

        <p>By default, you can see the 10 most recent reversals stored directly on the transfer object, but you can also retrieve details about a specific reversal stored on the transfer.</p>

        GET /v1/transfers/{transfer}/reversals/{id}

        Args:
            expand: Specifies which fields in the response should be expanded.
            id: str
            transfer: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.transfers.reversal.get(id="string", transfer="string")
        ```
        """
        models.TransferReversal.model_rebuild(_types_namespace=models._types_namespace)
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
            path=f"/v1/transfers/{transfer}/reversals/{id}",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.TransferReversal,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        id: str,
        data: typing.Union[
            typing.Optional[params.TransfersReversalCreateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TransferReversal:
        """
        Create a transfer reversal

        <p>When you create a new reversal, you must specify a transfer to create it on.</p>

        <p>When reversing transfers, you can optionally reverse part of the transfer. You can do so as many times as you wish until the entire transfer has been reversed.</p>

        <p>Once entirely reversed, a transfer can’t be reversed again. This method will return an error when called on an already-reversed transfer, or when trying to reverse more money than is left on a transfer.</p>

        POST /v1/transfers/{id}/reversals

        Args:
            data: TransfersReversalCreateBody
            id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.transfers.reversal.create(id="string")
        ```
        """
        models.TransferReversal.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerTransfersReversalCreateBody,
                style={
                    "amount": "form",
                    "description": "form",
                    "expand": "deepObject",
                    "metadata": "deepObject",
                    "refund_application_fee": "form",
                },
                explode={
                    "amount": True,
                    "description": True,
                    "expand": True,
                    "metadata": True,
                    "refund_application_fee": True,
                },
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/transfers/{id}/reversals",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.TransferReversal,
            request_options=request_options or default_request_options(),
        )

    def update(
        self,
        *,
        id: str,
        transfer: str,
        data: typing.Union[
            typing.Optional[params.TransfersReversalUpdateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TransferReversal:
        """
        Update a reversal

        <p>Updates the specified reversal by setting the values of the parameters passed. Any parameters not provided will be left unchanged.</p>

        <p>This request only accepts metadata and description as arguments.</p>

        POST /v1/transfers/{transfer}/reversals/{id}

        Args:
            data: TransfersReversalUpdateBody
            id: str
            transfer: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.transfers.reversal.update(id="string", transfer="string")
        ```
        """
        models.TransferReversal.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerTransfersReversalUpdateBody,
                style={"expand": "deepObject", "metadata": "deepObject"},
                explode={"expand": True, "metadata": True},
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/transfers/{transfer}/reversals/{id}",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.TransferReversal,
            request_options=request_options or default_request_options(),
        )


class AsyncReversalClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

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
    ) -> models.TransfersReversalListResponse:
        """
        List all reversals

        <p>You can see a list of the reversals belonging to a specific transfer. Note that the 10 most recent reversals are always available by default on the transfer object. If you need more than those 10, you can use this API method and the <code>limit</code> and <code>starting_after</code> parameters to page through additional reversals.</p>

        GET /v1/transfers/{id}/reversals

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
        await client.transfers.reversal.list(id="string")
        ```
        """
        models.TransfersReversalListResponse.model_rebuild(
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
            path=f"/v1/transfers/{id}/reversals",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.TransfersReversalListResponse,
            request_options=request_options or default_request_options(),
        )

    async def get(
        self,
        *,
        id: str,
        transfer: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TransferReversal:
        """
        Retrieve a reversal

        <p>By default, you can see the 10 most recent reversals stored directly on the transfer object, but you can also retrieve details about a specific reversal stored on the transfer.</p>

        GET /v1/transfers/{transfer}/reversals/{id}

        Args:
            expand: Specifies which fields in the response should be expanded.
            id: str
            transfer: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.transfers.reversal.get(id="string", transfer="string")
        ```
        """
        models.TransferReversal.model_rebuild(_types_namespace=models._types_namespace)
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
            path=f"/v1/transfers/{transfer}/reversals/{id}",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.TransferReversal,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        id: str,
        data: typing.Union[
            typing.Optional[params.TransfersReversalCreateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TransferReversal:
        """
        Create a transfer reversal

        <p>When you create a new reversal, you must specify a transfer to create it on.</p>

        <p>When reversing transfers, you can optionally reverse part of the transfer. You can do so as many times as you wish until the entire transfer has been reversed.</p>

        <p>Once entirely reversed, a transfer can’t be reversed again. This method will return an error when called on an already-reversed transfer, or when trying to reverse more money than is left on a transfer.</p>

        POST /v1/transfers/{id}/reversals

        Args:
            data: TransfersReversalCreateBody
            id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.transfers.reversal.create(id="string")
        ```
        """
        models.TransferReversal.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerTransfersReversalCreateBody,
                style={
                    "amount": "form",
                    "description": "form",
                    "expand": "deepObject",
                    "metadata": "deepObject",
                    "refund_application_fee": "form",
                },
                explode={
                    "amount": True,
                    "description": True,
                    "expand": True,
                    "metadata": True,
                    "refund_application_fee": True,
                },
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/transfers/{id}/reversals",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.TransferReversal,
            request_options=request_options or default_request_options(),
        )

    async def update(
        self,
        *,
        id: str,
        transfer: str,
        data: typing.Union[
            typing.Optional[params.TransfersReversalUpdateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TransferReversal:
        """
        Update a reversal

        <p>Updates the specified reversal by setting the values of the parameters passed. Any parameters not provided will be left unchanged.</p>

        <p>This request only accepts metadata and description as arguments.</p>

        POST /v1/transfers/{transfer}/reversals/{id}

        Args:
            data: TransfersReversalUpdateBody
            id: str
            transfer: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.transfers.reversal.update(id="string", transfer="string")
        ```
        """
        models.TransferReversal.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerTransfersReversalUpdateBody,
                style={"expand": "deepObject", "metadata": "deepObject"},
                explode={"expand": True, "metadata": True},
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/transfers/{transfer}/reversals/{id}",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.TransferReversal,
            request_options=request_options or default_request_options(),
        )
