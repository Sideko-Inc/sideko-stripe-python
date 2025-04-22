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


class FileLinkClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def list(
        self,
        *,
        created: typing.Union[
            typing.Optional[typing.Union[params.FileLinkListCreatedObj0, int]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        ending_before: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        expired: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        file: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        limit: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        starting_after: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.FileLinkListResponse:
        """
        List all file links

        <p>Returns a list of file links.</p>

        GET /v1/file_links

        Args:
            created: Only return links that were created during the given date interval.
            ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            expand: Specifies which fields in the response should be expanded.
            expired: Filter links by their expiration status. By default, Stripe returns all links.
            file: Only return links for the given file.
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
        client.file_link.list()
        ```
        """
        models.FileLinkListResponse.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _query: QueryParams = {}
        if not isinstance(created, type_utils.NotGiven):
            encode_query_param(
                _query,
                "created",
                to_encodable(
                    item=created,
                    dump_with=typing.Union[
                        params._SerializerFileLinkListCreatedObj0, int
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
        if not isinstance(expired, type_utils.NotGiven):
            encode_query_param(
                _query,
                "expired",
                to_encodable(item=expired, dump_with=bool),
                style="form",
                explode=True,
            )
        if not isinstance(file, type_utils.NotGiven):
            encode_query_param(
                _query,
                "file",
                to_encodable(item=file, dump_with=str),
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
            path="/v1/file_links",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.FileLinkListResponse,
            request_options=request_options or default_request_options(),
        )

    def get(
        self,
        *,
        link: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.FileLink:
        """
        Retrieve a file link

        <p>Retrieves the file link with the given ID.</p>

        GET /v1/file_links/{link}

        Args:
            expand: Specifies which fields in the response should be expanded.
            link: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.file_link.get(link="string")
        ```
        """
        models.FileLink.model_rebuild(_types_namespace=models._types_namespace)
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
            path=f"/v1/file_links/{link}",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.FileLink,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        file: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        expires_at: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        metadata: typing.Union[
            typing.Optional[typing.Union[params.FileLinkCreateBodyMetadataObj0, str]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.FileLink:
        """
        Create a file link

        <p>Creates a new file link object.</p>

        POST /v1/file_links

        Args:
            expand: Specifies which fields in the response should be expanded.
            expires_at: The link isn't usable after this future timestamp.
            metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
            file: The ID of the file. The file's `purpose` must be one of the following: `business_icon`, `business_logo`, `customer_signature`, `dispute_evidence`, `finance_report_run`, `financial_account_statement`, `identity_document_downloadable`, `issuing_regulatory_reporting`, `pci_document`, `selfie`, `sigma_scheduled_query`, `tax_document_user_upload`, or `terminal_reader_splashscreen`.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.file_link.create(file="string")
        ```
        """
        models.FileLink.model_rebuild(_types_namespace=models._types_namespace)
        _data = to_form_urlencoded(
            item={
                "expand": expand,
                "expires_at": expires_at,
                "metadata": metadata,
                "file": file,
            },
            dump_with=params._SerializerFileLinkCreateBody,
            style={
                "expand": "deepObject",
                "expires_at": "form",
                "file": "form",
                "metadata": "deepObject",
            },
            explode={
                "expand": True,
                "expires_at": True,
                "file": True,
                "metadata": True,
            },
        )
        return self._base_client.request(
            method="POST",
            path="/v1/file_links",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.FileLink,
            request_options=request_options or default_request_options(),
        )

    def update(
        self,
        *,
        link: str,
        data: typing.Union[
            typing.Optional[params.FileLinkUpdateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.FileLink:
        """
        Update a file link

        <p>Updates an existing file link object. Expired links can no longer be updated.</p>

        POST /v1/file_links/{link}

        Args:
            data: FileLinkUpdateBody
            link: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.file_link.update(link="string")
        ```
        """
        models.FileLink.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerFileLinkUpdateBody,
                style={
                    "expand": "deepObject",
                    "expires_at": "deepObject",
                    "metadata": "deepObject",
                },
                explode={"expand": True, "expires_at": True, "metadata": True},
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/file_links/{link}",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.FileLink,
            request_options=request_options or default_request_options(),
        )


class AsyncFileLinkClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def list(
        self,
        *,
        created: typing.Union[
            typing.Optional[typing.Union[params.FileLinkListCreatedObj0, int]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        ending_before: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        expired: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        file: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        limit: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        starting_after: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.FileLinkListResponse:
        """
        List all file links

        <p>Returns a list of file links.</p>

        GET /v1/file_links

        Args:
            created: Only return links that were created during the given date interval.
            ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            expand: Specifies which fields in the response should be expanded.
            expired: Filter links by their expiration status. By default, Stripe returns all links.
            file: Only return links for the given file.
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
        await client.file_link.list()
        ```
        """
        models.FileLinkListResponse.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _query: QueryParams = {}
        if not isinstance(created, type_utils.NotGiven):
            encode_query_param(
                _query,
                "created",
                to_encodable(
                    item=created,
                    dump_with=typing.Union[
                        params._SerializerFileLinkListCreatedObj0, int
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
        if not isinstance(expired, type_utils.NotGiven):
            encode_query_param(
                _query,
                "expired",
                to_encodable(item=expired, dump_with=bool),
                style="form",
                explode=True,
            )
        if not isinstance(file, type_utils.NotGiven):
            encode_query_param(
                _query,
                "file",
                to_encodable(item=file, dump_with=str),
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
            path="/v1/file_links",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.FileLinkListResponse,
            request_options=request_options or default_request_options(),
        )

    async def get(
        self,
        *,
        link: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.FileLink:
        """
        Retrieve a file link

        <p>Retrieves the file link with the given ID.</p>

        GET /v1/file_links/{link}

        Args:
            expand: Specifies which fields in the response should be expanded.
            link: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.file_link.get(link="string")
        ```
        """
        models.FileLink.model_rebuild(_types_namespace=models._types_namespace)
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
            path=f"/v1/file_links/{link}",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.FileLink,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        file: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        expires_at: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        metadata: typing.Union[
            typing.Optional[typing.Union[params.FileLinkCreateBodyMetadataObj0, str]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.FileLink:
        """
        Create a file link

        <p>Creates a new file link object.</p>

        POST /v1/file_links

        Args:
            expand: Specifies which fields in the response should be expanded.
            expires_at: The link isn't usable after this future timestamp.
            metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
            file: The ID of the file. The file's `purpose` must be one of the following: `business_icon`, `business_logo`, `customer_signature`, `dispute_evidence`, `finance_report_run`, `financial_account_statement`, `identity_document_downloadable`, `issuing_regulatory_reporting`, `pci_document`, `selfie`, `sigma_scheduled_query`, `tax_document_user_upload`, or `terminal_reader_splashscreen`.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.file_link.create(file="string")
        ```
        """
        models.FileLink.model_rebuild(_types_namespace=models._types_namespace)
        _data = to_form_urlencoded(
            item={
                "expand": expand,
                "expires_at": expires_at,
                "metadata": metadata,
                "file": file,
            },
            dump_with=params._SerializerFileLinkCreateBody,
            style={
                "expand": "deepObject",
                "expires_at": "form",
                "file": "form",
                "metadata": "deepObject",
            },
            explode={
                "expand": True,
                "expires_at": True,
                "file": True,
                "metadata": True,
            },
        )
        return await self._base_client.request(
            method="POST",
            path="/v1/file_links",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.FileLink,
            request_options=request_options or default_request_options(),
        )

    async def update(
        self,
        *,
        link: str,
        data: typing.Union[
            typing.Optional[params.FileLinkUpdateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.FileLink:
        """
        Update a file link

        <p>Updates an existing file link object. Expired links can no longer be updated.</p>

        POST /v1/file_links/{link}

        Args:
            data: FileLinkUpdateBody
            link: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.file_link.update(link="string")
        ```
        """
        models.FileLink.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerFileLinkUpdateBody,
                style={
                    "expand": "deepObject",
                    "expires_at": "deepObject",
                    "metadata": "deepObject",
                },
                explode={"expand": True, "expires_at": True, "metadata": True},
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/file_links/{link}",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.FileLink,
            request_options=request_options or default_request_options(),
        )
