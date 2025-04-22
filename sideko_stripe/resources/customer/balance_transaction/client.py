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


class BalanceTransactionClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def list(
        self,
        *,
        customer: str,
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
    ) -> models.CustomerBalanceTransactionListResponse:
        """
        List customer balance transactions

        <p>Returns a list of transactions that updated the customer’s <a href="/docs/billing/customer/balance">balances</a>.</p>

        GET /v1/customers/{customer}/balance_transactions

        Args:
            ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            expand: Specifies which fields in the response should be expanded.
            limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
            customer: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.customer.balance_transaction.list(customer="string")
        ```
        """
        models.CustomerBalanceTransactionListResponse.model_rebuild(
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
            path=f"/v1/customers/{customer}/balance_transactions",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.CustomerBalanceTransactionListResponse,
            request_options=request_options or default_request_options(),
        )

    def get(
        self,
        *,
        customer: str,
        transaction: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.CustomerBalanceTransaction:
        """
        Retrieve a customer balance transaction

        <p>Retrieves a specific customer balance transaction that updated the customer’s <a href="/docs/billing/customer/balance">balances</a>.</p>

        GET /v1/customers/{customer}/balance_transactions/{transaction}

        Args:
            expand: Specifies which fields in the response should be expanded.
            customer: str
            transaction: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.customer.balance_transaction.get(customer="string", transaction="string")
        ```
        """
        models.CustomerBalanceTransaction.model_rebuild(
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
            path=f"/v1/customers/{customer}/balance_transactions/{transaction}",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.CustomerBalanceTransaction,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        amount: int,
        currency: str,
        customer: str,
        description: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        metadata: typing.Union[
            typing.Optional[
                typing.Union[
                    params.CustomerBalanceTransactionCreateBodyMetadataObj0, str
                ]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.CustomerBalanceTransaction:
        """
        Create a customer balance transaction

        <p>Creates an immutable transaction that updates the customer’s credit <a href="/docs/billing/customer/balance">balance</a>.</p>

        POST /v1/customers/{customer}/balance_transactions

        Args:
            description: An arbitrary string attached to the object. Often useful for displaying to users.
            expand: Specifies which fields in the response should be expanded.
            metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
            amount: The integer amount in **cents (or local equivalent)** to apply to the customer's credit balance.
            currency: Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies). Specifies the [`invoice_credit_balance`](https://stripe.com/docs/api/customers/object#customer_object-invoice_credit_balance) that this transaction will apply to. If the customer's `currency` is not set, it will be updated to this value.
            customer: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.customer.balance_transaction.create(
            amount=123, currency="string", customer="string"
        )
        ```
        """
        models.CustomerBalanceTransaction.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _data = to_form_urlencoded(
            item={
                "description": description,
                "expand": expand,
                "metadata": metadata,
                "amount": amount,
                "currency": currency,
            },
            dump_with=params._SerializerCustomerBalanceTransactionCreateBody,
            style={
                "amount": "form",
                "currency": "form",
                "description": "form",
                "expand": "deepObject",
                "metadata": "deepObject",
            },
            explode={
                "amount": True,
                "currency": True,
                "description": True,
                "expand": True,
                "metadata": True,
            },
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/customers/{customer}/balance_transactions",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.CustomerBalanceTransaction,
            request_options=request_options or default_request_options(),
        )

    def update(
        self,
        *,
        customer: str,
        transaction: str,
        data: typing.Union[
            typing.Optional[params.CustomerBalanceTransactionUpdateBody],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.CustomerBalanceTransaction:
        """
        Update a customer credit balance transaction

        <p>Most credit balance transaction fields are immutable, but you may update its <code>description</code> and <code>metadata</code>.</p>

        POST /v1/customers/{customer}/balance_transactions/{transaction}

        Args:
            data: CustomerBalanceTransactionUpdateBody
            customer: str
            transaction: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.customer.balance_transaction.update(
            customer="string", transaction="string"
        )
        ```
        """
        models.CustomerBalanceTransaction.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerCustomerBalanceTransactionUpdateBody,
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
            path=f"/v1/customers/{customer}/balance_transactions/{transaction}",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.CustomerBalanceTransaction,
            request_options=request_options or default_request_options(),
        )


class AsyncBalanceTransactionClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def list(
        self,
        *,
        customer: str,
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
    ) -> models.CustomerBalanceTransactionListResponse:
        """
        List customer balance transactions

        <p>Returns a list of transactions that updated the customer’s <a href="/docs/billing/customer/balance">balances</a>.</p>

        GET /v1/customers/{customer}/balance_transactions

        Args:
            ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            expand: Specifies which fields in the response should be expanded.
            limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
            customer: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.customer.balance_transaction.list(customer="string")
        ```
        """
        models.CustomerBalanceTransactionListResponse.model_rebuild(
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
            path=f"/v1/customers/{customer}/balance_transactions",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.CustomerBalanceTransactionListResponse,
            request_options=request_options or default_request_options(),
        )

    async def get(
        self,
        *,
        customer: str,
        transaction: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.CustomerBalanceTransaction:
        """
        Retrieve a customer balance transaction

        <p>Retrieves a specific customer balance transaction that updated the customer’s <a href="/docs/billing/customer/balance">balances</a>.</p>

        GET /v1/customers/{customer}/balance_transactions/{transaction}

        Args:
            expand: Specifies which fields in the response should be expanded.
            customer: str
            transaction: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.customer.balance_transaction.get(
            customer="string", transaction="string"
        )
        ```
        """
        models.CustomerBalanceTransaction.model_rebuild(
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
            path=f"/v1/customers/{customer}/balance_transactions/{transaction}",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.CustomerBalanceTransaction,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        amount: int,
        currency: str,
        customer: str,
        description: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        metadata: typing.Union[
            typing.Optional[
                typing.Union[
                    params.CustomerBalanceTransactionCreateBodyMetadataObj0, str
                ]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.CustomerBalanceTransaction:
        """
        Create a customer balance transaction

        <p>Creates an immutable transaction that updates the customer’s credit <a href="/docs/billing/customer/balance">balance</a>.</p>

        POST /v1/customers/{customer}/balance_transactions

        Args:
            description: An arbitrary string attached to the object. Often useful for displaying to users.
            expand: Specifies which fields in the response should be expanded.
            metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
            amount: The integer amount in **cents (or local equivalent)** to apply to the customer's credit balance.
            currency: Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies). Specifies the [`invoice_credit_balance`](https://stripe.com/docs/api/customers/object#customer_object-invoice_credit_balance) that this transaction will apply to. If the customer's `currency` is not set, it will be updated to this value.
            customer: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.customer.balance_transaction.create(
            amount=123, currency="string", customer="string"
        )
        ```
        """
        models.CustomerBalanceTransaction.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _data = to_form_urlencoded(
            item={
                "description": description,
                "expand": expand,
                "metadata": metadata,
                "amount": amount,
                "currency": currency,
            },
            dump_with=params._SerializerCustomerBalanceTransactionCreateBody,
            style={
                "amount": "form",
                "currency": "form",
                "description": "form",
                "expand": "deepObject",
                "metadata": "deepObject",
            },
            explode={
                "amount": True,
                "currency": True,
                "description": True,
                "expand": True,
                "metadata": True,
            },
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/customers/{customer}/balance_transactions",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.CustomerBalanceTransaction,
            request_options=request_options or default_request_options(),
        )

    async def update(
        self,
        *,
        customer: str,
        transaction: str,
        data: typing.Union[
            typing.Optional[params.CustomerBalanceTransactionUpdateBody],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.CustomerBalanceTransaction:
        """
        Update a customer credit balance transaction

        <p>Most credit balance transaction fields are immutable, but you may update its <code>description</code> and <code>metadata</code>.</p>

        POST /v1/customers/{customer}/balance_transactions/{transaction}

        Args:
            data: CustomerBalanceTransactionUpdateBody
            customer: str
            transaction: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.customer.balance_transaction.update(
            customer="string", transaction="string"
        )
        ```
        """
        models.CustomerBalanceTransaction.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerCustomerBalanceTransactionUpdateBody,
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
            path=f"/v1/customers/{customer}/balance_transactions/{transaction}",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.CustomerBalanceTransaction,
            request_options=request_options or default_request_options(),
        )
