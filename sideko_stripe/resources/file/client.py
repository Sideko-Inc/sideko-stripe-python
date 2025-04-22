import httpx
import typing
import typing_extensions

from sideko_stripe.core import (
    AsyncBaseClient,
    QueryParams,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
    encode_query_param,
    filter_not_given,
    to_encodable,
    type_utils,
)
from sideko_stripe.types import models, params


class FileClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def list(
        self,
        *,
        created: typing.Union[
            typing.Optional[typing.Union[params.FileListCreatedObj0, int]],
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
        purpose: typing.Union[
            typing.Optional[
                typing_extensions.Literal[
                    "account_requirement",
                    "additional_verification",
                    "business_icon",
                    "business_logo",
                    "customer_signature",
                    "dispute_evidence",
                    "document_provider_identity_document",
                    "finance_report_run",
                    "financial_account_statement",
                    "identity_document",
                    "identity_document_downloadable",
                    "issuing_regulatory_reporting",
                    "pci_document",
                    "selfie",
                    "sigma_scheduled_query",
                    "tax_document_user_upload",
                    "terminal_reader_splashscreen",
                ]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        starting_after: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.FileListResponse:
        """
        List all files

        <p>Returns a list of the files that your account has access to. Stripe sorts and returns the files by their creation dates, placing the most recently created files at the top.</p>

        GET /v1/files

        Args:
            created: Only return files that were created during the given date interval.
            ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            expand: Specifies which fields in the response should be expanded.
            limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            purpose: Filter queries by the file purpose. If you don't provide a purpose, the queries return unfiltered files.
            starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.file.list()
        ```
        """
        models.FileListResponse.model_rebuild(_types_namespace=models._types_namespace)
        _query: QueryParams = {}
        if not isinstance(created, type_utils.NotGiven):
            encode_query_param(
                _query,
                "created",
                to_encodable(
                    item=created,
                    dump_with=typing.Union[params._SerializerFileListCreatedObj0, int],
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
        if not isinstance(purpose, type_utils.NotGiven):
            encode_query_param(
                _query,
                "purpose",
                to_encodable(
                    item=purpose,
                    dump_with=typing_extensions.Literal[
                        "account_requirement",
                        "additional_verification",
                        "business_icon",
                        "business_logo",
                        "customer_signature",
                        "dispute_evidence",
                        "document_provider_identity_document",
                        "finance_report_run",
                        "financial_account_statement",
                        "identity_document",
                        "identity_document_downloadable",
                        "issuing_regulatory_reporting",
                        "pci_document",
                        "selfie",
                        "sigma_scheduled_query",
                        "tax_document_user_upload",
                        "terminal_reader_splashscreen",
                    ],
                ),
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
            path="/v1/files",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.FileListResponse,
            request_options=request_options or default_request_options(),
        )

    def get(
        self,
        *,
        file: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.File:
        """
        Retrieve a file

        <p>Retrieves the details of an existing file object. After you supply a unique file ID, Stripe returns the corresponding file object. Learn how to <a href="/docs/file-upload#download-file-contents">access file contents</a>.</p>

        GET /v1/files/{file}

        Args:
            expand: Specifies which fields in the response should be expanded.
            file: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.file.get(file="string")
        ```
        """
        models.File.model_rebuild(_types_namespace=models._types_namespace)
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
            path=f"/v1/files/{file}",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.File,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        file: httpx._types.FileTypes,
        purpose: typing_extensions.Literal[
            "account_requirement",
            "additional_verification",
            "business_icon",
            "business_logo",
            "customer_signature",
            "dispute_evidence",
            "identity_document",
            "issuing_regulatory_reporting",
            "pci_document",
            "tax_document_user_upload",
            "terminal_reader_splashscreen",
        ],
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        file_link_data: typing.Union[
            typing.Optional[params.FileCreateBodyFileLinkData], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.File:
        """
        Create a file

        <p>To upload a file to Stripe, you need to send a request of type <code>multipart/form-data</code>. Include the file you want to upload in the request, and the parameters for creating a file.</p>

        <p>All of Stripe’s officially supported Client libraries support sending <code>multipart/form-data</code>.</p>

        POST /v1/files

        Args:
            expand: Specifies which fields in the response should be expanded.
            file_link_data: Optional parameters that automatically create a [file link](https://stripe.com/docs/api#file_links) for the newly created file.
            file: A file to upload. Make sure that the specifications follow RFC 2388, which defines file transfers for the `multipart/form-data` protocol.
            purpose: The [purpose](https://stripe.com/docs/file-upload#uploading-a-file) of the uploaded file.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.file.create(file=open("./file.txt", "rb"), purpose="account_requirement")
        ```
        """
        models.File.model_rebuild(_types_namespace=models._types_namespace)
        _data = to_encodable(
            item={
                "expand": expand,
                "file_link_data": file_link_data,
                "file": file,
                "purpose": purpose,
            },
            dump_with=params._SerializerFileCreateBody,
        )
        _files = params._SerializerFileCreateBody.get_files_from_typed_dict(
            filter_not_given(
                {
                    "expand": expand,
                    "file_link_data": file_link_data,
                    "file": file,
                    "purpose": purpose,
                }
            )
        )
        return self._base_client.request(
            method="POST",
            path="/v1/files",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            files=_files,
            cast_to=models.File,
            request_options=request_options or default_request_options(),
        )


class AsyncFileClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def list(
        self,
        *,
        created: typing.Union[
            typing.Optional[typing.Union[params.FileListCreatedObj0, int]],
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
        purpose: typing.Union[
            typing.Optional[
                typing_extensions.Literal[
                    "account_requirement",
                    "additional_verification",
                    "business_icon",
                    "business_logo",
                    "customer_signature",
                    "dispute_evidence",
                    "document_provider_identity_document",
                    "finance_report_run",
                    "financial_account_statement",
                    "identity_document",
                    "identity_document_downloadable",
                    "issuing_regulatory_reporting",
                    "pci_document",
                    "selfie",
                    "sigma_scheduled_query",
                    "tax_document_user_upload",
                    "terminal_reader_splashscreen",
                ]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        starting_after: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.FileListResponse:
        """
        List all files

        <p>Returns a list of the files that your account has access to. Stripe sorts and returns the files by their creation dates, placing the most recently created files at the top.</p>

        GET /v1/files

        Args:
            created: Only return files that were created during the given date interval.
            ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            expand: Specifies which fields in the response should be expanded.
            limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            purpose: Filter queries by the file purpose. If you don't provide a purpose, the queries return unfiltered files.
            starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.file.list()
        ```
        """
        models.FileListResponse.model_rebuild(_types_namespace=models._types_namespace)
        _query: QueryParams = {}
        if not isinstance(created, type_utils.NotGiven):
            encode_query_param(
                _query,
                "created",
                to_encodable(
                    item=created,
                    dump_with=typing.Union[params._SerializerFileListCreatedObj0, int],
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
        if not isinstance(purpose, type_utils.NotGiven):
            encode_query_param(
                _query,
                "purpose",
                to_encodable(
                    item=purpose,
                    dump_with=typing_extensions.Literal[
                        "account_requirement",
                        "additional_verification",
                        "business_icon",
                        "business_logo",
                        "customer_signature",
                        "dispute_evidence",
                        "document_provider_identity_document",
                        "finance_report_run",
                        "financial_account_statement",
                        "identity_document",
                        "identity_document_downloadable",
                        "issuing_regulatory_reporting",
                        "pci_document",
                        "selfie",
                        "sigma_scheduled_query",
                        "tax_document_user_upload",
                        "terminal_reader_splashscreen",
                    ],
                ),
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
            path="/v1/files",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.FileListResponse,
            request_options=request_options or default_request_options(),
        )

    async def get(
        self,
        *,
        file: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.File:
        """
        Retrieve a file

        <p>Retrieves the details of an existing file object. After you supply a unique file ID, Stripe returns the corresponding file object. Learn how to <a href="/docs/file-upload#download-file-contents">access file contents</a>.</p>

        GET /v1/files/{file}

        Args:
            expand: Specifies which fields in the response should be expanded.
            file: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.file.get(file="string")
        ```
        """
        models.File.model_rebuild(_types_namespace=models._types_namespace)
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
            path=f"/v1/files/{file}",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.File,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        file: httpx._types.FileTypes,
        purpose: typing_extensions.Literal[
            "account_requirement",
            "additional_verification",
            "business_icon",
            "business_logo",
            "customer_signature",
            "dispute_evidence",
            "identity_document",
            "issuing_regulatory_reporting",
            "pci_document",
            "tax_document_user_upload",
            "terminal_reader_splashscreen",
        ],
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        file_link_data: typing.Union[
            typing.Optional[params.FileCreateBodyFileLinkData], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.File:
        """
        Create a file

        <p>To upload a file to Stripe, you need to send a request of type <code>multipart/form-data</code>. Include the file you want to upload in the request, and the parameters for creating a file.</p>

        <p>All of Stripe’s officially supported Client libraries support sending <code>multipart/form-data</code>.</p>

        POST /v1/files

        Args:
            expand: Specifies which fields in the response should be expanded.
            file_link_data: Optional parameters that automatically create a [file link](https://stripe.com/docs/api#file_links) for the newly created file.
            file: A file to upload. Make sure that the specifications follow RFC 2388, which defines file transfers for the `multipart/form-data` protocol.
            purpose: The [purpose](https://stripe.com/docs/file-upload#uploading-a-file) of the uploaded file.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.file.create(
            file=open("./file.txt", "rb"), purpose="account_requirement"
        )
        ```
        """
        models.File.model_rebuild(_types_namespace=models._types_namespace)
        _data = to_encodable(
            item={
                "expand": expand,
                "file_link_data": file_link_data,
                "file": file,
                "purpose": purpose,
            },
            dump_with=params._SerializerFileCreateBody,
        )
        _files = params._SerializerFileCreateBody.get_files_from_typed_dict(
            filter_not_given(
                {
                    "expand": expand,
                    "file_link_data": file_link_data,
                    "file": file,
                    "purpose": purpose,
                }
            )
        )
        return await self._base_client.request(
            method="POST",
            path="/v1/files",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            files=_files,
            cast_to=models.File,
            request_options=request_options or default_request_options(),
        )
