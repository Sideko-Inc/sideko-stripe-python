import typing

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


class ReportTypeClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def list(
        self,
        *,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ReportingReportTypeListResponse:
        """
        List all Report Types

        <p>Returns a full list of Report Types.</p>

        GET /v1/reporting/report_types

        Args:
            expand: Specifies which fields in the response should be expanded.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.reporting.report_type.list()
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
            path="/v1/reporting/report_types",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.ReportingReportTypeListResponse,
            request_options=request_options or default_request_options(),
        )

    def get(
        self,
        *,
        report_type: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ReportingReportType:
        """
        Retrieve a Report Type

        <p>Retrieves the details of a Report Type. (Certain report types require a <a href="https://stripe.com/docs/keys#test-live-modes">live-mode API key</a>.)</p>

        GET /v1/reporting/report_types/{report_type}

        Args:
            expand: Specifies which fields in the response should be expanded.
            report_type: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.reporting.report_type.get(report_type="string")
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
            path=f"/v1/reporting/report_types/{report_type}",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.ReportingReportType,
            request_options=request_options or default_request_options(),
        )


class AsyncReportTypeClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def list(
        self,
        *,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ReportingReportTypeListResponse:
        """
        List all Report Types

        <p>Returns a full list of Report Types.</p>

        GET /v1/reporting/report_types

        Args:
            expand: Specifies which fields in the response should be expanded.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.reporting.report_type.list()
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
            path="/v1/reporting/report_types",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.ReportingReportTypeListResponse,
            request_options=request_options or default_request_options(),
        )

    async def get(
        self,
        *,
        report_type: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ReportingReportType:
        """
        Retrieve a Report Type

        <p>Retrieves the details of a Report Type. (Certain report types require a <a href="https://stripe.com/docs/keys#test-live-modes">live-mode API key</a>.)</p>

        GET /v1/reporting/report_types/{report_type}

        Args:
            expand: Specifies which fields in the response should be expanded.
            report_type: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.reporting.report_type.get(report_type="string")
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
            path=f"/v1/reporting/report_types/{report_type}",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.ReportingReportType,
            request_options=request_options or default_request_options(),
        )
