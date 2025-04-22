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


class OutboundPaymentClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def update(
        self,
        *,
        id: str,
        tracking_details: params.TestHelperTreasuryOutboundPaymentUpdateBodyTrackingDetails,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TreasuryOutboundPayment:
        """
        Test mode: Update an OutboundPayment

        <p>Updates a test mode created OutboundPayment with tracking details. The OutboundPayment must not be cancelable, and cannot be in the <code>canceled</code> or <code>failed</code> states.</p>

        POST /v1/test_helpers/treasury/outbound_payments/{id}

        Args:
            expand: Specifies which fields in the response should be expanded.
            id: str
            tracking_details: Details about network-specific tracking information.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.test_helper.treasury.outbound_payment.update(
            id="string", tracking_details={"type_": "ach"}
        )
        ```
        """
        models.TreasuryOutboundPayment.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _data = to_form_urlencoded(
            item={"expand": expand, "tracking_details": tracking_details},
            dump_with=params._SerializerTestHelperTreasuryOutboundPaymentUpdateBody,
            style={"expand": "deepObject", "tracking_details": "deepObject"},
            explode={"expand": True, "tracking_details": True},
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/test_helpers/treasury/outbound_payments/{id}",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.TreasuryOutboundPayment,
            request_options=request_options or default_request_options(),
        )

    def fail(
        self,
        *,
        id: str,
        data: typing.Union[
            typing.Optional[params.TestHelperTreasuryOutboundPaymentFailBody],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TreasuryOutboundPayment:
        """
        Test mode: Fail an OutboundPayment

        <p>Transitions a test mode created OutboundPayment to the <code>failed</code> status. The OutboundPayment must already be in the <code>processing</code> state.</p>

        POST /v1/test_helpers/treasury/outbound_payments/{id}/fail

        Args:
            data: TestHelperTreasuryOutboundPaymentFailBody
            id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.test_helper.treasury.outbound_payment.fail(id="string")
        ```
        """
        models.TreasuryOutboundPayment.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerTestHelperTreasuryOutboundPaymentFailBody,
                style={"expand": "deepObject"},
                explode={"expand": True},
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/test_helpers/treasury/outbound_payments/{id}/fail",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.TreasuryOutboundPayment,
            request_options=request_options or default_request_options(),
        )

    def post(
        self,
        *,
        id: str,
        data: typing.Union[
            typing.Optional[params.TestHelperTreasuryOutboundPaymentPostBody],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TreasuryOutboundPayment:
        """
        Test mode: Post an OutboundPayment

        <p>Transitions a test mode created OutboundPayment to the <code>posted</code> status. The OutboundPayment must already be in the <code>processing</code> state.</p>

        POST /v1/test_helpers/treasury/outbound_payments/{id}/post

        Args:
            data: TestHelperTreasuryOutboundPaymentPostBody
            id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.test_helper.treasury.outbound_payment.post(id="string")
        ```
        """
        models.TreasuryOutboundPayment.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerTestHelperTreasuryOutboundPaymentPostBody,
                style={"expand": "deepObject"},
                explode={"expand": True},
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/test_helpers/treasury/outbound_payments/{id}/post",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.TreasuryOutboundPayment,
            request_options=request_options or default_request_options(),
        )

    def returned(
        self,
        *,
        id: str,
        data: typing.Union[
            typing.Optional[params.TestHelperTreasuryOutboundPaymentReturnedBody],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TreasuryOutboundPayment:
        """
        Test mode: Return an OutboundPayment

        <p>Transitions a test mode created OutboundPayment to the <code>returned</code> status. The OutboundPayment must already be in the <code>processing</code> state.</p>

        POST /v1/test_helpers/treasury/outbound_payments/{id}/return

        Args:
            data: TestHelperTreasuryOutboundPaymentReturnedBody
            id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.test_helper.treasury.outbound_payment.returned(id="string")
        ```
        """
        models.TreasuryOutboundPayment.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerTestHelperTreasuryOutboundPaymentReturnedBody,
                style={"expand": "deepObject", "returned_details": "deepObject"},
                explode={"expand": True, "returned_details": True},
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/test_helpers/treasury/outbound_payments/{id}/return",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.TreasuryOutboundPayment,
            request_options=request_options or default_request_options(),
        )


class AsyncOutboundPaymentClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def update(
        self,
        *,
        id: str,
        tracking_details: params.TestHelperTreasuryOutboundPaymentUpdateBodyTrackingDetails,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TreasuryOutboundPayment:
        """
        Test mode: Update an OutboundPayment

        <p>Updates a test mode created OutboundPayment with tracking details. The OutboundPayment must not be cancelable, and cannot be in the <code>canceled</code> or <code>failed</code> states.</p>

        POST /v1/test_helpers/treasury/outbound_payments/{id}

        Args:
            expand: Specifies which fields in the response should be expanded.
            id: str
            tracking_details: Details about network-specific tracking information.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.test_helper.treasury.outbound_payment.update(
            id="string", tracking_details={"type_": "ach"}
        )
        ```
        """
        models.TreasuryOutboundPayment.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _data = to_form_urlencoded(
            item={"expand": expand, "tracking_details": tracking_details},
            dump_with=params._SerializerTestHelperTreasuryOutboundPaymentUpdateBody,
            style={"expand": "deepObject", "tracking_details": "deepObject"},
            explode={"expand": True, "tracking_details": True},
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/test_helpers/treasury/outbound_payments/{id}",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.TreasuryOutboundPayment,
            request_options=request_options or default_request_options(),
        )

    async def fail(
        self,
        *,
        id: str,
        data: typing.Union[
            typing.Optional[params.TestHelperTreasuryOutboundPaymentFailBody],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TreasuryOutboundPayment:
        """
        Test mode: Fail an OutboundPayment

        <p>Transitions a test mode created OutboundPayment to the <code>failed</code> status. The OutboundPayment must already be in the <code>processing</code> state.</p>

        POST /v1/test_helpers/treasury/outbound_payments/{id}/fail

        Args:
            data: TestHelperTreasuryOutboundPaymentFailBody
            id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.test_helper.treasury.outbound_payment.fail(id="string")
        ```
        """
        models.TreasuryOutboundPayment.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerTestHelperTreasuryOutboundPaymentFailBody,
                style={"expand": "deepObject"},
                explode={"expand": True},
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/test_helpers/treasury/outbound_payments/{id}/fail",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.TreasuryOutboundPayment,
            request_options=request_options or default_request_options(),
        )

    async def post(
        self,
        *,
        id: str,
        data: typing.Union[
            typing.Optional[params.TestHelperTreasuryOutboundPaymentPostBody],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TreasuryOutboundPayment:
        """
        Test mode: Post an OutboundPayment

        <p>Transitions a test mode created OutboundPayment to the <code>posted</code> status. The OutboundPayment must already be in the <code>processing</code> state.</p>

        POST /v1/test_helpers/treasury/outbound_payments/{id}/post

        Args:
            data: TestHelperTreasuryOutboundPaymentPostBody
            id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.test_helper.treasury.outbound_payment.post(id="string")
        ```
        """
        models.TreasuryOutboundPayment.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerTestHelperTreasuryOutboundPaymentPostBody,
                style={"expand": "deepObject"},
                explode={"expand": True},
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/test_helpers/treasury/outbound_payments/{id}/post",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.TreasuryOutboundPayment,
            request_options=request_options or default_request_options(),
        )

    async def returned(
        self,
        *,
        id: str,
        data: typing.Union[
            typing.Optional[params.TestHelperTreasuryOutboundPaymentReturnedBody],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TreasuryOutboundPayment:
        """
        Test mode: Return an OutboundPayment

        <p>Transitions a test mode created OutboundPayment to the <code>returned</code> status. The OutboundPayment must already be in the <code>processing</code> state.</p>

        POST /v1/test_helpers/treasury/outbound_payments/{id}/return

        Args:
            data: TestHelperTreasuryOutboundPaymentReturnedBody
            id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.test_helper.treasury.outbound_payment.returned(id="string")
        ```
        """
        models.TreasuryOutboundPayment.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerTestHelperTreasuryOutboundPaymentReturnedBody,
                style={"expand": "deepObject", "returned_details": "deepObject"},
                explode={"expand": True, "returned_details": True},
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/test_helpers/treasury/outbound_payments/{id}/return",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.TreasuryOutboundPayment,
            request_options=request_options or default_request_options(),
        )
