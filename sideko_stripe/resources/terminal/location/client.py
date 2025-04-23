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


class LocationClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def delete(
        self, *, location: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.DeletedTerminalLocation:
        """
        Delete a Location

        <p>Deletes a <code>Location</code> object.</p>

        DELETE /v1/terminal/locations/{location}

        Args:
            location: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.terminal.location.delete(location="string")
        ```
        """
        return self._base_client.request(
            method="DELETE",
            path=f"/v1/terminal/locations/{location}",
            auth_names=["bearerAuth"],
            cast_to=models.DeletedTerminalLocation,
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
    ) -> models.TerminalLocationListResponse:
        """
        List all Locations

        <p>Returns a list of <code>Location</code> objects.</p>

        GET /v1/terminal/locations

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
        client.terminal.location.list()
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
            path="/v1/terminal/locations",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.TerminalLocationListResponse,
            request_options=request_options or default_request_options(),
        )

    def get(
        self,
        *,
        location: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Union[models.TerminalLocation, models.DeletedTerminalLocation]:
        """
        Retrieve a Location

        <p>Retrieves a <code>Location</code> object.</p>

        GET /v1/terminal/locations/{location}

        Args:
            expand: Specifies which fields in the response should be expanded.
            location: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.terminal.location.get(location="string")
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
            path=f"/v1/terminal/locations/{location}",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=typing.Union[
                models.TerminalLocation, models.DeletedTerminalLocation
            ],
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        address: params.TerminalLocationCreateBodyAddress,
        display_name: str,
        configuration_overrides: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        metadata: typing.Union[
            typing.Optional[
                typing.Union[params.TerminalLocationCreateBodyMetadataObj0, str]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TerminalLocation:
        """
        Create a Location

        <p>Creates a new <code>Location</code> object.
        For further details, including which address fields are required in each country, see the <a href="/docs/terminal/fleet/locations">Manage locations</a> guide.</p>

        POST /v1/terminal/locations

        Args:
            configuration_overrides: The ID of a configuration that will be used to customize all readers in this location.
            expand: Specifies which fields in the response should be expanded.
            metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
            address: The full address of the location.
            display_name: A name for the location. Maximum length is 1000 characters.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.terminal.location.create(
            address={"country": "string"}, display_name="string"
        )
        ```
        """
        _data = to_form_urlencoded(
            item={
                "configuration_overrides": configuration_overrides,
                "expand": expand,
                "metadata": metadata,
                "address": address,
                "display_name": display_name,
            },
            dump_with=params._SerializerTerminalLocationCreateBody,
            style={
                "address": "deepObject",
                "configuration_overrides": "form",
                "display_name": "form",
                "expand": "deepObject",
                "metadata": "deepObject",
            },
            explode={
                "address": True,
                "configuration_overrides": True,
                "display_name": True,
                "expand": True,
                "metadata": True,
            },
        )
        return self._base_client.request(
            method="POST",
            path="/v1/terminal/locations",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.TerminalLocation,
            request_options=request_options or default_request_options(),
        )

    def update(
        self,
        *,
        location: str,
        data: typing.Union[
            typing.Optional[params.TerminalLocationUpdateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Union[models.TerminalLocation, models.DeletedTerminalLocation]:
        """
        Update a Location

        <p>Updates a <code>Location</code> object by setting the values of the parameters passed. Any parameters not provided will be left unchanged.</p>

        POST /v1/terminal/locations/{location}

        Args:
            data: TerminalLocationUpdateBody
            location: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.terminal.location.update(location="string")
        ```
        """
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerTerminalLocationUpdateBody,
                style={
                    "address": "deepObject",
                    "configuration_overrides": "deepObject",
                    "display_name": "form",
                    "expand": "deepObject",
                    "metadata": "deepObject",
                },
                explode={
                    "address": True,
                    "configuration_overrides": True,
                    "display_name": True,
                    "expand": True,
                    "metadata": True,
                },
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/terminal/locations/{location}",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=typing.Union[
                models.TerminalLocation, models.DeletedTerminalLocation
            ],
            request_options=request_options or default_request_options(),
        )


class AsyncLocationClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def delete(
        self, *, location: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.DeletedTerminalLocation:
        """
        Delete a Location

        <p>Deletes a <code>Location</code> object.</p>

        DELETE /v1/terminal/locations/{location}

        Args:
            location: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.terminal.location.delete(location="string")
        ```
        """
        return await self._base_client.request(
            method="DELETE",
            path=f"/v1/terminal/locations/{location}",
            auth_names=["bearerAuth"],
            cast_to=models.DeletedTerminalLocation,
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
    ) -> models.TerminalLocationListResponse:
        """
        List all Locations

        <p>Returns a list of <code>Location</code> objects.</p>

        GET /v1/terminal/locations

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
        await client.terminal.location.list()
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
            path="/v1/terminal/locations",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.TerminalLocationListResponse,
            request_options=request_options or default_request_options(),
        )

    async def get(
        self,
        *,
        location: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Union[models.TerminalLocation, models.DeletedTerminalLocation]:
        """
        Retrieve a Location

        <p>Retrieves a <code>Location</code> object.</p>

        GET /v1/terminal/locations/{location}

        Args:
            expand: Specifies which fields in the response should be expanded.
            location: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.terminal.location.get(location="string")
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
            path=f"/v1/terminal/locations/{location}",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=typing.Union[
                models.TerminalLocation, models.DeletedTerminalLocation
            ],
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        address: params.TerminalLocationCreateBodyAddress,
        display_name: str,
        configuration_overrides: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        metadata: typing.Union[
            typing.Optional[
                typing.Union[params.TerminalLocationCreateBodyMetadataObj0, str]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TerminalLocation:
        """
        Create a Location

        <p>Creates a new <code>Location</code> object.
        For further details, including which address fields are required in each country, see the <a href="/docs/terminal/fleet/locations">Manage locations</a> guide.</p>

        POST /v1/terminal/locations

        Args:
            configuration_overrides: The ID of a configuration that will be used to customize all readers in this location.
            expand: Specifies which fields in the response should be expanded.
            metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
            address: The full address of the location.
            display_name: A name for the location. Maximum length is 1000 characters.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.terminal.location.create(
            address={"country": "string"}, display_name="string"
        )
        ```
        """
        _data = to_form_urlencoded(
            item={
                "configuration_overrides": configuration_overrides,
                "expand": expand,
                "metadata": metadata,
                "address": address,
                "display_name": display_name,
            },
            dump_with=params._SerializerTerminalLocationCreateBody,
            style={
                "address": "deepObject",
                "configuration_overrides": "form",
                "display_name": "form",
                "expand": "deepObject",
                "metadata": "deepObject",
            },
            explode={
                "address": True,
                "configuration_overrides": True,
                "display_name": True,
                "expand": True,
                "metadata": True,
            },
        )
        return await self._base_client.request(
            method="POST",
            path="/v1/terminal/locations",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.TerminalLocation,
            request_options=request_options or default_request_options(),
        )

    async def update(
        self,
        *,
        location: str,
        data: typing.Union[
            typing.Optional[params.TerminalLocationUpdateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Union[models.TerminalLocation, models.DeletedTerminalLocation]:
        """
        Update a Location

        <p>Updates a <code>Location</code> object by setting the values of the parameters passed. Any parameters not provided will be left unchanged.</p>

        POST /v1/terminal/locations/{location}

        Args:
            data: TerminalLocationUpdateBody
            location: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.terminal.location.update(location="string")
        ```
        """
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerTerminalLocationUpdateBody,
                style={
                    "address": "deepObject",
                    "configuration_overrides": "deepObject",
                    "display_name": "form",
                    "expand": "deepObject",
                    "metadata": "deepObject",
                },
                explode={
                    "address": True,
                    "configuration_overrides": True,
                    "display_name": True,
                    "expand": True,
                    "metadata": True,
                },
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/terminal/locations/{location}",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=typing.Union[
                models.TerminalLocation, models.DeletedTerminalLocation
            ],
            request_options=request_options or default_request_options(),
        )
