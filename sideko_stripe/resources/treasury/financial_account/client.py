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


class FinancialAccountClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def list(
        self,
        *,
        created: typing.Union[
            typing.Optional[
                typing.Union[params.TreasuryFinancialAccountListCreatedObj0, int]
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
        starting_after: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TreasuryFinancialAccountListResponse:
        """
        List all FinancialAccounts

        <p>Returns a list of FinancialAccounts.</p>

        GET /v1/treasury/financial_accounts

        Args:
            created: Only return FinancialAccounts that were created during the given date interval.
            ending_before: An object ID cursor for use in pagination.
            expand: Specifies which fields in the response should be expanded.
            limit: A limit ranging from 1 to 100 (defaults to 10).
            starting_after: An object ID cursor for use in pagination.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.treasury.financial_account.list()
        ```
        """
        _query: QueryParams = {}
        if not isinstance(created, type_utils.NotGiven):
            encode_query_param(
                _query,
                "created",
                to_encodable(
                    item=created,
                    dump_with=typing.Union[
                        params._SerializerTreasuryFinancialAccountListCreatedObj0, int
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
            path="/v1/treasury/financial_accounts",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.TreasuryFinancialAccountListResponse,
            request_options=request_options or default_request_options(),
        )

    def get(
        self,
        *,
        financial_account: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TreasuryFinancialAccount:
        """
        Retrieve a FinancialAccount

        <p>Retrieves the details of a FinancialAccount.</p>

        GET /v1/treasury/financial_accounts/{financial_account}

        Args:
            expand: Specifies which fields in the response should be expanded.
            financial_account: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.treasury.financial_account.get(financial_account="string")
        ```
        """
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
            path=f"/v1/treasury/financial_accounts/{financial_account}",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.TreasuryFinancialAccount,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        supported_currencies: typing.List[str],
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        features: typing.Union[
            typing.Optional[params.TreasuryFinancialAccountCreateBodyFeatures],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        metadata: typing.Union[
            typing.Optional[params.TreasuryFinancialAccountCreateBodyMetadata],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        nickname: typing.Union[
            typing.Optional[typing.Union[str, str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        platform_restrictions: typing.Union[
            typing.Optional[
                params.TreasuryFinancialAccountCreateBodyPlatformRestrictions
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TreasuryFinancialAccount:
        """
        Create a FinancialAccount

        <p>Creates a new FinancialAccount. Each connected account can have up to three FinancialAccounts by default.</p>

        POST /v1/treasury/financial_accounts

        Args:
            expand: Specifies which fields in the response should be expanded.
            features: Encodes whether a FinancialAccount has access to a particular feature. Stripe or the platform can control features via the requested field.
            metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
            nickname: The nickname for the FinancialAccount.
            platform_restrictions: The set of functionalities that the platform can restrict on the FinancialAccount.
            supported_currencies: The currencies the FinancialAccount can hold a balance in.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.treasury.financial_account.create(supported_currencies=["string"])
        ```
        """
        _data = to_form_urlencoded(
            item={
                "expand": expand,
                "features": features,
                "metadata": metadata,
                "nickname": nickname,
                "platform_restrictions": platform_restrictions,
                "supported_currencies": supported_currencies,
            },
            dump_with=params._SerializerTreasuryFinancialAccountCreateBody,
            style={
                "expand": "deepObject",
                "features": "deepObject",
                "metadata": "deepObject",
                "nickname": "deepObject",
                "platform_restrictions": "deepObject",
                "supported_currencies": "deepObject",
            },
            explode={
                "expand": True,
                "features": True,
                "metadata": True,
                "nickname": True,
                "platform_restrictions": True,
                "supported_currencies": True,
            },
        )
        return self._base_client.request(
            method="POST",
            path="/v1/treasury/financial_accounts",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.TreasuryFinancialAccount,
            request_options=request_options or default_request_options(),
        )

    def update(
        self,
        *,
        financial_account: str,
        data: typing.Union[
            typing.Optional[params.TreasuryFinancialAccountUpdateBody],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TreasuryFinancialAccount:
        """
        Update a FinancialAccount

        <p>Updates the details of a FinancialAccount.</p>

        POST /v1/treasury/financial_accounts/{financial_account}

        Args:
            data: TreasuryFinancialAccountUpdateBody
            financial_account: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.treasury.financial_account.update(financial_account="string")
        ```
        """
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerTreasuryFinancialAccountUpdateBody,
                style={
                    "expand": "deepObject",
                    "features": "deepObject",
                    "forwarding_settings": "deepObject",
                    "metadata": "deepObject",
                    "nickname": "deepObject",
                    "platform_restrictions": "deepObject",
                },
                explode={
                    "expand": True,
                    "features": True,
                    "forwarding_settings": True,
                    "metadata": True,
                    "nickname": True,
                    "platform_restrictions": True,
                },
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/treasury/financial_accounts/{financial_account}",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.TreasuryFinancialAccount,
            request_options=request_options or default_request_options(),
        )

    def close(
        self,
        *,
        financial_account: str,
        data: typing.Union[
            typing.Optional[params.TreasuryFinancialAccountCloseBody],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TreasuryFinancialAccount:
        """
        Close a FinancialAccount

        <p>Closes a FinancialAccount. A FinancialAccount can only be closed if it has a zero balance, has no pending InboundTransfers, and has canceled all attached Issuing cards.</p>

        POST /v1/treasury/financial_accounts/{financial_account}/close

        Args:
            data: TreasuryFinancialAccountCloseBody
            financial_account: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.treasury.financial_account.close(financial_account="string")
        ```
        """
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerTreasuryFinancialAccountCloseBody,
                style={"expand": "deepObject", "forwarding_settings": "deepObject"},
                explode={"expand": True, "forwarding_settings": True},
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/treasury/financial_accounts/{financial_account}/close",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.TreasuryFinancialAccount,
            request_options=request_options or default_request_options(),
        )


class AsyncFinancialAccountClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def list(
        self,
        *,
        created: typing.Union[
            typing.Optional[
                typing.Union[params.TreasuryFinancialAccountListCreatedObj0, int]
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
        starting_after: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TreasuryFinancialAccountListResponse:
        """
        List all FinancialAccounts

        <p>Returns a list of FinancialAccounts.</p>

        GET /v1/treasury/financial_accounts

        Args:
            created: Only return FinancialAccounts that were created during the given date interval.
            ending_before: An object ID cursor for use in pagination.
            expand: Specifies which fields in the response should be expanded.
            limit: A limit ranging from 1 to 100 (defaults to 10).
            starting_after: An object ID cursor for use in pagination.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.treasury.financial_account.list()
        ```
        """
        _query: QueryParams = {}
        if not isinstance(created, type_utils.NotGiven):
            encode_query_param(
                _query,
                "created",
                to_encodable(
                    item=created,
                    dump_with=typing.Union[
                        params._SerializerTreasuryFinancialAccountListCreatedObj0, int
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
            path="/v1/treasury/financial_accounts",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.TreasuryFinancialAccountListResponse,
            request_options=request_options or default_request_options(),
        )

    async def get(
        self,
        *,
        financial_account: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TreasuryFinancialAccount:
        """
        Retrieve a FinancialAccount

        <p>Retrieves the details of a FinancialAccount.</p>

        GET /v1/treasury/financial_accounts/{financial_account}

        Args:
            expand: Specifies which fields in the response should be expanded.
            financial_account: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.treasury.financial_account.get(financial_account="string")
        ```
        """
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
            path=f"/v1/treasury/financial_accounts/{financial_account}",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.TreasuryFinancialAccount,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        supported_currencies: typing.List[str],
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        features: typing.Union[
            typing.Optional[params.TreasuryFinancialAccountCreateBodyFeatures],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        metadata: typing.Union[
            typing.Optional[params.TreasuryFinancialAccountCreateBodyMetadata],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        nickname: typing.Union[
            typing.Optional[typing.Union[str, str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        platform_restrictions: typing.Union[
            typing.Optional[
                params.TreasuryFinancialAccountCreateBodyPlatformRestrictions
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TreasuryFinancialAccount:
        """
        Create a FinancialAccount

        <p>Creates a new FinancialAccount. Each connected account can have up to three FinancialAccounts by default.</p>

        POST /v1/treasury/financial_accounts

        Args:
            expand: Specifies which fields in the response should be expanded.
            features: Encodes whether a FinancialAccount has access to a particular feature. Stripe or the platform can control features via the requested field.
            metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
            nickname: The nickname for the FinancialAccount.
            platform_restrictions: The set of functionalities that the platform can restrict on the FinancialAccount.
            supported_currencies: The currencies the FinancialAccount can hold a balance in.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.treasury.financial_account.create(supported_currencies=["string"])
        ```
        """
        _data = to_form_urlencoded(
            item={
                "expand": expand,
                "features": features,
                "metadata": metadata,
                "nickname": nickname,
                "platform_restrictions": platform_restrictions,
                "supported_currencies": supported_currencies,
            },
            dump_with=params._SerializerTreasuryFinancialAccountCreateBody,
            style={
                "expand": "deepObject",
                "features": "deepObject",
                "metadata": "deepObject",
                "nickname": "deepObject",
                "platform_restrictions": "deepObject",
                "supported_currencies": "deepObject",
            },
            explode={
                "expand": True,
                "features": True,
                "metadata": True,
                "nickname": True,
                "platform_restrictions": True,
                "supported_currencies": True,
            },
        )
        return await self._base_client.request(
            method="POST",
            path="/v1/treasury/financial_accounts",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.TreasuryFinancialAccount,
            request_options=request_options or default_request_options(),
        )

    async def update(
        self,
        *,
        financial_account: str,
        data: typing.Union[
            typing.Optional[params.TreasuryFinancialAccountUpdateBody],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TreasuryFinancialAccount:
        """
        Update a FinancialAccount

        <p>Updates the details of a FinancialAccount.</p>

        POST /v1/treasury/financial_accounts/{financial_account}

        Args:
            data: TreasuryFinancialAccountUpdateBody
            financial_account: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.treasury.financial_account.update(financial_account="string")
        ```
        """
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerTreasuryFinancialAccountUpdateBody,
                style={
                    "expand": "deepObject",
                    "features": "deepObject",
                    "forwarding_settings": "deepObject",
                    "metadata": "deepObject",
                    "nickname": "deepObject",
                    "platform_restrictions": "deepObject",
                },
                explode={
                    "expand": True,
                    "features": True,
                    "forwarding_settings": True,
                    "metadata": True,
                    "nickname": True,
                    "platform_restrictions": True,
                },
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/treasury/financial_accounts/{financial_account}",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.TreasuryFinancialAccount,
            request_options=request_options or default_request_options(),
        )

    async def close(
        self,
        *,
        financial_account: str,
        data: typing.Union[
            typing.Optional[params.TreasuryFinancialAccountCloseBody],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TreasuryFinancialAccount:
        """
        Close a FinancialAccount

        <p>Closes a FinancialAccount. A FinancialAccount can only be closed if it has a zero balance, has no pending InboundTransfers, and has canceled all attached Issuing cards.</p>

        POST /v1/treasury/financial_accounts/{financial_account}/close

        Args:
            data: TreasuryFinancialAccountCloseBody
            financial_account: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.treasury.financial_account.close(financial_account="string")
        ```
        """
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerTreasuryFinancialAccountCloseBody,
                style={"expand": "deepObject", "forwarding_settings": "deepObject"},
                explode={"expand": True, "forwarding_settings": True},
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/treasury/financial_accounts/{financial_account}/close",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.TreasuryFinancialAccount,
            request_options=request_options or default_request_options(),
        )
