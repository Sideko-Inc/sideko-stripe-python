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


class ShippingClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def deliver(
        self,
        *,
        card: str,
        data: typing.Union[
            typing.Optional[params.TestHelperIssuingCardShippingDeliverBody],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.IssuingCard:
        """
        Deliver a testmode card

        <p>Updates the shipping status of the specified Issuing <code>Card</code> object to <code>delivered</code>.</p>

        POST /v1/test_helpers/issuing/cards/{card}/shipping/deliver

        Args:
            data: TestHelperIssuingCardShippingDeliverBody
            card: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.test_helper.issuing.card.shipping.deliver(card="string")
        ```
        """
        models.IssuingCard.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerTestHelperIssuingCardShippingDeliverBody,
                style={"expand": "deepObject"},
                explode={"expand": True},
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/test_helpers/issuing/cards/{card}/shipping/deliver",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.IssuingCard,
            request_options=request_options or default_request_options(),
        )

    def fail(
        self,
        *,
        card: str,
        data: typing.Union[
            typing.Optional[params.TestHelperIssuingCardShippingFailBody],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.IssuingCard:
        """
        Fail a testmode card

        <p>Updates the shipping status of the specified Issuing <code>Card</code> object to <code>failure</code>.</p>

        POST /v1/test_helpers/issuing/cards/{card}/shipping/fail

        Args:
            data: TestHelperIssuingCardShippingFailBody
            card: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.test_helper.issuing.card.shipping.fail(card="string")
        ```
        """
        models.IssuingCard.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerTestHelperIssuingCardShippingFailBody,
                style={"expand": "deepObject"},
                explode={"expand": True},
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/test_helpers/issuing/cards/{card}/shipping/fail",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.IssuingCard,
            request_options=request_options or default_request_options(),
        )

    def returned(
        self,
        *,
        card: str,
        data: typing.Union[
            typing.Optional[params.TestHelperIssuingCardShippingReturnedBody],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.IssuingCard:
        """
        Return a testmode card

        <p>Updates the shipping status of the specified Issuing <code>Card</code> object to <code>returned</code>.</p>

        POST /v1/test_helpers/issuing/cards/{card}/shipping/return

        Args:
            data: TestHelperIssuingCardShippingReturnedBody
            card: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.test_helper.issuing.card.shipping.returned(card="string")
        ```
        """
        models.IssuingCard.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerTestHelperIssuingCardShippingReturnedBody,
                style={"expand": "deepObject"},
                explode={"expand": True},
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/test_helpers/issuing/cards/{card}/shipping/return",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.IssuingCard,
            request_options=request_options or default_request_options(),
        )

    def ship(
        self,
        *,
        card: str,
        data: typing.Union[
            typing.Optional[params.TestHelperIssuingCardShippingShipBody],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.IssuingCard:
        """
        Ship a testmode card

        <p>Updates the shipping status of the specified Issuing <code>Card</code> object to <code>shipped</code>.</p>

        POST /v1/test_helpers/issuing/cards/{card}/shipping/ship

        Args:
            data: TestHelperIssuingCardShippingShipBody
            card: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.test_helper.issuing.card.shipping.ship(card="string")
        ```
        """
        models.IssuingCard.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerTestHelperIssuingCardShippingShipBody,
                style={"expand": "deepObject"},
                explode={"expand": True},
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/test_helpers/issuing/cards/{card}/shipping/ship",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.IssuingCard,
            request_options=request_options or default_request_options(),
        )

    def submit(
        self,
        *,
        card: str,
        data: typing.Union[
            typing.Optional[params.TestHelperIssuingCardShippingSubmitBody],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.IssuingCard:
        """
        Submit a testmode card

        <p>Updates the shipping status of the specified Issuing <code>Card</code> object to <code>submitted</code>. This method requires Stripe Version ‘2024-09-30.acacia’ or later.</p>

        POST /v1/test_helpers/issuing/cards/{card}/shipping/submit

        Args:
            data: TestHelperIssuingCardShippingSubmitBody
            card: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.test_helper.issuing.card.shipping.submit(card="string")
        ```
        """
        models.IssuingCard.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerTestHelperIssuingCardShippingSubmitBody,
                style={"expand": "deepObject"},
                explode={"expand": True},
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/test_helpers/issuing/cards/{card}/shipping/submit",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.IssuingCard,
            request_options=request_options or default_request_options(),
        )


class AsyncShippingClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def deliver(
        self,
        *,
        card: str,
        data: typing.Union[
            typing.Optional[params.TestHelperIssuingCardShippingDeliverBody],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.IssuingCard:
        """
        Deliver a testmode card

        <p>Updates the shipping status of the specified Issuing <code>Card</code> object to <code>delivered</code>.</p>

        POST /v1/test_helpers/issuing/cards/{card}/shipping/deliver

        Args:
            data: TestHelperIssuingCardShippingDeliverBody
            card: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.test_helper.issuing.card.shipping.deliver(card="string")
        ```
        """
        models.IssuingCard.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerTestHelperIssuingCardShippingDeliverBody,
                style={"expand": "deepObject"},
                explode={"expand": True},
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/test_helpers/issuing/cards/{card}/shipping/deliver",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.IssuingCard,
            request_options=request_options or default_request_options(),
        )

    async def fail(
        self,
        *,
        card: str,
        data: typing.Union[
            typing.Optional[params.TestHelperIssuingCardShippingFailBody],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.IssuingCard:
        """
        Fail a testmode card

        <p>Updates the shipping status of the specified Issuing <code>Card</code> object to <code>failure</code>.</p>

        POST /v1/test_helpers/issuing/cards/{card}/shipping/fail

        Args:
            data: TestHelperIssuingCardShippingFailBody
            card: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.test_helper.issuing.card.shipping.fail(card="string")
        ```
        """
        models.IssuingCard.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerTestHelperIssuingCardShippingFailBody,
                style={"expand": "deepObject"},
                explode={"expand": True},
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/test_helpers/issuing/cards/{card}/shipping/fail",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.IssuingCard,
            request_options=request_options or default_request_options(),
        )

    async def returned(
        self,
        *,
        card: str,
        data: typing.Union[
            typing.Optional[params.TestHelperIssuingCardShippingReturnedBody],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.IssuingCard:
        """
        Return a testmode card

        <p>Updates the shipping status of the specified Issuing <code>Card</code> object to <code>returned</code>.</p>

        POST /v1/test_helpers/issuing/cards/{card}/shipping/return

        Args:
            data: TestHelperIssuingCardShippingReturnedBody
            card: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.test_helper.issuing.card.shipping.returned(card="string")
        ```
        """
        models.IssuingCard.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerTestHelperIssuingCardShippingReturnedBody,
                style={"expand": "deepObject"},
                explode={"expand": True},
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/test_helpers/issuing/cards/{card}/shipping/return",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.IssuingCard,
            request_options=request_options or default_request_options(),
        )

    async def ship(
        self,
        *,
        card: str,
        data: typing.Union[
            typing.Optional[params.TestHelperIssuingCardShippingShipBody],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.IssuingCard:
        """
        Ship a testmode card

        <p>Updates the shipping status of the specified Issuing <code>Card</code> object to <code>shipped</code>.</p>

        POST /v1/test_helpers/issuing/cards/{card}/shipping/ship

        Args:
            data: TestHelperIssuingCardShippingShipBody
            card: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.test_helper.issuing.card.shipping.ship(card="string")
        ```
        """
        models.IssuingCard.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerTestHelperIssuingCardShippingShipBody,
                style={"expand": "deepObject"},
                explode={"expand": True},
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/test_helpers/issuing/cards/{card}/shipping/ship",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.IssuingCard,
            request_options=request_options or default_request_options(),
        )

    async def submit(
        self,
        *,
        card: str,
        data: typing.Union[
            typing.Optional[params.TestHelperIssuingCardShippingSubmitBody],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.IssuingCard:
        """
        Submit a testmode card

        <p>Updates the shipping status of the specified Issuing <code>Card</code> object to <code>submitted</code>. This method requires Stripe Version ‘2024-09-30.acacia’ or later.</p>

        POST /v1/test_helpers/issuing/cards/{card}/shipping/submit

        Args:
            data: TestHelperIssuingCardShippingSubmitBody
            card: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.test_helper.issuing.card.shipping.submit(card="string")
        ```
        """
        models.IssuingCard.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerTestHelperIssuingCardShippingSubmitBody,
                style={"expand": "deepObject"},
                explode={"expand": True},
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/test_helpers/issuing/cards/{card}/shipping/submit",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.IssuingCard,
            request_options=request_options or default_request_options(),
        )
