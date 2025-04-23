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


class SettlementClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def get(
        self,
        *,
        settlement: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.IssuingSettlement:
        """
        Retrieve a settlement

        <p>Retrieves an Issuing <code>Settlement</code> object.</p>

        GET /v1/issuing/settlements/{settlement}

        Args:
            expand: Specifies which fields in the response should be expanded.
            settlement: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.issuing.settlement.get(settlement="string")
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
            path=f"/v1/issuing/settlements/{settlement}",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.IssuingSettlement,
            request_options=request_options or default_request_options(),
        )

    def update(
        self,
        *,
        settlement: str,
        data: typing.Union[
            typing.Optional[params.IssuingSettlementUpdateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.IssuingSettlement:
        """
        Update a settlement

        <p>Updates the specified Issuing <code>Settlement</code> object by setting the values of the parameters passed. Any parameters not provided will be left unchanged.</p>

        POST /v1/issuing/settlements/{settlement}

        Args:
            data: IssuingSettlementUpdateBody
            settlement: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.issuing.settlement.update(settlement="string")
        ```
        """
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerIssuingSettlementUpdateBody,
                style={"expand": "deepObject", "metadata": "deepObject"},
                explode={"expand": True, "metadata": True},
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/issuing/settlements/{settlement}",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.IssuingSettlement,
            request_options=request_options or default_request_options(),
        )


class AsyncSettlementClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def get(
        self,
        *,
        settlement: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.IssuingSettlement:
        """
        Retrieve a settlement

        <p>Retrieves an Issuing <code>Settlement</code> object.</p>

        GET /v1/issuing/settlements/{settlement}

        Args:
            expand: Specifies which fields in the response should be expanded.
            settlement: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.issuing.settlement.get(settlement="string")
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
            path=f"/v1/issuing/settlements/{settlement}",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.IssuingSettlement,
            request_options=request_options or default_request_options(),
        )

    async def update(
        self,
        *,
        settlement: str,
        data: typing.Union[
            typing.Optional[params.IssuingSettlementUpdateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.IssuingSettlement:
        """
        Update a settlement

        <p>Updates the specified Issuing <code>Settlement</code> object by setting the values of the parameters passed. Any parameters not provided will be left unchanged.</p>

        POST /v1/issuing/settlements/{settlement}

        Args:
            data: IssuingSettlementUpdateBody
            settlement: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.issuing.settlement.update(settlement="string")
        ```
        """
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerIssuingSettlementUpdateBody,
                style={"expand": "deepObject", "metadata": "deepObject"},
                explode={"expand": True, "metadata": True},
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/issuing/settlements/{settlement}",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.IssuingSettlement,
            request_options=request_options or default_request_options(),
        )
