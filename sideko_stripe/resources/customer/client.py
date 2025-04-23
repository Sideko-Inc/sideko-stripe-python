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
from sideko_stripe.resources.customer.balance_transaction import (
    AsyncBalanceTransactionClient,
    BalanceTransactionClient,
)
from sideko_stripe.resources.customer.bank_account import (
    AsyncBankAccountClient,
    BankAccountClient,
)
from sideko_stripe.resources.customer.card import AsyncCardClient, CardClient
from sideko_stripe.resources.customer.cash_balance import (
    AsyncCashBalanceClient,
    CashBalanceClient,
)
from sideko_stripe.resources.customer.cash_balance_transaction import (
    AsyncCashBalanceTransactionClient,
    CashBalanceTransactionClient,
)
from sideko_stripe.resources.customer.discount import (
    AsyncDiscountClient,
    DiscountClient,
)
from sideko_stripe.resources.customer.funding_instruction import (
    AsyncFundingInstructionClient,
    FundingInstructionClient,
)
from sideko_stripe.resources.customer.payment_method import (
    AsyncPaymentMethodClient,
    PaymentMethodClient,
)
from sideko_stripe.resources.customer.source import AsyncSourceClient, SourceClient
from sideko_stripe.resources.customer.subscription import (
    AsyncSubscriptionClient,
    SubscriptionClient,
)
from sideko_stripe.resources.customer.tax_id import AsyncTaxIdClient, TaxIdClient
from sideko_stripe.types import models, params


class CustomerClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        self.bank_account = BankAccountClient(base_client=self._base_client)
        self.card = CardClient(base_client=self._base_client)
        self.discount = DiscountClient(base_client=self._base_client)
        self.source = SourceClient(base_client=self._base_client)
        self.subscription = SubscriptionClient(base_client=self._base_client)
        self.tax_id = TaxIdClient(base_client=self._base_client)
        self.balance_transaction = BalanceTransactionClient(
            base_client=self._base_client
        )
        self.cash_balance = CashBalanceClient(base_client=self._base_client)
        self.cash_balance_transaction = CashBalanceTransactionClient(
            base_client=self._base_client
        )
        self.payment_method = PaymentMethodClient(base_client=self._base_client)
        self.funding_instruction = FundingInstructionClient(
            base_client=self._base_client
        )

    def delete(
        self, *, customer: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.DeletedCustomer:
        """
        Delete a customer

        <p>Permanently deletes a customer. It cannot be undone. Also immediately cancels any active subscriptions on the customer.</p>

        DELETE /v1/customers/{customer}

        Args:
            customer: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.customer.delete(customer="string")
        ```
        """
        return self._base_client.request(
            method="DELETE",
            path=f"/v1/customers/{customer}",
            auth_names=["bearerAuth"],
            cast_to=models.DeletedCustomer,
            request_options=request_options or default_request_options(),
        )

    def list(
        self,
        *,
        created: typing.Union[
            typing.Optional[typing.Union[params.CustomerListCreatedObj0, int]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        email: typing.Union[
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
        test_clock: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.CustomerListResponse:
        """
        List all customers

        <p>Returns a list of your customers. The customers are returned sorted by creation date, with the most recent customers appearing first.</p>

        GET /v1/customers

        Args:
            created: Only return customers that were created during the given date interval.
            email: A case-sensitive filter on the list based on the customer's `email` field. The value must be a string.
            ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            expand: Specifies which fields in the response should be expanded.
            limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
            test_clock: Provides a list of customers that are associated with the specified test clock. The response will not include customers with test clocks if this parameter is not set.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.customer.list()
        ```
        """
        models.CustomerListResponse.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _query: QueryParams = {}
        if not isinstance(created, type_utils.NotGiven):
            encode_query_param(
                _query,
                "created",
                to_encodable(
                    item=created,
                    dump_with=typing.Union[
                        params._SerializerCustomerListCreatedObj0, int
                    ],
                ),
                style="deepObject",
                explode=True,
            )
        if not isinstance(email, type_utils.NotGiven):
            encode_query_param(
                _query,
                "email",
                to_encodable(item=email, dump_with=str),
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
        if not isinstance(test_clock, type_utils.NotGiven):
            encode_query_param(
                _query,
                "test_clock",
                to_encodable(item=test_clock, dump_with=str),
                style="form",
                explode=True,
            )
        return self._base_client.request(
            method="GET",
            path="/v1/customers",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.CustomerListResponse,
            request_options=request_options or default_request_options(),
        )

    def search(
        self,
        *,
        query: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        limit: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        page: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.CustomerSearchResponse:
        """
        Search customers

        <p>Search for customers you’ve previously created using Stripe’s <a href="/docs/search#search-query-language">Search Query Language</a>.
        Don’t use search in read-after-write flows where strict consistency is necessary. Under normal operating
        conditions, data is searchable in less than a minute. Occasionally, propagation of new or updated data can be up
        to an hour behind during outages. Search functionality is not available to merchants in India.</p>

        GET /v1/customers/search

        Args:
            expand: Specifies which fields in the response should be expanded.
            limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            page: A cursor for pagination across multiple pages of results. Don't include this parameter on the first call. Use the next_page value returned in a previous response to request subsequent results.
            query: The search query string. See [search query language](https://stripe.com/docs/search#search-query-language) and the list of supported [query fields for customers](https://stripe.com/docs/search#query-fields-for-customers).
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.customer.search(query="string")
        ```
        """
        models.CustomerSearchResponse.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _query: QueryParams = {}
        encode_query_param(
            _query,
            "query",
            to_encodable(item=query, dump_with=str),
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
        if not isinstance(page, type_utils.NotGiven):
            encode_query_param(
                _query,
                "page",
                to_encodable(item=page, dump_with=str),
                style="form",
                explode=True,
            )
        return self._base_client.request(
            method="GET",
            path="/v1/customers/search",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.CustomerSearchResponse,
            request_options=request_options or default_request_options(),
        )

    def get(
        self,
        *,
        customer: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Union[models.Customer, models.DeletedCustomer]:
        """
        Retrieve a customer

        <p>Retrieves a Customer object.</p>

        GET /v1/customers/{customer}

        Args:
            expand: Specifies which fields in the response should be expanded.
            customer: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.customer.get(customer="string")
        ```
        """
        models.Customer.model_rebuild(_types_namespace=models._types_namespace)
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
            path=f"/v1/customers/{customer}",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=typing.Union[models.Customer, models.DeletedCustomer],
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        data: typing.Union[
            typing.Optional[params.CustomerCreateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Customer:
        """
        Create a customer

        <p>Creates a new customer object.</p>

        POST /v1/customers

        Args:
            data: CustomerCreateBody
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.customer.create()
        ```
        """
        models.Customer.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerCustomerCreateBody,
                style={
                    "address": "deepObject",
                    "balance": "form",
                    "cash_balance": "deepObject",
                    "description": "form",
                    "email": "form",
                    "expand": "deepObject",
                    "invoice_prefix": "form",
                    "invoice_settings": "deepObject",
                    "metadata": "deepObject",
                    "name": "form",
                    "next_invoice_sequence": "form",
                    "payment_method": "form",
                    "phone": "form",
                    "preferred_locales": "deepObject",
                    "shipping": "deepObject",
                    "source": "form",
                    "tax": "deepObject",
                    "tax_exempt": "form",
                    "tax_id_data": "deepObject",
                    "test_clock": "form",
                },
                explode={
                    "address": True,
                    "balance": True,
                    "cash_balance": True,
                    "description": True,
                    "email": True,
                    "expand": True,
                    "invoice_prefix": True,
                    "invoice_settings": True,
                    "metadata": True,
                    "name": True,
                    "next_invoice_sequence": True,
                    "payment_method": True,
                    "phone": True,
                    "preferred_locales": True,
                    "shipping": True,
                    "source": True,
                    "tax": True,
                    "tax_exempt": True,
                    "tax_id_data": True,
                    "test_clock": True,
                },
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path="/v1/customers",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.Customer,
            request_options=request_options or default_request_options(),
        )

    def update(
        self,
        *,
        customer: str,
        data: typing.Union[
            typing.Optional[params.CustomerUpdateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Customer:
        """
        Update a customer

        <p>Updates the specified customer by setting the values of the parameters passed. Any parameters not provided will be left unchanged. For example, if you pass the <strong>source</strong> parameter, that becomes the customer’s active source (e.g., a card) to be used for all charges in the future. When you update a customer to a new valid card source by passing the <strong>source</strong> parameter: for each of the customer’s current subscriptions, if the subscription bills automatically and is in the <code>past_due</code> state, then the latest open invoice for the subscription with automatic collection enabled will be retried. This retry will not count as an automatic retry, and will not affect the next regularly scheduled payment for the invoice. Changing the <strong>default_source</strong> for a customer will not trigger this behavior.</p>

        <p>This request accepts mostly the same arguments as the customer creation call.</p>

        POST /v1/customers/{customer}

        Args:
            data: CustomerUpdateBody
            customer: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.customer.update(customer="string")
        ```
        """
        models.Customer.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerCustomerUpdateBody,
                style={
                    "address": "deepObject",
                    "balance": "form",
                    "bank_account": "deepObject",
                    "card": "deepObject",
                    "cash_balance": "deepObject",
                    "default_alipay_account": "form",
                    "default_bank_account": "form",
                    "default_card": "form",
                    "default_source": "form",
                    "description": "form",
                    "email": "form",
                    "expand": "deepObject",
                    "invoice_prefix": "form",
                    "invoice_settings": "deepObject",
                    "metadata": "deepObject",
                    "name": "form",
                    "next_invoice_sequence": "form",
                    "phone": "form",
                    "preferred_locales": "deepObject",
                    "shipping": "deepObject",
                    "source": "form",
                    "tax": "deepObject",
                    "tax_exempt": "form",
                },
                explode={
                    "address": True,
                    "balance": True,
                    "bank_account": True,
                    "card": True,
                    "cash_balance": True,
                    "default_alipay_account": True,
                    "default_bank_account": True,
                    "default_card": True,
                    "default_source": True,
                    "description": True,
                    "email": True,
                    "expand": True,
                    "invoice_prefix": True,
                    "invoice_settings": True,
                    "metadata": True,
                    "name": True,
                    "next_invoice_sequence": True,
                    "phone": True,
                    "preferred_locales": True,
                    "shipping": True,
                    "source": True,
                    "tax": True,
                    "tax_exempt": True,
                },
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/customers/{customer}",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.Customer,
            request_options=request_options or default_request_options(),
        )


class AsyncCustomerClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        self.bank_account = AsyncBankAccountClient(base_client=self._base_client)
        self.card = AsyncCardClient(base_client=self._base_client)
        self.discount = AsyncDiscountClient(base_client=self._base_client)
        self.source = AsyncSourceClient(base_client=self._base_client)
        self.subscription = AsyncSubscriptionClient(base_client=self._base_client)
        self.tax_id = AsyncTaxIdClient(base_client=self._base_client)
        self.balance_transaction = AsyncBalanceTransactionClient(
            base_client=self._base_client
        )
        self.cash_balance = AsyncCashBalanceClient(base_client=self._base_client)
        self.cash_balance_transaction = AsyncCashBalanceTransactionClient(
            base_client=self._base_client
        )
        self.payment_method = AsyncPaymentMethodClient(base_client=self._base_client)
        self.funding_instruction = AsyncFundingInstructionClient(
            base_client=self._base_client
        )

    async def delete(
        self, *, customer: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.DeletedCustomer:
        """
        Delete a customer

        <p>Permanently deletes a customer. It cannot be undone. Also immediately cancels any active subscriptions on the customer.</p>

        DELETE /v1/customers/{customer}

        Args:
            customer: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.customer.delete(customer="string")
        ```
        """
        return await self._base_client.request(
            method="DELETE",
            path=f"/v1/customers/{customer}",
            auth_names=["bearerAuth"],
            cast_to=models.DeletedCustomer,
            request_options=request_options or default_request_options(),
        )

    async def list(
        self,
        *,
        created: typing.Union[
            typing.Optional[typing.Union[params.CustomerListCreatedObj0, int]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        email: typing.Union[
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
        test_clock: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.CustomerListResponse:
        """
        List all customers

        <p>Returns a list of your customers. The customers are returned sorted by creation date, with the most recent customers appearing first.</p>

        GET /v1/customers

        Args:
            created: Only return customers that were created during the given date interval.
            email: A case-sensitive filter on the list based on the customer's `email` field. The value must be a string.
            ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            expand: Specifies which fields in the response should be expanded.
            limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
            test_clock: Provides a list of customers that are associated with the specified test clock. The response will not include customers with test clocks if this parameter is not set.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.customer.list()
        ```
        """
        models.CustomerListResponse.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _query: QueryParams = {}
        if not isinstance(created, type_utils.NotGiven):
            encode_query_param(
                _query,
                "created",
                to_encodable(
                    item=created,
                    dump_with=typing.Union[
                        params._SerializerCustomerListCreatedObj0, int
                    ],
                ),
                style="deepObject",
                explode=True,
            )
        if not isinstance(email, type_utils.NotGiven):
            encode_query_param(
                _query,
                "email",
                to_encodable(item=email, dump_with=str),
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
        if not isinstance(test_clock, type_utils.NotGiven):
            encode_query_param(
                _query,
                "test_clock",
                to_encodable(item=test_clock, dump_with=str),
                style="form",
                explode=True,
            )
        return await self._base_client.request(
            method="GET",
            path="/v1/customers",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.CustomerListResponse,
            request_options=request_options or default_request_options(),
        )

    async def search(
        self,
        *,
        query: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        limit: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        page: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.CustomerSearchResponse:
        """
        Search customers

        <p>Search for customers you’ve previously created using Stripe’s <a href="/docs/search#search-query-language">Search Query Language</a>.
        Don’t use search in read-after-write flows where strict consistency is necessary. Under normal operating
        conditions, data is searchable in less than a minute. Occasionally, propagation of new or updated data can be up
        to an hour behind during outages. Search functionality is not available to merchants in India.</p>

        GET /v1/customers/search

        Args:
            expand: Specifies which fields in the response should be expanded.
            limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            page: A cursor for pagination across multiple pages of results. Don't include this parameter on the first call. Use the next_page value returned in a previous response to request subsequent results.
            query: The search query string. See [search query language](https://stripe.com/docs/search#search-query-language) and the list of supported [query fields for customers](https://stripe.com/docs/search#query-fields-for-customers).
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.customer.search(query="string")
        ```
        """
        models.CustomerSearchResponse.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _query: QueryParams = {}
        encode_query_param(
            _query,
            "query",
            to_encodable(item=query, dump_with=str),
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
        if not isinstance(page, type_utils.NotGiven):
            encode_query_param(
                _query,
                "page",
                to_encodable(item=page, dump_with=str),
                style="form",
                explode=True,
            )
        return await self._base_client.request(
            method="GET",
            path="/v1/customers/search",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.CustomerSearchResponse,
            request_options=request_options or default_request_options(),
        )

    async def get(
        self,
        *,
        customer: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Union[models.Customer, models.DeletedCustomer]:
        """
        Retrieve a customer

        <p>Retrieves a Customer object.</p>

        GET /v1/customers/{customer}

        Args:
            expand: Specifies which fields in the response should be expanded.
            customer: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.customer.get(customer="string")
        ```
        """
        models.Customer.model_rebuild(_types_namespace=models._types_namespace)
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
            path=f"/v1/customers/{customer}",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=typing.Union[models.Customer, models.DeletedCustomer],
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        data: typing.Union[
            typing.Optional[params.CustomerCreateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Customer:
        """
        Create a customer

        <p>Creates a new customer object.</p>

        POST /v1/customers

        Args:
            data: CustomerCreateBody
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.customer.create()
        ```
        """
        models.Customer.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerCustomerCreateBody,
                style={
                    "address": "deepObject",
                    "balance": "form",
                    "cash_balance": "deepObject",
                    "description": "form",
                    "email": "form",
                    "expand": "deepObject",
                    "invoice_prefix": "form",
                    "invoice_settings": "deepObject",
                    "metadata": "deepObject",
                    "name": "form",
                    "next_invoice_sequence": "form",
                    "payment_method": "form",
                    "phone": "form",
                    "preferred_locales": "deepObject",
                    "shipping": "deepObject",
                    "source": "form",
                    "tax": "deepObject",
                    "tax_exempt": "form",
                    "tax_id_data": "deepObject",
                    "test_clock": "form",
                },
                explode={
                    "address": True,
                    "balance": True,
                    "cash_balance": True,
                    "description": True,
                    "email": True,
                    "expand": True,
                    "invoice_prefix": True,
                    "invoice_settings": True,
                    "metadata": True,
                    "name": True,
                    "next_invoice_sequence": True,
                    "payment_method": True,
                    "phone": True,
                    "preferred_locales": True,
                    "shipping": True,
                    "source": True,
                    "tax": True,
                    "tax_exempt": True,
                    "tax_id_data": True,
                    "test_clock": True,
                },
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path="/v1/customers",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.Customer,
            request_options=request_options or default_request_options(),
        )

    async def update(
        self,
        *,
        customer: str,
        data: typing.Union[
            typing.Optional[params.CustomerUpdateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Customer:
        """
        Update a customer

        <p>Updates the specified customer by setting the values of the parameters passed. Any parameters not provided will be left unchanged. For example, if you pass the <strong>source</strong> parameter, that becomes the customer’s active source (e.g., a card) to be used for all charges in the future. When you update a customer to a new valid card source by passing the <strong>source</strong> parameter: for each of the customer’s current subscriptions, if the subscription bills automatically and is in the <code>past_due</code> state, then the latest open invoice for the subscription with automatic collection enabled will be retried. This retry will not count as an automatic retry, and will not affect the next regularly scheduled payment for the invoice. Changing the <strong>default_source</strong> for a customer will not trigger this behavior.</p>

        <p>This request accepts mostly the same arguments as the customer creation call.</p>

        POST /v1/customers/{customer}

        Args:
            data: CustomerUpdateBody
            customer: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.customer.update(customer="string")
        ```
        """
        models.Customer.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerCustomerUpdateBody,
                style={
                    "address": "deepObject",
                    "balance": "form",
                    "bank_account": "deepObject",
                    "card": "deepObject",
                    "cash_balance": "deepObject",
                    "default_alipay_account": "form",
                    "default_bank_account": "form",
                    "default_card": "form",
                    "default_source": "form",
                    "description": "form",
                    "email": "form",
                    "expand": "deepObject",
                    "invoice_prefix": "form",
                    "invoice_settings": "deepObject",
                    "metadata": "deepObject",
                    "name": "form",
                    "next_invoice_sequence": "form",
                    "phone": "form",
                    "preferred_locales": "deepObject",
                    "shipping": "deepObject",
                    "source": "form",
                    "tax": "deepObject",
                    "tax_exempt": "form",
                },
                explode={
                    "address": True,
                    "balance": True,
                    "bank_account": True,
                    "card": True,
                    "cash_balance": True,
                    "default_alipay_account": True,
                    "default_bank_account": True,
                    "default_card": True,
                    "default_source": True,
                    "description": True,
                    "email": True,
                    "expand": True,
                    "invoice_prefix": True,
                    "invoice_settings": True,
                    "metadata": True,
                    "name": True,
                    "next_invoice_sequence": True,
                    "phone": True,
                    "preferred_locales": True,
                    "shipping": True,
                    "source": True,
                    "tax": True,
                    "tax_exempt": True,
                },
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/customers/{customer}",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.Customer,
            request_options=request_options or default_request_options(),
        )
