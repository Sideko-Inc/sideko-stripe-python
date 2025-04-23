import typing

from sideko_stripe.core import (
    AsyncBaseClient,
    QueryParams,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
    encode_query_param,
    to_encodable,
    type_utils,
)
from sideko_stripe.types import models, params


class TransactionClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def list(
        self,
        *,
        account: str,
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
        transacted_at: typing.Union[
            typing.Optional[
                typing.Union[
                    params.FinancialConnectionsTransactionListTransactedAtObj0, int
                ]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        transaction_refresh: typing.Union[
            typing.Optional[
                params.FinancialConnectionsTransactionListTransactionRefresh
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.FinancialConnectionsTransactionListResponse:
        """
        List Transactions

        <p>Returns a list of Financial Connections <code>Transaction</code> objects.</p>

        GET /v1/financial_connections/transactions

        Args:
            ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            expand: Specifies which fields in the response should be expanded.
            limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
            transacted_at: A filter on the list based on the object `transacted_at` field. The value can be a string with an integer Unix timestamp, or it can be a dictionary with the following options:
            transaction_refresh: A filter on the list based on the object `transaction_refresh` field. The value can be a dictionary with the following options:
            account: The ID of the Financial Connections Account whose transactions will be retrieved.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.financial_connections.transaction.list(account="string")
        ```
        """
        _query: QueryParams = {}
        encode_query_param(
            _query,
            "account",
            to_encodable(item=account, dump_with=str),
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
        if not isinstance(transacted_at, type_utils.NotGiven):
            encode_query_param(
                _query,
                "transacted_at",
                to_encodable(
                    item=transacted_at,
                    dump_with=typing.Union[
                        params._SerializerFinancialConnectionsTransactionListTransactedAtObj0,
                        int,
                    ],
                ),
                style="deepObject",
                explode=True,
            )
        if not isinstance(transaction_refresh, type_utils.NotGiven):
            encode_query_param(
                _query,
                "transaction_refresh",
                to_encodable(
                    item=transaction_refresh,
                    dump_with=params._SerializerFinancialConnectionsTransactionListTransactionRefresh,
                ),
                style="deepObject",
                explode=True,
            )
        return self._base_client.request(
            method="GET",
            path="/v1/financial_connections/transactions",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.FinancialConnectionsTransactionListResponse,
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
    ) -> models.FinancialConnectionsTransaction:
        """
        Retrieve a Transaction

        <p>Retrieves the details of a Financial Connections <code>Transaction</code></p>

        GET /v1/financial_connections/transactions/{transaction}

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
        client.financial_connections.transaction.get(transaction="string")
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
            path=f"/v1/financial_connections/transactions/{transaction}",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.FinancialConnectionsTransaction,
            request_options=request_options or default_request_options(),
        )


class AsyncTransactionClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def list(
        self,
        *,
        account: str,
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
        transacted_at: typing.Union[
            typing.Optional[
                typing.Union[
                    params.FinancialConnectionsTransactionListTransactedAtObj0, int
                ]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        transaction_refresh: typing.Union[
            typing.Optional[
                params.FinancialConnectionsTransactionListTransactionRefresh
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.FinancialConnectionsTransactionListResponse:
        """
        List Transactions

        <p>Returns a list of Financial Connections <code>Transaction</code> objects.</p>

        GET /v1/financial_connections/transactions

        Args:
            ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            expand: Specifies which fields in the response should be expanded.
            limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
            transacted_at: A filter on the list based on the object `transacted_at` field. The value can be a string with an integer Unix timestamp, or it can be a dictionary with the following options:
            transaction_refresh: A filter on the list based on the object `transaction_refresh` field. The value can be a dictionary with the following options:
            account: The ID of the Financial Connections Account whose transactions will be retrieved.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.financial_connections.transaction.list(account="string")
        ```
        """
        _query: QueryParams = {}
        encode_query_param(
            _query,
            "account",
            to_encodable(item=account, dump_with=str),
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
        if not isinstance(transacted_at, type_utils.NotGiven):
            encode_query_param(
                _query,
                "transacted_at",
                to_encodable(
                    item=transacted_at,
                    dump_with=typing.Union[
                        params._SerializerFinancialConnectionsTransactionListTransactedAtObj0,
                        int,
                    ],
                ),
                style="deepObject",
                explode=True,
            )
        if not isinstance(transaction_refresh, type_utils.NotGiven):
            encode_query_param(
                _query,
                "transaction_refresh",
                to_encodable(
                    item=transaction_refresh,
                    dump_with=params._SerializerFinancialConnectionsTransactionListTransactionRefresh,
                ),
                style="deepObject",
                explode=True,
            )
        return await self._base_client.request(
            method="GET",
            path="/v1/financial_connections/transactions",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.FinancialConnectionsTransactionListResponse,
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
    ) -> models.FinancialConnectionsTransaction:
        """
        Retrieve a Transaction

        <p>Retrieves the details of a Financial Connections <code>Transaction</code></p>

        GET /v1/financial_connections/transactions/{transaction}

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
        await client.financial_connections.transaction.get(transaction="string")
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
            path=f"/v1/financial_connections/transactions/{transaction}",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.FinancialConnectionsTransaction,
            request_options=request_options or default_request_options(),
        )
