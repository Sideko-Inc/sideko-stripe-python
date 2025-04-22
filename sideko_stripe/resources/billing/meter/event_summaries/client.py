import typing
import typing_extensions

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


class EventSummariesClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def list(
        self,
        *,
        customer: str,
        end_time: int,
        id: str,
        start_time: int,
        ending_before: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        limit: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        starting_after: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        value_grouping_window: typing.Union[
            typing.Optional[typing_extensions.Literal["day", "hour"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.BillingMeterEventSummariesListResponse:
        """
        List billing meter event summaries

        <p>Retrieve a list of billing meter event summaries.</p>

        GET /v1/billing/meters/{id}/event_summaries

        Args:
            ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            expand: Specifies which fields in the response should be expanded.
            limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
            value_grouping_window: Specifies what granularity to use when generating event summaries. If not specified, a single event summary would be returned for the specified time range. For hourly granularity, start and end times must align with hour boundaries (e.g., 00:00, 01:00, ..., 23:00). For daily granularity, start and end times must align with UTC day boundaries (00:00 UTC).
            customer: The customer for which to fetch event summaries.
            end_time: The timestamp from when to stop aggregating meter events (exclusive). Must be aligned with minute boundaries.
            id: Unique identifier for the object.
            start_time: The timestamp from when to start aggregating meter events (inclusive). Must be aligned with minute boundaries.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.billing.meter.event_summaries.list(
            customer="string", end_time=123, id="string", start_time=123
        )
        ```
        """
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
            "end_time",
            to_encodable(item=end_time, dump_with=int),
            style="form",
            explode=True,
        )
        encode_query_param(
            _query,
            "start_time",
            to_encodable(item=start_time, dump_with=int),
            style="form",
            explode=True,
        )
        if not isinstance(ending_before, type_utils.NotGiven):
            encode_query_param(
                _query,
                "ending_before",
                to_encodable(item=ending_before, dump_with=str),
                style="form",
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
        if not isinstance(limit, type_utils.NotGiven):
            encode_query_param(
                _query,
                "limit",
                to_encodable(item=limit, dump_with=int),
                style="form",
                explode=True,
            )
        if not isinstance(starting_after, type_utils.NotGiven):
            encode_query_param(
                _query,
                "starting_after",
                to_encodable(item=starting_after, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(value_grouping_window, type_utils.NotGiven):
            encode_query_param(
                _query,
                "value_grouping_window",
                to_encodable(
                    item=value_grouping_window,
                    dump_with=typing_extensions.Literal["day", "hour"],
                ),
                style="form",
                explode=True,
            )
        return self._base_client.request(
            method="GET",
            path=f"/v1/billing/meters/{id}/event_summaries",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.BillingMeterEventSummariesListResponse,
            request_options=request_options or default_request_options(),
        )


class AsyncEventSummariesClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def list(
        self,
        *,
        customer: str,
        end_time: int,
        id: str,
        start_time: int,
        ending_before: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        limit: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        starting_after: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        value_grouping_window: typing.Union[
            typing.Optional[typing_extensions.Literal["day", "hour"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.BillingMeterEventSummariesListResponse:
        """
        List billing meter event summaries

        <p>Retrieve a list of billing meter event summaries.</p>

        GET /v1/billing/meters/{id}/event_summaries

        Args:
            ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            expand: Specifies which fields in the response should be expanded.
            limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
            value_grouping_window: Specifies what granularity to use when generating event summaries. If not specified, a single event summary would be returned for the specified time range. For hourly granularity, start and end times must align with hour boundaries (e.g., 00:00, 01:00, ..., 23:00). For daily granularity, start and end times must align with UTC day boundaries (00:00 UTC).
            customer: The customer for which to fetch event summaries.
            end_time: The timestamp from when to stop aggregating meter events (exclusive). Must be aligned with minute boundaries.
            id: Unique identifier for the object.
            start_time: The timestamp from when to start aggregating meter events (inclusive). Must be aligned with minute boundaries.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.billing.meter.event_summaries.list(
            customer="string", end_time=123, id="string", start_time=123
        )
        ```
        """
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
            "end_time",
            to_encodable(item=end_time, dump_with=int),
            style="form",
            explode=True,
        )
        encode_query_param(
            _query,
            "start_time",
            to_encodable(item=start_time, dump_with=int),
            style="form",
            explode=True,
        )
        if not isinstance(ending_before, type_utils.NotGiven):
            encode_query_param(
                _query,
                "ending_before",
                to_encodable(item=ending_before, dump_with=str),
                style="form",
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
        if not isinstance(limit, type_utils.NotGiven):
            encode_query_param(
                _query,
                "limit",
                to_encodable(item=limit, dump_with=int),
                style="form",
                explode=True,
            )
        if not isinstance(starting_after, type_utils.NotGiven):
            encode_query_param(
                _query,
                "starting_after",
                to_encodable(item=starting_after, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(value_grouping_window, type_utils.NotGiven):
            encode_query_param(
                _query,
                "value_grouping_window",
                to_encodable(
                    item=value_grouping_window,
                    dump_with=typing_extensions.Literal["day", "hour"],
                ),
                style="form",
                explode=True,
            )
        return await self._base_client.request(
            method="GET",
            path=f"/v1/billing/meters/{id}/event_summaries",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.BillingMeterEventSummariesListResponse,
            request_options=request_options or default_request_options(),
        )
