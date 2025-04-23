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
from sideko_stripe.types import models, params


class EarlyFraudWarningClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def list(
        self,
        *,
        charge: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        created: typing.Union[
            typing.Optional[
                typing.Union[params.RadarEarlyFraudWarningListCreatedObj0, int]
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
        payment_intent: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        starting_after: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.RadarEarlyFraudWarningListResponse:
        """
        List all early fraud warnings

        <p>Returns a list of early fraud warnings.</p>

        GET /v1/radar/early_fraud_warnings

        Args:
            charge: Only return early fraud warnings for the charge specified by this charge ID.
            created: Only return early fraud warnings that were created during the given date interval.
            ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            expand: Specifies which fields in the response should be expanded.
            limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            payment_intent: Only return early fraud warnings for charges that were created by the PaymentIntent specified by this PaymentIntent ID.
            starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.radar.early_fraud_warning.list()
        ```
        """
        models.RadarEarlyFraudWarningListResponse.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _query: QueryParams = {}
        if not isinstance(charge, type_utils.NotGiven):
            encode_query_param(
                _query,
                "charge",
                to_encodable(item=charge, dump_with=str),
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
                        params._SerializerRadarEarlyFraudWarningListCreatedObj0, int
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
        if not isinstance(payment_intent, type_utils.NotGiven):
            encode_query_param(
                _query,
                "payment_intent",
                to_encodable(item=payment_intent, dump_with=str),
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
            path="/v1/radar/early_fraud_warnings",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.RadarEarlyFraudWarningListResponse,
            request_options=request_options or default_request_options(),
        )

    def get(
        self,
        *,
        early_fraud_warning: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.RadarEarlyFraudWarning:
        """
        Retrieve an early fraud warning

        <p>Retrieves the details of an early fraud warning that has previously been created. </p>

        <p>Please refer to the <a href="#early_fraud_warning_object">early fraud warning</a> object reference for more details.</p>

        GET /v1/radar/early_fraud_warnings/{early_fraud_warning}

        Args:
            expand: Specifies which fields in the response should be expanded.
            early_fraud_warning: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.radar.early_fraud_warning.get(early_fraud_warning="string")
        ```
        """
        models.RadarEarlyFraudWarning.model_rebuild(
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
            path=f"/v1/radar/early_fraud_warnings/{early_fraud_warning}",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.RadarEarlyFraudWarning,
            request_options=request_options or default_request_options(),
        )


class AsyncEarlyFraudWarningClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def list(
        self,
        *,
        charge: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        created: typing.Union[
            typing.Optional[
                typing.Union[params.RadarEarlyFraudWarningListCreatedObj0, int]
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
        payment_intent: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        starting_after: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.RadarEarlyFraudWarningListResponse:
        """
        List all early fraud warnings

        <p>Returns a list of early fraud warnings.</p>

        GET /v1/radar/early_fraud_warnings

        Args:
            charge: Only return early fraud warnings for the charge specified by this charge ID.
            created: Only return early fraud warnings that were created during the given date interval.
            ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            expand: Specifies which fields in the response should be expanded.
            limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            payment_intent: Only return early fraud warnings for charges that were created by the PaymentIntent specified by this PaymentIntent ID.
            starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.radar.early_fraud_warning.list()
        ```
        """
        models.RadarEarlyFraudWarningListResponse.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _query: QueryParams = {}
        if not isinstance(charge, type_utils.NotGiven):
            encode_query_param(
                _query,
                "charge",
                to_encodable(item=charge, dump_with=str),
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
                        params._SerializerRadarEarlyFraudWarningListCreatedObj0, int
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
        if not isinstance(payment_intent, type_utils.NotGiven):
            encode_query_param(
                _query,
                "payment_intent",
                to_encodable(item=payment_intent, dump_with=str),
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
            path="/v1/radar/early_fraud_warnings",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.RadarEarlyFraudWarningListResponse,
            request_options=request_options or default_request_options(),
        )

    async def get(
        self,
        *,
        early_fraud_warning: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.RadarEarlyFraudWarning:
        """
        Retrieve an early fraud warning

        <p>Retrieves the details of an early fraud warning that has previously been created. </p>

        <p>Please refer to the <a href="#early_fraud_warning_object">early fraud warning</a> object reference for more details.</p>

        GET /v1/radar/early_fraud_warnings/{early_fraud_warning}

        Args:
            expand: Specifies which fields in the response should be expanded.
            early_fraud_warning: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.radar.early_fraud_warning.get(early_fraud_warning="string")
        ```
        """
        models.RadarEarlyFraudWarning.model_rebuild(
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
            path=f"/v1/radar/early_fraud_warnings/{early_fraud_warning}",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.RadarEarlyFraudWarning,
            request_options=request_options or default_request_options(),
        )
