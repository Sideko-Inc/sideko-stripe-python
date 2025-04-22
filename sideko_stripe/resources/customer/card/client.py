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


class CardClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def delete(
        self,
        *,
        customer: str,
        id: str,
        data: typing.Union[
            typing.Optional[params.CustomerCardDeleteBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Union[
        typing.Union[models.Account, models.BankAccount, models.Card, models.Source],
        typing.Union[models.DeletedBankAccount, models.DeletedCard],
    ]:
        """
        Delete a customer source

        <p>Delete a specified source for a given customer.</p>

        DELETE /v1/customers/{customer}/cards/{id}

        Args:
            data: CustomerCardDeleteBody
            customer: str
            id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.customer.card.delete(customer="string", id="string")
        ```
        """
        models.Account.model_rebuild(_types_namespace=models._types_namespace)
        models.BankAccount.model_rebuild(_types_namespace=models._types_namespace)
        models.Card.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerCustomerCardDeleteBody,
                style={"expand": "deepObject"},
                explode={"expand": True},
            )
            if data
            else None
        )
        return self._base_client.request(
            method="DELETE",
            path=f"/v1/customers/{customer}/cards/{id}",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=typing.Union[
                typing.Union[
                    models.Account, models.BankAccount, models.Card, models.Source
                ],
                typing.Union[models.DeletedBankAccount, models.DeletedCard],
            ],
            request_options=request_options or default_request_options(),
        )

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
    ) -> models.CustomerCardListResponse:
        """
        List all cards

        <p>You can see a list of the cards belonging to a customer.
        Note that the 10 most recent sources are always available on the <code>Customer</code> object.
        If you need more than those 10, you can use this API method and the <code>limit</code> and <code>starting_after</code> parameters to page through additional cards.</p>

        GET /v1/customers/{customer}/cards

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
        client.customer.card.list(customer="string")
        ```
        """
        models.CustomerCardListResponse.model_rebuild(
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
            path=f"/v1/customers/{customer}/cards",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.CustomerCardListResponse,
            request_options=request_options or default_request_options(),
        )

    def get(
        self,
        *,
        customer: str,
        id: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Card:
        """
        Retrieve a card

        <p>You can always see the 10 most recent cards directly on a customer; this method lets you retrieve details about a specific card stored on the customer.</p>

        GET /v1/customers/{customer}/cards/{id}

        Args:
            expand: Specifies which fields in the response should be expanded.
            customer: str
            id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.customer.card.get(customer="string", id="string")
        ```
        """
        models.Card.model_rebuild(_types_namespace=models._types_namespace)
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
            path=f"/v1/customers/{customer}/cards/{id}",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.Card,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        customer: str,
        data: typing.Union[
            typing.Optional[params.CustomerCardCreateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Union[models.Account, models.BankAccount, models.Card, models.Source]:
        """
        Create a card

        <p>When you create a new credit card, you must specify a customer or recipient on which to create it.</p>

        <p>If the card’s owner has no default card, then the new card will become the default.
        However, if the owner already has a default, then it will not change.
        To change the default, you should <a href="/docs/api#update_customer">update the customer</a> to have a new <code>default_source</code>.</p>

        POST /v1/customers/{customer}/cards

        Args:
            data: CustomerCardCreateBody
            customer: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.customer.card.create(customer="string")
        ```
        """
        models.Account.model_rebuild(_types_namespace=models._types_namespace)
        models.BankAccount.model_rebuild(_types_namespace=models._types_namespace)
        models.Card.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerCustomerCardCreateBody,
                style={
                    "alipay_account": "form",
                    "bank_account": "deepObject",
                    "card": "deepObject",
                    "expand": "deepObject",
                    "metadata": "deepObject",
                    "source": "form",
                },
                explode={
                    "alipay_account": True,
                    "bank_account": True,
                    "card": True,
                    "expand": True,
                    "metadata": True,
                    "source": True,
                },
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/customers/{customer}/cards",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=typing.Union[
                models.Account, models.BankAccount, models.Card, models.Source
            ],
            request_options=request_options or default_request_options(),
        )

    def update(
        self,
        *,
        customer: str,
        id: str,
        data: typing.Union[
            typing.Optional[params.CustomerCardUpdateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Union[models.Card, models.BankAccount, models.Source]:
        """
        <p>Update a specified source for a given customer.</p>

        POST /v1/customers/{customer}/cards/{id}

        Args:
            data: CustomerCardUpdateBody
            customer: str
            id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.customer.card.update(customer="string", id="string")
        ```
        """
        models.BankAccount.model_rebuild(_types_namespace=models._types_namespace)
        models.Card.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerCustomerCardUpdateBody,
                style={
                    "account_holder_name": "form",
                    "account_holder_type": "form",
                    "address_city": "form",
                    "address_country": "form",
                    "address_line1": "form",
                    "address_line2": "form",
                    "address_state": "form",
                    "address_zip": "form",
                    "exp_month": "form",
                    "exp_year": "form",
                    "expand": "deepObject",
                    "metadata": "deepObject",
                    "name": "form",
                    "owner": "deepObject",
                },
                explode={
                    "account_holder_name": True,
                    "account_holder_type": True,
                    "address_city": True,
                    "address_country": True,
                    "address_line1": True,
                    "address_line2": True,
                    "address_state": True,
                    "address_zip": True,
                    "exp_month": True,
                    "exp_year": True,
                    "expand": True,
                    "metadata": True,
                    "name": True,
                    "owner": True,
                },
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/customers/{customer}/cards/{id}",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=typing.Union[models.Card, models.BankAccount, models.Source],
            request_options=request_options or default_request_options(),
        )


class AsyncCardClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def delete(
        self,
        *,
        customer: str,
        id: str,
        data: typing.Union[
            typing.Optional[params.CustomerCardDeleteBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Union[
        typing.Union[models.Account, models.BankAccount, models.Card, models.Source],
        typing.Union[models.DeletedBankAccount, models.DeletedCard],
    ]:
        """
        Delete a customer source

        <p>Delete a specified source for a given customer.</p>

        DELETE /v1/customers/{customer}/cards/{id}

        Args:
            data: CustomerCardDeleteBody
            customer: str
            id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.customer.card.delete(customer="string", id="string")
        ```
        """
        models.Account.model_rebuild(_types_namespace=models._types_namespace)
        models.BankAccount.model_rebuild(_types_namespace=models._types_namespace)
        models.Card.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerCustomerCardDeleteBody,
                style={"expand": "deepObject"},
                explode={"expand": True},
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="DELETE",
            path=f"/v1/customers/{customer}/cards/{id}",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=typing.Union[
                typing.Union[
                    models.Account, models.BankAccount, models.Card, models.Source
                ],
                typing.Union[models.DeletedBankAccount, models.DeletedCard],
            ],
            request_options=request_options or default_request_options(),
        )

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
    ) -> models.CustomerCardListResponse:
        """
        List all cards

        <p>You can see a list of the cards belonging to a customer.
        Note that the 10 most recent sources are always available on the <code>Customer</code> object.
        If you need more than those 10, you can use this API method and the <code>limit</code> and <code>starting_after</code> parameters to page through additional cards.</p>

        GET /v1/customers/{customer}/cards

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
        await client.customer.card.list(customer="string")
        ```
        """
        models.CustomerCardListResponse.model_rebuild(
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
            path=f"/v1/customers/{customer}/cards",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.CustomerCardListResponse,
            request_options=request_options or default_request_options(),
        )

    async def get(
        self,
        *,
        customer: str,
        id: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Card:
        """
        Retrieve a card

        <p>You can always see the 10 most recent cards directly on a customer; this method lets you retrieve details about a specific card stored on the customer.</p>

        GET /v1/customers/{customer}/cards/{id}

        Args:
            expand: Specifies which fields in the response should be expanded.
            customer: str
            id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.customer.card.get(customer="string", id="string")
        ```
        """
        models.Card.model_rebuild(_types_namespace=models._types_namespace)
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
            path=f"/v1/customers/{customer}/cards/{id}",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.Card,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        customer: str,
        data: typing.Union[
            typing.Optional[params.CustomerCardCreateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Union[models.Account, models.BankAccount, models.Card, models.Source]:
        """
        Create a card

        <p>When you create a new credit card, you must specify a customer or recipient on which to create it.</p>

        <p>If the card’s owner has no default card, then the new card will become the default.
        However, if the owner already has a default, then it will not change.
        To change the default, you should <a href="/docs/api#update_customer">update the customer</a> to have a new <code>default_source</code>.</p>

        POST /v1/customers/{customer}/cards

        Args:
            data: CustomerCardCreateBody
            customer: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.customer.card.create(customer="string")
        ```
        """
        models.Account.model_rebuild(_types_namespace=models._types_namespace)
        models.BankAccount.model_rebuild(_types_namespace=models._types_namespace)
        models.Card.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerCustomerCardCreateBody,
                style={
                    "alipay_account": "form",
                    "bank_account": "deepObject",
                    "card": "deepObject",
                    "expand": "deepObject",
                    "metadata": "deepObject",
                    "source": "form",
                },
                explode={
                    "alipay_account": True,
                    "bank_account": True,
                    "card": True,
                    "expand": True,
                    "metadata": True,
                    "source": True,
                },
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/customers/{customer}/cards",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=typing.Union[
                models.Account, models.BankAccount, models.Card, models.Source
            ],
            request_options=request_options or default_request_options(),
        )

    async def update(
        self,
        *,
        customer: str,
        id: str,
        data: typing.Union[
            typing.Optional[params.CustomerCardUpdateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Union[models.Card, models.BankAccount, models.Source]:
        """
        <p>Update a specified source for a given customer.</p>

        POST /v1/customers/{customer}/cards/{id}

        Args:
            data: CustomerCardUpdateBody
            customer: str
            id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.customer.card.update(customer="string", id="string")
        ```
        """
        models.BankAccount.model_rebuild(_types_namespace=models._types_namespace)
        models.Card.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerCustomerCardUpdateBody,
                style={
                    "account_holder_name": "form",
                    "account_holder_type": "form",
                    "address_city": "form",
                    "address_country": "form",
                    "address_line1": "form",
                    "address_line2": "form",
                    "address_state": "form",
                    "address_zip": "form",
                    "exp_month": "form",
                    "exp_year": "form",
                    "expand": "deepObject",
                    "metadata": "deepObject",
                    "name": "form",
                    "owner": "deepObject",
                },
                explode={
                    "account_holder_name": True,
                    "account_holder_type": True,
                    "address_city": True,
                    "address_country": True,
                    "address_line1": True,
                    "address_line2": True,
                    "address_state": True,
                    "address_zip": True,
                    "exp_month": True,
                    "exp_year": True,
                    "expand": True,
                    "metadata": True,
                    "name": True,
                    "owner": True,
                },
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/customers/{customer}/cards/{id}",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=typing.Union[models.Card, models.BankAccount, models.Source],
            request_options=request_options or default_request_options(),
        )
