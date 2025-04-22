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


class OutboundTransferClient:
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
                    "canceled", "failed", "posted", "processing", "returned"
                ]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TreasuryOutboundTransferListResponse:
        """
        List all OutboundTransfers

        <p>Returns a list of OutboundTransfers sent from the specified FinancialAccount.</p>

        GET /v1/treasury/outbound_transfers

        Args:
            ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            expand: Specifies which fields in the response should be expanded.
            limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
            status: Only return OutboundTransfers that have the given status: `processing`, `canceled`, `failed`, `posted`, or `returned`.
            financial_account: Returns objects associated with this FinancialAccount.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.treasury.outbound_transfer.list(financial_account="string")
        ```
        """
        models.TreasuryOutboundTransferListResponse.model_rebuild(
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
                        "canceled", "failed", "posted", "processing", "returned"
                    ],
                ),
                style="form",
                explode=True,
            )
        return self._base_client.request(
            method="GET",
            path="/v1/treasury/outbound_transfers",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.TreasuryOutboundTransferListResponse,
            request_options=request_options or default_request_options(),
        )

    def get(
        self,
        *,
        outbound_transfer: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TreasuryOutboundTransfer:
        """
        Retrieve an OutboundTransfer

        <p>Retrieves the details of an existing OutboundTransfer by passing the unique OutboundTransfer ID from either the OutboundTransfer creation request or OutboundTransfer list.</p>

        GET /v1/treasury/outbound_transfers/{outbound_transfer}

        Args:
            expand: Specifies which fields in the response should be expanded.
            outbound_transfer: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.treasury.outbound_transfer.get(outbound_transfer="string")
        ```
        """
        models.TreasuryOutboundTransfer.model_rebuild(
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
            path=f"/v1/treasury/outbound_transfers/{outbound_transfer}",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.TreasuryOutboundTransfer,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        amount: int,
        currency: str,
        financial_account: str,
        description: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        destination_payment_method: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        destination_payment_method_data: typing.Union[
            typing.Optional[
                params.TreasuryOutboundTransferCreateBodyDestinationPaymentMethodData
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        destination_payment_method_options: typing.Union[
            typing.Optional[
                params.TreasuryOutboundTransferCreateBodyDestinationPaymentMethodOptions
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        metadata: typing.Union[
            typing.Optional[params.TreasuryOutboundTransferCreateBodyMetadata],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        statement_descriptor: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TreasuryOutboundTransfer:
        """
        Create an OutboundTransfer

        <p>Creates an OutboundTransfer.</p>

        POST /v1/treasury/outbound_transfers

        Args:
            description: An arbitrary string attached to the object. Often useful for displaying to users.
            destination_payment_method: The PaymentMethod to use as the payment instrument for the OutboundTransfer.
            destination_payment_method_data: Hash used to generate the PaymentMethod to be used for this OutboundTransfer. Exclusive with `destination_payment_method`.
            destination_payment_method_options: Hash describing payment method configuration details.
            expand: Specifies which fields in the response should be expanded.
            metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
            statement_descriptor: Statement descriptor to be shown on the receiving end of an OutboundTransfer. Maximum 10 characters for `ach` transfers or 140 characters for `us_domestic_wire` transfers. The default value is "transfer".
            amount: Amount (in cents) to be transferred.
            currency: Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
            financial_account: The FinancialAccount to pull funds from.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.treasury.outbound_transfer.create(
            amount=123, currency="string", financial_account="string"
        )
        ```
        """
        models.TreasuryOutboundTransfer.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _data = to_form_urlencoded(
            item={
                "description": description,
                "destination_payment_method": destination_payment_method,
                "destination_payment_method_data": destination_payment_method_data,
                "destination_payment_method_options": destination_payment_method_options,
                "expand": expand,
                "metadata": metadata,
                "statement_descriptor": statement_descriptor,
                "amount": amount,
                "currency": currency,
                "financial_account": financial_account,
            },
            dump_with=params._SerializerTreasuryOutboundTransferCreateBody,
            style={
                "amount": "form",
                "currency": "form",
                "description": "form",
                "destination_payment_method": "form",
                "destination_payment_method_data": "deepObject",
                "destination_payment_method_options": "deepObject",
                "expand": "deepObject",
                "financial_account": "form",
                "metadata": "deepObject",
                "statement_descriptor": "form",
            },
            explode={
                "amount": True,
                "currency": True,
                "description": True,
                "destination_payment_method": True,
                "destination_payment_method_data": True,
                "destination_payment_method_options": True,
                "expand": True,
                "financial_account": True,
                "metadata": True,
                "statement_descriptor": True,
            },
        )
        return self._base_client.request(
            method="POST",
            path="/v1/treasury/outbound_transfers",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.TreasuryOutboundTransfer,
            request_options=request_options or default_request_options(),
        )

    def cancel(
        self,
        *,
        outbound_transfer: str,
        data: typing.Union[
            typing.Optional[params.TreasuryOutboundTransferCancelBody],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TreasuryOutboundTransfer:
        """
        Cancel an OutboundTransfer

        <p>An OutboundTransfer can be canceled if the funds have not yet been paid out.</p>

        POST /v1/treasury/outbound_transfers/{outbound_transfer}/cancel

        Args:
            data: TreasuryOutboundTransferCancelBody
            outbound_transfer: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.treasury.outbound_transfer.cancel(outbound_transfer="string")
        ```
        """
        models.TreasuryOutboundTransfer.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerTreasuryOutboundTransferCancelBody,
                style={"expand": "deepObject"},
                explode={"expand": True},
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/treasury/outbound_transfers/{outbound_transfer}/cancel",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.TreasuryOutboundTransfer,
            request_options=request_options or default_request_options(),
        )


class AsyncOutboundTransferClient:
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
                    "canceled", "failed", "posted", "processing", "returned"
                ]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TreasuryOutboundTransferListResponse:
        """
        List all OutboundTransfers

        <p>Returns a list of OutboundTransfers sent from the specified FinancialAccount.</p>

        GET /v1/treasury/outbound_transfers

        Args:
            ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            expand: Specifies which fields in the response should be expanded.
            limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
            status: Only return OutboundTransfers that have the given status: `processing`, `canceled`, `failed`, `posted`, or `returned`.
            financial_account: Returns objects associated with this FinancialAccount.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.treasury.outbound_transfer.list(financial_account="string")
        ```
        """
        models.TreasuryOutboundTransferListResponse.model_rebuild(
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
                        "canceled", "failed", "posted", "processing", "returned"
                    ],
                ),
                style="form",
                explode=True,
            )
        return await self._base_client.request(
            method="GET",
            path="/v1/treasury/outbound_transfers",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.TreasuryOutboundTransferListResponse,
            request_options=request_options or default_request_options(),
        )

    async def get(
        self,
        *,
        outbound_transfer: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TreasuryOutboundTransfer:
        """
        Retrieve an OutboundTransfer

        <p>Retrieves the details of an existing OutboundTransfer by passing the unique OutboundTransfer ID from either the OutboundTransfer creation request or OutboundTransfer list.</p>

        GET /v1/treasury/outbound_transfers/{outbound_transfer}

        Args:
            expand: Specifies which fields in the response should be expanded.
            outbound_transfer: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.treasury.outbound_transfer.get(outbound_transfer="string")
        ```
        """
        models.TreasuryOutboundTransfer.model_rebuild(
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
            path=f"/v1/treasury/outbound_transfers/{outbound_transfer}",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.TreasuryOutboundTransfer,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        amount: int,
        currency: str,
        financial_account: str,
        description: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        destination_payment_method: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        destination_payment_method_data: typing.Union[
            typing.Optional[
                params.TreasuryOutboundTransferCreateBodyDestinationPaymentMethodData
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        destination_payment_method_options: typing.Union[
            typing.Optional[
                params.TreasuryOutboundTransferCreateBodyDestinationPaymentMethodOptions
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        metadata: typing.Union[
            typing.Optional[params.TreasuryOutboundTransferCreateBodyMetadata],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        statement_descriptor: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TreasuryOutboundTransfer:
        """
        Create an OutboundTransfer

        <p>Creates an OutboundTransfer.</p>

        POST /v1/treasury/outbound_transfers

        Args:
            description: An arbitrary string attached to the object. Often useful for displaying to users.
            destination_payment_method: The PaymentMethod to use as the payment instrument for the OutboundTransfer.
            destination_payment_method_data: Hash used to generate the PaymentMethod to be used for this OutboundTransfer. Exclusive with `destination_payment_method`.
            destination_payment_method_options: Hash describing payment method configuration details.
            expand: Specifies which fields in the response should be expanded.
            metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
            statement_descriptor: Statement descriptor to be shown on the receiving end of an OutboundTransfer. Maximum 10 characters for `ach` transfers or 140 characters for `us_domestic_wire` transfers. The default value is "transfer".
            amount: Amount (in cents) to be transferred.
            currency: Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
            financial_account: The FinancialAccount to pull funds from.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.treasury.outbound_transfer.create(
            amount=123, currency="string", financial_account="string"
        )
        ```
        """
        models.TreasuryOutboundTransfer.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _data = to_form_urlencoded(
            item={
                "description": description,
                "destination_payment_method": destination_payment_method,
                "destination_payment_method_data": destination_payment_method_data,
                "destination_payment_method_options": destination_payment_method_options,
                "expand": expand,
                "metadata": metadata,
                "statement_descriptor": statement_descriptor,
                "amount": amount,
                "currency": currency,
                "financial_account": financial_account,
            },
            dump_with=params._SerializerTreasuryOutboundTransferCreateBody,
            style={
                "amount": "form",
                "currency": "form",
                "description": "form",
                "destination_payment_method": "form",
                "destination_payment_method_data": "deepObject",
                "destination_payment_method_options": "deepObject",
                "expand": "deepObject",
                "financial_account": "form",
                "metadata": "deepObject",
                "statement_descriptor": "form",
            },
            explode={
                "amount": True,
                "currency": True,
                "description": True,
                "destination_payment_method": True,
                "destination_payment_method_data": True,
                "destination_payment_method_options": True,
                "expand": True,
                "financial_account": True,
                "metadata": True,
                "statement_descriptor": True,
            },
        )
        return await self._base_client.request(
            method="POST",
            path="/v1/treasury/outbound_transfers",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.TreasuryOutboundTransfer,
            request_options=request_options or default_request_options(),
        )

    async def cancel(
        self,
        *,
        outbound_transfer: str,
        data: typing.Union[
            typing.Optional[params.TreasuryOutboundTransferCancelBody],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TreasuryOutboundTransfer:
        """
        Cancel an OutboundTransfer

        <p>An OutboundTransfer can be canceled if the funds have not yet been paid out.</p>

        POST /v1/treasury/outbound_transfers/{outbound_transfer}/cancel

        Args:
            data: TreasuryOutboundTransferCancelBody
            outbound_transfer: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.treasury.outbound_transfer.cancel(outbound_transfer="string")
        ```
        """
        models.TreasuryOutboundTransfer.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerTreasuryOutboundTransferCancelBody,
                style={"expand": "deepObject"},
                explode={"expand": True},
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/treasury/outbound_transfers/{outbound_transfer}/cancel",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.TreasuryOutboundTransfer,
            request_options=request_options or default_request_options(),
        )
