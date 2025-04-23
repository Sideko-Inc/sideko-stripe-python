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
from sideko_stripe.types import models


class DiscountClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def delete(
        self,
        *,
        customer: str,
        subscription_exposed_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.DeletedDiscount:
        """
        Delete a customer discount

        <p>Removes the currently applied discount on a customer.</p>

        DELETE /v1/customers/{customer}/subscriptions/{subscription_exposed_id}/discount

        Args:
            customer: str
            subscription_exposed_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.customer.subscription.discount.delete(
            customer="string", subscription_exposed_id="string"
        )
        ```
        """
        models.DeletedDiscount.model_rebuild(_types_namespace=models._types_namespace)
        return self._base_client.request(
            method="DELETE",
            path=f"/v1/customers/{customer}/subscriptions/{subscription_exposed_id}/discount",
            auth_names=["bearerAuth"],
            cast_to=models.DeletedDiscount,
            request_options=request_options or default_request_options(),
        )

    def list(
        self,
        *,
        customer: str,
        subscription_exposed_id: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Discount:
        """


        GET /v1/customers/{customer}/subscriptions/{subscription_exposed_id}/discount

        Args:
            expand: Specifies which fields in the response should be expanded.
            customer: str
            subscription_exposed_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.customer.subscription.discount.list(
            customer="string", subscription_exposed_id="string"
        )
        ```
        """
        models.Discount.model_rebuild(_types_namespace=models._types_namespace)
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
            path=f"/v1/customers/{customer}/subscriptions/{subscription_exposed_id}/discount",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.Discount,
            request_options=request_options or default_request_options(),
        )


class AsyncDiscountClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def delete(
        self,
        *,
        customer: str,
        subscription_exposed_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.DeletedDiscount:
        """
        Delete a customer discount

        <p>Removes the currently applied discount on a customer.</p>

        DELETE /v1/customers/{customer}/subscriptions/{subscription_exposed_id}/discount

        Args:
            customer: str
            subscription_exposed_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.customer.subscription.discount.delete(
            customer="string", subscription_exposed_id="string"
        )
        ```
        """
        models.DeletedDiscount.model_rebuild(_types_namespace=models._types_namespace)
        return await self._base_client.request(
            method="DELETE",
            path=f"/v1/customers/{customer}/subscriptions/{subscription_exposed_id}/discount",
            auth_names=["bearerAuth"],
            cast_to=models.DeletedDiscount,
            request_options=request_options or default_request_options(),
        )

    async def list(
        self,
        *,
        customer: str,
        subscription_exposed_id: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Discount:
        """


        GET /v1/customers/{customer}/subscriptions/{subscription_exposed_id}/discount

        Args:
            expand: Specifies which fields in the response should be expanded.
            customer: str
            subscription_exposed_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.customer.subscription.discount.list(
            customer="string", subscription_exposed_id="string"
        )
        ```
        """
        models.Discount.model_rebuild(_types_namespace=models._types_namespace)
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
            path=f"/v1/customers/{customer}/subscriptions/{subscription_exposed_id}/discount",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.Discount,
            request_options=request_options or default_request_options(),
        )
