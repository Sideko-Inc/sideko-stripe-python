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


class AlertClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def list(
        self,
        *,
        alert_type: typing.Union[
            typing.Optional[typing_extensions.Literal["usage_threshold"]],
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
        meter: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        starting_after: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.BillingAlertListResponse:
        """
        List billing alerts

        <p>Lists billing active and inactive alerts</p>

        GET /v1/billing/alerts

        Args:
            alert_type: Filter results to only include this type of alert.
            ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            expand: Specifies which fields in the response should be expanded.
            limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            meter: Filter results to only include alerts with the given meter.
            starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.billing.alert.list()
        ```
        """
        models.BillingAlertListResponse.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _query: QueryParams = {}
        if not isinstance(alert_type, type_utils.NotGiven):
            encode_query_param(
                _query,
                "alert_type",
                to_encodable(
                    item=alert_type,
                    dump_with=typing_extensions.Literal["usage_threshold"],
                ),
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
        if not isinstance(meter, type_utils.NotGiven):
            encode_query_param(
                _query,
                "meter",
                to_encodable(item=meter, dump_with=str),
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
            path="/v1/billing/alerts",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.BillingAlertListResponse,
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
    ) -> models.BillingAlert:
        """
        Retrieve a billing alert

        <p>Retrieves a billing alert given an ID</p>

        GET /v1/billing/alerts/{id}

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
        client.billing.alert.get(id="string")
        ```
        """
        models.BillingAlert.model_rebuild(_types_namespace=models._types_namespace)
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
            path=f"/v1/billing/alerts/{id}",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.BillingAlert,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        alert_type: typing_extensions.Literal["usage_threshold"],
        title: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        usage_threshold: typing.Union[
            typing.Optional[params.BillingAlertCreateBodyUsageThreshold],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.BillingAlert:
        """
        Create a billing alert

        <p>Creates a billing alert</p>

        POST /v1/billing/alerts

        Args:
            expand: Specifies which fields in the response should be expanded.
            usage_threshold: The configuration of the usage threshold.
            alert_type: The type of alert to create.
            title: The title of the alert.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.billing.alert.create(alert_type="usage_threshold", title="string")
        ```
        """
        models.BillingAlert.model_rebuild(_types_namespace=models._types_namespace)
        _data = to_form_urlencoded(
            item={
                "expand": expand,
                "usage_threshold": usage_threshold,
                "alert_type": alert_type,
                "title": title,
            },
            dump_with=params._SerializerBillingAlertCreateBody,
            style={
                "alert_type": "form",
                "expand": "deepObject",
                "title": "form",
                "usage_threshold": "deepObject",
            },
            explode={
                "alert_type": True,
                "expand": True,
                "title": True,
                "usage_threshold": True,
            },
        )
        return self._base_client.request(
            method="POST",
            path="/v1/billing/alerts",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.BillingAlert,
            request_options=request_options or default_request_options(),
        )

    def activate(
        self,
        *,
        id: str,
        data: typing.Union[
            typing.Optional[params.BillingAlertActivateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.BillingAlert:
        """
        Activate a billing alert

        <p>Reactivates this alert, allowing it to trigger again.</p>

        POST /v1/billing/alerts/{id}/activate

        Args:
            data: BillingAlertActivateBody
            id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.billing.alert.activate(id="string")
        ```
        """
        models.BillingAlert.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerBillingAlertActivateBody,
                style={"expand": "deepObject"},
                explode={"expand": True},
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/billing/alerts/{id}/activate",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.BillingAlert,
            request_options=request_options or default_request_options(),
        )

    def archive(
        self,
        *,
        id: str,
        data: typing.Union[
            typing.Optional[params.BillingAlertArchiveBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.BillingAlert:
        """
        Archive a billing alert

        <p>Archives this alert, removing it from the list view and APIs. This is non-reversible.</p>

        POST /v1/billing/alerts/{id}/archive

        Args:
            data: BillingAlertArchiveBody
            id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.billing.alert.archive(id="string")
        ```
        """
        models.BillingAlert.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerBillingAlertArchiveBody,
                style={"expand": "deepObject"},
                explode={"expand": True},
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/billing/alerts/{id}/archive",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.BillingAlert,
            request_options=request_options or default_request_options(),
        )

    def deactivate(
        self,
        *,
        id: str,
        data: typing.Union[
            typing.Optional[params.BillingAlertDeactivateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.BillingAlert:
        """
        Deactivate a billing alert

        <p>Deactivates this alert, preventing it from triggering.</p>

        POST /v1/billing/alerts/{id}/deactivate

        Args:
            data: BillingAlertDeactivateBody
            id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.billing.alert.deactivate(id="string")
        ```
        """
        models.BillingAlert.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerBillingAlertDeactivateBody,
                style={"expand": "deepObject"},
                explode={"expand": True},
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/billing/alerts/{id}/deactivate",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.BillingAlert,
            request_options=request_options or default_request_options(),
        )


class AsyncAlertClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def list(
        self,
        *,
        alert_type: typing.Union[
            typing.Optional[typing_extensions.Literal["usage_threshold"]],
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
        meter: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        starting_after: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.BillingAlertListResponse:
        """
        List billing alerts

        <p>Lists billing active and inactive alerts</p>

        GET /v1/billing/alerts

        Args:
            alert_type: Filter results to only include this type of alert.
            ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            expand: Specifies which fields in the response should be expanded.
            limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            meter: Filter results to only include alerts with the given meter.
            starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.billing.alert.list()
        ```
        """
        models.BillingAlertListResponse.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _query: QueryParams = {}
        if not isinstance(alert_type, type_utils.NotGiven):
            encode_query_param(
                _query,
                "alert_type",
                to_encodable(
                    item=alert_type,
                    dump_with=typing_extensions.Literal["usage_threshold"],
                ),
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
        if not isinstance(meter, type_utils.NotGiven):
            encode_query_param(
                _query,
                "meter",
                to_encodable(item=meter, dump_with=str),
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
            path="/v1/billing/alerts",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.BillingAlertListResponse,
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
    ) -> models.BillingAlert:
        """
        Retrieve a billing alert

        <p>Retrieves a billing alert given an ID</p>

        GET /v1/billing/alerts/{id}

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
        await client.billing.alert.get(id="string")
        ```
        """
        models.BillingAlert.model_rebuild(_types_namespace=models._types_namespace)
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
            path=f"/v1/billing/alerts/{id}",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.BillingAlert,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        alert_type: typing_extensions.Literal["usage_threshold"],
        title: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        usage_threshold: typing.Union[
            typing.Optional[params.BillingAlertCreateBodyUsageThreshold],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.BillingAlert:
        """
        Create a billing alert

        <p>Creates a billing alert</p>

        POST /v1/billing/alerts

        Args:
            expand: Specifies which fields in the response should be expanded.
            usage_threshold: The configuration of the usage threshold.
            alert_type: The type of alert to create.
            title: The title of the alert.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.billing.alert.create(alert_type="usage_threshold", title="string")
        ```
        """
        models.BillingAlert.model_rebuild(_types_namespace=models._types_namespace)
        _data = to_form_urlencoded(
            item={
                "expand": expand,
                "usage_threshold": usage_threshold,
                "alert_type": alert_type,
                "title": title,
            },
            dump_with=params._SerializerBillingAlertCreateBody,
            style={
                "alert_type": "form",
                "expand": "deepObject",
                "title": "form",
                "usage_threshold": "deepObject",
            },
            explode={
                "alert_type": True,
                "expand": True,
                "title": True,
                "usage_threshold": True,
            },
        )
        return await self._base_client.request(
            method="POST",
            path="/v1/billing/alerts",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.BillingAlert,
            request_options=request_options or default_request_options(),
        )

    async def activate(
        self,
        *,
        id: str,
        data: typing.Union[
            typing.Optional[params.BillingAlertActivateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.BillingAlert:
        """
        Activate a billing alert

        <p>Reactivates this alert, allowing it to trigger again.</p>

        POST /v1/billing/alerts/{id}/activate

        Args:
            data: BillingAlertActivateBody
            id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.billing.alert.activate(id="string")
        ```
        """
        models.BillingAlert.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerBillingAlertActivateBody,
                style={"expand": "deepObject"},
                explode={"expand": True},
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/billing/alerts/{id}/activate",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.BillingAlert,
            request_options=request_options or default_request_options(),
        )

    async def archive(
        self,
        *,
        id: str,
        data: typing.Union[
            typing.Optional[params.BillingAlertArchiveBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.BillingAlert:
        """
        Archive a billing alert

        <p>Archives this alert, removing it from the list view and APIs. This is non-reversible.</p>

        POST /v1/billing/alerts/{id}/archive

        Args:
            data: BillingAlertArchiveBody
            id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.billing.alert.archive(id="string")
        ```
        """
        models.BillingAlert.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerBillingAlertArchiveBody,
                style={"expand": "deepObject"},
                explode={"expand": True},
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/billing/alerts/{id}/archive",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.BillingAlert,
            request_options=request_options or default_request_options(),
        )

    async def deactivate(
        self,
        *,
        id: str,
        data: typing.Union[
            typing.Optional[params.BillingAlertDeactivateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.BillingAlert:
        """
        Deactivate a billing alert

        <p>Deactivates this alert, preventing it from triggering.</p>

        POST /v1/billing/alerts/{id}/deactivate

        Args:
            data: BillingAlertDeactivateBody
            id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.billing.alert.deactivate(id="string")
        ```
        """
        models.BillingAlert.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerBillingAlertDeactivateBody,
                style={"expand": "deepObject"},
                explode={"expand": True},
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/billing/alerts/{id}/deactivate",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.BillingAlert,
            request_options=request_options or default_request_options(),
        )
