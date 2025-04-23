import typing

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
from sideko_stripe.types import models, params


class SubscriptionScheduleClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def list(
        self,
        *,
        canceled_at: typing.Union[
            typing.Optional[
                typing.Union[params.SubscriptionScheduleListCanceledAtObj0, int]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        completed_at: typing.Union[
            typing.Optional[
                typing.Union[params.SubscriptionScheduleListCompletedAtObj0, int]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        created: typing.Union[
            typing.Optional[
                typing.Union[params.SubscriptionScheduleListCreatedObj0, int]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        customer: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        ending_before: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        limit: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        released_at: typing.Union[
            typing.Optional[
                typing.Union[params.SubscriptionScheduleListReleasedAtObj0, int]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        scheduled: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        starting_after: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.SubscriptionScheduleListResponse:
        """
        List all schedules

        <p>Retrieves the list of your subscription schedules.</p>

        GET /v1/subscription_schedules

        Args:
            canceled_at: Only return subscription schedules that were created canceled the given date interval.
            completed_at: Only return subscription schedules that completed during the given date interval.
            created: Only return subscription schedules that were created during the given date interval.
            customer: Only return subscription schedules for the given customer.
            ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            expand: Specifies which fields in the response should be expanded.
            limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            released_at: Only return subscription schedules that were released during the given date interval.
            scheduled: Only return subscription schedules that have not started yet.
            starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.subscription_schedule.list()
        ```
        """
        models.SubscriptionScheduleListResponse.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _query: QueryParams = {}
        if not isinstance(canceled_at, type_utils.NotGiven):
            encode_query_param(
                _query,
                "canceled_at",
                to_encodable(
                    item=canceled_at,
                    dump_with=typing.Union[
                        params._SerializerSubscriptionScheduleListCanceledAtObj0, int
                    ],
                ),
                style="deepObject",
                explode=True,
            )
        if not isinstance(completed_at, type_utils.NotGiven):
            encode_query_param(
                _query,
                "completed_at",
                to_encodable(
                    item=completed_at,
                    dump_with=typing.Union[
                        params._SerializerSubscriptionScheduleListCompletedAtObj0, int
                    ],
                ),
                style="deepObject",
                explode=True,
            )
        if not isinstance(created, type_utils.NotGiven):
            encode_query_param(
                _query,
                "created",
                to_encodable(
                    item=created,
                    dump_with=typing.Union[
                        params._SerializerSubscriptionScheduleListCreatedObj0, int
                    ],
                ),
                style="deepObject",
                explode=True,
            )
        if not isinstance(customer, type_utils.NotGiven):
            encode_query_param(
                _query,
                "customer",
                to_encodable(item=customer, dump_with=str),
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
        if not isinstance(released_at, type_utils.NotGiven):
            encode_query_param(
                _query,
                "released_at",
                to_encodable(
                    item=released_at,
                    dump_with=typing.Union[
                        params._SerializerSubscriptionScheduleListReleasedAtObj0, int
                    ],
                ),
                style="deepObject",
                explode=True,
            )
        if not isinstance(scheduled, type_utils.NotGiven):
            encode_query_param(
                _query,
                "scheduled",
                to_encodable(item=scheduled, dump_with=bool),
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
        return self._base_client.request(
            method="GET",
            path="/v1/subscription_schedules",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.SubscriptionScheduleListResponse,
            request_options=request_options or default_request_options(),
        )

    def get(
        self,
        *,
        schedule: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.SubscriptionSchedule1:
        """
        Retrieve a schedule

        <p>Retrieves the details of an existing subscription schedule. You only need to supply the unique subscription schedule identifier that was returned upon subscription schedule creation.</p>

        GET /v1/subscription_schedules/{schedule}

        Args:
            expand: Specifies which fields in the response should be expanded.
            schedule: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.subscription_schedule.get(schedule="string")
        ```
        """
        models.SubscriptionSchedule1.model_rebuild(
            _types_namespace=models._types_namespace
        )
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
            path=f"/v1/subscription_schedules/{schedule}",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.SubscriptionSchedule1,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        data: typing.Union[
            typing.Optional[params.SubscriptionScheduleCreateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.SubscriptionSchedule1:
        """
        Create a schedule

        <p>Creates a new subscription schedule object. Each customer can have up to 500 active or scheduled subscriptions.</p>

        POST /v1/subscription_schedules

        Args:
            data: SubscriptionScheduleCreateBody
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.subscription_schedule.create()
        ```
        """
        models.SubscriptionSchedule1.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerSubscriptionScheduleCreateBody,
                style={
                    "customer": "form",
                    "default_settings": "deepObject",
                    "end_behavior": "form",
                    "expand": "deepObject",
                    "from_subscription": "form",
                    "metadata": "deepObject",
                    "phases": "deepObject",
                    "start_date": "deepObject",
                },
                explode={
                    "customer": True,
                    "default_settings": True,
                    "end_behavior": True,
                    "expand": True,
                    "from_subscription": True,
                    "metadata": True,
                    "phases": True,
                    "start_date": True,
                },
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path="/v1/subscription_schedules",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.SubscriptionSchedule1,
            request_options=request_options or default_request_options(),
        )

    def update(
        self,
        *,
        schedule: str,
        data: typing.Union[
            typing.Optional[params.SubscriptionScheduleUpdateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.SubscriptionSchedule1:
        """
        Update a schedule

        <p>Updates an existing subscription schedule.</p>

        POST /v1/subscription_schedules/{schedule}

        Args:
            data: SubscriptionScheduleUpdateBody
            schedule: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.subscription_schedule.update(schedule="string")
        ```
        """
        models.SubscriptionSchedule1.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerSubscriptionScheduleUpdateBody,
                style={
                    "default_settings": "deepObject",
                    "end_behavior": "form",
                    "expand": "deepObject",
                    "metadata": "deepObject",
                    "phases": "deepObject",
                    "proration_behavior": "form",
                },
                explode={
                    "default_settings": True,
                    "end_behavior": True,
                    "expand": True,
                    "metadata": True,
                    "phases": True,
                    "proration_behavior": True,
                },
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/subscription_schedules/{schedule}",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.SubscriptionSchedule1,
            request_options=request_options or default_request_options(),
        )

    def cancel(
        self,
        *,
        schedule: str,
        data: typing.Union[
            typing.Optional[params.SubscriptionScheduleCancelBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.SubscriptionSchedule1:
        """
        Cancel a schedule

        <p>Cancels a subscription schedule and its associated subscription immediately (if the subscription schedule has an active subscription). A subscription schedule can only be canceled if its status is <code>not_started</code> or <code>active</code>.</p>

        POST /v1/subscription_schedules/{schedule}/cancel

        Args:
            data: SubscriptionScheduleCancelBody
            schedule: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.subscription_schedule.cancel(schedule="string")
        ```
        """
        models.SubscriptionSchedule1.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerSubscriptionScheduleCancelBody,
                style={
                    "expand": "deepObject",
                    "invoice_now": "form",
                    "prorate": "form",
                },
                explode={"expand": True, "invoice_now": True, "prorate": True},
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/subscription_schedules/{schedule}/cancel",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.SubscriptionSchedule1,
            request_options=request_options or default_request_options(),
        )

    def release(
        self,
        *,
        schedule: str,
        data: typing.Union[
            typing.Optional[params.SubscriptionScheduleReleaseBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.SubscriptionSchedule1:
        """
        Release a schedule

        <p>Releases the subscription schedule immediately, which will stop scheduling of its phases, but leave any existing subscription in place. A schedule can only be released if its status is <code>not_started</code> or <code>active</code>. If the subscription schedule is currently associated with a subscription, releasing it will remove its <code>subscription</code> property and set the subscription’s ID to the <code>released_subscription</code> property.</p>

        POST /v1/subscription_schedules/{schedule}/release

        Args:
            data: SubscriptionScheduleReleaseBody
            schedule: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.subscription_schedule.release(schedule="string")
        ```
        """
        models.SubscriptionSchedule1.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerSubscriptionScheduleReleaseBody,
                style={"expand": "deepObject", "preserve_cancel_date": "form"},
                explode={"expand": True, "preserve_cancel_date": True},
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/subscription_schedules/{schedule}/release",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.SubscriptionSchedule1,
            request_options=request_options or default_request_options(),
        )


class AsyncSubscriptionScheduleClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def list(
        self,
        *,
        canceled_at: typing.Union[
            typing.Optional[
                typing.Union[params.SubscriptionScheduleListCanceledAtObj0, int]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        completed_at: typing.Union[
            typing.Optional[
                typing.Union[params.SubscriptionScheduleListCompletedAtObj0, int]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        created: typing.Union[
            typing.Optional[
                typing.Union[params.SubscriptionScheduleListCreatedObj0, int]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        customer: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        ending_before: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        limit: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        released_at: typing.Union[
            typing.Optional[
                typing.Union[params.SubscriptionScheduleListReleasedAtObj0, int]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        scheduled: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        starting_after: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.SubscriptionScheduleListResponse:
        """
        List all schedules

        <p>Retrieves the list of your subscription schedules.</p>

        GET /v1/subscription_schedules

        Args:
            canceled_at: Only return subscription schedules that were created canceled the given date interval.
            completed_at: Only return subscription schedules that completed during the given date interval.
            created: Only return subscription schedules that were created during the given date interval.
            customer: Only return subscription schedules for the given customer.
            ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            expand: Specifies which fields in the response should be expanded.
            limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            released_at: Only return subscription schedules that were released during the given date interval.
            scheduled: Only return subscription schedules that have not started yet.
            starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.subscription_schedule.list()
        ```
        """
        models.SubscriptionScheduleListResponse.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _query: QueryParams = {}
        if not isinstance(canceled_at, type_utils.NotGiven):
            encode_query_param(
                _query,
                "canceled_at",
                to_encodable(
                    item=canceled_at,
                    dump_with=typing.Union[
                        params._SerializerSubscriptionScheduleListCanceledAtObj0, int
                    ],
                ),
                style="deepObject",
                explode=True,
            )
        if not isinstance(completed_at, type_utils.NotGiven):
            encode_query_param(
                _query,
                "completed_at",
                to_encodable(
                    item=completed_at,
                    dump_with=typing.Union[
                        params._SerializerSubscriptionScheduleListCompletedAtObj0, int
                    ],
                ),
                style="deepObject",
                explode=True,
            )
        if not isinstance(created, type_utils.NotGiven):
            encode_query_param(
                _query,
                "created",
                to_encodable(
                    item=created,
                    dump_with=typing.Union[
                        params._SerializerSubscriptionScheduleListCreatedObj0, int
                    ],
                ),
                style="deepObject",
                explode=True,
            )
        if not isinstance(customer, type_utils.NotGiven):
            encode_query_param(
                _query,
                "customer",
                to_encodable(item=customer, dump_with=str),
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
        if not isinstance(released_at, type_utils.NotGiven):
            encode_query_param(
                _query,
                "released_at",
                to_encodable(
                    item=released_at,
                    dump_with=typing.Union[
                        params._SerializerSubscriptionScheduleListReleasedAtObj0, int
                    ],
                ),
                style="deepObject",
                explode=True,
            )
        if not isinstance(scheduled, type_utils.NotGiven):
            encode_query_param(
                _query,
                "scheduled",
                to_encodable(item=scheduled, dump_with=bool),
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
        return await self._base_client.request(
            method="GET",
            path="/v1/subscription_schedules",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.SubscriptionScheduleListResponse,
            request_options=request_options or default_request_options(),
        )

    async def get(
        self,
        *,
        schedule: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.SubscriptionSchedule1:
        """
        Retrieve a schedule

        <p>Retrieves the details of an existing subscription schedule. You only need to supply the unique subscription schedule identifier that was returned upon subscription schedule creation.</p>

        GET /v1/subscription_schedules/{schedule}

        Args:
            expand: Specifies which fields in the response should be expanded.
            schedule: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.subscription_schedule.get(schedule="string")
        ```
        """
        models.SubscriptionSchedule1.model_rebuild(
            _types_namespace=models._types_namespace
        )
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
            path=f"/v1/subscription_schedules/{schedule}",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.SubscriptionSchedule1,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        data: typing.Union[
            typing.Optional[params.SubscriptionScheduleCreateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.SubscriptionSchedule1:
        """
        Create a schedule

        <p>Creates a new subscription schedule object. Each customer can have up to 500 active or scheduled subscriptions.</p>

        POST /v1/subscription_schedules

        Args:
            data: SubscriptionScheduleCreateBody
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.subscription_schedule.create()
        ```
        """
        models.SubscriptionSchedule1.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerSubscriptionScheduleCreateBody,
                style={
                    "customer": "form",
                    "default_settings": "deepObject",
                    "end_behavior": "form",
                    "expand": "deepObject",
                    "from_subscription": "form",
                    "metadata": "deepObject",
                    "phases": "deepObject",
                    "start_date": "deepObject",
                },
                explode={
                    "customer": True,
                    "default_settings": True,
                    "end_behavior": True,
                    "expand": True,
                    "from_subscription": True,
                    "metadata": True,
                    "phases": True,
                    "start_date": True,
                },
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path="/v1/subscription_schedules",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.SubscriptionSchedule1,
            request_options=request_options or default_request_options(),
        )

    async def update(
        self,
        *,
        schedule: str,
        data: typing.Union[
            typing.Optional[params.SubscriptionScheduleUpdateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.SubscriptionSchedule1:
        """
        Update a schedule

        <p>Updates an existing subscription schedule.</p>

        POST /v1/subscription_schedules/{schedule}

        Args:
            data: SubscriptionScheduleUpdateBody
            schedule: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.subscription_schedule.update(schedule="string")
        ```
        """
        models.SubscriptionSchedule1.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerSubscriptionScheduleUpdateBody,
                style={
                    "default_settings": "deepObject",
                    "end_behavior": "form",
                    "expand": "deepObject",
                    "metadata": "deepObject",
                    "phases": "deepObject",
                    "proration_behavior": "form",
                },
                explode={
                    "default_settings": True,
                    "end_behavior": True,
                    "expand": True,
                    "metadata": True,
                    "phases": True,
                    "proration_behavior": True,
                },
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/subscription_schedules/{schedule}",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.SubscriptionSchedule1,
            request_options=request_options or default_request_options(),
        )

    async def cancel(
        self,
        *,
        schedule: str,
        data: typing.Union[
            typing.Optional[params.SubscriptionScheduleCancelBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.SubscriptionSchedule1:
        """
        Cancel a schedule

        <p>Cancels a subscription schedule and its associated subscription immediately (if the subscription schedule has an active subscription). A subscription schedule can only be canceled if its status is <code>not_started</code> or <code>active</code>.</p>

        POST /v1/subscription_schedules/{schedule}/cancel

        Args:
            data: SubscriptionScheduleCancelBody
            schedule: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.subscription_schedule.cancel(schedule="string")
        ```
        """
        models.SubscriptionSchedule1.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerSubscriptionScheduleCancelBody,
                style={
                    "expand": "deepObject",
                    "invoice_now": "form",
                    "prorate": "form",
                },
                explode={"expand": True, "invoice_now": True, "prorate": True},
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/subscription_schedules/{schedule}/cancel",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.SubscriptionSchedule1,
            request_options=request_options or default_request_options(),
        )

    async def release(
        self,
        *,
        schedule: str,
        data: typing.Union[
            typing.Optional[params.SubscriptionScheduleReleaseBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.SubscriptionSchedule1:
        """
        Release a schedule

        <p>Releases the subscription schedule immediately, which will stop scheduling of its phases, but leave any existing subscription in place. A schedule can only be released if its status is <code>not_started</code> or <code>active</code>. If the subscription schedule is currently associated with a subscription, releasing it will remove its <code>subscription</code> property and set the subscription’s ID to the <code>released_subscription</code> property.</p>

        POST /v1/subscription_schedules/{schedule}/release

        Args:
            data: SubscriptionScheduleReleaseBody
            schedule: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.subscription_schedule.release(schedule="string")
        ```
        """
        models.SubscriptionSchedule1.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerSubscriptionScheduleReleaseBody,
                style={"expand": "deepObject", "preserve_cancel_date": "form"},
                explode={"expand": True, "preserve_cancel_date": True},
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/subscription_schedules/{schedule}/release",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.SubscriptionSchedule1,
            request_options=request_options or default_request_options(),
        )
