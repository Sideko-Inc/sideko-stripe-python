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


class InboundTransferClient:
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
        starting_after: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        status: typing.Union[
            typing.Optional[
                typing_extensions.Literal[
                    "canceled", "failed", "processing", "succeeded"
                ]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TreasuryInboundTransferListResponse:
        """
        List all InboundTransfers

        <p>Returns a list of InboundTransfers sent from the specified FinancialAccount.</p>

        GET /v1/treasury/inbound_transfers

        Args:
            ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            expand: Specifies which fields in the response should be expanded.
            limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
            status: Only return InboundTransfers that have the given status: `processing`, `succeeded`, `failed` or `canceled`.
            financial_account: Returns objects associated with this FinancialAccount.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.treasury.inbound_transfer.list(financial_account="string")
        ```
        """
        models.TreasuryInboundTransferListResponse.model_rebuild(
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
                        "canceled", "failed", "processing", "succeeded"
                    ],
                ),
                style="form",
                explode=True,
            )
        return self._base_client.request(
            method="GET",
            path="/v1/treasury/inbound_transfers",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.TreasuryInboundTransferListResponse,
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
    ) -> models.TreasuryInboundTransfer:
        """
        Retrieve an InboundTransfer

        <p>Retrieves the details of an existing InboundTransfer.</p>

        GET /v1/treasury/inbound_transfers/{id}

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
        client.treasury.inbound_transfer.get(id="string")
        ```
        """
        models.TreasuryInboundTransfer.model_rebuild(
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
            path=f"/v1/treasury/inbound_transfers/{id}",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.TreasuryInboundTransfer,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        amount: int,
        currency: str,
        financial_account: str,
        origin_payment_method: str,
        description: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        metadata: typing.Union[
            typing.Optional[params.TreasuryInboundTransferCreateBodyMetadata],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        statement_descriptor: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TreasuryInboundTransfer:
        """
        Create an InboundTransfer

        <p>Creates an InboundTransfer.</p>

        POST /v1/treasury/inbound_transfers

        Args:
            description: An arbitrary string attached to the object. Often useful for displaying to users.
            expand: Specifies which fields in the response should be expanded.
            metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
            statement_descriptor: The complete description that appears on your customers' statements. Maximum 10 characters.
            amount: Amount (in cents) to be transferred.
            currency: Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
            financial_account: The FinancialAccount to send funds to.
            origin_payment_method: The origin payment method to be debited for the InboundTransfer.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.treasury.inbound_transfer.create(
            amount=123,
            currency="string",
            financial_account="string",
            origin_payment_method="string",
        )
        ```
        """
        models.TreasuryInboundTransfer.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _data = to_form_urlencoded(
            item={
                "description": description,
                "expand": expand,
                "metadata": metadata,
                "statement_descriptor": statement_descriptor,
                "amount": amount,
                "currency": currency,
                "financial_account": financial_account,
                "origin_payment_method": origin_payment_method,
            },
            dump_with=params._SerializerTreasuryInboundTransferCreateBody,
            style={
                "amount": "form",
                "currency": "form",
                "description": "form",
                "expand": "deepObject",
                "financial_account": "form",
                "metadata": "deepObject",
                "origin_payment_method": "form",
                "statement_descriptor": "form",
            },
            explode={
                "amount": True,
                "currency": True,
                "description": True,
                "expand": True,
                "financial_account": True,
                "metadata": True,
                "origin_payment_method": True,
                "statement_descriptor": True,
            },
        )
        return self._base_client.request(
            method="POST",
            path="/v1/treasury/inbound_transfers",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.TreasuryInboundTransfer,
            request_options=request_options or default_request_options(),
        )

    def cance(
        self,
        *,
        inbound_transfer: str,
        data: typing.Union[
            typing.Optional[params.TreasuryInboundTransferCanceBody],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TreasuryInboundTransfer:
        """
        Cancel an InboundTransfer

        <p>Cancels an InboundTransfer.</p>

        POST /v1/treasury/inbound_transfers/{inbound_transfer}/cancel

        Args:
            data: TreasuryInboundTransferCanceBody
            inbound_transfer: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.treasury.inbound_transfer.cance(inbound_transfer="string")
        ```
        """
        models.TreasuryInboundTransfer.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerTreasuryInboundTransferCanceBody,
                style={"expand": "deepObject"},
                explode={"expand": True},
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/treasury/inbound_transfers/{inbound_transfer}/cancel",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.TreasuryInboundTransfer,
            request_options=request_options or default_request_options(),
        )


class AsyncInboundTransferClient:
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
        starting_after: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        status: typing.Union[
            typing.Optional[
                typing_extensions.Literal[
                    "canceled", "failed", "processing", "succeeded"
                ]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TreasuryInboundTransferListResponse:
        """
        List all InboundTransfers

        <p>Returns a list of InboundTransfers sent from the specified FinancialAccount.</p>

        GET /v1/treasury/inbound_transfers

        Args:
            ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            expand: Specifies which fields in the response should be expanded.
            limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
            status: Only return InboundTransfers that have the given status: `processing`, `succeeded`, `failed` or `canceled`.
            financial_account: Returns objects associated with this FinancialAccount.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.treasury.inbound_transfer.list(financial_account="string")
        ```
        """
        models.TreasuryInboundTransferListResponse.model_rebuild(
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
                        "canceled", "failed", "processing", "succeeded"
                    ],
                ),
                style="form",
                explode=True,
            )
        return await self._base_client.request(
            method="GET",
            path="/v1/treasury/inbound_transfers",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.TreasuryInboundTransferListResponse,
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
    ) -> models.TreasuryInboundTransfer:
        """
        Retrieve an InboundTransfer

        <p>Retrieves the details of an existing InboundTransfer.</p>

        GET /v1/treasury/inbound_transfers/{id}

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
        await client.treasury.inbound_transfer.get(id="string")
        ```
        """
        models.TreasuryInboundTransfer.model_rebuild(
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
            path=f"/v1/treasury/inbound_transfers/{id}",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.TreasuryInboundTransfer,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        amount: int,
        currency: str,
        financial_account: str,
        origin_payment_method: str,
        description: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        metadata: typing.Union[
            typing.Optional[params.TreasuryInboundTransferCreateBodyMetadata],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        statement_descriptor: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TreasuryInboundTransfer:
        """
        Create an InboundTransfer

        <p>Creates an InboundTransfer.</p>

        POST /v1/treasury/inbound_transfers

        Args:
            description: An arbitrary string attached to the object. Often useful for displaying to users.
            expand: Specifies which fields in the response should be expanded.
            metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
            statement_descriptor: The complete description that appears on your customers' statements. Maximum 10 characters.
            amount: Amount (in cents) to be transferred.
            currency: Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
            financial_account: The FinancialAccount to send funds to.
            origin_payment_method: The origin payment method to be debited for the InboundTransfer.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.treasury.inbound_transfer.create(
            amount=123,
            currency="string",
            financial_account="string",
            origin_payment_method="string",
        )
        ```
        """
        models.TreasuryInboundTransfer.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _data = to_form_urlencoded(
            item={
                "description": description,
                "expand": expand,
                "metadata": metadata,
                "statement_descriptor": statement_descriptor,
                "amount": amount,
                "currency": currency,
                "financial_account": financial_account,
                "origin_payment_method": origin_payment_method,
            },
            dump_with=params._SerializerTreasuryInboundTransferCreateBody,
            style={
                "amount": "form",
                "currency": "form",
                "description": "form",
                "expand": "deepObject",
                "financial_account": "form",
                "metadata": "deepObject",
                "origin_payment_method": "form",
                "statement_descriptor": "form",
            },
            explode={
                "amount": True,
                "currency": True,
                "description": True,
                "expand": True,
                "financial_account": True,
                "metadata": True,
                "origin_payment_method": True,
                "statement_descriptor": True,
            },
        )
        return await self._base_client.request(
            method="POST",
            path="/v1/treasury/inbound_transfers",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.TreasuryInboundTransfer,
            request_options=request_options or default_request_options(),
        )

    async def cance(
        self,
        *,
        inbound_transfer: str,
        data: typing.Union[
            typing.Optional[params.TreasuryInboundTransferCanceBody],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TreasuryInboundTransfer:
        """
        Cancel an InboundTransfer

        <p>Cancels an InboundTransfer.</p>

        POST /v1/treasury/inbound_transfers/{inbound_transfer}/cancel

        Args:
            data: TreasuryInboundTransferCanceBody
            inbound_transfer: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.treasury.inbound_transfer.cance(inbound_transfer="string")
        ```
        """
        models.TreasuryInboundTransfer.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerTreasuryInboundTransferCanceBody,
                style={"expand": "deepObject"},
                explode={"expand": True},
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/treasury/inbound_transfers/{inbound_transfer}/cancel",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.TreasuryInboundTransfer,
            request_options=request_options or default_request_options(),
        )
