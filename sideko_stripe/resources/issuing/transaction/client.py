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


class TransactionClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def list(
        self,
        *,
        card: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        cardholder: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        created: typing.Union[
            typing.Optional[
                typing.Union[params.IssuingTransactionListCreatedObj0, int]
            ],
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
        type_: typing.Union[
            typing.Optional[typing_extensions.Literal["capture", "refund"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.IssuingTransactionListResponse:
        """
        List all transactions

        <p>Returns a list of Issuing <code>Transaction</code> objects. The objects are sorted in descending order by creation date, with the most recently created object appearing first.</p>

        GET /v1/issuing/transactions

        Args:
            card: Only return transactions that belong to the given card.
            cardholder: Only return transactions that belong to the given cardholder.
            created: Only return transactions that were created during the given date interval.
            ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            expand: Specifies which fields in the response should be expanded.
            limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
            type: Only return transactions that have the given type. One of `capture` or `refund`.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.issuing.transaction.list()
        ```
        """
        models.IssuingTransactionListResponse.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _query: QueryParams = {}
        if not isinstance(card, type_utils.NotGiven):
            encode_query_param(
                _query,
                "card",
                to_encodable(item=card, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(cardholder, type_utils.NotGiven):
            encode_query_param(
                _query,
                "cardholder",
                to_encodable(item=cardholder, dump_with=str),
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
                        params._SerializerIssuingTransactionListCreatedObj0, int
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
        if not isinstance(type_, type_utils.NotGiven):
            encode_query_param(
                _query,
                "type",
                to_encodable(
                    item=type_, dump_with=typing_extensions.Literal["capture", "refund"]
                ),
                style="form",
                explode=True,
            )
        return self._base_client.request(
            method="GET",
            path="/v1/issuing/transactions",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.IssuingTransactionListResponse,
            request_options=request_options or default_request_options(),
        )

    def get(
        self,
        *,
        transaction: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.IssuingTransaction:
        """
        Retrieve a transaction

        <p>Retrieves an Issuing <code>Transaction</code> object.</p>

        GET /v1/issuing/transactions/{transaction}

        Args:
            expand: Specifies which fields in the response should be expanded.
            transaction: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.issuing.transaction.get(transaction="string")
        ```
        """
        models.IssuingTransaction.model_rebuild(
            _types_namespace=models._types_namespace
        )
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
            path=f"/v1/issuing/transactions/{transaction}",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.IssuingTransaction,
            request_options=request_options or default_request_options(),
        )

    def update(
        self,
        *,
        transaction: str,
        data: typing.Union[
            typing.Optional[params.IssuingTransactionUpdateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.IssuingTransaction:
        """
        Update a transaction

        <p>Updates the specified Issuing <code>Transaction</code> object by setting the values of the parameters passed. Any parameters not provided will be left unchanged.</p>

        POST /v1/issuing/transactions/{transaction}

        Args:
            data: IssuingTransactionUpdateBody
            transaction: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.issuing.transaction.update(transaction="string")
        ```
        """
        models.IssuingTransaction.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerIssuingTransactionUpdateBody,
                style={"expand": "deepObject", "metadata": "deepObject"},
                explode={"expand": True, "metadata": True},
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/issuing/transactions/{transaction}",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.IssuingTransaction,
            request_options=request_options or default_request_options(),
        )


class AsyncTransactionClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def list(
        self,
        *,
        card: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        cardholder: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        created: typing.Union[
            typing.Optional[
                typing.Union[params.IssuingTransactionListCreatedObj0, int]
            ],
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
        type_: typing.Union[
            typing.Optional[typing_extensions.Literal["capture", "refund"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.IssuingTransactionListResponse:
        """
        List all transactions

        <p>Returns a list of Issuing <code>Transaction</code> objects. The objects are sorted in descending order by creation date, with the most recently created object appearing first.</p>

        GET /v1/issuing/transactions

        Args:
            card: Only return transactions that belong to the given card.
            cardholder: Only return transactions that belong to the given cardholder.
            created: Only return transactions that were created during the given date interval.
            ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            expand: Specifies which fields in the response should be expanded.
            limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
            type: Only return transactions that have the given type. One of `capture` or `refund`.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.issuing.transaction.list()
        ```
        """
        models.IssuingTransactionListResponse.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _query: QueryParams = {}
        if not isinstance(card, type_utils.NotGiven):
            encode_query_param(
                _query,
                "card",
                to_encodable(item=card, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(cardholder, type_utils.NotGiven):
            encode_query_param(
                _query,
                "cardholder",
                to_encodable(item=cardholder, dump_with=str),
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
                        params._SerializerIssuingTransactionListCreatedObj0, int
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
        if not isinstance(type_, type_utils.NotGiven):
            encode_query_param(
                _query,
                "type",
                to_encodable(
                    item=type_, dump_with=typing_extensions.Literal["capture", "refund"]
                ),
                style="form",
                explode=True,
            )
        return await self._base_client.request(
            method="GET",
            path="/v1/issuing/transactions",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.IssuingTransactionListResponse,
            request_options=request_options or default_request_options(),
        )

    async def get(
        self,
        *,
        transaction: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.IssuingTransaction:
        """
        Retrieve a transaction

        <p>Retrieves an Issuing <code>Transaction</code> object.</p>

        GET /v1/issuing/transactions/{transaction}

        Args:
            expand: Specifies which fields in the response should be expanded.
            transaction: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.issuing.transaction.get(transaction="string")
        ```
        """
        models.IssuingTransaction.model_rebuild(
            _types_namespace=models._types_namespace
        )
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
            path=f"/v1/issuing/transactions/{transaction}",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.IssuingTransaction,
            request_options=request_options or default_request_options(),
        )

    async def update(
        self,
        *,
        transaction: str,
        data: typing.Union[
            typing.Optional[params.IssuingTransactionUpdateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.IssuingTransaction:
        """
        Update a transaction

        <p>Updates the specified Issuing <code>Transaction</code> object by setting the values of the parameters passed. Any parameters not provided will be left unchanged.</p>

        POST /v1/issuing/transactions/{transaction}

        Args:
            data: IssuingTransactionUpdateBody
            transaction: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.issuing.transaction.update(transaction="string")
        ```
        """
        models.IssuingTransaction.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerIssuingTransactionUpdateBody,
                style={"expand": "deepObject", "metadata": "deepObject"},
                explode={"expand": True, "metadata": True},
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/issuing/transactions/{transaction}",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.IssuingTransaction,
            request_options=request_options or default_request_options(),
        )
