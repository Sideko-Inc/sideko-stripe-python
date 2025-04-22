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
from sideko_stripe.resources.financial_connections.account.owners import (
    AsyncOwnersClient,
    OwnersClient,
)
from sideko_stripe.types import models, params


class AccountClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        self.owners = OwnersClient(base_client=self._base_client)

    def list(
        self,
        *,
        account_holder: typing.Union[
            typing.Optional[params.FinancialConnectionsAccountListAccountHolder],
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
        session: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        starting_after: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.FinancialConnectionsAccountListResponse:
        """
        List Accounts

        <p>Returns a list of Financial Connections <code>Account</code> objects.</p>

        GET /v1/financial_connections/accounts

        Args:
            account_holder: If present, only return accounts that belong to the specified account holder. `account_holder[customer]` and `account_holder[account]` are mutually exclusive.
            ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            expand: Specifies which fields in the response should be expanded.
            limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            session: If present, only return accounts that were collected as part of the given session.
            starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.financial_connections.account.list()
        ```
        """
        models.FinancialConnectionsAccountListResponse.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _query: QueryParams = {}
        if not isinstance(account_holder, type_utils.NotGiven):
            encode_query_param(
                _query,
                "account_holder",
                to_encodable(
                    item=account_holder,
                    dump_with=params._SerializerFinancialConnectionsAccountListAccountHolder,
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
        if not isinstance(session, type_utils.NotGiven):
            encode_query_param(
                _query,
                "session",
                to_encodable(item=session, dump_with=str),
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
            path="/v1/financial_connections/accounts",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.FinancialConnectionsAccountListResponse,
            request_options=request_options or default_request_options(),
        )

    def get(
        self,
        *,
        account: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.FinancialConnectionsAccount:
        """
        Retrieve an Account

        <p>Retrieves the details of an Financial Connections <code>Account</code>.</p>

        GET /v1/financial_connections/accounts/{account}

        Args:
            expand: Specifies which fields in the response should be expanded.
            account: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.financial_connections.account.get(account="string")
        ```
        """
        models.FinancialConnectionsAccount.model_rebuild(
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
            path=f"/v1/financial_connections/accounts/{account}",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.FinancialConnectionsAccount,
            request_options=request_options or default_request_options(),
        )

    def disconnect(
        self,
        *,
        account: str,
        data: typing.Union[
            typing.Optional[params.FinancialConnectionsAccountDisconnectBody],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.FinancialConnectionsAccount:
        """
        Disconnect an Account

        <p>Disables your access to a Financial Connections <code>Account</code>. You will no longer be able to access data associated with the account (e.g. balances, transactions).</p>

        POST /v1/financial_connections/accounts/{account}/disconnect

        Args:
            data: FinancialConnectionsAccountDisconnectBody
            account: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.financial_connections.account.disconnect(account="string")
        ```
        """
        models.FinancialConnectionsAccount.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerFinancialConnectionsAccountDisconnectBody,
                style={"expand": "deepObject"},
                explode={"expand": True},
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/financial_connections/accounts/{account}/disconnect",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.FinancialConnectionsAccount,
            request_options=request_options or default_request_options(),
        )

    def refresh(
        self,
        *,
        account: str,
        features: typing.List[
            typing_extensions.Literal["balance", "ownership", "transactions"]
        ],
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.FinancialConnectionsAccount:
        """
        Refresh Account data

        <p>Refreshes the data associated with a Financial Connections <code>Account</code>.</p>

        POST /v1/financial_connections/accounts/{account}/refresh

        Args:
            expand: Specifies which fields in the response should be expanded.
            account: str
            features: The list of account features that you would like to refresh.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.financial_connections.account.refresh(
            account="string", features=["balance"]
        )
        ```
        """
        models.FinancialConnectionsAccount.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _data = to_form_urlencoded(
            item={"expand": expand, "features": features},
            dump_with=params._SerializerFinancialConnectionsAccountRefreshBody,
            style={"expand": "deepObject", "features": "deepObject"},
            explode={"expand": True, "features": True},
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/financial_connections/accounts/{account}/refresh",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.FinancialConnectionsAccount,
            request_options=request_options or default_request_options(),
        )

    def subscribe(
        self,
        *,
        account: str,
        features: typing.List[typing_extensions.Literal["transactions"]],
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.FinancialConnectionsAccount:
        """
        Subscribe to data refreshes for an Account

        <p>Subscribes to periodic refreshes of data associated with a Financial Connections <code>Account</code>.</p>

        POST /v1/financial_connections/accounts/{account}/subscribe

        Args:
            expand: Specifies which fields in the response should be expanded.
            account: str
            features: The list of account features to which you would like to subscribe.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.financial_connections.account.subscribe(
            account="string", features=["transactions"]
        )
        ```
        """
        models.FinancialConnectionsAccount.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _data = to_form_urlencoded(
            item={"expand": expand, "features": features},
            dump_with=params._SerializerFinancialConnectionsAccountSubscribeBody,
            style={"expand": "deepObject", "features": "deepObject"},
            explode={"expand": True, "features": True},
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/financial_connections/accounts/{account}/subscribe",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.FinancialConnectionsAccount,
            request_options=request_options or default_request_options(),
        )

    def unsubscribe(
        self,
        *,
        account: str,
        features: typing.List[typing_extensions.Literal["transactions"]],
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.FinancialConnectionsAccount:
        """
        Unsubscribe from data refreshes for an Account

        <p>Unsubscribes from periodic refreshes of data associated with a Financial Connections <code>Account</code>.</p>

        POST /v1/financial_connections/accounts/{account}/unsubscribe

        Args:
            expand: Specifies which fields in the response should be expanded.
            account: str
            features: The list of account features from which you would like to unsubscribe.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.financial_connections.account.unsubscribe(
            account="string", features=["transactions"]
        )
        ```
        """
        models.FinancialConnectionsAccount.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _data = to_form_urlencoded(
            item={"expand": expand, "features": features},
            dump_with=params._SerializerFinancialConnectionsAccountUnsubscribeBody,
            style={"expand": "deepObject", "features": "deepObject"},
            explode={"expand": True, "features": True},
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/financial_connections/accounts/{account}/unsubscribe",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.FinancialConnectionsAccount,
            request_options=request_options or default_request_options(),
        )


class AsyncAccountClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        self.owners = AsyncOwnersClient(base_client=self._base_client)

    async def list(
        self,
        *,
        account_holder: typing.Union[
            typing.Optional[params.FinancialConnectionsAccountListAccountHolder],
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
        session: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        starting_after: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.FinancialConnectionsAccountListResponse:
        """
        List Accounts

        <p>Returns a list of Financial Connections <code>Account</code> objects.</p>

        GET /v1/financial_connections/accounts

        Args:
            account_holder: If present, only return accounts that belong to the specified account holder. `account_holder[customer]` and `account_holder[account]` are mutually exclusive.
            ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            expand: Specifies which fields in the response should be expanded.
            limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            session: If present, only return accounts that were collected as part of the given session.
            starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.financial_connections.account.list()
        ```
        """
        models.FinancialConnectionsAccountListResponse.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _query: QueryParams = {}
        if not isinstance(account_holder, type_utils.NotGiven):
            encode_query_param(
                _query,
                "account_holder",
                to_encodable(
                    item=account_holder,
                    dump_with=params._SerializerFinancialConnectionsAccountListAccountHolder,
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
        if not isinstance(session, type_utils.NotGiven):
            encode_query_param(
                _query,
                "session",
                to_encodable(item=session, dump_with=str),
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
            path="/v1/financial_connections/accounts",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.FinancialConnectionsAccountListResponse,
            request_options=request_options or default_request_options(),
        )

    async def get(
        self,
        *,
        account: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.FinancialConnectionsAccount:
        """
        Retrieve an Account

        <p>Retrieves the details of an Financial Connections <code>Account</code>.</p>

        GET /v1/financial_connections/accounts/{account}

        Args:
            expand: Specifies which fields in the response should be expanded.
            account: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.financial_connections.account.get(account="string")
        ```
        """
        models.FinancialConnectionsAccount.model_rebuild(
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
            path=f"/v1/financial_connections/accounts/{account}",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.FinancialConnectionsAccount,
            request_options=request_options or default_request_options(),
        )

    async def disconnect(
        self,
        *,
        account: str,
        data: typing.Union[
            typing.Optional[params.FinancialConnectionsAccountDisconnectBody],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.FinancialConnectionsAccount:
        """
        Disconnect an Account

        <p>Disables your access to a Financial Connections <code>Account</code>. You will no longer be able to access data associated with the account (e.g. balances, transactions).</p>

        POST /v1/financial_connections/accounts/{account}/disconnect

        Args:
            data: FinancialConnectionsAccountDisconnectBody
            account: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.financial_connections.account.disconnect(account="string")
        ```
        """
        models.FinancialConnectionsAccount.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerFinancialConnectionsAccountDisconnectBody,
                style={"expand": "deepObject"},
                explode={"expand": True},
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/financial_connections/accounts/{account}/disconnect",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.FinancialConnectionsAccount,
            request_options=request_options or default_request_options(),
        )

    async def refresh(
        self,
        *,
        account: str,
        features: typing.List[
            typing_extensions.Literal["balance", "ownership", "transactions"]
        ],
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.FinancialConnectionsAccount:
        """
        Refresh Account data

        <p>Refreshes the data associated with a Financial Connections <code>Account</code>.</p>

        POST /v1/financial_connections/accounts/{account}/refresh

        Args:
            expand: Specifies which fields in the response should be expanded.
            account: str
            features: The list of account features that you would like to refresh.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.financial_connections.account.refresh(
            account="string", features=["balance"]
        )
        ```
        """
        models.FinancialConnectionsAccount.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _data = to_form_urlencoded(
            item={"expand": expand, "features": features},
            dump_with=params._SerializerFinancialConnectionsAccountRefreshBody,
            style={"expand": "deepObject", "features": "deepObject"},
            explode={"expand": True, "features": True},
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/financial_connections/accounts/{account}/refresh",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.FinancialConnectionsAccount,
            request_options=request_options or default_request_options(),
        )

    async def subscribe(
        self,
        *,
        account: str,
        features: typing.List[typing_extensions.Literal["transactions"]],
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.FinancialConnectionsAccount:
        """
        Subscribe to data refreshes for an Account

        <p>Subscribes to periodic refreshes of data associated with a Financial Connections <code>Account</code>.</p>

        POST /v1/financial_connections/accounts/{account}/subscribe

        Args:
            expand: Specifies which fields in the response should be expanded.
            account: str
            features: The list of account features to which you would like to subscribe.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.financial_connections.account.subscribe(
            account="string", features=["transactions"]
        )
        ```
        """
        models.FinancialConnectionsAccount.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _data = to_form_urlencoded(
            item={"expand": expand, "features": features},
            dump_with=params._SerializerFinancialConnectionsAccountSubscribeBody,
            style={"expand": "deepObject", "features": "deepObject"},
            explode={"expand": True, "features": True},
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/financial_connections/accounts/{account}/subscribe",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.FinancialConnectionsAccount,
            request_options=request_options or default_request_options(),
        )

    async def unsubscribe(
        self,
        *,
        account: str,
        features: typing.List[typing_extensions.Literal["transactions"]],
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.FinancialConnectionsAccount:
        """
        Unsubscribe from data refreshes for an Account

        <p>Unsubscribes from periodic refreshes of data associated with a Financial Connections <code>Account</code>.</p>

        POST /v1/financial_connections/accounts/{account}/unsubscribe

        Args:
            expand: Specifies which fields in the response should be expanded.
            account: str
            features: The list of account features from which you would like to unsubscribe.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.financial_connections.account.unsubscribe(
            account="string", features=["transactions"]
        )
        ```
        """
        models.FinancialConnectionsAccount.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _data = to_form_urlencoded(
            item={"expand": expand, "features": features},
            dump_with=params._SerializerFinancialConnectionsAccountUnsubscribeBody,
            style={"expand": "deepObject", "features": "deepObject"},
            explode={"expand": True, "features": True},
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/financial_connections/accounts/{account}/unsubscribe",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.FinancialConnectionsAccount,
            request_options=request_options or default_request_options(),
        )
