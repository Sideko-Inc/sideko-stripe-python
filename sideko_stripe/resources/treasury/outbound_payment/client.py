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


class OutboundPaymentClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def list(
        self,
        *,
        financial_account: str,
        created: typing.Union[
            typing.Optional[
                typing.Union[params.TreasuryOutboundPaymentListCreatedObj0, int]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        customer: typing.Union[
            typing.Optional[str], type_utils.NotGiven
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
                typing_extensions.Literal[
                    "canceled", "failed", "posted", "processing", "returned"
                ]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TreasuryOutboundPaymentListResponse:
        """
        List all OutboundPayments

        <p>Returns a list of OutboundPayments sent from the specified FinancialAccount.</p>

        GET /v1/treasury/outbound_payments

        Args:
            created: Only return OutboundPayments that were created during the given date interval.
            customer: Only return OutboundPayments sent to this customer.
            ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            expand: Specifies which fields in the response should be expanded.
            limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
            status: Only return OutboundPayments that have the given status: `processing`, `failed`, `posted`, `returned`, or `canceled`.
            financial_account: Returns objects associated with this FinancialAccount.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.treasury.outbound_payment.list(financial_account="string")
        ```
        """
        models.TreasuryOutboundPaymentListResponse.model_rebuild(
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
                        params._SerializerTreasuryOutboundPaymentListCreatedObj0, int
                    ],
                ),
                style="deepObject",
                explode=True,
            )
        if not isinstance(customer, type_utils.NotGiven):
            encode_query_param(
                _query,
                "customer",
                to_encodable(item=customer, dump_with=str),
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
            path="/v1/treasury/outbound_payments",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.TreasuryOutboundPaymentListResponse,
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
    ) -> models.TreasuryOutboundPayment:
        """
        Retrieve an OutboundPayment

        <p>Retrieves the details of an existing OutboundPayment by passing the unique OutboundPayment ID from either the OutboundPayment creation request or OutboundPayment list.</p>

        GET /v1/treasury/outbound_payments/{id}

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
        client.treasury.outbound_payment.get(id="string")
        ```
        """
        models.TreasuryOutboundPayment.model_rebuild(
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
            path=f"/v1/treasury/outbound_payments/{id}",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.TreasuryOutboundPayment,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        amount: int,
        currency: str,
        financial_account: str,
        customer: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        description: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        destination_payment_method: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        destination_payment_method_data: typing.Union[
            typing.Optional[
                params.TreasuryOutboundPaymentCreateBodyDestinationPaymentMethodData
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        destination_payment_method_options: typing.Union[
            typing.Optional[
                params.TreasuryOutboundPaymentCreateBodyDestinationPaymentMethodOptions
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        end_user_details: typing.Union[
            typing.Optional[params.TreasuryOutboundPaymentCreateBodyEndUserDetails],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        metadata: typing.Union[
            typing.Optional[params.TreasuryOutboundPaymentCreateBodyMetadata],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        statement_descriptor: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TreasuryOutboundPayment:
        """
        Create an OutboundPayment

        <p>Creates an OutboundPayment.</p>

        POST /v1/treasury/outbound_payments

        Args:
            customer: ID of the customer to whom the OutboundPayment is sent. Must match the Customer attached to the `destination_payment_method` passed in.
            description: An arbitrary string attached to the object. Often useful for displaying to users.
            destination_payment_method: The PaymentMethod to use as the payment instrument for the OutboundPayment. Exclusive with `destination_payment_method_data`.
            destination_payment_method_data: Hash used to generate the PaymentMethod to be used for this OutboundPayment. Exclusive with `destination_payment_method`.
            destination_payment_method_options: Payment method-specific configuration for this OutboundPayment.
            end_user_details: End user details.
            expand: Specifies which fields in the response should be expanded.
            metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
            statement_descriptor: The description that appears on the receiving end for this OutboundPayment (for example, bank statement for external bank transfer). Maximum 10 characters for `ach` payments, 140 characters for `us_domestic_wire` payments, or 500 characters for `stripe` network transfers. The default value is "payment".
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
        client.treasury.outbound_payment.create(
            amount=123, currency="string", financial_account="string"
        )
        ```
        """
        models.TreasuryOutboundPayment.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _data = to_form_urlencoded(
            item={
                "customer": customer,
                "description": description,
                "destination_payment_method": destination_payment_method,
                "destination_payment_method_data": destination_payment_method_data,
                "destination_payment_method_options": destination_payment_method_options,
                "end_user_details": end_user_details,
                "expand": expand,
                "metadata": metadata,
                "statement_descriptor": statement_descriptor,
                "amount": amount,
                "currency": currency,
                "financial_account": financial_account,
            },
            dump_with=params._SerializerTreasuryOutboundPaymentCreateBody,
            style={
                "amount": "form",
                "currency": "form",
                "customer": "form",
                "description": "form",
                "destination_payment_method": "form",
                "destination_payment_method_data": "deepObject",
                "destination_payment_method_options": "deepObject",
                "end_user_details": "deepObject",
                "expand": "deepObject",
                "financial_account": "form",
                "metadata": "deepObject",
                "statement_descriptor": "form",
            },
            explode={
                "amount": True,
                "currency": True,
                "customer": True,
                "description": True,
                "destination_payment_method": True,
                "destination_payment_method_data": True,
                "destination_payment_method_options": True,
                "end_user_details": True,
                "expand": True,
                "financial_account": True,
                "metadata": True,
                "statement_descriptor": True,
            },
        )
        return self._base_client.request(
            method="POST",
            path="/v1/treasury/outbound_payments",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.TreasuryOutboundPayment,
            request_options=request_options or default_request_options(),
        )

    def cancel(
        self,
        *,
        id: str,
        data: typing.Union[
            typing.Optional[params.TreasuryOutboundPaymentCancelBody],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TreasuryOutboundPayment:
        """
        Cancel an OutboundPayment

        <p>Cancel an OutboundPayment.</p>

        POST /v1/treasury/outbound_payments/{id}/cancel

        Args:
            data: TreasuryOutboundPaymentCancelBody
            id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.treasury.outbound_payment.cancel(id="string")
        ```
        """
        models.TreasuryOutboundPayment.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerTreasuryOutboundPaymentCancelBody,
                style={"expand": "deepObject"},
                explode={"expand": True},
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/treasury/outbound_payments/{id}/cancel",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.TreasuryOutboundPayment,
            request_options=request_options or default_request_options(),
        )


class AsyncOutboundPaymentClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def list(
        self,
        *,
        financial_account: str,
        created: typing.Union[
            typing.Optional[
                typing.Union[params.TreasuryOutboundPaymentListCreatedObj0, int]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        customer: typing.Union[
            typing.Optional[str], type_utils.NotGiven
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
                typing_extensions.Literal[
                    "canceled", "failed", "posted", "processing", "returned"
                ]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TreasuryOutboundPaymentListResponse:
        """
        List all OutboundPayments

        <p>Returns a list of OutboundPayments sent from the specified FinancialAccount.</p>

        GET /v1/treasury/outbound_payments

        Args:
            created: Only return OutboundPayments that were created during the given date interval.
            customer: Only return OutboundPayments sent to this customer.
            ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            expand: Specifies which fields in the response should be expanded.
            limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
            status: Only return OutboundPayments that have the given status: `processing`, `failed`, `posted`, `returned`, or `canceled`.
            financial_account: Returns objects associated with this FinancialAccount.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.treasury.outbound_payment.list(financial_account="string")
        ```
        """
        models.TreasuryOutboundPaymentListResponse.model_rebuild(
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
                        params._SerializerTreasuryOutboundPaymentListCreatedObj0, int
                    ],
                ),
                style="deepObject",
                explode=True,
            )
        if not isinstance(customer, type_utils.NotGiven):
            encode_query_param(
                _query,
                "customer",
                to_encodable(item=customer, dump_with=str),
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
            path="/v1/treasury/outbound_payments",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.TreasuryOutboundPaymentListResponse,
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
    ) -> models.TreasuryOutboundPayment:
        """
        Retrieve an OutboundPayment

        <p>Retrieves the details of an existing OutboundPayment by passing the unique OutboundPayment ID from either the OutboundPayment creation request or OutboundPayment list.</p>

        GET /v1/treasury/outbound_payments/{id}

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
        await client.treasury.outbound_payment.get(id="string")
        ```
        """
        models.TreasuryOutboundPayment.model_rebuild(
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
            path=f"/v1/treasury/outbound_payments/{id}",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.TreasuryOutboundPayment,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        amount: int,
        currency: str,
        financial_account: str,
        customer: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        description: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        destination_payment_method: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        destination_payment_method_data: typing.Union[
            typing.Optional[
                params.TreasuryOutboundPaymentCreateBodyDestinationPaymentMethodData
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        destination_payment_method_options: typing.Union[
            typing.Optional[
                params.TreasuryOutboundPaymentCreateBodyDestinationPaymentMethodOptions
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        end_user_details: typing.Union[
            typing.Optional[params.TreasuryOutboundPaymentCreateBodyEndUserDetails],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        metadata: typing.Union[
            typing.Optional[params.TreasuryOutboundPaymentCreateBodyMetadata],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        statement_descriptor: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TreasuryOutboundPayment:
        """
        Create an OutboundPayment

        <p>Creates an OutboundPayment.</p>

        POST /v1/treasury/outbound_payments

        Args:
            customer: ID of the customer to whom the OutboundPayment is sent. Must match the Customer attached to the `destination_payment_method` passed in.
            description: An arbitrary string attached to the object. Often useful for displaying to users.
            destination_payment_method: The PaymentMethod to use as the payment instrument for the OutboundPayment. Exclusive with `destination_payment_method_data`.
            destination_payment_method_data: Hash used to generate the PaymentMethod to be used for this OutboundPayment. Exclusive with `destination_payment_method`.
            destination_payment_method_options: Payment method-specific configuration for this OutboundPayment.
            end_user_details: End user details.
            expand: Specifies which fields in the response should be expanded.
            metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
            statement_descriptor: The description that appears on the receiving end for this OutboundPayment (for example, bank statement for external bank transfer). Maximum 10 characters for `ach` payments, 140 characters for `us_domestic_wire` payments, or 500 characters for `stripe` network transfers. The default value is "payment".
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
        await client.treasury.outbound_payment.create(
            amount=123, currency="string", financial_account="string"
        )
        ```
        """
        models.TreasuryOutboundPayment.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _data = to_form_urlencoded(
            item={
                "customer": customer,
                "description": description,
                "destination_payment_method": destination_payment_method,
                "destination_payment_method_data": destination_payment_method_data,
                "destination_payment_method_options": destination_payment_method_options,
                "end_user_details": end_user_details,
                "expand": expand,
                "metadata": metadata,
                "statement_descriptor": statement_descriptor,
                "amount": amount,
                "currency": currency,
                "financial_account": financial_account,
            },
            dump_with=params._SerializerTreasuryOutboundPaymentCreateBody,
            style={
                "amount": "form",
                "currency": "form",
                "customer": "form",
                "description": "form",
                "destination_payment_method": "form",
                "destination_payment_method_data": "deepObject",
                "destination_payment_method_options": "deepObject",
                "end_user_details": "deepObject",
                "expand": "deepObject",
                "financial_account": "form",
                "metadata": "deepObject",
                "statement_descriptor": "form",
            },
            explode={
                "amount": True,
                "currency": True,
                "customer": True,
                "description": True,
                "destination_payment_method": True,
                "destination_payment_method_data": True,
                "destination_payment_method_options": True,
                "end_user_details": True,
                "expand": True,
                "financial_account": True,
                "metadata": True,
                "statement_descriptor": True,
            },
        )
        return await self._base_client.request(
            method="POST",
            path="/v1/treasury/outbound_payments",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.TreasuryOutboundPayment,
            request_options=request_options or default_request_options(),
        )

    async def cancel(
        self,
        *,
        id: str,
        data: typing.Union[
            typing.Optional[params.TreasuryOutboundPaymentCancelBody],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TreasuryOutboundPayment:
        """
        Cancel an OutboundPayment

        <p>Cancel an OutboundPayment.</p>

        POST /v1/treasury/outbound_payments/{id}/cancel

        Args:
            data: TreasuryOutboundPaymentCancelBody
            id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.treasury.outbound_payment.cancel(id="string")
        ```
        """
        models.TreasuryOutboundPayment.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerTreasuryOutboundPaymentCancelBody,
                style={"expand": "deepObject"},
                explode={"expand": True},
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/treasury/outbound_payments/{id}/cancel",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.TreasuryOutboundPayment,
            request_options=request_options or default_request_options(),
        )
