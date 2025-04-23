import typing
import typing_extensions

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


class RegistrationClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

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
        status: typing.Union[
            typing.Optional[
                typing_extensions.Literal["active", "all", "expired", "scheduled"]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TaxRegistrationListResponse:
        """
        List registrations

        <p>Returns a list of Tax <code>Registration</code> objects.</p>

        GET /v1/tax/registrations

        Args:
            ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            expand: Specifies which fields in the response should be expanded.
            limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
            status: The status of the Tax Registration.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.tax.registration.list()
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
        if not isinstance(status, type_utils.NotGiven):
            encode_query_param(
                _query,
                "status",
                to_encodable(
                    item=status,
                    dump_with=typing_extensions.Literal[
                        "active", "all", "expired", "scheduled"
                    ],
                ),
                style="form",
                explode=True,
            )
        return self._base_client.request(
            method="GET",
            path="/v1/tax/registrations",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.TaxRegistrationListResponse,
            request_options=request_options or default_request_options(),
        )

    def get(
        self,
        *,
        id: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TaxRegistration:
        """
        Retrieve a registration

        <p>Returns a Tax <code>Registration</code> object.</p>

        GET /v1/tax/registrations/{id}

        Args:
            expand: Specifies which fields in the response should be expanded.
            id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.tax.registration.get(id="string")
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
            path=f"/v1/tax/registrations/{id}",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.TaxRegistration,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        active_from: typing.Union[typing_extensions.Literal["now"], int],
        country: str,
        country_options: params.TaxRegistrationCreateBodyCountryOptions,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        expires_at: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TaxRegistration:
        """
        Create a registration

        <p>Creates a new Tax <code>Registration</code> object.</p>

        POST /v1/tax/registrations

        Args:
            expand: Specifies which fields in the response should be expanded.
            expires_at: If set, the Tax Registration stops being active at this time. If not set, the Tax Registration will be active indefinitely. Timestamp measured in seconds since the Unix epoch.
            active_from: Time at which the Tax Registration becomes active. It can be either `now` to indicate the current time, or a future timestamp measured in seconds since the Unix epoch.
            country: Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
            country_options: Specific options for a registration in the specified `country`.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.tax.registration.create(
            active_from="now", country="string", country_options={}
        )
        ```
        """
        _data = to_form_urlencoded(
            item={
                "expand": expand,
                "expires_at": expires_at,
                "active_from": active_from,
                "country": country,
                "country_options": country_options,
            },
            dump_with=params._SerializerTaxRegistrationCreateBody,
            style={
                "active_from": "deepObject",
                "country": "form",
                "country_options": "deepObject",
                "expand": "deepObject",
                "expires_at": "form",
            },
            explode={
                "active_from": True,
                "country": True,
                "country_options": True,
                "expand": True,
                "expires_at": True,
            },
        )
        return self._base_client.request(
            method="POST",
            path="/v1/tax/registrations",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.TaxRegistration,
            request_options=request_options or default_request_options(),
        )

    def update(
        self,
        *,
        id: str,
        data: typing.Union[
            typing.Optional[params.TaxRegistrationUpdateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TaxRegistration:
        """
        Update a registration

        <p>Updates an existing Tax <code>Registration</code> object.</p>

        <p>A registration cannot be deleted after it has been created. If you wish to end a registration you may do so by setting <code>expires_at</code>.</p>

        POST /v1/tax/registrations/{id}

        Args:
            data: TaxRegistrationUpdateBody
            id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.tax.registration.update(id="string")
        ```
        """
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerTaxRegistrationUpdateBody,
                style={
                    "active_from": "deepObject",
                    "expand": "deepObject",
                    "expires_at": "deepObject",
                },
                explode={"active_from": True, "expand": True, "expires_at": True},
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/tax/registrations/{id}",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.TaxRegistration,
            request_options=request_options or default_request_options(),
        )


class AsyncRegistrationClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

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
        status: typing.Union[
            typing.Optional[
                typing_extensions.Literal["active", "all", "expired", "scheduled"]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TaxRegistrationListResponse:
        """
        List registrations

        <p>Returns a list of Tax <code>Registration</code> objects.</p>

        GET /v1/tax/registrations

        Args:
            ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            expand: Specifies which fields in the response should be expanded.
            limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
            status: The status of the Tax Registration.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.tax.registration.list()
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
        if not isinstance(status, type_utils.NotGiven):
            encode_query_param(
                _query,
                "status",
                to_encodable(
                    item=status,
                    dump_with=typing_extensions.Literal[
                        "active", "all", "expired", "scheduled"
                    ],
                ),
                style="form",
                explode=True,
            )
        return await self._base_client.request(
            method="GET",
            path="/v1/tax/registrations",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.TaxRegistrationListResponse,
            request_options=request_options or default_request_options(),
        )

    async def get(
        self,
        *,
        id: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TaxRegistration:
        """
        Retrieve a registration

        <p>Returns a Tax <code>Registration</code> object.</p>

        GET /v1/tax/registrations/{id}

        Args:
            expand: Specifies which fields in the response should be expanded.
            id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.tax.registration.get(id="string")
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
            path=f"/v1/tax/registrations/{id}",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.TaxRegistration,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        active_from: typing.Union[typing_extensions.Literal["now"], int],
        country: str,
        country_options: params.TaxRegistrationCreateBodyCountryOptions,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        expires_at: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TaxRegistration:
        """
        Create a registration

        <p>Creates a new Tax <code>Registration</code> object.</p>

        POST /v1/tax/registrations

        Args:
            expand: Specifies which fields in the response should be expanded.
            expires_at: If set, the Tax Registration stops being active at this time. If not set, the Tax Registration will be active indefinitely. Timestamp measured in seconds since the Unix epoch.
            active_from: Time at which the Tax Registration becomes active. It can be either `now` to indicate the current time, or a future timestamp measured in seconds since the Unix epoch.
            country: Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
            country_options: Specific options for a registration in the specified `country`.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.tax.registration.create(
            active_from="now", country="string", country_options={}
        )
        ```
        """
        _data = to_form_urlencoded(
            item={
                "expand": expand,
                "expires_at": expires_at,
                "active_from": active_from,
                "country": country,
                "country_options": country_options,
            },
            dump_with=params._SerializerTaxRegistrationCreateBody,
            style={
                "active_from": "deepObject",
                "country": "form",
                "country_options": "deepObject",
                "expand": "deepObject",
                "expires_at": "form",
            },
            explode={
                "active_from": True,
                "country": True,
                "country_options": True,
                "expand": True,
                "expires_at": True,
            },
        )
        return await self._base_client.request(
            method="POST",
            path="/v1/tax/registrations",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.TaxRegistration,
            request_options=request_options or default_request_options(),
        )

    async def update(
        self,
        *,
        id: str,
        data: typing.Union[
            typing.Optional[params.TaxRegistrationUpdateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.TaxRegistration:
        """
        Update a registration

        <p>Updates an existing Tax <code>Registration</code> object.</p>

        <p>A registration cannot be deleted after it has been created. If you wish to end a registration you may do so by setting <code>expires_at</code>.</p>

        POST /v1/tax/registrations/{id}

        Args:
            data: TaxRegistrationUpdateBody
            id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.tax.registration.update(id="string")
        ```
        """
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerTaxRegistrationUpdateBody,
                style={
                    "active_from": "deepObject",
                    "expand": "deepObject",
                    "expires_at": "deepObject",
                },
                explode={"active_from": True, "expand": True, "expires_at": True},
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/tax/registrations/{id}",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.TaxRegistration,
            request_options=request_options or default_request_options(),
        )
