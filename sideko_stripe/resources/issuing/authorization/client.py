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


class AuthorizationClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def list(
        self,
        *,
        card: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        cardholder: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        created: typing.Union[
            typing.Optional[
                typing.Union[params.IssuingAuthorizationListCreatedObj0, int]
            ],
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
        starting_after: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        status: typing.Union[
            typing.Optional[
                typing_extensions.Literal["closed", "expired", "pending", "reversed"]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.IssuingAuthorizationListResponse:
        """
        List all authorizations

        <p>Returns a list of Issuing <code>Authorization</code> objects. The objects are sorted in descending order by creation date, with the most recently created object appearing first.</p>

        GET /v1/issuing/authorizations

        Args:
            card: Only return authorizations that belong to the given card.
            cardholder: Only return authorizations that belong to the given cardholder.
            created: Only return authorizations that were created during the given date interval.
            ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            expand: Specifies which fields in the response should be expanded.
            limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
            status: Only return authorizations with the given status. One of `pending`, `closed`, or `reversed`.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.issuing.authorization.list()
        ```
        """
        models.IssuingAuthorizationListResponse.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _query: QueryParams = {}
        if not isinstance(card, type_utils.NotGiven):
            encode_query_param(
                _query,
                "card",
                to_encodable(item=card, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(cardholder, type_utils.NotGiven):
            encode_query_param(
                _query,
                "cardholder",
                to_encodable(item=cardholder, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(created, type_utils.NotGiven):
            encode_query_param(
                _query,
                "created",
                to_encodable(
                    item=created,
                    dump_with=typing.Union[
                        params._SerializerIssuingAuthorizationListCreatedObj0, int
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
                        "closed", "expired", "pending", "reversed"
                    ],
                ),
                style="form",
                explode=True,
            )
        return self._base_client.request(
            method="GET",
            path="/v1/issuing/authorizations",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.IssuingAuthorizationListResponse,
            request_options=request_options or default_request_options(),
        )

    def get(
        self,
        *,
        authorization: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.IssuingAuthorization:
        """
        Retrieve an authorization

        <p>Retrieves an Issuing <code>Authorization</code> object.</p>

        GET /v1/issuing/authorizations/{authorization}

        Args:
            expand: Specifies which fields in the response should be expanded.
            authorization: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.issuing.authorization.get(authorization="string")
        ```
        """
        models.IssuingAuthorization.model_rebuild(
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
            path=f"/v1/issuing/authorizations/{authorization}",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.IssuingAuthorization,
            request_options=request_options or default_request_options(),
        )

    def update(
        self,
        *,
        authorization: str,
        data: typing.Union[
            typing.Optional[params.IssuingAuthorizationUpdateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.IssuingAuthorization:
        """
        Update an authorization

        <p>Updates the specified Issuing <code>Authorization</code> object by setting the values of the parameters passed. Any parameters not provided will be left unchanged.</p>

        POST /v1/issuing/authorizations/{authorization}

        Args:
            data: IssuingAuthorizationUpdateBody
            authorization: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.issuing.authorization.update(authorization="string")
        ```
        """
        models.IssuingAuthorization.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerIssuingAuthorizationUpdateBody,
                style={"expand": "deepObject", "metadata": "deepObject"},
                explode={"expand": True, "metadata": True},
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/issuing/authorizations/{authorization}",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.IssuingAuthorization,
            request_options=request_options or default_request_options(),
        )

    def approve(
        self,
        *,
        authorization: str,
        data: typing.Union[
            typing.Optional[params.IssuingAuthorizationApproveBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.IssuingAuthorization:
        """
        Approve an authorization

        <p>[Deprecated] Approves a pending Issuing <code>Authorization</code> object. This request should be made within the timeout window of the <a href="/docs/issuing/controls/real-time-authorizations">real-time authorization</a> flow.
        This method is deprecated. Instead, <a href="/docs/issuing/controls/real-time-authorizations#authorization-handling">respond directly to the webhook request to approve an authorization</a>.</p>

        POST /v1/issuing/authorizations/{authorization}/approve

        Args:
            data: IssuingAuthorizationApproveBody
            authorization: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.issuing.authorization.approve(authorization="string")
        ```
        """
        models.IssuingAuthorization.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerIssuingAuthorizationApproveBody,
                style={
                    "amount": "form",
                    "expand": "deepObject",
                    "metadata": "deepObject",
                },
                explode={"amount": True, "expand": True, "metadata": True},
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/issuing/authorizations/{authorization}/approve",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.IssuingAuthorization,
            request_options=request_options or default_request_options(),
        )

    def decline(
        self,
        *,
        authorization: str,
        data: typing.Union[
            typing.Optional[params.IssuingAuthorizationDeclineBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.IssuingAuthorization:
        """
        Decline an authorization

        <p>[Deprecated] Declines a pending Issuing <code>Authorization</code> object. This request should be made within the timeout window of the <a href="/docs/issuing/controls/real-time-authorizations">real time authorization</a> flow.
        This method is deprecated. Instead, <a href="/docs/issuing/controls/real-time-authorizations#authorization-handling">respond directly to the webhook request to decline an authorization</a>.</p>

        POST /v1/issuing/authorizations/{authorization}/decline

        Args:
            data: IssuingAuthorizationDeclineBody
            authorization: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.issuing.authorization.decline(authorization="string")
        ```
        """
        models.IssuingAuthorization.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerIssuingAuthorizationDeclineBody,
                style={"expand": "deepObject", "metadata": "deepObject"},
                explode={"expand": True, "metadata": True},
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/issuing/authorizations/{authorization}/decline",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.IssuingAuthorization,
            request_options=request_options or default_request_options(),
        )


class AsyncAuthorizationClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def list(
        self,
        *,
        card: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        cardholder: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        created: typing.Union[
            typing.Optional[
                typing.Union[params.IssuingAuthorizationListCreatedObj0, int]
            ],
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
        starting_after: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        status: typing.Union[
            typing.Optional[
                typing_extensions.Literal["closed", "expired", "pending", "reversed"]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.IssuingAuthorizationListResponse:
        """
        List all authorizations

        <p>Returns a list of Issuing <code>Authorization</code> objects. The objects are sorted in descending order by creation date, with the most recently created object appearing first.</p>

        GET /v1/issuing/authorizations

        Args:
            card: Only return authorizations that belong to the given card.
            cardholder: Only return authorizations that belong to the given cardholder.
            created: Only return authorizations that were created during the given date interval.
            ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            expand: Specifies which fields in the response should be expanded.
            limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
            status: Only return authorizations with the given status. One of `pending`, `closed`, or `reversed`.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.issuing.authorization.list()
        ```
        """
        models.IssuingAuthorizationListResponse.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _query: QueryParams = {}
        if not isinstance(card, type_utils.NotGiven):
            encode_query_param(
                _query,
                "card",
                to_encodable(item=card, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(cardholder, type_utils.NotGiven):
            encode_query_param(
                _query,
                "cardholder",
                to_encodable(item=cardholder, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(created, type_utils.NotGiven):
            encode_query_param(
                _query,
                "created",
                to_encodable(
                    item=created,
                    dump_with=typing.Union[
                        params._SerializerIssuingAuthorizationListCreatedObj0, int
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
                        "closed", "expired", "pending", "reversed"
                    ],
                ),
                style="form",
                explode=True,
            )
        return await self._base_client.request(
            method="GET",
            path="/v1/issuing/authorizations",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.IssuingAuthorizationListResponse,
            request_options=request_options or default_request_options(),
        )

    async def get(
        self,
        *,
        authorization: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.IssuingAuthorization:
        """
        Retrieve an authorization

        <p>Retrieves an Issuing <code>Authorization</code> object.</p>

        GET /v1/issuing/authorizations/{authorization}

        Args:
            expand: Specifies which fields in the response should be expanded.
            authorization: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.issuing.authorization.get(authorization="string")
        ```
        """
        models.IssuingAuthorization.model_rebuild(
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
            path=f"/v1/issuing/authorizations/{authorization}",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.IssuingAuthorization,
            request_options=request_options or default_request_options(),
        )

    async def update(
        self,
        *,
        authorization: str,
        data: typing.Union[
            typing.Optional[params.IssuingAuthorizationUpdateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.IssuingAuthorization:
        """
        Update an authorization

        <p>Updates the specified Issuing <code>Authorization</code> object by setting the values of the parameters passed. Any parameters not provided will be left unchanged.</p>

        POST /v1/issuing/authorizations/{authorization}

        Args:
            data: IssuingAuthorizationUpdateBody
            authorization: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.issuing.authorization.update(authorization="string")
        ```
        """
        models.IssuingAuthorization.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerIssuingAuthorizationUpdateBody,
                style={"expand": "deepObject", "metadata": "deepObject"},
                explode={"expand": True, "metadata": True},
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/issuing/authorizations/{authorization}",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.IssuingAuthorization,
            request_options=request_options or default_request_options(),
        )

    async def approve(
        self,
        *,
        authorization: str,
        data: typing.Union[
            typing.Optional[params.IssuingAuthorizationApproveBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.IssuingAuthorization:
        """
        Approve an authorization

        <p>[Deprecated] Approves a pending Issuing <code>Authorization</code> object. This request should be made within the timeout window of the <a href="/docs/issuing/controls/real-time-authorizations">real-time authorization</a> flow.
        This method is deprecated. Instead, <a href="/docs/issuing/controls/real-time-authorizations#authorization-handling">respond directly to the webhook request to approve an authorization</a>.</p>

        POST /v1/issuing/authorizations/{authorization}/approve

        Args:
            data: IssuingAuthorizationApproveBody
            authorization: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.issuing.authorization.approve(authorization="string")
        ```
        """
        models.IssuingAuthorization.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerIssuingAuthorizationApproveBody,
                style={
                    "amount": "form",
                    "expand": "deepObject",
                    "metadata": "deepObject",
                },
                explode={"amount": True, "expand": True, "metadata": True},
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/issuing/authorizations/{authorization}/approve",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.IssuingAuthorization,
            request_options=request_options or default_request_options(),
        )

    async def decline(
        self,
        *,
        authorization: str,
        data: typing.Union[
            typing.Optional[params.IssuingAuthorizationDeclineBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.IssuingAuthorization:
        """
        Decline an authorization

        <p>[Deprecated] Declines a pending Issuing <code>Authorization</code> object. This request should be made within the timeout window of the <a href="/docs/issuing/controls/real-time-authorizations">real time authorization</a> flow.
        This method is deprecated. Instead, <a href="/docs/issuing/controls/real-time-authorizations#authorization-handling">respond directly to the webhook request to decline an authorization</a>.</p>

        POST /v1/issuing/authorizations/{authorization}/decline

        Args:
            data: IssuingAuthorizationDeclineBody
            authorization: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.issuing.authorization.decline(authorization="string")
        ```
        """
        models.IssuingAuthorization.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerIssuingAuthorizationDeclineBody,
                style={"expand": "deepObject", "metadata": "deepObject"},
                explode={"expand": True, "metadata": True},
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/issuing/authorizations/{authorization}/decline",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.IssuingAuthorization,
            request_options=request_options or default_request_options(),
        )
