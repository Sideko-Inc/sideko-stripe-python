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


class TopupsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def list(
        self,
        *,
        amount: typing.Union[
            typing.Optional[typing.Union[params.TopupsListAmountObj0, int]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        created: typing.Union[
            typing.Optional[typing.Union[params.TopupsListCreatedObj0, int]],
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
        status: typing.Union[
            typing.Optional[
                typing_extensions.Literal["canceled", "failed", "pending", "succeeded"]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TopupsListResponse:
        """
        List all top-ups

        <p>Returns a list of top-ups.</p>

        GET /v1/topups

        Args:
            amount: A positive integer representing how much to transfer.
            created: A filter on the list, based on the object `created` field. The value can be a string with an integer Unix timestamp, or it can be a dictionary with a number of different query options.
            ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            expand: Specifies which fields in the response should be expanded.
            limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
            status: Only return top-ups that have the given status. One of `canceled`, `failed`, `pending` or `succeeded`.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.topups.list()
        ```
        """
        models.TopupsListResponse.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _query: QueryParams = {}
        if not isinstance(amount, type_utils.NotGiven):
            encode_query_param(
                _query,
                "amount",
                to_encodable(
                    item=amount,
                    dump_with=typing.Union[params._SerializerTopupsListAmountObj0, int],
                ),
                style="deepObject",
                explode=True,
            )
        if not isinstance(created, type_utils.NotGiven):
            encode_query_param(
                _query,
                "created",
                to_encodable(
                    item=created,
                    dump_with=typing.Union[
                        params._SerializerTopupsListCreatedObj0, int
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
        if not isinstance(status, type_utils.NotGiven):
            encode_query_param(
                _query,
                "status",
                to_encodable(
                    item=status,
                    dump_with=typing_extensions.Literal[
                        "canceled", "failed", "pending", "succeeded"
                    ],
                ),
                style="form",
                explode=True,
            )
        return self._base_client.request(
            method="GET",
            path="/v1/topups",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.TopupsListResponse,
            request_options=request_options or default_request_options(),
        )

    def get(
        self,
        *,
        topup: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Topup:
        """
        Retrieve a top-up

        <p>Retrieves the details of a top-up that has previously been created. Supply the unique top-up ID that was returned from your previous request, and Stripe will return the corresponding top-up information.</p>

        GET /v1/topups/{topup}

        Args:
            expand: Specifies which fields in the response should be expanded.
            topup: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.topups.get(topup="string")
        ```
        """
        models.Topup.model_rebuild(_types_namespace=models._types_namespace)
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
            path=f"/v1/topups/{topup}",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.Topup,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        amount: int,
        currency: str,
        description: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        metadata: typing.Union[
            typing.Optional[typing.Union[params.TopupsCreateBodyMetadataObj0, str]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        source: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        statement_descriptor: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        transfer_group: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Topup:
        """
        Create a top-up

        <p>Top up the balance of an account</p>

        POST /v1/topups

        Args:
            description: An arbitrary string attached to the object. Often useful for displaying to users.
            expand: Specifies which fields in the response should be expanded.
            metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
            source: The ID of a source to transfer funds from. For most users, this should be left unspecified which will use the bank account that was set up in the dashboard for the specified currency. In test mode, this can be a test bank token (see [Testing Top-ups](https://stripe.com/docs/connect/testing#testing-top-ups)).
            statement_descriptor: Extra information about a top-up for the source's bank statement. Limited to 15 ASCII characters.
            transfer_group: A string that identifies this top-up as part of a group.
            amount: A positive integer representing how much to transfer.
            currency: Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.topups.create(amount=123, currency="string")
        ```
        """
        models.Topup.model_rebuild(_types_namespace=models._types_namespace)
        _data = to_form_urlencoded(
            item={
                "description": description,
                "expand": expand,
                "metadata": metadata,
                "source": source,
                "statement_descriptor": statement_descriptor,
                "transfer_group": transfer_group,
                "amount": amount,
                "currency": currency,
            },
            dump_with=params._SerializerTopupsCreateBody,
            style={
                "amount": "form",
                "currency": "form",
                "description": "form",
                "expand": "deepObject",
                "metadata": "deepObject",
                "source": "form",
                "statement_descriptor": "form",
                "transfer_group": "form",
            },
            explode={
                "amount": True,
                "currency": True,
                "description": True,
                "expand": True,
                "metadata": True,
                "source": True,
                "statement_descriptor": True,
                "transfer_group": True,
            },
        )
        return self._base_client.request(
            method="POST",
            path="/v1/topups",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.Topup,
            request_options=request_options or default_request_options(),
        )

    def update(
        self,
        *,
        topup: str,
        data: typing.Union[
            typing.Optional[params.TopupsUpdateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Topup:
        """
        Update a top-up

        <p>Updates the metadata of a top-up. Other top-up details are not editable by design.</p>

        POST /v1/topups/{topup}

        Args:
            data: TopupsUpdateBody
            topup: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.topups.update(topup="string")
        ```
        """
        models.Topup.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerTopupsUpdateBody,
                style={
                    "description": "form",
                    "expand": "deepObject",
                    "metadata": "deepObject",
                },
                explode={"description": True, "expand": True, "metadata": True},
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/topups/{topup}",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.Topup,
            request_options=request_options or default_request_options(),
        )

    def cancel(
        self,
        *,
        topup: str,
        data: typing.Union[
            typing.Optional[params.TopupsCancelBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Topup:
        """
        Cancel a top-up

        <p>Cancels a top-up. Only pending top-ups can be canceled.</p>

        POST /v1/topups/{topup}/cancel

        Args:
            data: TopupsCancelBody
            topup: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.topups.cancel(topup="string")
        ```
        """
        models.Topup.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerTopupsCancelBody,
                style={"expand": "deepObject"},
                explode={"expand": True},
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/topups/{topup}/cancel",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.Topup,
            request_options=request_options or default_request_options(),
        )


class AsyncTopupsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def list(
        self,
        *,
        amount: typing.Union[
            typing.Optional[typing.Union[params.TopupsListAmountObj0, int]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        created: typing.Union[
            typing.Optional[typing.Union[params.TopupsListCreatedObj0, int]],
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
        status: typing.Union[
            typing.Optional[
                typing_extensions.Literal["canceled", "failed", "pending", "succeeded"]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TopupsListResponse:
        """
        List all top-ups

        <p>Returns a list of top-ups.</p>

        GET /v1/topups

        Args:
            amount: A positive integer representing how much to transfer.
            created: A filter on the list, based on the object `created` field. The value can be a string with an integer Unix timestamp, or it can be a dictionary with a number of different query options.
            ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            expand: Specifies which fields in the response should be expanded.
            limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
            status: Only return top-ups that have the given status. One of `canceled`, `failed`, `pending` or `succeeded`.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.topups.list()
        ```
        """
        models.TopupsListResponse.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _query: QueryParams = {}
        if not isinstance(amount, type_utils.NotGiven):
            encode_query_param(
                _query,
                "amount",
                to_encodable(
                    item=amount,
                    dump_with=typing.Union[params._SerializerTopupsListAmountObj0, int],
                ),
                style="deepObject",
                explode=True,
            )
        if not isinstance(created, type_utils.NotGiven):
            encode_query_param(
                _query,
                "created",
                to_encodable(
                    item=created,
                    dump_with=typing.Union[
                        params._SerializerTopupsListCreatedObj0, int
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
        if not isinstance(status, type_utils.NotGiven):
            encode_query_param(
                _query,
                "status",
                to_encodable(
                    item=status,
                    dump_with=typing_extensions.Literal[
                        "canceled", "failed", "pending", "succeeded"
                    ],
                ),
                style="form",
                explode=True,
            )
        return await self._base_client.request(
            method="GET",
            path="/v1/topups",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.TopupsListResponse,
            request_options=request_options or default_request_options(),
        )

    async def get(
        self,
        *,
        topup: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Topup:
        """
        Retrieve a top-up

        <p>Retrieves the details of a top-up that has previously been created. Supply the unique top-up ID that was returned from your previous request, and Stripe will return the corresponding top-up information.</p>

        GET /v1/topups/{topup}

        Args:
            expand: Specifies which fields in the response should be expanded.
            topup: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.topups.get(topup="string")
        ```
        """
        models.Topup.model_rebuild(_types_namespace=models._types_namespace)
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
            path=f"/v1/topups/{topup}",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.Topup,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        amount: int,
        currency: str,
        description: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        metadata: typing.Union[
            typing.Optional[typing.Union[params.TopupsCreateBodyMetadataObj0, str]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        source: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        statement_descriptor: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        transfer_group: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Topup:
        """
        Create a top-up

        <p>Top up the balance of an account</p>

        POST /v1/topups

        Args:
            description: An arbitrary string attached to the object. Often useful for displaying to users.
            expand: Specifies which fields in the response should be expanded.
            metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
            source: The ID of a source to transfer funds from. For most users, this should be left unspecified which will use the bank account that was set up in the dashboard for the specified currency. In test mode, this can be a test bank token (see [Testing Top-ups](https://stripe.com/docs/connect/testing#testing-top-ups)).
            statement_descriptor: Extra information about a top-up for the source's bank statement. Limited to 15 ASCII characters.
            transfer_group: A string that identifies this top-up as part of a group.
            amount: A positive integer representing how much to transfer.
            currency: Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.topups.create(amount=123, currency="string")
        ```
        """
        models.Topup.model_rebuild(_types_namespace=models._types_namespace)
        _data = to_form_urlencoded(
            item={
                "description": description,
                "expand": expand,
                "metadata": metadata,
                "source": source,
                "statement_descriptor": statement_descriptor,
                "transfer_group": transfer_group,
                "amount": amount,
                "currency": currency,
            },
            dump_with=params._SerializerTopupsCreateBody,
            style={
                "amount": "form",
                "currency": "form",
                "description": "form",
                "expand": "deepObject",
                "metadata": "deepObject",
                "source": "form",
                "statement_descriptor": "form",
                "transfer_group": "form",
            },
            explode={
                "amount": True,
                "currency": True,
                "description": True,
                "expand": True,
                "metadata": True,
                "source": True,
                "statement_descriptor": True,
                "transfer_group": True,
            },
        )
        return await self._base_client.request(
            method="POST",
            path="/v1/topups",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.Topup,
            request_options=request_options or default_request_options(),
        )

    async def update(
        self,
        *,
        topup: str,
        data: typing.Union[
            typing.Optional[params.TopupsUpdateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Topup:
        """
        Update a top-up

        <p>Updates the metadata of a top-up. Other top-up details are not editable by design.</p>

        POST /v1/topups/{topup}

        Args:
            data: TopupsUpdateBody
            topup: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.topups.update(topup="string")
        ```
        """
        models.Topup.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerTopupsUpdateBody,
                style={
                    "description": "form",
                    "expand": "deepObject",
                    "metadata": "deepObject",
                },
                explode={"description": True, "expand": True, "metadata": True},
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/topups/{topup}",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.Topup,
            request_options=request_options or default_request_options(),
        )

    async def cancel(
        self,
        *,
        topup: str,
        data: typing.Union[
            typing.Optional[params.TopupsCancelBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Topup:
        """
        Cancel a top-up

        <p>Cancels a top-up. Only pending top-ups can be canceled.</p>

        POST /v1/topups/{topup}/cancel

        Args:
            data: TopupsCancelBody
            topup: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.topups.cancel(topup="string")
        ```
        """
        models.Topup.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerTopupsCancelBody,
                style={"expand": "deepObject"},
                explode={"expand": True},
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/topups/{topup}/cancel",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.Topup,
            request_options=request_options or default_request_options(),
        )
