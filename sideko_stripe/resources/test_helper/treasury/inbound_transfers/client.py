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


class InboundTransfersClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def fail(
        self,
        *,
        id: str,
        data: typing.Union[
            typing.Optional[params.TestHelperTreasuryInboundTransfersFailBody],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TreasuryInboundTransfer:
        """
        Test mode: Fail an InboundTransfer

        <p>Transitions a test mode created InboundTransfer to the <code>failed</code> status. The InboundTransfer must already be in the <code>processing</code> state.</p>

        POST /v1/test_helpers/treasury/inbound_transfers/{id}/fail

        Args:
            data: TestHelperTreasuryInboundTransfersFailBody
            id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.test_helper.treasury.inbound_transfers.fail(id="string")
        ```
        """
        models.TreasuryInboundTransfer.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerTestHelperTreasuryInboundTransfersFailBody,
                style={"expand": "deepObject", "failure_details": "deepObject"},
                explode={"expand": True, "failure_details": True},
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/test_helpers/treasury/inbound_transfers/{id}/fail",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.TreasuryInboundTransfer,
            request_options=request_options or default_request_options(),
        )

    def returned(
        self,
        *,
        id: str,
        data: typing.Union[
            typing.Optional[params.TestHelperTreasuryInboundTransfersReturnedBody],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TreasuryInboundTransfer:
        """
        Test mode: Return an InboundTransfer

        <p>Marks the test mode InboundTransfer object as returned and links the InboundTransfer to a ReceivedDebit. The InboundTransfer must already be in the <code>succeeded</code> state.</p>

        POST /v1/test_helpers/treasury/inbound_transfers/{id}/return

        Args:
            data: TestHelperTreasuryInboundTransfersReturnedBody
            id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.test_helper.treasury.inbound_transfers.returned(id="string")
        ```
        """
        models.TreasuryInboundTransfer.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerTestHelperTreasuryInboundTransfersReturnedBody,
                style={"expand": "deepObject"},
                explode={"expand": True},
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/test_helpers/treasury/inbound_transfers/{id}/return",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.TreasuryInboundTransfer,
            request_options=request_options or default_request_options(),
        )

    def succeed(
        self,
        *,
        id: str,
        data: typing.Union[
            typing.Optional[params.TestHelperTreasuryInboundTransfersSucceedBody],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TreasuryInboundTransfer:
        """
        Test mode: Succeed an InboundTransfer

        <p>Transitions a test mode created InboundTransfer to the <code>succeeded</code> status. The InboundTransfer must already be in the <code>processing</code> state.</p>

        POST /v1/test_helpers/treasury/inbound_transfers/{id}/succeed

        Args:
            data: TestHelperTreasuryInboundTransfersSucceedBody
            id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.test_helper.treasury.inbound_transfers.succeed(id="string")
        ```
        """
        models.TreasuryInboundTransfer.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerTestHelperTreasuryInboundTransfersSucceedBody,
                style={"expand": "deepObject"},
                explode={"expand": True},
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/test_helpers/treasury/inbound_transfers/{id}/succeed",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.TreasuryInboundTransfer,
            request_options=request_options or default_request_options(),
        )


class AsyncInboundTransfersClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def fail(
        self,
        *,
        id: str,
        data: typing.Union[
            typing.Optional[params.TestHelperTreasuryInboundTransfersFailBody],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TreasuryInboundTransfer:
        """
        Test mode: Fail an InboundTransfer

        <p>Transitions a test mode created InboundTransfer to the <code>failed</code> status. The InboundTransfer must already be in the <code>processing</code> state.</p>

        POST /v1/test_helpers/treasury/inbound_transfers/{id}/fail

        Args:
            data: TestHelperTreasuryInboundTransfersFailBody
            id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.test_helper.treasury.inbound_transfers.fail(id="string")
        ```
        """
        models.TreasuryInboundTransfer.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerTestHelperTreasuryInboundTransfersFailBody,
                style={"expand": "deepObject", "failure_details": "deepObject"},
                explode={"expand": True, "failure_details": True},
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/test_helpers/treasury/inbound_transfers/{id}/fail",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.TreasuryInboundTransfer,
            request_options=request_options or default_request_options(),
        )

    async def returned(
        self,
        *,
        id: str,
        data: typing.Union[
            typing.Optional[params.TestHelperTreasuryInboundTransfersReturnedBody],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TreasuryInboundTransfer:
        """
        Test mode: Return an InboundTransfer

        <p>Marks the test mode InboundTransfer object as returned and links the InboundTransfer to a ReceivedDebit. The InboundTransfer must already be in the <code>succeeded</code> state.</p>

        POST /v1/test_helpers/treasury/inbound_transfers/{id}/return

        Args:
            data: TestHelperTreasuryInboundTransfersReturnedBody
            id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.test_helper.treasury.inbound_transfers.returned(id="string")
        ```
        """
        models.TreasuryInboundTransfer.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerTestHelperTreasuryInboundTransfersReturnedBody,
                style={"expand": "deepObject"},
                explode={"expand": True},
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/test_helpers/treasury/inbound_transfers/{id}/return",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.TreasuryInboundTransfer,
            request_options=request_options or default_request_options(),
        )

    async def succeed(
        self,
        *,
        id: str,
        data: typing.Union[
            typing.Optional[params.TestHelperTreasuryInboundTransfersSucceedBody],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TreasuryInboundTransfer:
        """
        Test mode: Succeed an InboundTransfer

        <p>Transitions a test mode created InboundTransfer to the <code>succeeded</code> status. The InboundTransfer must already be in the <code>processing</code> state.</p>

        POST /v1/test_helpers/treasury/inbound_transfers/{id}/succeed

        Args:
            data: TestHelperTreasuryInboundTransfersSucceedBody
            id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.test_helper.treasury.inbound_transfers.succeed(id="string")
        ```
        """
        models.TreasuryInboundTransfer.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerTestHelperTreasuryInboundTransfersSucceedBody,
                style={"expand": "deepObject"},
                explode={"expand": True},
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/test_helpers/treasury/inbound_transfers/{id}/succeed",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.TreasuryInboundTransfer,
            request_options=request_options or default_request_options(),
        )
