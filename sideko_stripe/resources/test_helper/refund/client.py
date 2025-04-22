import typing

from sideko_stripe.core import (
    AsyncBaseClient,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
    to_form_urlencoded,
    type_utils,
)
from sideko_stripe.types import models, params


class RefundClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def expire(
        self,
        *,
        refund: str,
        data: typing.Union[
            typing.Optional[params.TestHelperRefundExpireBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Refund:
        """
        Expire a pending refund.

        <p>Expire a refund with a status of <code>requires_action</code>.</p>

        POST /v1/test_helpers/refunds/{refund}/expire

        Args:
            data: TestHelperRefundExpireBody
            refund: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.test_helper.refund.expire(refund="string")
        ```
        """
        models.Refund.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerTestHelperRefundExpireBody,
                style={"expand": "deepObject"},
                explode={"expand": True},
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/test_helpers/refunds/{refund}/expire",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.Refund,
            request_options=request_options or default_request_options(),
        )


class AsyncRefundClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def expire(
        self,
        *,
        refund: str,
        data: typing.Union[
            typing.Optional[params.TestHelperRefundExpireBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Refund:
        """
        Expire a pending refund.

        <p>Expire a refund with a status of <code>requires_action</code>.</p>

        POST /v1/test_helpers/refunds/{refund}/expire

        Args:
            data: TestHelperRefundExpireBody
            refund: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.test_helper.refund.expire(refund="string")
        ```
        """
        models.Refund.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerTestHelperRefundExpireBody,
                style={"expand": "deepObject"},
                explode={"expand": True},
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/test_helpers/refunds/{refund}/expire",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.Refund,
            request_options=request_options or default_request_options(),
        )
