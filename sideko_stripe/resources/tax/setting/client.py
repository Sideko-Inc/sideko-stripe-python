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


class SettingClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def list(
        self,
        *,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TaxSettings:
        """
        Retrieve settings

        <p>Retrieves Tax <code>Settings</code> for a merchant.</p>

        GET /v1/tax/settings

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
        client.tax.setting.list()
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
            path="/v1/tax/settings",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.TaxSettings,
            request_options=request_options or default_request_options(),
        )

    def update(
        self,
        *,
        data: typing.Union[
            typing.Optional[params.TaxSettingUpdateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TaxSettings:
        """
        Update settings

        <p>Updates Tax <code>Settings</code> parameters used in tax calculations. All parameters are editable but none can be removed once set.</p>

        POST /v1/tax/settings

        Args:
            data: TaxSettingUpdateBody
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.tax.setting.update()
        ```
        """
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerTaxSettingUpdateBody,
                style={
                    "defaults": "deepObject",
                    "expand": "deepObject",
                    "head_office": "deepObject",
                },
                explode={"defaults": True, "expand": True, "head_office": True},
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path="/v1/tax/settings",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.TaxSettings,
            request_options=request_options or default_request_options(),
        )


class AsyncSettingClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def list(
        self,
        *,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TaxSettings:
        """
        Retrieve settings

        <p>Retrieves Tax <code>Settings</code> for a merchant.</p>

        GET /v1/tax/settings

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
        await client.tax.setting.list()
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
            path="/v1/tax/settings",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.TaxSettings,
            request_options=request_options or default_request_options(),
        )

    async def update(
        self,
        *,
        data: typing.Union[
            typing.Optional[params.TaxSettingUpdateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TaxSettings:
        """
        Update settings

        <p>Updates Tax <code>Settings</code> parameters used in tax calculations. All parameters are editable but none can be removed once set.</p>

        POST /v1/tax/settings

        Args:
            data: TaxSettingUpdateBody
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.tax.setting.update()
        ```
        """
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerTaxSettingUpdateBody,
                style={
                    "defaults": "deepObject",
                    "expand": "deepObject",
                    "head_office": "deepObject",
                },
                explode={"defaults": True, "expand": True, "head_office": True},
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path="/v1/tax/settings",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.TaxSettings,
            request_options=request_options or default_request_options(),
        )
