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
    type_utils,
)
from sideko_stripe.types import models, params


class TransactionEntryClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def list(
        self,
        *,
        financial_account: str,
        created: typing.Union[
            typing.Optional[
                typing.Union[params.TreasuryTransactionEntryListCreatedObj0, int]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        effective_at: typing.Union[
            typing.Optional[
                typing.Union[params.TreasuryTransactionEntryListEffectiveAtObj0, int]
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
        order_by: typing.Union[
            typing.Optional[typing_extensions.Literal["created", "effective_at"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        starting_after: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        transaction: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TreasuryTransactionEntryListResponse:
        """
        List all TransactionEntries

        <p>Retrieves a list of TransactionEntry objects.</p>

        GET /v1/treasury/transaction_entries

        Args:
            created: Only return TransactionEntries that were created during the given date interval.
            effective_at: typing.Union[TreasuryTransactionEntryListEffectiveAtObj0, int]
            ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            expand: Specifies which fields in the response should be expanded.
            limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            order_by: The results are in reverse chronological order by `created` or `effective_at`. The default is `created`.
            starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
            transaction: Only return TransactionEntries associated with this Transaction.
            financial_account: Returns objects associated with this FinancialAccount.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.treasury.transaction_entry.list(financial_account="string")
        ```
        """
        models.TreasuryTransactionEntryListResponse.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _query: QueryParams = {}
        encode_query_param(
            _query,
            "financial_account",
            to_encodable(item=financial_account, dump_with=str),
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
                        params._SerializerTreasuryTransactionEntryListCreatedObj0, int
                    ],
                ),
                style="deepObject",
                explode=True,
            )
        if not isinstance(effective_at, type_utils.NotGiven):
            encode_query_param(
                _query,
                "effective_at",
                to_encodable(
                    item=effective_at,
                    dump_with=typing.Union[
                        params._SerializerTreasuryTransactionEntryListEffectiveAtObj0,
                        int,
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
        if not isinstance(order_by, type_utils.NotGiven):
            encode_query_param(
                _query,
                "order_by",
                to_encodable(
                    item=order_by,
                    dump_with=typing_extensions.Literal["created", "effective_at"],
                ),
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
        if not isinstance(transaction, type_utils.NotGiven):
            encode_query_param(
                _query,
                "transaction",
                to_encodable(item=transaction, dump_with=str),
                style="form",
                explode=True,
            )
        return self._base_client.request(
            method="GET",
            path="/v1/treasury/transaction_entries",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.TreasuryTransactionEntryListResponse,
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
    ) -> models.TreasuryTransactionEntry:
        """
        Retrieve a TransactionEntry

        <p>Retrieves a TransactionEntry object.</p>

        GET /v1/treasury/transaction_entries/{id}

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
        client.treasury.transaction_entry.get(id="string")
        ```
        """
        models.TreasuryTransactionEntry.model_rebuild(
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
            path=f"/v1/treasury/transaction_entries/{id}",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.TreasuryTransactionEntry,
            request_options=request_options or default_request_options(),
        )


class AsyncTransactionEntryClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def list(
        self,
        *,
        financial_account: str,
        created: typing.Union[
            typing.Optional[
                typing.Union[params.TreasuryTransactionEntryListCreatedObj0, int]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        effective_at: typing.Union[
            typing.Optional[
                typing.Union[params.TreasuryTransactionEntryListEffectiveAtObj0, int]
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
        order_by: typing.Union[
            typing.Optional[typing_extensions.Literal["created", "effective_at"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        starting_after: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        transaction: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TreasuryTransactionEntryListResponse:
        """
        List all TransactionEntries

        <p>Retrieves a list of TransactionEntry objects.</p>

        GET /v1/treasury/transaction_entries

        Args:
            created: Only return TransactionEntries that were created during the given date interval.
            effective_at: typing.Union[TreasuryTransactionEntryListEffectiveAtObj0, int]
            ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            expand: Specifies which fields in the response should be expanded.
            limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            order_by: The results are in reverse chronological order by `created` or `effective_at`. The default is `created`.
            starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
            transaction: Only return TransactionEntries associated with this Transaction.
            financial_account: Returns objects associated with this FinancialAccount.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.treasury.transaction_entry.list(financial_account="string")
        ```
        """
        models.TreasuryTransactionEntryListResponse.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _query: QueryParams = {}
        encode_query_param(
            _query,
            "financial_account",
            to_encodable(item=financial_account, dump_with=str),
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
                        params._SerializerTreasuryTransactionEntryListCreatedObj0, int
                    ],
                ),
                style="deepObject",
                explode=True,
            )
        if not isinstance(effective_at, type_utils.NotGiven):
            encode_query_param(
                _query,
                "effective_at",
                to_encodable(
                    item=effective_at,
                    dump_with=typing.Union[
                        params._SerializerTreasuryTransactionEntryListEffectiveAtObj0,
                        int,
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
        if not isinstance(order_by, type_utils.NotGiven):
            encode_query_param(
                _query,
                "order_by",
                to_encodable(
                    item=order_by,
                    dump_with=typing_extensions.Literal["created", "effective_at"],
                ),
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
        if not isinstance(transaction, type_utils.NotGiven):
            encode_query_param(
                _query,
                "transaction",
                to_encodable(item=transaction, dump_with=str),
                style="form",
                explode=True,
            )
        return await self._base_client.request(
            method="GET",
            path="/v1/treasury/transaction_entries",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.TreasuryTransactionEntryListResponse,
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
    ) -> models.TreasuryTransactionEntry:
        """
        Retrieve a TransactionEntry

        <p>Retrieves a TransactionEntry object.</p>

        GET /v1/treasury/transaction_entries/{id}

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
        await client.treasury.transaction_entry.get(id="string")
        ```
        """
        models.TreasuryTransactionEntry.model_rebuild(
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
            path=f"/v1/treasury/transaction_entries/{id}",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.TreasuryTransactionEntry,
            request_options=request_options or default_request_options(),
        )
