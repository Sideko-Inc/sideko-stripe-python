import typing

from sideko_stripe.core import (
    AsyncBaseClient,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
)
from sideko_stripe.types import models


class DiscountClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def delete(
        self,
        *,
        subscription_exposed_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.DeletedDiscount:
        """
        Delete a subscription discount

        <p>Removes the currently applied discount on a subscription.</p>

        DELETE /v1/subscriptions/{subscription_exposed_id}/discount

        Args:
            subscription_exposed_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.subscriptions.discount.delete(subscription_exposed_id="string")
        ```
        """
        models.DeletedDiscount.model_rebuild(_types_namespace=models._types_namespace)
        return self._base_client.request(
            method="DELETE",
            path=f"/v1/subscriptions/{subscription_exposed_id}/discount",
            auth_names=["basicAuth", "bearerAuth"],
            cast_to=models.DeletedDiscount,
            request_options=request_options or default_request_options(),
        )


class AsyncDiscountClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def delete(
        self,
        *,
        subscription_exposed_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.DeletedDiscount:
        """
        Delete a subscription discount

        <p>Removes the currently applied discount on a subscription.</p>

        DELETE /v1/subscriptions/{subscription_exposed_id}/discount

        Args:
            subscription_exposed_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.subscriptions.discount.delete(subscription_exposed_id="string")
        ```
        """
        models.DeletedDiscount.model_rebuild(_types_namespace=models._types_namespace)
        return await self._base_client.request(
            method="DELETE",
            path=f"/v1/subscriptions/{subscription_exposed_id}/discount",
            auth_names=["basicAuth", "bearerAuth"],
            cast_to=models.DeletedDiscount,
            request_options=request_options or default_request_options(),
        )
