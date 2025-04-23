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


class DisputeClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def list(
        self,
        *,
        created: typing.Union[
            typing.Optional[typing.Union[params.IssuingDisputeListCreatedObj0, int]],
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
                typing_extensions.Literal[
                    "expired", "lost", "submitted", "unsubmitted", "won"
                ]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        transaction: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.IssuingDisputeListResponse:
        """
        List all disputes

        <p>Returns a list of Issuing <code>Dispute</code> objects. The objects are sorted in descending order by creation date, with the most recently created object appearing first.</p>

        GET /v1/issuing/disputes

        Args:
            created: Only return Issuing disputes that were created during the given date interval.
            ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            expand: Specifies which fields in the response should be expanded.
            limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
            status: Select Issuing disputes with the given status.
            transaction: Select the Issuing dispute for the given transaction.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.issuing.dispute.list()
        ```
        """
        models.IssuingDisputeListResponse.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _query: QueryParams = {}
        if not isinstance(created, type_utils.NotGiven):
            encode_query_param(
                _query,
                "created",
                to_encodable(
                    item=created,
                    dump_with=typing.Union[
                        params._SerializerIssuingDisputeListCreatedObj0, int
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
                        "expired", "lost", "submitted", "unsubmitted", "won"
                    ],
                ),
                style="form",
                explode=True,
            )
        if not isinstance(transaction, type_utils.NotGiven):
            encode_query_param(
                _query,
                "transaction",
                to_encodable(item=transaction, dump_with=str),
                style="form",
                explode=True,
            )
        return self._base_client.request(
            method="GET",
            path="/v1/issuing/disputes",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.IssuingDisputeListResponse,
            request_options=request_options or default_request_options(),
        )

    def get(
        self,
        *,
        dispute: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.IssuingDispute:
        """
        Retrieve a dispute

        <p>Retrieves an Issuing <code>Dispute</code> object.</p>

        GET /v1/issuing/disputes/{dispute}

        Args:
            expand: Specifies which fields in the response should be expanded.
            dispute: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.issuing.dispute.get(dispute="string")
        ```
        """
        models.IssuingDispute.model_rebuild(_types_namespace=models._types_namespace)
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
            path=f"/v1/issuing/disputes/{dispute}",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.IssuingDispute,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        data: typing.Union[
            typing.Optional[params.IssuingDisputeCreateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.IssuingDispute:
        """
        Create a dispute

        <p>Creates an Issuing <code>Dispute</code> object. Individual pieces of evidence within the <code>evidence</code> object are optional at this point. Stripe only validates that required evidence is present during submission. Refer to <a href="/docs/issuing/purchases/disputes#dispute-reasons-and-evidence">Dispute reasons and evidence</a> for more details about evidence requirements.</p>

        POST /v1/issuing/disputes

        Args:
            data: IssuingDisputeCreateBody
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.issuing.dispute.create()
        ```
        """
        models.IssuingDispute.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerIssuingDisputeCreateBody,
                style={
                    "amount": "form",
                    "evidence": "deepObject",
                    "expand": "deepObject",
                    "metadata": "deepObject",
                    "transaction": "form",
                    "treasury": "deepObject",
                },
                explode={
                    "amount": True,
                    "evidence": True,
                    "expand": True,
                    "metadata": True,
                    "transaction": True,
                    "treasury": True,
                },
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path="/v1/issuing/disputes",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.IssuingDispute,
            request_options=request_options or default_request_options(),
        )

    def update(
        self,
        *,
        dispute: str,
        data: typing.Union[
            typing.Optional[params.IssuingDisputeUpdateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.IssuingDispute:
        """
        Update a dispute

        <p>Updates the specified Issuing <code>Dispute</code> object by setting the values of the parameters passed. Any parameters not provided will be left unchanged. Properties on the <code>evidence</code> object can be unset by passing in an empty string.</p>

        POST /v1/issuing/disputes/{dispute}

        Args:
            data: IssuingDisputeUpdateBody
            dispute: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.issuing.dispute.update(dispute="string")
        ```
        """
        models.IssuingDispute.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerIssuingDisputeUpdateBody,
                style={
                    "amount": "form",
                    "evidence": "deepObject",
                    "expand": "deepObject",
                    "metadata": "deepObject",
                },
                explode={
                    "amount": True,
                    "evidence": True,
                    "expand": True,
                    "metadata": True,
                },
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/issuing/disputes/{dispute}",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.IssuingDispute,
            request_options=request_options or default_request_options(),
        )

    def submit(
        self,
        *,
        dispute: str,
        data: typing.Union[
            typing.Optional[params.IssuingDisputeSubmitBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.IssuingDispute:
        """
        Submit a dispute

        <p>Submits an Issuing <code>Dispute</code> to the card network. Stripe validates that all evidence fields required for the dispute’s reason are present. For more details, see <a href="/docs/issuing/purchases/disputes#dispute-reasons-and-evidence">Dispute reasons and evidence</a>.</p>

        POST /v1/issuing/disputes/{dispute}/submit

        Args:
            data: IssuingDisputeSubmitBody
            dispute: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.issuing.dispute.submit(dispute="string")
        ```
        """
        models.IssuingDispute.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerIssuingDisputeSubmitBody,
                style={"expand": "deepObject", "metadata": "deepObject"},
                explode={"expand": True, "metadata": True},
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/issuing/disputes/{dispute}/submit",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.IssuingDispute,
            request_options=request_options or default_request_options(),
        )


class AsyncDisputeClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def list(
        self,
        *,
        created: typing.Union[
            typing.Optional[typing.Union[params.IssuingDisputeListCreatedObj0, int]],
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
                typing_extensions.Literal[
                    "expired", "lost", "submitted", "unsubmitted", "won"
                ]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        transaction: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.IssuingDisputeListResponse:
        """
        List all disputes

        <p>Returns a list of Issuing <code>Dispute</code> objects. The objects are sorted in descending order by creation date, with the most recently created object appearing first.</p>

        GET /v1/issuing/disputes

        Args:
            created: Only return Issuing disputes that were created during the given date interval.
            ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            expand: Specifies which fields in the response should be expanded.
            limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
            status: Select Issuing disputes with the given status.
            transaction: Select the Issuing dispute for the given transaction.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.issuing.dispute.list()
        ```
        """
        models.IssuingDisputeListResponse.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _query: QueryParams = {}
        if not isinstance(created, type_utils.NotGiven):
            encode_query_param(
                _query,
                "created",
                to_encodable(
                    item=created,
                    dump_with=typing.Union[
                        params._SerializerIssuingDisputeListCreatedObj0, int
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
                        "expired", "lost", "submitted", "unsubmitted", "won"
                    ],
                ),
                style="form",
                explode=True,
            )
        if not isinstance(transaction, type_utils.NotGiven):
            encode_query_param(
                _query,
                "transaction",
                to_encodable(item=transaction, dump_with=str),
                style="form",
                explode=True,
            )
        return await self._base_client.request(
            method="GET",
            path="/v1/issuing/disputes",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.IssuingDisputeListResponse,
            request_options=request_options or default_request_options(),
        )

    async def get(
        self,
        *,
        dispute: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.IssuingDispute:
        """
        Retrieve a dispute

        <p>Retrieves an Issuing <code>Dispute</code> object.</p>

        GET /v1/issuing/disputes/{dispute}

        Args:
            expand: Specifies which fields in the response should be expanded.
            dispute: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.issuing.dispute.get(dispute="string")
        ```
        """
        models.IssuingDispute.model_rebuild(_types_namespace=models._types_namespace)
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
            path=f"/v1/issuing/disputes/{dispute}",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.IssuingDispute,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        data: typing.Union[
            typing.Optional[params.IssuingDisputeCreateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.IssuingDispute:
        """
        Create a dispute

        <p>Creates an Issuing <code>Dispute</code> object. Individual pieces of evidence within the <code>evidence</code> object are optional at this point. Stripe only validates that required evidence is present during submission. Refer to <a href="/docs/issuing/purchases/disputes#dispute-reasons-and-evidence">Dispute reasons and evidence</a> for more details about evidence requirements.</p>

        POST /v1/issuing/disputes

        Args:
            data: IssuingDisputeCreateBody
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.issuing.dispute.create()
        ```
        """
        models.IssuingDispute.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerIssuingDisputeCreateBody,
                style={
                    "amount": "form",
                    "evidence": "deepObject",
                    "expand": "deepObject",
                    "metadata": "deepObject",
                    "transaction": "form",
                    "treasury": "deepObject",
                },
                explode={
                    "amount": True,
                    "evidence": True,
                    "expand": True,
                    "metadata": True,
                    "transaction": True,
                    "treasury": True,
                },
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path="/v1/issuing/disputes",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.IssuingDispute,
            request_options=request_options or default_request_options(),
        )

    async def update(
        self,
        *,
        dispute: str,
        data: typing.Union[
            typing.Optional[params.IssuingDisputeUpdateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.IssuingDispute:
        """
        Update a dispute

        <p>Updates the specified Issuing <code>Dispute</code> object by setting the values of the parameters passed. Any parameters not provided will be left unchanged. Properties on the <code>evidence</code> object can be unset by passing in an empty string.</p>

        POST /v1/issuing/disputes/{dispute}

        Args:
            data: IssuingDisputeUpdateBody
            dispute: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.issuing.dispute.update(dispute="string")
        ```
        """
        models.IssuingDispute.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerIssuingDisputeUpdateBody,
                style={
                    "amount": "form",
                    "evidence": "deepObject",
                    "expand": "deepObject",
                    "metadata": "deepObject",
                },
                explode={
                    "amount": True,
                    "evidence": True,
                    "expand": True,
                    "metadata": True,
                },
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/issuing/disputes/{dispute}",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.IssuingDispute,
            request_options=request_options or default_request_options(),
        )

    async def submit(
        self,
        *,
        dispute: str,
        data: typing.Union[
            typing.Optional[params.IssuingDisputeSubmitBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.IssuingDispute:
        """
        Submit a dispute

        <p>Submits an Issuing <code>Dispute</code> to the card network. Stripe validates that all evidence fields required for the dispute’s reason are present. For more details, see <a href="/docs/issuing/purchases/disputes#dispute-reasons-and-evidence">Dispute reasons and evidence</a>.</p>

        POST /v1/issuing/disputes/{dispute}/submit

        Args:
            data: IssuingDisputeSubmitBody
            dispute: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.issuing.dispute.submit(dispute="string")
        ```
        """
        models.IssuingDispute.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerIssuingDisputeSubmitBody,
                style={"expand": "deepObject", "metadata": "deepObject"},
                explode={"expand": True, "metadata": True},
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/issuing/disputes/{dispute}/submit",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.IssuingDispute,
            request_options=request_options or default_request_options(),
        )
