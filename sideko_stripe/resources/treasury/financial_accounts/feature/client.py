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


class FeatureClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def list(
        self,
        *,
        financial_account: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TreasuryFinancialAccountFeatures:
        """
        Retrieve FinancialAccount Features

        <p>Retrieves Features information associated with the FinancialAccount.</p>

        GET /v1/treasury/financial_accounts/{financial_account}/features

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
        client.treasury.financial_accounts.feature.list(financial_account="string")
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
            path=f"/v1/treasury/financial_accounts/{financial_account}/features",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.TreasuryFinancialAccountFeatures,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        financial_account: str,
        data: typing.Union[
            typing.Optional[params.TreasuryFinancialAccountsFeatureCreateBody],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TreasuryFinancialAccountFeatures:
        """
        Update FinancialAccount Features

        <p>Updates the Features associated with a FinancialAccount.</p>

        POST /v1/treasury/financial_accounts/{financial_account}/features

        Args:
            data: TreasuryFinancialAccountsFeatureCreateBody
            financial_account: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.treasury.financial_accounts.feature.create(financial_account="string")
        ```
        """
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerTreasuryFinancialAccountsFeatureCreateBody,
                style={
                    "card_issuing": "deepObject",
                    "deposit_insurance": "deepObject",
                    "expand": "deepObject",
                    "financial_addresses": "deepObject",
                    "inbound_transfers": "deepObject",
                    "intra_stripe_flows": "deepObject",
                    "outbound_payments": "deepObject",
                    "outbound_transfers": "deepObject",
                },
                explode={
                    "card_issuing": True,
                    "deposit_insurance": True,
                    "expand": True,
                    "financial_addresses": True,
                    "inbound_transfers": True,
                    "intra_stripe_flows": True,
                    "outbound_payments": True,
                    "outbound_transfers": True,
                },
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/treasury/financial_accounts/{financial_account}/features",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.TreasuryFinancialAccountFeatures,
            request_options=request_options or default_request_options(),
        )


class AsyncFeatureClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def list(
        self,
        *,
        financial_account: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TreasuryFinancialAccountFeatures:
        """
        Retrieve FinancialAccount Features

        <p>Retrieves Features information associated with the FinancialAccount.</p>

        GET /v1/treasury/financial_accounts/{financial_account}/features

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
        await client.treasury.financial_accounts.feature.list(
            financial_account="string"
        )
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
            path=f"/v1/treasury/financial_accounts/{financial_account}/features",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.TreasuryFinancialAccountFeatures,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        financial_account: str,
        data: typing.Union[
            typing.Optional[params.TreasuryFinancialAccountsFeatureCreateBody],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TreasuryFinancialAccountFeatures:
        """
        Update FinancialAccount Features

        <p>Updates the Features associated with a FinancialAccount.</p>

        POST /v1/treasury/financial_accounts/{financial_account}/features

        Args:
            data: TreasuryFinancialAccountsFeatureCreateBody
            financial_account: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.treasury.financial_accounts.feature.create(
            financial_account="string"
        )
        ```
        """
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerTreasuryFinancialAccountsFeatureCreateBody,
                style={
                    "card_issuing": "deepObject",
                    "deposit_insurance": "deepObject",
                    "expand": "deepObject",
                    "financial_addresses": "deepObject",
                    "inbound_transfers": "deepObject",
                    "intra_stripe_flows": "deepObject",
                    "outbound_payments": "deepObject",
                    "outbound_transfers": "deepObject",
                },
                explode={
                    "card_issuing": True,
                    "deposit_insurance": True,
                    "expand": True,
                    "financial_addresses": True,
                    "inbound_transfers": True,
                    "intra_stripe_flows": True,
                    "outbound_payments": True,
                    "outbound_transfers": True,
                },
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/treasury/financial_accounts/{financial_account}/features",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.TreasuryFinancialAccountFeatures,
            request_options=request_options or default_request_options(),
        )
