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


class SuppliersClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def get(
        self,
        *,
        supplier: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ClimateSupplier:
        """
        Retrieve a supplier

        <p>Retrieves a Climate supplier object.</p>

        GET /v1/climate/suppliers/{supplier}

        Args:
            expand: Specifies which fields in the response should be expanded.
            supplier: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.climate.suppliers.get(supplier="string")
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
            path=f"/v1/climate/suppliers/{supplier}",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.ClimateSupplier,
            request_options=request_options or default_request_options(),
        )


class AsyncSuppliersClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def get(
        self,
        *,
        supplier: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ClimateSupplier:
        """
        Retrieve a supplier

        <p>Retrieves a Climate supplier object.</p>

        GET /v1/climate/suppliers/{supplier}

        Args:
            expand: Specifies which fields in the response should be expanded.
            supplier: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.climate.suppliers.get(supplier="string")
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
            path=f"/v1/climate/suppliers/{supplier}",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.ClimateSupplier,
            request_options=request_options or default_request_options(),
        )
