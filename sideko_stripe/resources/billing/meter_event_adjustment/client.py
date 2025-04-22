import typing
import typing_extensions

from sideko_stripe.core import (
    AsyncBaseClient,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
    to_form_urlencoded,
    type_utils,
)
from sideko_stripe.types import models, params


class MeterEventAdjustmentClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def create(
        self,
        *,
        event_name: str,
        type_: typing_extensions.Literal["cancel"],
        cancel: typing.Union[
            typing.Optional[params.BillingMeterEventAdjustmentCreateBodyCancel],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.BillingMeterEventAdjustment:
        """
        Create a billing meter event adjustment

        <p>Creates a billing meter event adjustment.</p>

        POST /v1/billing/meter_event_adjustments

        Args:
            cancel: Specifies which event to cancel.
            expand: Specifies which fields in the response should be expanded.
            event_name: The name of the meter event. Corresponds with the `event_name` field on a meter.
            type: Specifies whether to cancel a single event or a range of events for a time period. Time period cancellation is not supported yet.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.billing.meter_event_adjustment.create(
            event_name="string", type_="cancel"
        )
        ```
        """
        _data = to_form_urlencoded(
            item={
                "cancel": cancel,
                "expand": expand,
                "event_name": event_name,
                "type_": type_,
            },
            dump_with=params._SerializerBillingMeterEventAdjustmentCreateBody,
            style={
                "cancel": "deepObject",
                "event_name": "form",
                "expand": "deepObject",
                "type": "form",
            },
            explode={"cancel": True, "event_name": True, "expand": True, "type": True},
        )
        return self._base_client.request(
            method="POST",
            path="/v1/billing/meter_event_adjustments",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.BillingMeterEventAdjustment,
            request_options=request_options or default_request_options(),
        )


class AsyncMeterEventAdjustmentClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def create(
        self,
        *,
        event_name: str,
        type_: typing_extensions.Literal["cancel"],
        cancel: typing.Union[
            typing.Optional[params.BillingMeterEventAdjustmentCreateBodyCancel],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.BillingMeterEventAdjustment:
        """
        Create a billing meter event adjustment

        <p>Creates a billing meter event adjustment.</p>

        POST /v1/billing/meter_event_adjustments

        Args:
            cancel: Specifies which event to cancel.
            expand: Specifies which fields in the response should be expanded.
            event_name: The name of the meter event. Corresponds with the `event_name` field on a meter.
            type: Specifies whether to cancel a single event or a range of events for a time period. Time period cancellation is not supported yet.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.billing.meter_event_adjustment.create(
            event_name="string", type_="cancel"
        )
        ```
        """
        _data = to_form_urlencoded(
            item={
                "cancel": cancel,
                "expand": expand,
                "event_name": event_name,
                "type_": type_,
            },
            dump_with=params._SerializerBillingMeterEventAdjustmentCreateBody,
            style={
                "cancel": "deepObject",
                "event_name": "form",
                "expand": "deepObject",
                "type": "form",
            },
            explode={"cancel": True, "event_name": True, "expand": True, "type": True},
        )
        return await self._base_client.request(
            method="POST",
            path="/v1/billing/meter_event_adjustments",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.BillingMeterEventAdjustment,
            request_options=request_options or default_request_options(),
        )
