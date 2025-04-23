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


class LinkAccountSessionClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def get(
        self,
        *,
        session: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.FinancialConnectionsSession:
        """
        Retrieve a Session

        <p>Retrieves the details of a Financial Connections <code>Session</code></p>

        GET /v1/link_account_sessions/{session}

        Args:
            expand: Specifies which fields in the response should be expanded.
            session: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.link_account_session.get(session="string")
        ```
        """
        models.FinancialConnectionsSession.model_rebuild(
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
            path=f"/v1/link_account_sessions/{session}",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.FinancialConnectionsSession,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        account_holder: params.LinkAccountSessionCreateBodyAccountHolder,
        permissions: typing.List[
            typing_extensions.Literal[
                "balances", "ownership", "payment_method", "transactions"
            ]
        ],
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        filters: typing.Union[
            typing.Optional[params.LinkAccountSessionCreateBodyFilters],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        prefetch: typing.Union[
            typing.Optional[
                typing.List[
                    typing_extensions.Literal["balances", "ownership", "transactions"]
                ]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        return_url: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.FinancialConnectionsSession:
        """
        Create a Session

        <p>To launch the Financial Connections authorization flow, create a <code>Session</code>. The session’s <code>client_secret</code> can be used to launch the flow using Stripe.js.</p>

        POST /v1/link_account_sessions

        Args:
            expand: Specifies which fields in the response should be expanded.
            filters: Filters to restrict the kinds of accounts to collect.
            prefetch: List of data features that you would like to retrieve upon account creation.
            return_url: For webview integrations only. Upon completing OAuth login in the native browser, the user will be redirected to this URL to return to your app.
            account_holder: The account holder to link accounts for.
            permissions: List of data features that you would like to request access to.

        Possible values are `balances`, `transactions`, `ownership`, and `payment_method`.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.link_account_session.create(
            account_holder={"type_": "account"}, permissions=["balances"]
        )
        ```
        """
        models.FinancialConnectionsSession.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _data = to_form_urlencoded(
            item={
                "expand": expand,
                "filters": filters,
                "prefetch": prefetch,
                "return_url": return_url,
                "account_holder": account_holder,
                "permissions": permissions,
            },
            dump_with=params._SerializerLinkAccountSessionCreateBody,
            style={
                "account_holder": "deepObject",
                "expand": "deepObject",
                "filters": "deepObject",
                "permissions": "deepObject",
                "prefetch": "deepObject",
                "return_url": "form",
            },
            explode={
                "account_holder": True,
                "expand": True,
                "filters": True,
                "permissions": True,
                "prefetch": True,
                "return_url": True,
            },
        )
        return self._base_client.request(
            method="POST",
            path="/v1/link_account_sessions",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.FinancialConnectionsSession,
            request_options=request_options or default_request_options(),
        )


class AsyncLinkAccountSessionClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def get(
        self,
        *,
        session: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.FinancialConnectionsSession:
        """
        Retrieve a Session

        <p>Retrieves the details of a Financial Connections <code>Session</code></p>

        GET /v1/link_account_sessions/{session}

        Args:
            expand: Specifies which fields in the response should be expanded.
            session: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.link_account_session.get(session="string")
        ```
        """
        models.FinancialConnectionsSession.model_rebuild(
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
            path=f"/v1/link_account_sessions/{session}",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.FinancialConnectionsSession,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        account_holder: params.LinkAccountSessionCreateBodyAccountHolder,
        permissions: typing.List[
            typing_extensions.Literal[
                "balances", "ownership", "payment_method", "transactions"
            ]
        ],
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        filters: typing.Union[
            typing.Optional[params.LinkAccountSessionCreateBodyFilters],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        prefetch: typing.Union[
            typing.Optional[
                typing.List[
                    typing_extensions.Literal["balances", "ownership", "transactions"]
                ]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        return_url: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.FinancialConnectionsSession:
        """
        Create a Session

        <p>To launch the Financial Connections authorization flow, create a <code>Session</code>. The session’s <code>client_secret</code> can be used to launch the flow using Stripe.js.</p>

        POST /v1/link_account_sessions

        Args:
            expand: Specifies which fields in the response should be expanded.
            filters: Filters to restrict the kinds of accounts to collect.
            prefetch: List of data features that you would like to retrieve upon account creation.
            return_url: For webview integrations only. Upon completing OAuth login in the native browser, the user will be redirected to this URL to return to your app.
            account_holder: The account holder to link accounts for.
            permissions: List of data features that you would like to request access to.

        Possible values are `balances`, `transactions`, `ownership`, and `payment_method`.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.link_account_session.create(
            account_holder={"type_": "account"}, permissions=["balances"]
        )
        ```
        """
        models.FinancialConnectionsSession.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _data = to_form_urlencoded(
            item={
                "expand": expand,
                "filters": filters,
                "prefetch": prefetch,
                "return_url": return_url,
                "account_holder": account_holder,
                "permissions": permissions,
            },
            dump_with=params._SerializerLinkAccountSessionCreateBody,
            style={
                "account_holder": "deepObject",
                "expand": "deepObject",
                "filters": "deepObject",
                "permissions": "deepObject",
                "prefetch": "deepObject",
                "return_url": "form",
            },
            explode={
                "account_holder": True,
                "expand": True,
                "filters": True,
                "permissions": True,
                "prefetch": True,
                "return_url": True,
            },
        )
        return await self._base_client.request(
            method="POST",
            path="/v1/link_account_sessions",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.FinancialConnectionsSession,
            request_options=request_options or default_request_options(),
        )
