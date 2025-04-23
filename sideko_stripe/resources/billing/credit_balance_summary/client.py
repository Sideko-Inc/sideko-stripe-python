import typing

from sideko_stripe.core import (
    AsyncBaseClient,
    QueryParams,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
    encode_query_param,
    to_encodable,
    type_utils,
)
from sideko_stripe.types import models, params


class CreditBalanceSummaryClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def get(
        self,
        *,
        customer: str,
        filter: params.BillingCreditBalanceSummaryGetFilter,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.BillingCreditBalanceSummary:
        """
        Retrieve the credit balance summary for a customer

        <p>Retrieves the credit balance summary for a customer.</p>

        GET /v1/billing/credit_balance_summary

        Args:
            expand: Specifies which fields in the response should be expanded.
            customer: The customer for which to fetch credit balance summary.
            filter: The filter criteria for the credit balance summary.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.billing.credit_balance_summary.get(
            customer="string", filter={"type_": "applicability_scope"}
        )
        ```
        """
        models.BillingCreditBalanceSummary.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _query: QueryParams = {}
        encode_query_param(
            _query,
            "customer",
            to_encodable(item=customer, dump_with=str),
            style="form",
            explode=True,
        )
        encode_query_param(
            _query,
            "filter",
            to_encodable(
                item=filter,
                dump_with=params._SerializerBillingCreditBalanceSummaryGetFilter,
            ),
            style="deepObject",
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
        return self._base_client.request(
            method="GET",
            path="/v1/billing/credit_balance_summary",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.BillingCreditBalanceSummary,
            request_options=request_options or default_request_options(),
        )


class AsyncCreditBalanceSummaryClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def get(
        self,
        *,
        customer: str,
        filter: params.BillingCreditBalanceSummaryGetFilter,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.BillingCreditBalanceSummary:
        """
        Retrieve the credit balance summary for a customer

        <p>Retrieves the credit balance summary for a customer.</p>

        GET /v1/billing/credit_balance_summary

        Args:
            expand: Specifies which fields in the response should be expanded.
            customer: The customer for which to fetch credit balance summary.
            filter: The filter criteria for the credit balance summary.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.billing.credit_balance_summary.get(
            customer="string", filter={"type_": "applicability_scope"}
        )
        ```
        """
        models.BillingCreditBalanceSummary.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _query: QueryParams = {}
        encode_query_param(
            _query,
            "customer",
            to_encodable(item=customer, dump_with=str),
            style="form",
            explode=True,
        )
        encode_query_param(
            _query,
            "filter",
            to_encodable(
                item=filter,
                dump_with=params._SerializerBillingCreditBalanceSummaryGetFilter,
            ),
            style="deepObject",
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
        return await self._base_client.request(
            method="GET",
            path="/v1/billing/credit_balance_summary",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.BillingCreditBalanceSummary,
            request_options=request_options or default_request_options(),
        )
