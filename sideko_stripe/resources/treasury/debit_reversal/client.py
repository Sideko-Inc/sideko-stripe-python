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


class DebitReversalClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def list(
        self,
        *,
        financial_account: str,
        ending_before: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        limit: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        received_debit: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        resolution: typing.Union[
            typing.Optional[typing_extensions.Literal["lost", "won"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        starting_after: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        status: typing.Union[
            typing.Optional[
                typing_extensions.Literal["canceled", "completed", "processing"]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TreasuryDebitReversalListResponse:
        """
        List all DebitReversals

        <p>Returns a list of DebitReversals.</p>

        GET /v1/treasury/debit_reversals

        Args:
            ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            expand: Specifies which fields in the response should be expanded.
            limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            received_debit: Only return DebitReversals for the ReceivedDebit ID.
            resolution: Only return DebitReversals for a given resolution.
            starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
            status: Only return DebitReversals for a given status.
            financial_account: Returns objects associated with this FinancialAccount.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.treasury.debit_reversal.list(financial_account="string")
        ```
        """
        models.TreasuryDebitReversalListResponse.model_rebuild(
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
        if not isinstance(received_debit, type_utils.NotGiven):
            encode_query_param(
                _query,
                "received_debit",
                to_encodable(item=received_debit, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(resolution, type_utils.NotGiven):
            encode_query_param(
                _query,
                "resolution",
                to_encodable(
                    item=resolution, dump_with=typing_extensions.Literal["lost", "won"]
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
        if not isinstance(status, type_utils.NotGiven):
            encode_query_param(
                _query,
                "status",
                to_encodable(
                    item=status,
                    dump_with=typing_extensions.Literal[
                        "canceled", "completed", "processing"
                    ],
                ),
                style="form",
                explode=True,
            )
        return self._base_client.request(
            method="GET",
            path="/v1/treasury/debit_reversals",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.TreasuryDebitReversalListResponse,
            request_options=request_options or default_request_options(),
        )

    def get(
        self,
        *,
        debit_reversal: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TreasuryDebitReversal:
        """
        Retrieve a DebitReversal

        <p>Retrieves a DebitReversal object.</p>

        GET /v1/treasury/debit_reversals/{debit_reversal}

        Args:
            expand: Specifies which fields in the response should be expanded.
            debit_reversal: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.treasury.debit_reversal.get(debit_reversal="string")
        ```
        """
        models.TreasuryDebitReversal.model_rebuild(
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
            path=f"/v1/treasury/debit_reversals/{debit_reversal}",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.TreasuryDebitReversal,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        received_debit: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        metadata: typing.Union[
            typing.Optional[params.TreasuryDebitReversalCreateBodyMetadata],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TreasuryDebitReversal:
        """
        Create a DebitReversal

        <p>Reverses a ReceivedDebit and creates a DebitReversal object.</p>

        POST /v1/treasury/debit_reversals

        Args:
            expand: Specifies which fields in the response should be expanded.
            metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
            received_debit: The ReceivedDebit to reverse.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.treasury.debit_reversal.create(received_debit="string")
        ```
        """
        models.TreasuryDebitReversal.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _data = to_form_urlencoded(
            item={
                "expand": expand,
                "metadata": metadata,
                "received_debit": received_debit,
            },
            dump_with=params._SerializerTreasuryDebitReversalCreateBody,
            style={
                "expand": "deepObject",
                "metadata": "deepObject",
                "received_debit": "form",
            },
            explode={"expand": True, "metadata": True, "received_debit": True},
        )
        return self._base_client.request(
            method="POST",
            path="/v1/treasury/debit_reversals",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.TreasuryDebitReversal,
            request_options=request_options or default_request_options(),
        )


class AsyncDebitReversalClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def list(
        self,
        *,
        financial_account: str,
        ending_before: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        limit: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        received_debit: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        resolution: typing.Union[
            typing.Optional[typing_extensions.Literal["lost", "won"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        starting_after: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        status: typing.Union[
            typing.Optional[
                typing_extensions.Literal["canceled", "completed", "processing"]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TreasuryDebitReversalListResponse:
        """
        List all DebitReversals

        <p>Returns a list of DebitReversals.</p>

        GET /v1/treasury/debit_reversals

        Args:
            ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            expand: Specifies which fields in the response should be expanded.
            limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            received_debit: Only return DebitReversals for the ReceivedDebit ID.
            resolution: Only return DebitReversals for a given resolution.
            starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
            status: Only return DebitReversals for a given status.
            financial_account: Returns objects associated with this FinancialAccount.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.treasury.debit_reversal.list(financial_account="string")
        ```
        """
        models.TreasuryDebitReversalListResponse.model_rebuild(
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
        if not isinstance(received_debit, type_utils.NotGiven):
            encode_query_param(
                _query,
                "received_debit",
                to_encodable(item=received_debit, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(resolution, type_utils.NotGiven):
            encode_query_param(
                _query,
                "resolution",
                to_encodable(
                    item=resolution, dump_with=typing_extensions.Literal["lost", "won"]
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
        if not isinstance(status, type_utils.NotGiven):
            encode_query_param(
                _query,
                "status",
                to_encodable(
                    item=status,
                    dump_with=typing_extensions.Literal[
                        "canceled", "completed", "processing"
                    ],
                ),
                style="form",
                explode=True,
            )
        return await self._base_client.request(
            method="GET",
            path="/v1/treasury/debit_reversals",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.TreasuryDebitReversalListResponse,
            request_options=request_options or default_request_options(),
        )

    async def get(
        self,
        *,
        debit_reversal: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TreasuryDebitReversal:
        """
        Retrieve a DebitReversal

        <p>Retrieves a DebitReversal object.</p>

        GET /v1/treasury/debit_reversals/{debit_reversal}

        Args:
            expand: Specifies which fields in the response should be expanded.
            debit_reversal: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.treasury.debit_reversal.get(debit_reversal="string")
        ```
        """
        models.TreasuryDebitReversal.model_rebuild(
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
            path=f"/v1/treasury/debit_reversals/{debit_reversal}",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.TreasuryDebitReversal,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        received_debit: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        metadata: typing.Union[
            typing.Optional[params.TreasuryDebitReversalCreateBodyMetadata],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TreasuryDebitReversal:
        """
        Create a DebitReversal

        <p>Reverses a ReceivedDebit and creates a DebitReversal object.</p>

        POST /v1/treasury/debit_reversals

        Args:
            expand: Specifies which fields in the response should be expanded.
            metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
            received_debit: The ReceivedDebit to reverse.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.treasury.debit_reversal.create(received_debit="string")
        ```
        """
        models.TreasuryDebitReversal.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _data = to_form_urlencoded(
            item={
                "expand": expand,
                "metadata": metadata,
                "received_debit": received_debit,
            },
            dump_with=params._SerializerTreasuryDebitReversalCreateBody,
            style={
                "expand": "deepObject",
                "metadata": "deepObject",
                "received_debit": "form",
            },
            explode={"expand": True, "metadata": True, "received_debit": True},
        )
        return await self._base_client.request(
            method="POST",
            path="/v1/treasury/debit_reversals",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.TreasuryDebitReversal,
            request_options=request_options or default_request_options(),
        )
