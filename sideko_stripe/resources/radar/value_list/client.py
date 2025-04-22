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
from sideko_stripe.types import models, params


class ValueListClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def delete(
        self,
        *,
        value_list: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.DeletedRadarValueList:
        """
        Delete a value list

        <p>Deletes a <code>ValueList</code> object, also deleting any items contained within the value list. To be deleted, a value list must not be referenced in any rules.</p>

        DELETE /v1/radar/value_lists/{value_list}

        Args:
            value_list: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.radar.value_list.delete(value_list="string")
        ```
        """
        return self._base_client.request(
            method="DELETE",
            path=f"/v1/radar/value_lists/{value_list}",
            auth_names=["basicAuth", "bearerAuth"],
            cast_to=models.DeletedRadarValueList,
            request_options=request_options or default_request_options(),
        )

    def list(
        self,
        *,
        alias: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        contains: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        created: typing.Union[
            typing.Optional[typing.Union[params.RadarValueListListCreatedObj0, int]],
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
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.RadarValueListListResponse:
        """
        List all value lists

        <p>Returns a list of <code>ValueList</code> objects. The objects are sorted in descending order by creation date, with the most recently created object appearing first.</p>

        GET /v1/radar/value_lists

        Args:
            alias: The alias used to reference the value list when writing rules.
            contains: A value contained within a value list - returns all value lists containing this value.
            created: Only return value lists that were created during the given date interval.
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
        client.radar.value_list.list()
        ```
        """
        _query: QueryParams = {}
        if not isinstance(alias, type_utils.NotGiven):
            encode_query_param(
                _query,
                "alias",
                to_encodable(item=alias, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(contains, type_utils.NotGiven):
            encode_query_param(
                _query,
                "contains",
                to_encodable(item=contains, dump_with=str),
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
                        params._SerializerRadarValueListListCreatedObj0, int
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
        return self._base_client.request(
            method="GET",
            path="/v1/radar/value_lists",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.RadarValueListListResponse,
            request_options=request_options or default_request_options(),
        )

    def get(
        self,
        *,
        value_list: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.RadarValueList:
        """
        Retrieve a value list

        <p>Retrieves a <code>ValueList</code> object.</p>

        GET /v1/radar/value_lists/{value_list}

        Args:
            expand: Specifies which fields in the response should be expanded.
            value_list: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.radar.value_list.get(value_list="string")
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
            path=f"/v1/radar/value_lists/{value_list}",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.RadarValueList,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        alias: str,
        name: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        item_type: typing.Union[
            typing.Optional[
                typing_extensions.Literal[
                    "card_bin",
                    "card_fingerprint",
                    "case_sensitive_string",
                    "country",
                    "customer_id",
                    "email",
                    "ip_address",
                    "sepa_debit_fingerprint",
                    "string",
                    "us_bank_account_fingerprint",
                ]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        metadata: typing.Union[
            typing.Optional[params.RadarValueListCreateBodyMetadata],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.RadarValueList:
        """
        Create a value list

        <p>Creates a new <code>ValueList</code> object, which can then be referenced in rules.</p>

        POST /v1/radar/value_lists

        Args:
            expand: Specifies which fields in the response should be expanded.
            item_type: Type of the items in the value list. One of `card_fingerprint`, `us_bank_account_fingerprint`, `sepa_debit_fingerprint`, `card_bin`, `email`, `ip_address`, `country`, `string`, `case_sensitive_string`, or `customer_id`. Use `string` if the item type is unknown or mixed.
            metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
            alias: The name of the value list for use in rules.
            name: The human-readable name of the value list.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.radar.value_list.create(alias="string", name="string")
        ```
        """
        _data = to_form_urlencoded(
            item={
                "expand": expand,
                "item_type": item_type,
                "metadata": metadata,
                "alias": alias,
                "name": name,
            },
            dump_with=params._SerializerRadarValueListCreateBody,
            style={
                "alias": "form",
                "expand": "deepObject",
                "item_type": "form",
                "metadata": "deepObject",
                "name": "form",
            },
            explode={
                "alias": True,
                "expand": True,
                "item_type": True,
                "metadata": True,
                "name": True,
            },
        )
        return self._base_client.request(
            method="POST",
            path="/v1/radar/value_lists",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.RadarValueList,
            request_options=request_options or default_request_options(),
        )

    def update(
        self,
        *,
        value_list: str,
        data: typing.Union[
            typing.Optional[params.RadarValueListUpdateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.RadarValueList:
        """
        Update a value list

        <p>Updates a <code>ValueList</code> object by setting the values of the parameters passed. Any parameters not provided will be left unchanged. Note that <code>item_type</code> is immutable.</p>

        POST /v1/radar/value_lists/{value_list}

        Args:
            data: RadarValueListUpdateBody
            value_list: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.radar.value_list.update(value_list="string")
        ```
        """
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerRadarValueListUpdateBody,
                style={
                    "alias": "form",
                    "expand": "deepObject",
                    "metadata": "deepObject",
                    "name": "form",
                },
                explode={"alias": True, "expand": True, "metadata": True, "name": True},
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/radar/value_lists/{value_list}",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.RadarValueList,
            request_options=request_options or default_request_options(),
        )


class AsyncValueListClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def delete(
        self,
        *,
        value_list: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.DeletedRadarValueList:
        """
        Delete a value list

        <p>Deletes a <code>ValueList</code> object, also deleting any items contained within the value list. To be deleted, a value list must not be referenced in any rules.</p>

        DELETE /v1/radar/value_lists/{value_list}

        Args:
            value_list: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.radar.value_list.delete(value_list="string")
        ```
        """
        return await self._base_client.request(
            method="DELETE",
            path=f"/v1/radar/value_lists/{value_list}",
            auth_names=["basicAuth", "bearerAuth"],
            cast_to=models.DeletedRadarValueList,
            request_options=request_options or default_request_options(),
        )

    async def list(
        self,
        *,
        alias: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        contains: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        created: typing.Union[
            typing.Optional[typing.Union[params.RadarValueListListCreatedObj0, int]],
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
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.RadarValueListListResponse:
        """
        List all value lists

        <p>Returns a list of <code>ValueList</code> objects. The objects are sorted in descending order by creation date, with the most recently created object appearing first.</p>

        GET /v1/radar/value_lists

        Args:
            alias: The alias used to reference the value list when writing rules.
            contains: A value contained within a value list - returns all value lists containing this value.
            created: Only return value lists that were created during the given date interval.
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
        await client.radar.value_list.list()
        ```
        """
        _query: QueryParams = {}
        if not isinstance(alias, type_utils.NotGiven):
            encode_query_param(
                _query,
                "alias",
                to_encodable(item=alias, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(contains, type_utils.NotGiven):
            encode_query_param(
                _query,
                "contains",
                to_encodable(item=contains, dump_with=str),
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
                        params._SerializerRadarValueListListCreatedObj0, int
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
        return await self._base_client.request(
            method="GET",
            path="/v1/radar/value_lists",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.RadarValueListListResponse,
            request_options=request_options or default_request_options(),
        )

    async def get(
        self,
        *,
        value_list: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.RadarValueList:
        """
        Retrieve a value list

        <p>Retrieves a <code>ValueList</code> object.</p>

        GET /v1/radar/value_lists/{value_list}

        Args:
            expand: Specifies which fields in the response should be expanded.
            value_list: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.radar.value_list.get(value_list="string")
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
            path=f"/v1/radar/value_lists/{value_list}",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.RadarValueList,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        alias: str,
        name: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        item_type: typing.Union[
            typing.Optional[
                typing_extensions.Literal[
                    "card_bin",
                    "card_fingerprint",
                    "case_sensitive_string",
                    "country",
                    "customer_id",
                    "email",
                    "ip_address",
                    "sepa_debit_fingerprint",
                    "string",
                    "us_bank_account_fingerprint",
                ]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        metadata: typing.Union[
            typing.Optional[params.RadarValueListCreateBodyMetadata],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.RadarValueList:
        """
        Create a value list

        <p>Creates a new <code>ValueList</code> object, which can then be referenced in rules.</p>

        POST /v1/radar/value_lists

        Args:
            expand: Specifies which fields in the response should be expanded.
            item_type: Type of the items in the value list. One of `card_fingerprint`, `us_bank_account_fingerprint`, `sepa_debit_fingerprint`, `card_bin`, `email`, `ip_address`, `country`, `string`, `case_sensitive_string`, or `customer_id`. Use `string` if the item type is unknown or mixed.
            metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
            alias: The name of the value list for use in rules.
            name: The human-readable name of the value list.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.radar.value_list.create(alias="string", name="string")
        ```
        """
        _data = to_form_urlencoded(
            item={
                "expand": expand,
                "item_type": item_type,
                "metadata": metadata,
                "alias": alias,
                "name": name,
            },
            dump_with=params._SerializerRadarValueListCreateBody,
            style={
                "alias": "form",
                "expand": "deepObject",
                "item_type": "form",
                "metadata": "deepObject",
                "name": "form",
            },
            explode={
                "alias": True,
                "expand": True,
                "item_type": True,
                "metadata": True,
                "name": True,
            },
        )
        return await self._base_client.request(
            method="POST",
            path="/v1/radar/value_lists",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.RadarValueList,
            request_options=request_options or default_request_options(),
        )

    async def update(
        self,
        *,
        value_list: str,
        data: typing.Union[
            typing.Optional[params.RadarValueListUpdateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.RadarValueList:
        """
        Update a value list

        <p>Updates a <code>ValueList</code> object by setting the values of the parameters passed. Any parameters not provided will be left unchanged. Note that <code>item_type</code> is immutable.</p>

        POST /v1/radar/value_lists/{value_list}

        Args:
            data: RadarValueListUpdateBody
            value_list: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.radar.value_list.update(value_list="string")
        ```
        """
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerRadarValueListUpdateBody,
                style={
                    "alias": "form",
                    "expand": "deepObject",
                    "metadata": "deepObject",
                    "name": "form",
                },
                explode={"alias": True, "expand": True, "metadata": True, "name": True},
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/radar/value_lists/{value_list}",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.RadarValueList,
            request_options=request_options or default_request_options(),
        )
