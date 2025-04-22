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


class CashBalanceClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def get(
        self,
        *,
        customer: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.CashBalance:
        """
        Retrieve a cash balance

        <p>Retrieves a customer’s cash balance.</p>

        GET /v1/customers/{customer}/cash_balance

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
        client.customer.cash_balance.get(customer="string")
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
            path=f"/v1/customers/{customer}/cash_balance",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.CashBalance,
            request_options=request_options or default_request_options(),
        )

    def modify(
        self,
        *,
        customer: str,
        data: typing.Union[
            typing.Optional[params.CustomerCashBalanceModifyBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.CashBalance:
        """
        Update a cash balance's settings

        <p>Changes the settings on a customer’s cash balance.</p>

        POST /v1/customers/{customer}/cash_balance

        Args:
            data: CustomerCashBalanceModifyBody
            customer: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.customer.cash_balance.modify(customer="string")
        ```
        """
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerCustomerCashBalanceModifyBody,
                style={"expand": "deepObject", "settings": "deepObject"},
                explode={"expand": True, "settings": True},
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/customers/{customer}/cash_balance",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.CashBalance,
            request_options=request_options or default_request_options(),
        )


class AsyncCashBalanceClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def get(
        self,
        *,
        customer: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.CashBalance:
        """
        Retrieve a cash balance

        <p>Retrieves a customer’s cash balance.</p>

        GET /v1/customers/{customer}/cash_balance

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
        await client.customer.cash_balance.get(customer="string")
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
            path=f"/v1/customers/{customer}/cash_balance",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.CashBalance,
            request_options=request_options or default_request_options(),
        )

    async def modify(
        self,
        *,
        customer: str,
        data: typing.Union[
            typing.Optional[params.CustomerCashBalanceModifyBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.CashBalance:
        """
        Update a cash balance's settings

        <p>Changes the settings on a customer’s cash balance.</p>

        POST /v1/customers/{customer}/cash_balance

        Args:
            data: CustomerCashBalanceModifyBody
            customer: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.customer.cash_balance.modify(customer="string")
        ```
        """
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerCustomerCashBalanceModifyBody,
                style={"expand": "deepObject", "settings": "deepObject"},
                explode={"expand": True, "settings": True},
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/customers/{customer}/cash_balance",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.CashBalance,
            request_options=request_options or default_request_options(),
        )
