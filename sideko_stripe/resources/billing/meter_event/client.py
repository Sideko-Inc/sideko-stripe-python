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


class MeterEventClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def create(
        self,
        *,
        event_name: str,
        payload: params.BillingMeterEventCreateBodyPayload,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        identifier: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        timestamp: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.BillingMeterEvent:
        """
        Create a billing meter event

        <p>Creates a billing meter event.</p>

        POST /v1/billing/meter_events

        Args:
            expand: Specifies which fields in the response should be expanded.
            identifier: A unique identifier for the event. If not provided, one is generated. We recommend using UUID-like identifiers. We will enforce uniqueness within a rolling period of at least 24 hours. The enforcement of uniqueness primarily addresses issues arising from accidental retries or other problems occurring within extremely brief time intervals. This approach helps prevent duplicate entries and ensures data integrity in high-frequency operations.
            timestamp: The time of the event. Measured in seconds since the Unix epoch. Must be within the past 35 calendar days or up to 5 minutes in the future. Defaults to current timestamp if not specified.
            event_name: The name of the meter event. Corresponds with the `event_name` field on a meter.
            payload: The payload of the event. This must contain the fields corresponding to a meter's `customer_mapping.event_payload_key` (default is `stripe_customer_id`) and `value_settings.event_payload_key` (default is `value`). Read more about the [payload](https://docs.stripe.com/billing/subscriptions/usage-based/recording-usage#payload-key-overrides).
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.billing.meter_event.create(event_name="string", payload={})
        ```
        """
        _data = to_form_urlencoded(
            item={
                "expand": expand,
                "identifier": identifier,
                "timestamp": timestamp,
                "event_name": event_name,
                "payload": payload,
            },
            dump_with=params._SerializerBillingMeterEventCreateBody,
            style={
                "event_name": "form",
                "expand": "deepObject",
                "identifier": "form",
                "payload": "deepObject",
                "timestamp": "form",
            },
            explode={
                "event_name": True,
                "expand": True,
                "identifier": True,
                "payload": True,
                "timestamp": True,
            },
        )
        return self._base_client.request(
            method="POST",
            path="/v1/billing/meter_events",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.BillingMeterEvent,
            request_options=request_options or default_request_options(),
        )


class AsyncMeterEventClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def create(
        self,
        *,
        event_name: str,
        payload: params.BillingMeterEventCreateBodyPayload,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        identifier: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        timestamp: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.BillingMeterEvent:
        """
        Create a billing meter event

        <p>Creates a billing meter event.</p>

        POST /v1/billing/meter_events

        Args:
            expand: Specifies which fields in the response should be expanded.
            identifier: A unique identifier for the event. If not provided, one is generated. We recommend using UUID-like identifiers. We will enforce uniqueness within a rolling period of at least 24 hours. The enforcement of uniqueness primarily addresses issues arising from accidental retries or other problems occurring within extremely brief time intervals. This approach helps prevent duplicate entries and ensures data integrity in high-frequency operations.
            timestamp: The time of the event. Measured in seconds since the Unix epoch. Must be within the past 35 calendar days or up to 5 minutes in the future. Defaults to current timestamp if not specified.
            event_name: The name of the meter event. Corresponds with the `event_name` field on a meter.
            payload: The payload of the event. This must contain the fields corresponding to a meter's `customer_mapping.event_payload_key` (default is `stripe_customer_id`) and `value_settings.event_payload_key` (default is `value`). Read more about the [payload](https://docs.stripe.com/billing/subscriptions/usage-based/recording-usage#payload-key-overrides).
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.billing.meter_event.create(event_name="string", payload={})
        ```
        """
        _data = to_form_urlencoded(
            item={
                "expand": expand,
                "identifier": identifier,
                "timestamp": timestamp,
                "event_name": event_name,
                "payload": payload,
            },
            dump_with=params._SerializerBillingMeterEventCreateBody,
            style={
                "event_name": "form",
                "expand": "deepObject",
                "identifier": "form",
                "payload": "deepObject",
                "timestamp": "form",
            },
            explode={
                "event_name": True,
                "expand": True,
                "identifier": True,
                "payload": True,
                "timestamp": True,
            },
        )
        return await self._base_client.request(
            method="POST",
            path="/v1/billing/meter_events",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.BillingMeterEvent,
            request_options=request_options or default_request_options(),
        )
