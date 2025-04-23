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


class TestClockClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def delete(
        self,
        *,
        test_clock: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.DeletedTestHelpersTestClock:
        """
        Delete a test clock

        <p>Deletes a test clock.</p>

        DELETE /v1/test_helpers/test_clocks/{test_clock}

        Args:
            test_clock: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.test_helper.test_clock.delete(test_clock="string")
        ```
        """
        return self._base_client.request(
            method="DELETE",
            path=f"/v1/test_helpers/test_clocks/{test_clock}",
            auth_names=["bearerAuth"],
            cast_to=models.DeletedTestHelpersTestClock,
            request_options=request_options or default_request_options(),
        )

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
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TestHelperTestClockListResponse:
        """
        List all test clocks

        <p>Returns a list of your test clocks.</p>

        GET /v1/test_helpers/test_clocks

        Args:
            ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            expand: Specifies which fields in the response should be expanded.
            limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.test_helper.test_clock.list()
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
        return self._base_client.request(
            method="GET",
            path="/v1/test_helpers/test_clocks",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.TestHelperTestClockListResponse,
            request_options=request_options or default_request_options(),
        )

    def get(
        self,
        *,
        test_clock: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TestHelpersTestClock:
        """
        Retrieve a test clock

        <p>Retrieves a test clock.</p>

        GET /v1/test_helpers/test_clocks/{test_clock}

        Args:
            expand: Specifies which fields in the response should be expanded.
            test_clock: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.test_helper.test_clock.get(test_clock="string")
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
            path=f"/v1/test_helpers/test_clocks/{test_clock}",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.TestHelpersTestClock,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        frozen_time: int,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TestHelpersTestClock:
        """
        Create a test clock

        <p>Creates a new test clock that can be attached to new customers and quotes.</p>

        POST /v1/test_helpers/test_clocks

        Args:
            expand: Specifies which fields in the response should be expanded.
            name: The name for this test clock.
            frozen_time: The initial frozen time for this test clock.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.test_helper.test_clock.create(frozen_time=123)
        ```
        """
        _data = to_form_urlencoded(
            item={"expand": expand, "name": name, "frozen_time": frozen_time},
            dump_with=params._SerializerTestHelperTestClockCreateBody,
            style={"expand": "deepObject", "frozen_time": "form", "name": "form"},
            explode={"expand": True, "frozen_time": True, "name": True},
        )
        return self._base_client.request(
            method="POST",
            path="/v1/test_helpers/test_clocks",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.TestHelpersTestClock,
            request_options=request_options or default_request_options(),
        )

    def advance(
        self,
        *,
        frozen_time: int,
        test_clock: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TestHelpersTestClock:
        """
        Advance a test clock

        <p>Starts advancing a test clock to a specified time in the future. Advancement is done when status changes to <code>Ready</code>.</p>

        POST /v1/test_helpers/test_clocks/{test_clock}/advance

        Args:
            expand: Specifies which fields in the response should be expanded.
            frozen_time: The time to advance the test clock. Must be after the test clock's current frozen time. Cannot be more than two intervals in the future from the shortest subscription in this test clock. If there are no subscriptions in this test clock, it cannot be more than two years in the future.
            test_clock: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.test_helper.test_clock.advance(frozen_time=123, test_clock="string")
        ```
        """
        _data = to_form_urlencoded(
            item={"expand": expand, "frozen_time": frozen_time},
            dump_with=params._SerializerTestHelperTestClockAdvanceBody,
            style={"expand": "deepObject", "frozen_time": "form"},
            explode={"expand": True, "frozen_time": True},
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/test_helpers/test_clocks/{test_clock}/advance",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.TestHelpersTestClock,
            request_options=request_options or default_request_options(),
        )


class AsyncTestClockClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def delete(
        self,
        *,
        test_clock: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.DeletedTestHelpersTestClock:
        """
        Delete a test clock

        <p>Deletes a test clock.</p>

        DELETE /v1/test_helpers/test_clocks/{test_clock}

        Args:
            test_clock: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.test_helper.test_clock.delete(test_clock="string")
        ```
        """
        return await self._base_client.request(
            method="DELETE",
            path=f"/v1/test_helpers/test_clocks/{test_clock}",
            auth_names=["bearerAuth"],
            cast_to=models.DeletedTestHelpersTestClock,
            request_options=request_options or default_request_options(),
        )

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
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TestHelperTestClockListResponse:
        """
        List all test clocks

        <p>Returns a list of your test clocks.</p>

        GET /v1/test_helpers/test_clocks

        Args:
            ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            expand: Specifies which fields in the response should be expanded.
            limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.test_helper.test_clock.list()
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
        return await self._base_client.request(
            method="GET",
            path="/v1/test_helpers/test_clocks",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.TestHelperTestClockListResponse,
            request_options=request_options or default_request_options(),
        )

    async def get(
        self,
        *,
        test_clock: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TestHelpersTestClock:
        """
        Retrieve a test clock

        <p>Retrieves a test clock.</p>

        GET /v1/test_helpers/test_clocks/{test_clock}

        Args:
            expand: Specifies which fields in the response should be expanded.
            test_clock: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.test_helper.test_clock.get(test_clock="string")
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
            path=f"/v1/test_helpers/test_clocks/{test_clock}",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.TestHelpersTestClock,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        frozen_time: int,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TestHelpersTestClock:
        """
        Create a test clock

        <p>Creates a new test clock that can be attached to new customers and quotes.</p>

        POST /v1/test_helpers/test_clocks

        Args:
            expand: Specifies which fields in the response should be expanded.
            name: The name for this test clock.
            frozen_time: The initial frozen time for this test clock.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.test_helper.test_clock.create(frozen_time=123)
        ```
        """
        _data = to_form_urlencoded(
            item={"expand": expand, "name": name, "frozen_time": frozen_time},
            dump_with=params._SerializerTestHelperTestClockCreateBody,
            style={"expand": "deepObject", "frozen_time": "form", "name": "form"},
            explode={"expand": True, "frozen_time": True, "name": True},
        )
        return await self._base_client.request(
            method="POST",
            path="/v1/test_helpers/test_clocks",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.TestHelpersTestClock,
            request_options=request_options or default_request_options(),
        )

    async def advance(
        self,
        *,
        frozen_time: int,
        test_clock: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TestHelpersTestClock:
        """
        Advance a test clock

        <p>Starts advancing a test clock to a specified time in the future. Advancement is done when status changes to <code>Ready</code>.</p>

        POST /v1/test_helpers/test_clocks/{test_clock}/advance

        Args:
            expand: Specifies which fields in the response should be expanded.
            frozen_time: The time to advance the test clock. Must be after the test clock's current frozen time. Cannot be more than two intervals in the future from the shortest subscription in this test clock. If there are no subscriptions in this test clock, it cannot be more than two years in the future.
            test_clock: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.test_helper.test_clock.advance(
            frozen_time=123, test_clock="string"
        )
        ```
        """
        _data = to_form_urlencoded(
            item={"expand": expand, "frozen_time": frozen_time},
            dump_with=params._SerializerTestHelperTestClockAdvanceBody,
            style={"expand": "deepObject", "frozen_time": "form"},
            explode={"expand": True, "frozen_time": True},
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/test_helpers/test_clocks/{test_clock}/advance",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.TestHelpersTestClock,
            request_options=request_options or default_request_options(),
        )
