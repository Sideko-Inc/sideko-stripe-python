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


class ValueListItemClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def delete(
        self, *, item: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.DeletedRadarValueListItem:
        """
        Delete a value list item

        <p>Deletes a <code>ValueListItem</code> object, removing it from its parent value list.</p>

        DELETE /v1/radar/value_list_items/{item}

        Args:
            item: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.radar.value_list_item.delete(item="string")
        ```
        """
        return self._base_client.request(
            method="DELETE",
            path=f"/v1/radar/value_list_items/{item}",
            auth_names=["bearerAuth"],
            cast_to=models.DeletedRadarValueListItem,
            request_options=request_options or default_request_options(),
        )

    def list(
        self,
        *,
        value_list: str,
        created: typing.Union[
            typing.Optional[
                typing.Union[params.RadarValueListItemListCreatedObj0, int]
            ],
            type_utils.NotGiven,
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
        starting_after: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        value: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.RadarValueListItemListResponse:
        """
        List all value list items

        <p>Returns a list of <code>ValueListItem</code> objects. The objects are sorted in descending order by creation date, with the most recently created object appearing first.</p>

        GET /v1/radar/value_list_items

        Args:
            created: Only return items that were created during the given date interval.
            ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            expand: Specifies which fields in the response should be expanded.
            limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
            value: Return items belonging to the parent list whose value matches the specified value (using an "is like" match).
            value_list: Identifier for the parent value list this item belongs to.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.radar.value_list_item.list(value_list="string")
        ```
        """
        _query: QueryParams = {}
        encode_query_param(
            _query,
            "value_list",
            to_encodable(item=value_list, dump_with=str),
            style="form",
            explode=True,
        )
        if not isinstance(created, type_utils.NotGiven):
            encode_query_param(
                _query,
                "created",
                to_encodable(
                    item=created,
                    dump_with=typing.Union[
                        params._SerializerRadarValueListItemListCreatedObj0, int
                    ],
                ),
                style="deepObject",
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
        if not isinstance(value, type_utils.NotGiven):
            encode_query_param(
                _query,
                "value",
                to_encodable(item=value, dump_with=str),
                style="form",
                explode=True,
            )
        return self._base_client.request(
            method="GET",
            path="/v1/radar/value_list_items",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.RadarValueListItemListResponse,
            request_options=request_options or default_request_options(),
        )

    def get(
        self,
        *,
        item: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.RadarValueListItem:
        """
        Retrieve a value list item

        <p>Retrieves a <code>ValueListItem</code> object.</p>

        GET /v1/radar/value_list_items/{item}

        Args:
            expand: Specifies which fields in the response should be expanded.
            item: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.radar.value_list_item.get(item="string")
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
            path=f"/v1/radar/value_list_items/{item}",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.RadarValueListItem,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        value: str,
        value_list: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.RadarValueListItem:
        """
        Create a value list item

        <p>Creates a new <code>ValueListItem</code> object, which is added to the specified parent value list.</p>

        POST /v1/radar/value_list_items

        Args:
            expand: Specifies which fields in the response should be expanded.
            value: The value of the item (whose type must match the type of the parent value list).
            value_list: The identifier of the value list which the created item will be added to.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.radar.value_list_item.create(value="string", value_list="string")
        ```
        """
        _data = to_form_urlencoded(
            item={"expand": expand, "value": value, "value_list": value_list},
            dump_with=params._SerializerRadarValueListItemCreateBody,
            style={"expand": "deepObject", "value": "form", "value_list": "form"},
            explode={"expand": True, "value": True, "value_list": True},
        )
        return self._base_client.request(
            method="POST",
            path="/v1/radar/value_list_items",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.RadarValueListItem,
            request_options=request_options or default_request_options(),
        )


class AsyncValueListItemClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def delete(
        self, *, item: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.DeletedRadarValueListItem:
        """
        Delete a value list item

        <p>Deletes a <code>ValueListItem</code> object, removing it from its parent value list.</p>

        DELETE /v1/radar/value_list_items/{item}

        Args:
            item: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.radar.value_list_item.delete(item="string")
        ```
        """
        return await self._base_client.request(
            method="DELETE",
            path=f"/v1/radar/value_list_items/{item}",
            auth_names=["bearerAuth"],
            cast_to=models.DeletedRadarValueListItem,
            request_options=request_options or default_request_options(),
        )

    async def list(
        self,
        *,
        value_list: str,
        created: typing.Union[
            typing.Optional[
                typing.Union[params.RadarValueListItemListCreatedObj0, int]
            ],
            type_utils.NotGiven,
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
        starting_after: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        value: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.RadarValueListItemListResponse:
        """
        List all value list items

        <p>Returns a list of <code>ValueListItem</code> objects. The objects are sorted in descending order by creation date, with the most recently created object appearing first.</p>

        GET /v1/radar/value_list_items

        Args:
            created: Only return items that were created during the given date interval.
            ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            expand: Specifies which fields in the response should be expanded.
            limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
            value: Return items belonging to the parent list whose value matches the specified value (using an "is like" match).
            value_list: Identifier for the parent value list this item belongs to.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.radar.value_list_item.list(value_list="string")
        ```
        """
        _query: QueryParams = {}
        encode_query_param(
            _query,
            "value_list",
            to_encodable(item=value_list, dump_with=str),
            style="form",
            explode=True,
        )
        if not isinstance(created, type_utils.NotGiven):
            encode_query_param(
                _query,
                "created",
                to_encodable(
                    item=created,
                    dump_with=typing.Union[
                        params._SerializerRadarValueListItemListCreatedObj0, int
                    ],
                ),
                style="deepObject",
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
        if not isinstance(value, type_utils.NotGiven):
            encode_query_param(
                _query,
                "value",
                to_encodable(item=value, dump_with=str),
                style="form",
                explode=True,
            )
        return await self._base_client.request(
            method="GET",
            path="/v1/radar/value_list_items",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.RadarValueListItemListResponse,
            request_options=request_options or default_request_options(),
        )

    async def get(
        self,
        *,
        item: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.RadarValueListItem:
        """
        Retrieve a value list item

        <p>Retrieves a <code>ValueListItem</code> object.</p>

        GET /v1/radar/value_list_items/{item}

        Args:
            expand: Specifies which fields in the response should be expanded.
            item: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.radar.value_list_item.get(item="string")
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
            path=f"/v1/radar/value_list_items/{item}",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.RadarValueListItem,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        value: str,
        value_list: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.RadarValueListItem:
        """
        Create a value list item

        <p>Creates a new <code>ValueListItem</code> object, which is added to the specified parent value list.</p>

        POST /v1/radar/value_list_items

        Args:
            expand: Specifies which fields in the response should be expanded.
            value: The value of the item (whose type must match the type of the parent value list).
            value_list: The identifier of the value list which the created item will be added to.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.radar.value_list_item.create(value="string", value_list="string")
        ```
        """
        _data = to_form_urlencoded(
            item={"expand": expand, "value": value, "value_list": value_list},
            dump_with=params._SerializerRadarValueListItemCreateBody,
            style={"expand": "deepObject", "value": "form", "value_list": "form"},
            explode={"expand": True, "value": True, "value_list": True},
        )
        return await self._base_client.request(
            method="POST",
            path="/v1/radar/value_list_items",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.RadarValueListItem,
            request_options=request_options or default_request_options(),
        )
