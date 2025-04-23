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


class MandateNotificationsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def get(
        self,
        *,
        mandate_notification: str,
        source: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.SourceMandateNotification:
        """
        Retrieve a Source MandateNotification

        <p>Retrieves a new Source MandateNotification.</p>

        GET /v1/sources/{source}/mandate_notifications/{mandate_notification}

        Args:
            expand: Specifies which fields in the response should be expanded.
            mandate_notification: str
            source: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.source.mandate_notifications.get(
            mandate_notification="string", source="string"
        )
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
            path=f"/v1/sources/{source}/mandate_notifications/{mandate_notification}",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.SourceMandateNotification,
            request_options=request_options or default_request_options(),
        )


class AsyncMandateNotificationsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def get(
        self,
        *,
        mandate_notification: str,
        source: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.SourceMandateNotification:
        """
        Retrieve a Source MandateNotification

        <p>Retrieves a new Source MandateNotification.</p>

        GET /v1/sources/{source}/mandate_notifications/{mandate_notification}

        Args:
            expand: Specifies which fields in the response should be expanded.
            mandate_notification: str
            source: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.source.mandate_notifications.get(
            mandate_notification="string", source="string"
        )
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
            path=f"/v1/sources/{source}/mandate_notifications/{mandate_notification}",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.SourceMandateNotification,
            request_options=request_options or default_request_options(),
        )
