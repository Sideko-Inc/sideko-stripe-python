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


class RequestClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def list(
        self,
        *,
        created: typing.Union[
            typing.Optional[params.ForwardingRequestListCreated], type_utils.NotGiven
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
    ) -> models.ForwardingRequestListResponse:
        """
        List all ForwardingRequests

        <p>Lists all ForwardingRequest objects.</p>

        GET /v1/forwarding/requests

        Args:
            created: Similar to other List endpoints, filters results based on created timestamp. You can pass gt, gte, lt, and lte timestamp values.
            ending_before: A pagination cursor to fetch the previous page of the list. The value must be a ForwardingRequest ID.
            expand: Specifies which fields in the response should be expanded.
            limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            starting_after: A pagination cursor to fetch the next page of the list. The value must be a ForwardingRequest ID.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.forwarding.request.list()
        ```
        """
        _query: QueryParams = {}
        if not isinstance(created, type_utils.NotGiven):
            encode_query_param(
                _query,
                "created",
                to_encodable(
                    item=created,
                    dump_with=params._SerializerForwardingRequestListCreated,
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
            path="/v1/forwarding/requests",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.ForwardingRequestListResponse,
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
    ) -> models.ForwardingRequest:
        """
        Retrieve a ForwardingRequest

        <p>Retrieves a ForwardingRequest object.</p>

        GET /v1/forwarding/requests/{id}

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
        client.forwarding.request.get(id="string")
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
            path=f"/v1/forwarding/requests/{id}",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.ForwardingRequest,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        payment_method: str,
        replacements: typing.List[
            typing_extensions.Literal[
                "card_cvc",
                "card_expiry",
                "card_number",
                "cardholder_name",
                "request_signature",
            ]
        ],
        url: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        metadata: typing.Union[
            typing.Optional[params.ForwardingRequestCreateBodyMetadata],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request: typing.Union[
            typing.Optional[params.ForwardingRequestCreateBodyRequest],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ForwardingRequest:
        """
        Create a ForwardingRequest

        <p>Creates a ForwardingRequest object.</p>

        POST /v1/forwarding/requests

        Args:
            expand: Specifies which fields in the response should be expanded.
            metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
            request: The request body and headers to be sent to the destination endpoint.
            payment_method: The PaymentMethod to insert into the forwarded request. Forwarding previously consumed PaymentMethods is allowed.
            replacements: The field kinds to be replaced in the forwarded request.
            url: The destination URL for the forwarded request. Must be supported by the config.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.forwarding.request.create(
            payment_method="string", replacements=["card_cvc"], url="string"
        )
        ```
        """
        _data = to_form_urlencoded(
            item={
                "expand": expand,
                "metadata": metadata,
                "request": request,
                "payment_method": payment_method,
                "replacements": replacements,
                "url": url,
            },
            dump_with=params._SerializerForwardingRequestCreateBody,
            style={
                "expand": "deepObject",
                "metadata": "deepObject",
                "payment_method": "form",
                "replacements": "deepObject",
                "request": "deepObject",
                "url": "form",
            },
            explode={
                "expand": True,
                "metadata": True,
                "payment_method": True,
                "replacements": True,
                "request": True,
                "url": True,
            },
        )
        return self._base_client.request(
            method="POST",
            path="/v1/forwarding/requests",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.ForwardingRequest,
            request_options=request_options or default_request_options(),
        )


class AsyncRequestClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def list(
        self,
        *,
        created: typing.Union[
            typing.Optional[params.ForwardingRequestListCreated], type_utils.NotGiven
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
    ) -> models.ForwardingRequestListResponse:
        """
        List all ForwardingRequests

        <p>Lists all ForwardingRequest objects.</p>

        GET /v1/forwarding/requests

        Args:
            created: Similar to other List endpoints, filters results based on created timestamp. You can pass gt, gte, lt, and lte timestamp values.
            ending_before: A pagination cursor to fetch the previous page of the list. The value must be a ForwardingRequest ID.
            expand: Specifies which fields in the response should be expanded.
            limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            starting_after: A pagination cursor to fetch the next page of the list. The value must be a ForwardingRequest ID.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.forwarding.request.list()
        ```
        """
        _query: QueryParams = {}
        if not isinstance(created, type_utils.NotGiven):
            encode_query_param(
                _query,
                "created",
                to_encodable(
                    item=created,
                    dump_with=params._SerializerForwardingRequestListCreated,
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
            path="/v1/forwarding/requests",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.ForwardingRequestListResponse,
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
    ) -> models.ForwardingRequest:
        """
        Retrieve a ForwardingRequest

        <p>Retrieves a ForwardingRequest object.</p>

        GET /v1/forwarding/requests/{id}

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
        await client.forwarding.request.get(id="string")
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
            path=f"/v1/forwarding/requests/{id}",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.ForwardingRequest,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        payment_method: str,
        replacements: typing.List[
            typing_extensions.Literal[
                "card_cvc",
                "card_expiry",
                "card_number",
                "cardholder_name",
                "request_signature",
            ]
        ],
        url: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        metadata: typing.Union[
            typing.Optional[params.ForwardingRequestCreateBodyMetadata],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request: typing.Union[
            typing.Optional[params.ForwardingRequestCreateBodyRequest],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ForwardingRequest:
        """
        Create a ForwardingRequest

        <p>Creates a ForwardingRequest object.</p>

        POST /v1/forwarding/requests

        Args:
            expand: Specifies which fields in the response should be expanded.
            metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
            request: The request body and headers to be sent to the destination endpoint.
            payment_method: The PaymentMethod to insert into the forwarded request. Forwarding previously consumed PaymentMethods is allowed.
            replacements: The field kinds to be replaced in the forwarded request.
            url: The destination URL for the forwarded request. Must be supported by the config.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.forwarding.request.create(
            payment_method="string", replacements=["card_cvc"], url="string"
        )
        ```
        """
        _data = to_form_urlencoded(
            item={
                "expand": expand,
                "metadata": metadata,
                "request": request,
                "payment_method": payment_method,
                "replacements": replacements,
                "url": url,
            },
            dump_with=params._SerializerForwardingRequestCreateBody,
            style={
                "expand": "deepObject",
                "metadata": "deepObject",
                "payment_method": "form",
                "replacements": "deepObject",
                "request": "deepObject",
                "url": "form",
            },
            explode={
                "expand": True,
                "metadata": True,
                "payment_method": True,
                "replacements": True,
                "request": True,
                "url": True,
            },
        )
        return await self._base_client.request(
            method="POST",
            path="/v1/forwarding/requests",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.ForwardingRequest,
            request_options=request_options or default_request_options(),
        )
