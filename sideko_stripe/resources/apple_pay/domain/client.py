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


class DomainClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def delete(
        self, *, domain: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.DeletedApplePayDomain:
        """
        <p>Delete an apple pay domain.</p>

        DELETE /v1/apple_pay/domains/{domain}

        Args:
            domain: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.apple_pay.domain.delete(domain="string")
        ```
        """
        return self._base_client.request(
            method="DELETE",
            path=f"/v1/apple_pay/domains/{domain}",
            auth_names=["basicAuth", "bearerAuth"],
            cast_to=models.DeletedApplePayDomain,
            request_options=request_options or default_request_options(),
        )

    def list(
        self,
        *,
        domain_name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
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
    ) -> models.ApplePayDomainListResponse:
        """
        <p>List apple pay domains.</p>

        GET /v1/apple_pay/domains

        Args:
            domain_name: str
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
        client.apple_pay.domain.list()
        ```
        """
        _query: QueryParams = {}
        if not isinstance(domain_name, type_utils.NotGiven):
            encode_query_param(
                _query,
                "domain_name",
                to_encodable(item=domain_name, dump_with=str),
                style="form",
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
            path="/v1/apple_pay/domains",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.ApplePayDomainListResponse,
            request_options=request_options or default_request_options(),
        )

    def get(
        self,
        *,
        domain: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ApplePayDomain:
        """
        <p>Retrieve an apple pay domain.</p>

        GET /v1/apple_pay/domains/{domain}

        Args:
            expand: Specifies which fields in the response should be expanded.
            domain: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.apple_pay.domain.get(domain="string")
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
            path=f"/v1/apple_pay/domains/{domain}",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.ApplePayDomain,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        domain_name: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ApplePayDomain:
        """
        <p>Create an apple pay domain.</p>

        POST /v1/apple_pay/domains

        Args:
            expand: Specifies which fields in the response should be expanded.
            domain_name: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.apple_pay.domain.create(domain_name="string")
        ```
        """
        _data = to_form_urlencoded(
            item={"expand": expand, "domain_name": domain_name},
            dump_with=params._SerializerApplePayDomainCreateBody,
            style={"domain_name": "form", "expand": "deepObject"},
            explode={"domain_name": True, "expand": True},
        )
        return self._base_client.request(
            method="POST",
            path="/v1/apple_pay/domains",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.ApplePayDomain,
            request_options=request_options or default_request_options(),
        )


class AsyncDomainClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def delete(
        self, *, domain: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.DeletedApplePayDomain:
        """
        <p>Delete an apple pay domain.</p>

        DELETE /v1/apple_pay/domains/{domain}

        Args:
            domain: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.apple_pay.domain.delete(domain="string")
        ```
        """
        return await self._base_client.request(
            method="DELETE",
            path=f"/v1/apple_pay/domains/{domain}",
            auth_names=["basicAuth", "bearerAuth"],
            cast_to=models.DeletedApplePayDomain,
            request_options=request_options or default_request_options(),
        )

    async def list(
        self,
        *,
        domain_name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
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
    ) -> models.ApplePayDomainListResponse:
        """
        <p>List apple pay domains.</p>

        GET /v1/apple_pay/domains

        Args:
            domain_name: str
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
        await client.apple_pay.domain.list()
        ```
        """
        _query: QueryParams = {}
        if not isinstance(domain_name, type_utils.NotGiven):
            encode_query_param(
                _query,
                "domain_name",
                to_encodable(item=domain_name, dump_with=str),
                style="form",
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
            path="/v1/apple_pay/domains",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.ApplePayDomainListResponse,
            request_options=request_options or default_request_options(),
        )

    async def get(
        self,
        *,
        domain: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ApplePayDomain:
        """
        <p>Retrieve an apple pay domain.</p>

        GET /v1/apple_pay/domains/{domain}

        Args:
            expand: Specifies which fields in the response should be expanded.
            domain: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.apple_pay.domain.get(domain="string")
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
            path=f"/v1/apple_pay/domains/{domain}",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.ApplePayDomain,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        domain_name: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ApplePayDomain:
        """
        <p>Create an apple pay domain.</p>

        POST /v1/apple_pay/domains

        Args:
            expand: Specifies which fields in the response should be expanded.
            domain_name: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.apple_pay.domain.create(domain_name="string")
        ```
        """
        _data = to_form_urlencoded(
            item={"expand": expand, "domain_name": domain_name},
            dump_with=params._SerializerApplePayDomainCreateBody,
            style={"domain_name": "form", "expand": "deepObject"},
            explode={"domain_name": True, "expand": True},
        )
        return await self._base_client.request(
            method="POST",
            path="/v1/apple_pay/domains",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.ApplePayDomain,
            request_options=request_options or default_request_options(),
        )
