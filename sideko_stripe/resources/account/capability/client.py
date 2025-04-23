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


class CapabilityClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def list(
        self,
        *,
        account: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.AccountCapabilityListResponse:
        """
        List all account capabilities

        <p>Returns a list of capabilities associated with the account. The capabilities are returned sorted by creation date, with the most recent capability appearing first.</p>

        GET /v1/accounts/{account}/capabilities

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
        client.account.capability.list(account="string")
        ```
        """
        models.AccountCapabilityListResponse.model_rebuild(
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
            path=f"/v1/accounts/{account}/capabilities",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.AccountCapabilityListResponse,
            request_options=request_options or default_request_options(),
        )

    def get(
        self,
        *,
        account: str,
        capability: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Capability:
        """
        Retrieve an Account Capability

        <p>Retrieves information about the specified Account Capability.</p>

        GET /v1/accounts/{account}/capabilities/{capability}

        Args:
            expand: Specifies which fields in the response should be expanded.
            account: str
            capability: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.account.capability.get(account="string", capability="string")
        ```
        """
        models.Capability.model_rebuild(_types_namespace=models._types_namespace)
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
            path=f"/v1/accounts/{account}/capabilities/{capability}",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.Capability,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        account: str,
        capability: str,
        data: typing.Union[
            typing.Optional[params.AccountCapabilityCreateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Capability:
        """
        Update an Account Capability

        <p>Updates an existing Account Capability. Request or remove a capability by updating its <code>requested</code> parameter.</p>

        POST /v1/accounts/{account}/capabilities/{capability}

        Args:
            data: AccountCapabilityCreateBody
            account: str
            capability: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.account.capability.create(account="string", capability="string")
        ```
        """
        models.Capability.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerAccountCapabilityCreateBody,
                style={"expand": "deepObject", "requested": "form"},
                explode={"expand": True, "requested": True},
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/accounts/{account}/capabilities/{capability}",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.Capability,
            request_options=request_options or default_request_options(),
        )


class AsyncCapabilityClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def list(
        self,
        *,
        account: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.AccountCapabilityListResponse:
        """
        List all account capabilities

        <p>Returns a list of capabilities associated with the account. The capabilities are returned sorted by creation date, with the most recent capability appearing first.</p>

        GET /v1/accounts/{account}/capabilities

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
        await client.account.capability.list(account="string")
        ```
        """
        models.AccountCapabilityListResponse.model_rebuild(
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
            path=f"/v1/accounts/{account}/capabilities",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.AccountCapabilityListResponse,
            request_options=request_options or default_request_options(),
        )

    async def get(
        self,
        *,
        account: str,
        capability: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Capability:
        """
        Retrieve an Account Capability

        <p>Retrieves information about the specified Account Capability.</p>

        GET /v1/accounts/{account}/capabilities/{capability}

        Args:
            expand: Specifies which fields in the response should be expanded.
            account: str
            capability: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.account.capability.get(account="string", capability="string")
        ```
        """
        models.Capability.model_rebuild(_types_namespace=models._types_namespace)
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
            path=f"/v1/accounts/{account}/capabilities/{capability}",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.Capability,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        account: str,
        capability: str,
        data: typing.Union[
            typing.Optional[params.AccountCapabilityCreateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Capability:
        """
        Update an Account Capability

        <p>Updates an existing Account Capability. Request or remove a capability by updating its <code>requested</code> parameter.</p>

        POST /v1/accounts/{account}/capabilities/{capability}

        Args:
            data: AccountCapabilityCreateBody
            account: str
            capability: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.account.capability.create(account="string", capability="string")
        ```
        """
        models.Capability.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerAccountCapabilityCreateBody,
                style={"expand": "deepObject", "requested": "form"},
                explode={"expand": True, "requested": True},
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/accounts/{account}/capabilities/{capability}",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.Capability,
            request_options=request_options or default_request_options(),
        )
