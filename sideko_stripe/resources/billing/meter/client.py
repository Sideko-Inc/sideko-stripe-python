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
    to_form_urlencoded,
    type_utils,
)
from sideko_stripe.resources.billing.meter.event_summaries import (
    AsyncEventSummariesClient,
    EventSummariesClient,
)
from sideko_stripe.types import models, params


class MeterClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        self.event_summaries = EventSummariesClient(base_client=self._base_client)

    def list(
        self,
        *,
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
        status: typing.Union[
            typing.Optional[typing_extensions.Literal["active", "inactive"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.BillingMeterListResponse:
        """
        List billing meters

        <p>Retrieve a list of billing meters.</p>

        GET /v1/billing/meters

        Args:
            ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            expand: Specifies which fields in the response should be expanded.
            limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
            status: Filter results to only include meters with the given status.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.billing.meter.list()
        ```
        """
        _query: QueryParams = {}
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
        if not isinstance(status, type_utils.NotGiven):
            encode_query_param(
                _query,
                "status",
                to_encodable(
                    item=status,
                    dump_with=typing_extensions.Literal["active", "inactive"],
                ),
                style="form",
                explode=True,
            )
        return self._base_client.request(
            method="GET",
            path="/v1/billing/meters",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.BillingMeterListResponse,
            request_options=request_options or default_request_options(),
        )

    def get(
        self,
        *,
        id: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.BillingMeter:
        """
        Retrieve a billing meter

        <p>Retrieves a billing meter given an ID.</p>

        GET /v1/billing/meters/{id}

        Args:
            expand: Specifies which fields in the response should be expanded.
            id: Unique identifier for the object.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.billing.meter.get(id="string")
        ```
        """
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
            path=f"/v1/billing/meters/{id}",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.BillingMeter,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        default_aggregation: params.BillingMeterCreateBodyDefaultAggregation,
        display_name: str,
        event_name: str,
        customer_mapping: typing.Union[
            typing.Optional[params.BillingMeterCreateBodyCustomerMapping],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        event_time_window: typing.Union[
            typing.Optional[typing_extensions.Literal["day", "hour"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        value_settings: typing.Union[
            typing.Optional[params.BillingMeterCreateBodyValueSettings],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.BillingMeter:
        """
        Create a billing meter

        <p>Creates a billing meter.</p>

        POST /v1/billing/meters

        Args:
            customer_mapping: Fields that specify how to map a meter event to a customer.
            event_time_window: The time window to pre-aggregate meter events for, if any.
            expand: Specifies which fields in the response should be expanded.
            value_settings: Fields that specify how to calculate a meter event's value.
            default_aggregation: The default settings to aggregate a meter's events with.
            display_name: The meter’s name. Not visible to the customer.
            event_name: The name of the meter event to record usage for. Corresponds with the `event_name` field on meter events.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.billing.meter.create(
            default_aggregation={"formula": "count"},
            display_name="string",
            event_name="string",
        )
        ```
        """
        _data = to_form_urlencoded(
            item={
                "customer_mapping": customer_mapping,
                "event_time_window": event_time_window,
                "expand": expand,
                "value_settings": value_settings,
                "default_aggregation": default_aggregation,
                "display_name": display_name,
                "event_name": event_name,
            },
            dump_with=params._SerializerBillingMeterCreateBody,
            style={
                "customer_mapping": "deepObject",
                "default_aggregation": "deepObject",
                "display_name": "form",
                "event_name": "form",
                "event_time_window": "form",
                "expand": "deepObject",
                "value_settings": "deepObject",
            },
            explode={
                "customer_mapping": True,
                "default_aggregation": True,
                "display_name": True,
                "event_name": True,
                "event_time_window": True,
                "expand": True,
                "value_settings": True,
            },
        )
        return self._base_client.request(
            method="POST",
            path="/v1/billing/meters",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.BillingMeter,
            request_options=request_options or default_request_options(),
        )

    def update(
        self,
        *,
        id: str,
        data: typing.Union[
            typing.Optional[params.BillingMeterUpdateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.BillingMeter:
        """
        Update a billing meter

        <p>Updates a billing meter.</p>

        POST /v1/billing/meters/{id}

        Args:
            data: BillingMeterUpdateBody
            id: Unique identifier for the object.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.billing.meter.update(id="string")
        ```
        """
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerBillingMeterUpdateBody,
                style={"display_name": "form", "expand": "deepObject"},
                explode={"display_name": True, "expand": True},
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/billing/meters/{id}",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.BillingMeter,
            request_options=request_options or default_request_options(),
        )

    def deactivate(
        self,
        *,
        id: str,
        data: typing.Union[
            typing.Optional[params.BillingMeterDeactivateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.BillingMeter:
        """
        Deactivate a billing meter

        <p>When a meter is deactivated, no more meter events will be accepted for this meter. You can’t attach a deactivated meter to a price.</p>

        POST /v1/billing/meters/{id}/deactivate

        Args:
            data: BillingMeterDeactivateBody
            id: Unique identifier for the object.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.billing.meter.deactivate(id="string")
        ```
        """
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerBillingMeterDeactivateBody,
                style={"expand": "deepObject"},
                explode={"expand": True},
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/billing/meters/{id}/deactivate",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.BillingMeter,
            request_options=request_options or default_request_options(),
        )

    def reactivate(
        self,
        *,
        id: str,
        data: typing.Union[
            typing.Optional[params.BillingMeterReactivateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.BillingMeter:
        """
        Reactivate a billing meter

        <p>When a meter is reactivated, events for this meter can be accepted and you can attach the meter to a price.</p>

        POST /v1/billing/meters/{id}/reactivate

        Args:
            data: BillingMeterReactivateBody
            id: Unique identifier for the object.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.billing.meter.reactivate(id="string")
        ```
        """
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerBillingMeterReactivateBody,
                style={"expand": "deepObject"},
                explode={"expand": True},
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/billing/meters/{id}/reactivate",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.BillingMeter,
            request_options=request_options or default_request_options(),
        )


class AsyncMeterClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        self.event_summaries = AsyncEventSummariesClient(base_client=self._base_client)

    async def list(
        self,
        *,
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
        status: typing.Union[
            typing.Optional[typing_extensions.Literal["active", "inactive"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.BillingMeterListResponse:
        """
        List billing meters

        <p>Retrieve a list of billing meters.</p>

        GET /v1/billing/meters

        Args:
            ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            expand: Specifies which fields in the response should be expanded.
            limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
            status: Filter results to only include meters with the given status.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.billing.meter.list()
        ```
        """
        _query: QueryParams = {}
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
        if not isinstance(status, type_utils.NotGiven):
            encode_query_param(
                _query,
                "status",
                to_encodable(
                    item=status,
                    dump_with=typing_extensions.Literal["active", "inactive"],
                ),
                style="form",
                explode=True,
            )
        return await self._base_client.request(
            method="GET",
            path="/v1/billing/meters",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.BillingMeterListResponse,
            request_options=request_options or default_request_options(),
        )

    async def get(
        self,
        *,
        id: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.BillingMeter:
        """
        Retrieve a billing meter

        <p>Retrieves a billing meter given an ID.</p>

        GET /v1/billing/meters/{id}

        Args:
            expand: Specifies which fields in the response should be expanded.
            id: Unique identifier for the object.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.billing.meter.get(id="string")
        ```
        """
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
            path=f"/v1/billing/meters/{id}",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.BillingMeter,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        default_aggregation: params.BillingMeterCreateBodyDefaultAggregation,
        display_name: str,
        event_name: str,
        customer_mapping: typing.Union[
            typing.Optional[params.BillingMeterCreateBodyCustomerMapping],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        event_time_window: typing.Union[
            typing.Optional[typing_extensions.Literal["day", "hour"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        value_settings: typing.Union[
            typing.Optional[params.BillingMeterCreateBodyValueSettings],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.BillingMeter:
        """
        Create a billing meter

        <p>Creates a billing meter.</p>

        POST /v1/billing/meters

        Args:
            customer_mapping: Fields that specify how to map a meter event to a customer.
            event_time_window: The time window to pre-aggregate meter events for, if any.
            expand: Specifies which fields in the response should be expanded.
            value_settings: Fields that specify how to calculate a meter event's value.
            default_aggregation: The default settings to aggregate a meter's events with.
            display_name: The meter’s name. Not visible to the customer.
            event_name: The name of the meter event to record usage for. Corresponds with the `event_name` field on meter events.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.billing.meter.create(
            default_aggregation={"formula": "count"},
            display_name="string",
            event_name="string",
        )
        ```
        """
        _data = to_form_urlencoded(
            item={
                "customer_mapping": customer_mapping,
                "event_time_window": event_time_window,
                "expand": expand,
                "value_settings": value_settings,
                "default_aggregation": default_aggregation,
                "display_name": display_name,
                "event_name": event_name,
            },
            dump_with=params._SerializerBillingMeterCreateBody,
            style={
                "customer_mapping": "deepObject",
                "default_aggregation": "deepObject",
                "display_name": "form",
                "event_name": "form",
                "event_time_window": "form",
                "expand": "deepObject",
                "value_settings": "deepObject",
            },
            explode={
                "customer_mapping": True,
                "default_aggregation": True,
                "display_name": True,
                "event_name": True,
                "event_time_window": True,
                "expand": True,
                "value_settings": True,
            },
        )
        return await self._base_client.request(
            method="POST",
            path="/v1/billing/meters",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.BillingMeter,
            request_options=request_options or default_request_options(),
        )

    async def update(
        self,
        *,
        id: str,
        data: typing.Union[
            typing.Optional[params.BillingMeterUpdateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.BillingMeter:
        """
        Update a billing meter

        <p>Updates a billing meter.</p>

        POST /v1/billing/meters/{id}

        Args:
            data: BillingMeterUpdateBody
            id: Unique identifier for the object.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.billing.meter.update(id="string")
        ```
        """
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerBillingMeterUpdateBody,
                style={"display_name": "form", "expand": "deepObject"},
                explode={"display_name": True, "expand": True},
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/billing/meters/{id}",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.BillingMeter,
            request_options=request_options or default_request_options(),
        )

    async def deactivate(
        self,
        *,
        id: str,
        data: typing.Union[
            typing.Optional[params.BillingMeterDeactivateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.BillingMeter:
        """
        Deactivate a billing meter

        <p>When a meter is deactivated, no more meter events will be accepted for this meter. You can’t attach a deactivated meter to a price.</p>

        POST /v1/billing/meters/{id}/deactivate

        Args:
            data: BillingMeterDeactivateBody
            id: Unique identifier for the object.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.billing.meter.deactivate(id="string")
        ```
        """
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerBillingMeterDeactivateBody,
                style={"expand": "deepObject"},
                explode={"expand": True},
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/billing/meters/{id}/deactivate",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.BillingMeter,
            request_options=request_options or default_request_options(),
        )

    async def reactivate(
        self,
        *,
        id: str,
        data: typing.Union[
            typing.Optional[params.BillingMeterReactivateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.BillingMeter:
        """
        Reactivate a billing meter

        <p>When a meter is reactivated, events for this meter can be accepted and you can attach the meter to a price.</p>

        POST /v1/billing/meters/{id}/reactivate

        Args:
            data: BillingMeterReactivateBody
            id: Unique identifier for the object.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.billing.meter.reactivate(id="string")
        ```
        """
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerBillingMeterReactivateBody,
                style={"expand": "deepObject"},
                explode={"expand": True},
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/billing/meters/{id}/reactivate",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.BillingMeter,
            request_options=request_options or default_request_options(),
        )
