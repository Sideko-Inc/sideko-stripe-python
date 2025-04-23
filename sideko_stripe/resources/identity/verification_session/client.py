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


class VerificationSessionClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def list(
        self,
        *,
        client_reference_id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        created: typing.Union[
            typing.Optional[
                typing.Union[params.IdentityVerificationSessionListCreatedObj0, int]
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
        related_customer: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        starting_after: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        status: typing.Union[
            typing.Optional[
                typing_extensions.Literal[
                    "canceled", "processing", "requires_input", "verified"
                ]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.IdentityVerificationSessionListResponse:
        """
        List VerificationSessions

        <p>Returns a list of VerificationSessions</p>

        GET /v1/identity/verification_sessions

        Args:
            client_reference_id: A string to reference this user. This can be a customer ID, a session ID, or similar, and can be used to reconcile this verification with your internal systems.
            created: Only return VerificationSessions that were created during the given date interval.
            ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            expand: Specifies which fields in the response should be expanded.
            limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            related_customer: str
            starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
            status: Only return VerificationSessions with this status. [Learn more about the lifecycle of sessions](https://stripe.com/docs/identity/how-sessions-work).
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.identity.verification_session.list()
        ```
        """
        _query: QueryParams = {}
        if not isinstance(client_reference_id, type_utils.NotGiven):
            encode_query_param(
                _query,
                "client_reference_id",
                to_encodable(item=client_reference_id, dump_with=str),
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
                        params._SerializerIdentityVerificationSessionListCreatedObj0,
                        int,
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
        if not isinstance(related_customer, type_utils.NotGiven):
            encode_query_param(
                _query,
                "related_customer",
                to_encodable(item=related_customer, dump_with=str),
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
                        "canceled", "processing", "requires_input", "verified"
                    ],
                ),
                style="form",
                explode=True,
            )
        return self._base_client.request(
            method="GET",
            path="/v1/identity/verification_sessions",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.IdentityVerificationSessionListResponse,
            request_options=request_options or default_request_options(),
        )

    def get(
        self,
        *,
        session: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.IdentityVerificationSession:
        """
        Retrieve a VerificationSession

        <p>Retrieves the details of a VerificationSession that was previously created.</p>

        <p>When the session status is <code>requires_input</code>, you can use this method to retrieve a valid
        <code>client_secret</code> or <code>url</code> to allow re-submission.</p>

        GET /v1/identity/verification_sessions/{session}

        Args:
            expand: Specifies which fields in the response should be expanded.
            session: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.identity.verification_session.get(session="string")
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
            path=f"/v1/identity/verification_sessions/{session}",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.IdentityVerificationSession,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        data: typing.Union[
            typing.Optional[params.IdentityVerificationSessionCreateBody],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.IdentityVerificationSession:
        """
        Create a VerificationSession

        <p>Creates a VerificationSession object.</p>

        <p>After the VerificationSession is created, display a verification modal using the session <code>client_secret</code> or send your users to the session’s <code>url</code>.</p>

        <p>If your API key is in test mode, verification checks won’t actually process, though everything else will occur as if in live mode.</p>

        <p>Related guide: <a href="/docs/identity/verify-identity-documents">Verify your users’ identity documents</a></p>

        POST /v1/identity/verification_sessions

        Args:
            data: IdentityVerificationSessionCreateBody
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.identity.verification_session.create()
        ```
        """
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerIdentityVerificationSessionCreateBody,
                style={
                    "client_reference_id": "form",
                    "expand": "deepObject",
                    "metadata": "deepObject",
                    "options": "deepObject",
                    "provided_details": "deepObject",
                    "related_customer": "form",
                    "return_url": "form",
                    "type": "form",
                    "verification_flow": "form",
                },
                explode={
                    "client_reference_id": True,
                    "expand": True,
                    "metadata": True,
                    "options": True,
                    "provided_details": True,
                    "related_customer": True,
                    "return_url": True,
                    "type": True,
                    "verification_flow": True,
                },
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path="/v1/identity/verification_sessions",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.IdentityVerificationSession,
            request_options=request_options or default_request_options(),
        )

    def update(
        self,
        *,
        session: str,
        data: typing.Union[
            typing.Optional[params.IdentityVerificationSessionUpdateBody],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.IdentityVerificationSession:
        """
        Update a VerificationSession

        <p>Updates a VerificationSession object.</p>

        <p>When the session status is <code>requires_input</code>, you can use this method to update the
        verification check and options.</p>

        POST /v1/identity/verification_sessions/{session}

        Args:
            data: IdentityVerificationSessionUpdateBody
            session: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.identity.verification_session.update(session="string")
        ```
        """
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerIdentityVerificationSessionUpdateBody,
                style={
                    "expand": "deepObject",
                    "metadata": "deepObject",
                    "options": "deepObject",
                    "provided_details": "deepObject",
                    "type": "form",
                },
                explode={
                    "expand": True,
                    "metadata": True,
                    "options": True,
                    "provided_details": True,
                    "type": True,
                },
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/identity/verification_sessions/{session}",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.IdentityVerificationSession,
            request_options=request_options or default_request_options(),
        )

    def cancel(
        self,
        *,
        session: str,
        data: typing.Union[
            typing.Optional[params.IdentityVerificationSessionCancelBody],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.IdentityVerificationSession:
        """
        Cancel a VerificationSession

        <p>A VerificationSession object can be canceled when it is in <code>requires_input</code> <a href="/docs/identity/how-sessions-work">status</a>.</p>

        <p>Once canceled, future submission attempts are disabled. This cannot be undone. <a href="/docs/identity/verification-sessions#cancel">Learn more</a>.</p>

        POST /v1/identity/verification_sessions/{session}/cancel

        Args:
            data: IdentityVerificationSessionCancelBody
            session: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.identity.verification_session.cancel(session="string")
        ```
        """
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerIdentityVerificationSessionCancelBody,
                style={"expand": "deepObject"},
                explode={"expand": True},
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/identity/verification_sessions/{session}/cancel",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.IdentityVerificationSession,
            request_options=request_options or default_request_options(),
        )

    def redact(
        self,
        *,
        session: str,
        data: typing.Union[
            typing.Optional[params.IdentityVerificationSessionRedactBody],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.IdentityVerificationSession:
        """
        Redact a VerificationSession

        <p>Redact a VerificationSession to remove all collected information from Stripe. This will redact
        the VerificationSession and all objects related to it, including VerificationReports, Events,
        request logs, etc.</p>

        <p>A VerificationSession object can be redacted when it is in <code>requires_input</code> or <code>verified</code>
        <a href="/docs/identity/how-sessions-work">status</a>. Redacting a VerificationSession in <code>requires_action</code>
        state will automatically cancel it.</p>

        <p>The redaction process may take up to four days. When the redaction process is in progress, the
        VerificationSession’s <code>redaction.status</code> field will be set to <code>processing</code>; when the process is
        finished, it will change to <code>redacted</code> and an <code>identity.verification_session.redacted</code> event
        will be emitted.</p>

        <p>Redaction is irreversible. Redacted objects are still accessible in the Stripe API, but all the
        fields that contain personal data will be replaced by the string <code>[redacted]</code> or a similar
        placeholder. The <code>metadata</code> field will also be erased. Redacted objects cannot be updated or
        used for any purpose.</p>

        <p><a href="/docs/identity/verification-sessions#redact">Learn more</a>.</p>

        POST /v1/identity/verification_sessions/{session}/redact

        Args:
            data: IdentityVerificationSessionRedactBody
            session: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.identity.verification_session.redact(session="string")
        ```
        """
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerIdentityVerificationSessionRedactBody,
                style={"expand": "deepObject"},
                explode={"expand": True},
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/identity/verification_sessions/{session}/redact",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.IdentityVerificationSession,
            request_options=request_options or default_request_options(),
        )


class AsyncVerificationSessionClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def list(
        self,
        *,
        client_reference_id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        created: typing.Union[
            typing.Optional[
                typing.Union[params.IdentityVerificationSessionListCreatedObj0, int]
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
        related_customer: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        starting_after: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        status: typing.Union[
            typing.Optional[
                typing_extensions.Literal[
                    "canceled", "processing", "requires_input", "verified"
                ]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.IdentityVerificationSessionListResponse:
        """
        List VerificationSessions

        <p>Returns a list of VerificationSessions</p>

        GET /v1/identity/verification_sessions

        Args:
            client_reference_id: A string to reference this user. This can be a customer ID, a session ID, or similar, and can be used to reconcile this verification with your internal systems.
            created: Only return VerificationSessions that were created during the given date interval.
            ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            expand: Specifies which fields in the response should be expanded.
            limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            related_customer: str
            starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
            status: Only return VerificationSessions with this status. [Learn more about the lifecycle of sessions](https://stripe.com/docs/identity/how-sessions-work).
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.identity.verification_session.list()
        ```
        """
        _query: QueryParams = {}
        if not isinstance(client_reference_id, type_utils.NotGiven):
            encode_query_param(
                _query,
                "client_reference_id",
                to_encodable(item=client_reference_id, dump_with=str),
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
                        params._SerializerIdentityVerificationSessionListCreatedObj0,
                        int,
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
        if not isinstance(related_customer, type_utils.NotGiven):
            encode_query_param(
                _query,
                "related_customer",
                to_encodable(item=related_customer, dump_with=str),
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
                        "canceled", "processing", "requires_input", "verified"
                    ],
                ),
                style="form",
                explode=True,
            )
        return await self._base_client.request(
            method="GET",
            path="/v1/identity/verification_sessions",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.IdentityVerificationSessionListResponse,
            request_options=request_options or default_request_options(),
        )

    async def get(
        self,
        *,
        session: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.IdentityVerificationSession:
        """
        Retrieve a VerificationSession

        <p>Retrieves the details of a VerificationSession that was previously created.</p>

        <p>When the session status is <code>requires_input</code>, you can use this method to retrieve a valid
        <code>client_secret</code> or <code>url</code> to allow re-submission.</p>

        GET /v1/identity/verification_sessions/{session}

        Args:
            expand: Specifies which fields in the response should be expanded.
            session: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.identity.verification_session.get(session="string")
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
            path=f"/v1/identity/verification_sessions/{session}",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.IdentityVerificationSession,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        data: typing.Union[
            typing.Optional[params.IdentityVerificationSessionCreateBody],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.IdentityVerificationSession:
        """
        Create a VerificationSession

        <p>Creates a VerificationSession object.</p>

        <p>After the VerificationSession is created, display a verification modal using the session <code>client_secret</code> or send your users to the session’s <code>url</code>.</p>

        <p>If your API key is in test mode, verification checks won’t actually process, though everything else will occur as if in live mode.</p>

        <p>Related guide: <a href="/docs/identity/verify-identity-documents">Verify your users’ identity documents</a></p>

        POST /v1/identity/verification_sessions

        Args:
            data: IdentityVerificationSessionCreateBody
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.identity.verification_session.create()
        ```
        """
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerIdentityVerificationSessionCreateBody,
                style={
                    "client_reference_id": "form",
                    "expand": "deepObject",
                    "metadata": "deepObject",
                    "options": "deepObject",
                    "provided_details": "deepObject",
                    "related_customer": "form",
                    "return_url": "form",
                    "type": "form",
                    "verification_flow": "form",
                },
                explode={
                    "client_reference_id": True,
                    "expand": True,
                    "metadata": True,
                    "options": True,
                    "provided_details": True,
                    "related_customer": True,
                    "return_url": True,
                    "type": True,
                    "verification_flow": True,
                },
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path="/v1/identity/verification_sessions",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.IdentityVerificationSession,
            request_options=request_options or default_request_options(),
        )

    async def update(
        self,
        *,
        session: str,
        data: typing.Union[
            typing.Optional[params.IdentityVerificationSessionUpdateBody],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.IdentityVerificationSession:
        """
        Update a VerificationSession

        <p>Updates a VerificationSession object.</p>

        <p>When the session status is <code>requires_input</code>, you can use this method to update the
        verification check and options.</p>

        POST /v1/identity/verification_sessions/{session}

        Args:
            data: IdentityVerificationSessionUpdateBody
            session: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.identity.verification_session.update(session="string")
        ```
        """
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerIdentityVerificationSessionUpdateBody,
                style={
                    "expand": "deepObject",
                    "metadata": "deepObject",
                    "options": "deepObject",
                    "provided_details": "deepObject",
                    "type": "form",
                },
                explode={
                    "expand": True,
                    "metadata": True,
                    "options": True,
                    "provided_details": True,
                    "type": True,
                },
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/identity/verification_sessions/{session}",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.IdentityVerificationSession,
            request_options=request_options or default_request_options(),
        )

    async def cancel(
        self,
        *,
        session: str,
        data: typing.Union[
            typing.Optional[params.IdentityVerificationSessionCancelBody],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.IdentityVerificationSession:
        """
        Cancel a VerificationSession

        <p>A VerificationSession object can be canceled when it is in <code>requires_input</code> <a href="/docs/identity/how-sessions-work">status</a>.</p>

        <p>Once canceled, future submission attempts are disabled. This cannot be undone. <a href="/docs/identity/verification-sessions#cancel">Learn more</a>.</p>

        POST /v1/identity/verification_sessions/{session}/cancel

        Args:
            data: IdentityVerificationSessionCancelBody
            session: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.identity.verification_session.cancel(session="string")
        ```
        """
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerIdentityVerificationSessionCancelBody,
                style={"expand": "deepObject"},
                explode={"expand": True},
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/identity/verification_sessions/{session}/cancel",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.IdentityVerificationSession,
            request_options=request_options or default_request_options(),
        )

    async def redact(
        self,
        *,
        session: str,
        data: typing.Union[
            typing.Optional[params.IdentityVerificationSessionRedactBody],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.IdentityVerificationSession:
        """
        Redact a VerificationSession

        <p>Redact a VerificationSession to remove all collected information from Stripe. This will redact
        the VerificationSession and all objects related to it, including VerificationReports, Events,
        request logs, etc.</p>

        <p>A VerificationSession object can be redacted when it is in <code>requires_input</code> or <code>verified</code>
        <a href="/docs/identity/how-sessions-work">status</a>. Redacting a VerificationSession in <code>requires_action</code>
        state will automatically cancel it.</p>

        <p>The redaction process may take up to four days. When the redaction process is in progress, the
        VerificationSession’s <code>redaction.status</code> field will be set to <code>processing</code>; when the process is
        finished, it will change to <code>redacted</code> and an <code>identity.verification_session.redacted</code> event
        will be emitted.</p>

        <p>Redaction is irreversible. Redacted objects are still accessible in the Stripe API, but all the
        fields that contain personal data will be replaced by the string <code>[redacted]</code> or a similar
        placeholder. The <code>metadata</code> field will also be erased. Redacted objects cannot be updated or
        used for any purpose.</p>

        <p><a href="/docs/identity/verification-sessions#redact">Learn more</a>.</p>

        POST /v1/identity/verification_sessions/{session}/redact

        Args:
            data: IdentityVerificationSessionRedactBody
            session: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.identity.verification_session.redact(session="string")
        ```
        """
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerIdentityVerificationSessionRedactBody,
                style={"expand": "deepObject"},
                explode={"expand": True},
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/identity/verification_sessions/{session}/redact",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.IdentityVerificationSession,
            request_options=request_options or default_request_options(),
        )
