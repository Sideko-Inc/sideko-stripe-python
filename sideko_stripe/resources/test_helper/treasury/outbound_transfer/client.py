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


class OutboundTransferClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def update(
        self,
        *,
        outbound_transfer: str,
        tracking_details: params.TestHelperTreasuryOutboundTransferUpdateBodyTrackingDetails,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TreasuryOutboundTransfer:
        """
        Test mode: Update an OutboundTransfer

        <p>Updates a test mode created OutboundTransfer with tracking details. The OutboundTransfer must not be cancelable, and cannot be in the <code>canceled</code> or <code>failed</code> states.</p>

        POST /v1/test_helpers/treasury/outbound_transfers/{outbound_transfer}

        Args:
            expand: Specifies which fields in the response should be expanded.
            outbound_transfer: str
            tracking_details: Details about network-specific tracking information.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.test_helper.treasury.outbound_transfer.update(
            outbound_transfer="string", tracking_details={"type_": "ach"}
        )
        ```
        """
        models.TreasuryOutboundTransfer.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _data = to_form_urlencoded(
            item={"expand": expand, "tracking_details": tracking_details},
            dump_with=params._SerializerTestHelperTreasuryOutboundTransferUpdateBody,
            style={"expand": "deepObject", "tracking_details": "deepObject"},
            explode={"expand": True, "tracking_details": True},
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/test_helpers/treasury/outbound_transfers/{outbound_transfer}",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.TreasuryOutboundTransfer,
            request_options=request_options or default_request_options(),
        )

    def fail(
        self,
        *,
        outbound_transfer: str,
        data: typing.Union[
            typing.Optional[params.TestHelperTreasuryOutboundTransferFailBody],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TreasuryOutboundTransfer:
        """
        Test mode: Fail an OutboundTransfer

        <p>Transitions a test mode created OutboundTransfer to the <code>failed</code> status. The OutboundTransfer must already be in the <code>processing</code> state.</p>

        POST /v1/test_helpers/treasury/outbound_transfers/{outbound_transfer}/fail

        Args:
            data: TestHelperTreasuryOutboundTransferFailBody
            outbound_transfer: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.test_helper.treasury.outbound_transfer.fail(outbound_transfer="string")
        ```
        """
        models.TreasuryOutboundTransfer.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerTestHelperTreasuryOutboundTransferFailBody,
                style={"expand": "deepObject"},
                explode={"expand": True},
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/test_helpers/treasury/outbound_transfers/{outbound_transfer}/fail",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.TreasuryOutboundTransfer,
            request_options=request_options or default_request_options(),
        )

    def post(
        self,
        *,
        outbound_transfer: str,
        data: typing.Union[
            typing.Optional[params.TestHelperTreasuryOutboundTransferPostBody],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TreasuryOutboundTransfer:
        """
        Test mode: Post an OutboundTransfer

        <p>Transitions a test mode created OutboundTransfer to the <code>posted</code> status. The OutboundTransfer must already be in the <code>processing</code> state.</p>

        POST /v1/test_helpers/treasury/outbound_transfers/{outbound_transfer}/post

        Args:
            data: TestHelperTreasuryOutboundTransferPostBody
            outbound_transfer: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.test_helper.treasury.outbound_transfer.post(outbound_transfer="string")
        ```
        """
        models.TreasuryOutboundTransfer.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerTestHelperTreasuryOutboundTransferPostBody,
                style={"expand": "deepObject"},
                explode={"expand": True},
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/test_helpers/treasury/outbound_transfers/{outbound_transfer}/post",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.TreasuryOutboundTransfer,
            request_options=request_options or default_request_options(),
        )

    def returned(
        self,
        *,
        outbound_transfer: str,
        data: typing.Union[
            typing.Optional[params.TestHelperTreasuryOutboundTransferReturnedBody],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TreasuryOutboundTransfer:
        """
        Test mode: Return an OutboundTransfer

        <p>Transitions a test mode created OutboundTransfer to the <code>returned</code> status. The OutboundTransfer must already be in the <code>processing</code> state.</p>

        POST /v1/test_helpers/treasury/outbound_transfers/{outbound_transfer}/return

        Args:
            data: TestHelperTreasuryOutboundTransferReturnedBody
            outbound_transfer: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.test_helper.treasury.outbound_transfer.returned(
            outbound_transfer="string"
        )
        ```
        """
        models.TreasuryOutboundTransfer.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerTestHelperTreasuryOutboundTransferReturnedBody,
                style={"expand": "deepObject", "returned_details": "deepObject"},
                explode={"expand": True, "returned_details": True},
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/test_helpers/treasury/outbound_transfers/{outbound_transfer}/return",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.TreasuryOutboundTransfer,
            request_options=request_options or default_request_options(),
        )


class AsyncOutboundTransferClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def update(
        self,
        *,
        outbound_transfer: str,
        tracking_details: params.TestHelperTreasuryOutboundTransferUpdateBodyTrackingDetails,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TreasuryOutboundTransfer:
        """
        Test mode: Update an OutboundTransfer

        <p>Updates a test mode created OutboundTransfer with tracking details. The OutboundTransfer must not be cancelable, and cannot be in the <code>canceled</code> or <code>failed</code> states.</p>

        POST /v1/test_helpers/treasury/outbound_transfers/{outbound_transfer}

        Args:
            expand: Specifies which fields in the response should be expanded.
            outbound_transfer: str
            tracking_details: Details about network-specific tracking information.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.test_helper.treasury.outbound_transfer.update(
            outbound_transfer="string", tracking_details={"type_": "ach"}
        )
        ```
        """
        models.TreasuryOutboundTransfer.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _data = to_form_urlencoded(
            item={"expand": expand, "tracking_details": tracking_details},
            dump_with=params._SerializerTestHelperTreasuryOutboundTransferUpdateBody,
            style={"expand": "deepObject", "tracking_details": "deepObject"},
            explode={"expand": True, "tracking_details": True},
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/test_helpers/treasury/outbound_transfers/{outbound_transfer}",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.TreasuryOutboundTransfer,
            request_options=request_options or default_request_options(),
        )

    async def fail(
        self,
        *,
        outbound_transfer: str,
        data: typing.Union[
            typing.Optional[params.TestHelperTreasuryOutboundTransferFailBody],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TreasuryOutboundTransfer:
        """
        Test mode: Fail an OutboundTransfer

        <p>Transitions a test mode created OutboundTransfer to the <code>failed</code> status. The OutboundTransfer must already be in the <code>processing</code> state.</p>

        POST /v1/test_helpers/treasury/outbound_transfers/{outbound_transfer}/fail

        Args:
            data: TestHelperTreasuryOutboundTransferFailBody
            outbound_transfer: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.test_helper.treasury.outbound_transfer.fail(
            outbound_transfer="string"
        )
        ```
        """
        models.TreasuryOutboundTransfer.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerTestHelperTreasuryOutboundTransferFailBody,
                style={"expand": "deepObject"},
                explode={"expand": True},
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/test_helpers/treasury/outbound_transfers/{outbound_transfer}/fail",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.TreasuryOutboundTransfer,
            request_options=request_options or default_request_options(),
        )

    async def post(
        self,
        *,
        outbound_transfer: str,
        data: typing.Union[
            typing.Optional[params.TestHelperTreasuryOutboundTransferPostBody],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TreasuryOutboundTransfer:
        """
        Test mode: Post an OutboundTransfer

        <p>Transitions a test mode created OutboundTransfer to the <code>posted</code> status. The OutboundTransfer must already be in the <code>processing</code> state.</p>

        POST /v1/test_helpers/treasury/outbound_transfers/{outbound_transfer}/post

        Args:
            data: TestHelperTreasuryOutboundTransferPostBody
            outbound_transfer: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.test_helper.treasury.outbound_transfer.post(
            outbound_transfer="string"
        )
        ```
        """
        models.TreasuryOutboundTransfer.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerTestHelperTreasuryOutboundTransferPostBody,
                style={"expand": "deepObject"},
                explode={"expand": True},
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/test_helpers/treasury/outbound_transfers/{outbound_transfer}/post",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.TreasuryOutboundTransfer,
            request_options=request_options or default_request_options(),
        )

    async def returned(
        self,
        *,
        outbound_transfer: str,
        data: typing.Union[
            typing.Optional[params.TestHelperTreasuryOutboundTransferReturnedBody],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TreasuryOutboundTransfer:
        """
        Test mode: Return an OutboundTransfer

        <p>Transitions a test mode created OutboundTransfer to the <code>returned</code> status. The OutboundTransfer must already be in the <code>processing</code> state.</p>

        POST /v1/test_helpers/treasury/outbound_transfers/{outbound_transfer}/return

        Args:
            data: TestHelperTreasuryOutboundTransferReturnedBody
            outbound_transfer: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.test_helper.treasury.outbound_transfer.returned(
            outbound_transfer="string"
        )
        ```
        """
        models.TreasuryOutboundTransfer.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerTestHelperTreasuryOutboundTransferReturnedBody,
                style={"expand": "deepObject", "returned_details": "deepObject"},
                explode={"expand": True, "returned_details": True},
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/test_helpers/treasury/outbound_transfers/{outbound_transfer}/return",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.TreasuryOutboundTransfer,
            request_options=request_options or default_request_options(),
        )
