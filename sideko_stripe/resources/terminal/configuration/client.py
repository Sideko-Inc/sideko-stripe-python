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


class ConfigurationClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def delete(
        self,
        *,
        configuration: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.DeletedTerminalConfiguration:
        """
        Delete a Configuration

        <p>Deletes a <code>Configuration</code> object.</p>

        DELETE /v1/terminal/configurations/{configuration}

        Args:
            configuration: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.terminal.configuration.delete(configuration="string")
        ```
        """
        return self._base_client.request(
            method="DELETE",
            path=f"/v1/terminal/configurations/{configuration}",
            auth_names=["bearerAuth"],
            cast_to=models.DeletedTerminalConfiguration,
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
        is_account_default: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        limit: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        starting_after: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TerminalConfigurationListResponse:
        """
        List all Configurations

        <p>Returns a list of <code>Configuration</code> objects.</p>

        GET /v1/terminal/configurations

        Args:
            ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            expand: Specifies which fields in the response should be expanded.
            is_account_default: if present, only return the account default or non-default configurations.
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
        client.terminal.configuration.list()
        ```
        """
        models.TerminalConfigurationListResponse.model_rebuild(
            _types_namespace=models._types_namespace
        )
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
        if not isinstance(is_account_default, type_utils.NotGiven):
            encode_query_param(
                _query,
                "is_account_default",
                to_encodable(item=is_account_default, dump_with=bool),
                style="form",
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
            path="/v1/terminal/configurations",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.TerminalConfigurationListResponse,
            request_options=request_options or default_request_options(),
        )

    def get(
        self,
        *,
        configuration: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Union[
        models.TerminalConfiguration, models.DeletedTerminalConfiguration
    ]:
        """
        Retrieve a Configuration

        <p>Retrieves a <code>Configuration</code> object.</p>

        GET /v1/terminal/configurations/{configuration}

        Args:
            expand: Specifies which fields in the response should be expanded.
            configuration: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.terminal.configuration.get(configuration="string")
        ```
        """
        models.TerminalConfiguration.model_rebuild(
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
            path=f"/v1/terminal/configurations/{configuration}",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=typing.Union[
                models.TerminalConfiguration, models.DeletedTerminalConfiguration
            ],
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        data: typing.Union[
            typing.Optional[params.TerminalConfigurationCreateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TerminalConfiguration:
        """
        Create a Configuration

        <p>Creates a new <code>Configuration</code> object.</p>

        POST /v1/terminal/configurations

        Args:
            data: TerminalConfigurationCreateBody
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.terminal.configuration.create()
        ```
        """
        models.TerminalConfiguration.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerTerminalConfigurationCreateBody,
                style={
                    "bbpos_wisepos_e": "deepObject",
                    "expand": "deepObject",
                    "name": "form",
                    "offline": "deepObject",
                    "reboot_window": "deepObject",
                    "stripe_s700": "deepObject",
                    "tipping": "deepObject",
                    "verifone_p400": "deepObject",
                    "wifi": "deepObject",
                },
                explode={
                    "bbpos_wisepos_e": True,
                    "expand": True,
                    "name": True,
                    "offline": True,
                    "reboot_window": True,
                    "stripe_s700": True,
                    "tipping": True,
                    "verifone_p400": True,
                    "wifi": True,
                },
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path="/v1/terminal/configurations",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.TerminalConfiguration,
            request_options=request_options or default_request_options(),
        )

    def update(
        self,
        *,
        configuration: str,
        data: typing.Union[
            typing.Optional[params.TerminalConfigurationUpdateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Union[
        models.TerminalConfiguration, models.DeletedTerminalConfiguration
    ]:
        """
        Update a Configuration

        <p>Updates a new <code>Configuration</code> object.</p>

        POST /v1/terminal/configurations/{configuration}

        Args:
            data: TerminalConfigurationUpdateBody
            configuration: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.terminal.configuration.update(configuration="string")
        ```
        """
        models.TerminalConfiguration.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerTerminalConfigurationUpdateBody,
                style={
                    "bbpos_wisepos_e": "deepObject",
                    "expand": "deepObject",
                    "name": "form",
                    "offline": "deepObject",
                    "reboot_window": "deepObject",
                    "stripe_s700": "deepObject",
                    "tipping": "deepObject",
                    "verifone_p400": "deepObject",
                    "wifi": "deepObject",
                },
                explode={
                    "bbpos_wisepos_e": True,
                    "expand": True,
                    "name": True,
                    "offline": True,
                    "reboot_window": True,
                    "stripe_s700": True,
                    "tipping": True,
                    "verifone_p400": True,
                    "wifi": True,
                },
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/terminal/configurations/{configuration}",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=typing.Union[
                models.TerminalConfiguration, models.DeletedTerminalConfiguration
            ],
            request_options=request_options or default_request_options(),
        )


class AsyncConfigurationClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def delete(
        self,
        *,
        configuration: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.DeletedTerminalConfiguration:
        """
        Delete a Configuration

        <p>Deletes a <code>Configuration</code> object.</p>

        DELETE /v1/terminal/configurations/{configuration}

        Args:
            configuration: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.terminal.configuration.delete(configuration="string")
        ```
        """
        return await self._base_client.request(
            method="DELETE",
            path=f"/v1/terminal/configurations/{configuration}",
            auth_names=["bearerAuth"],
            cast_to=models.DeletedTerminalConfiguration,
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
        is_account_default: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        limit: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        starting_after: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TerminalConfigurationListResponse:
        """
        List all Configurations

        <p>Returns a list of <code>Configuration</code> objects.</p>

        GET /v1/terminal/configurations

        Args:
            ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            expand: Specifies which fields in the response should be expanded.
            is_account_default: if present, only return the account default or non-default configurations.
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
        await client.terminal.configuration.list()
        ```
        """
        models.TerminalConfigurationListResponse.model_rebuild(
            _types_namespace=models._types_namespace
        )
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
        if not isinstance(is_account_default, type_utils.NotGiven):
            encode_query_param(
                _query,
                "is_account_default",
                to_encodable(item=is_account_default, dump_with=bool),
                style="form",
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
            path="/v1/terminal/configurations",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.TerminalConfigurationListResponse,
            request_options=request_options or default_request_options(),
        )

    async def get(
        self,
        *,
        configuration: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Union[
        models.TerminalConfiguration, models.DeletedTerminalConfiguration
    ]:
        """
        Retrieve a Configuration

        <p>Retrieves a <code>Configuration</code> object.</p>

        GET /v1/terminal/configurations/{configuration}

        Args:
            expand: Specifies which fields in the response should be expanded.
            configuration: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.terminal.configuration.get(configuration="string")
        ```
        """
        models.TerminalConfiguration.model_rebuild(
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
            path=f"/v1/terminal/configurations/{configuration}",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=typing.Union[
                models.TerminalConfiguration, models.DeletedTerminalConfiguration
            ],
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        data: typing.Union[
            typing.Optional[params.TerminalConfigurationCreateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TerminalConfiguration:
        """
        Create a Configuration

        <p>Creates a new <code>Configuration</code> object.</p>

        POST /v1/terminal/configurations

        Args:
            data: TerminalConfigurationCreateBody
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.terminal.configuration.create()
        ```
        """
        models.TerminalConfiguration.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerTerminalConfigurationCreateBody,
                style={
                    "bbpos_wisepos_e": "deepObject",
                    "expand": "deepObject",
                    "name": "form",
                    "offline": "deepObject",
                    "reboot_window": "deepObject",
                    "stripe_s700": "deepObject",
                    "tipping": "deepObject",
                    "verifone_p400": "deepObject",
                    "wifi": "deepObject",
                },
                explode={
                    "bbpos_wisepos_e": True,
                    "expand": True,
                    "name": True,
                    "offline": True,
                    "reboot_window": True,
                    "stripe_s700": True,
                    "tipping": True,
                    "verifone_p400": True,
                    "wifi": True,
                },
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path="/v1/terminal/configurations",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.TerminalConfiguration,
            request_options=request_options or default_request_options(),
        )

    async def update(
        self,
        *,
        configuration: str,
        data: typing.Union[
            typing.Optional[params.TerminalConfigurationUpdateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Union[
        models.TerminalConfiguration, models.DeletedTerminalConfiguration
    ]:
        """
        Update a Configuration

        <p>Updates a new <code>Configuration</code> object.</p>

        POST /v1/terminal/configurations/{configuration}

        Args:
            data: TerminalConfigurationUpdateBody
            configuration: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.terminal.configuration.update(configuration="string")
        ```
        """
        models.TerminalConfiguration.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerTerminalConfigurationUpdateBody,
                style={
                    "bbpos_wisepos_e": "deepObject",
                    "expand": "deepObject",
                    "name": "form",
                    "offline": "deepObject",
                    "reboot_window": "deepObject",
                    "stripe_s700": "deepObject",
                    "tipping": "deepObject",
                    "verifone_p400": "deepObject",
                    "wifi": "deepObject",
                },
                explode={
                    "bbpos_wisepos_e": True,
                    "expand": True,
                    "name": True,
                    "offline": True,
                    "reboot_window": True,
                    "stripe_s700": True,
                    "tipping": True,
                    "verifone_p400": True,
                    "wifi": True,
                },
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/terminal/configurations/{configuration}",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=typing.Union[
                models.TerminalConfiguration, models.DeletedTerminalConfiguration
            ],
            request_options=request_options or default_request_options(),
        )
