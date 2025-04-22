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


class CreditGrantClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def list(
        self,
        *,
        customer: typing.Union[
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
    ) -> models.BillingCreditGrantListResponse:
        """
        List credit grants

        <p>Retrieve a list of credit grants.</p>

        GET /v1/billing/credit_grants

        Args:
            customer: Only return credit grants for this customer.
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
        client.billing.credit_grant.list()
        ```
        """
        models.BillingCreditGrantListResponse.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _query: QueryParams = {}
        if not isinstance(customer, type_utils.NotGiven):
            encode_query_param(
                _query,
                "customer",
                to_encodable(item=customer, dump_with=str),
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
            path="/v1/billing/credit_grants",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.BillingCreditGrantListResponse,
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
    ) -> models.BillingCreditGrant:
        """
        Retrieve a credit grant

        <p>Retrieves a credit grant.</p>

        GET /v1/billing/credit_grants/{id}

        Args:
            expand: Specifies which fields in the response should be expanded.
            id: Unique identifier for the object.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.billing.credit_grant.get(id="string")
        ```
        """
        models.BillingCreditGrant.model_rebuild(
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
            path=f"/v1/billing/credit_grants/{id}",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.BillingCreditGrant,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        amount: params.BillingCreditGrantCreateBodyAmount,
        applicability_config: params.BillingCreditGrantCreateBodyApplicabilityConfig,
        category: typing_extensions.Literal["paid", "promotional"],
        customer: str,
        effective_at: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        expires_at: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        metadata: typing.Union[
            typing.Optional[params.BillingCreditGrantCreateBodyMetadata],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        priority: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.BillingCreditGrant:
        """
        Create a credit grant

        <p>Creates a credit grant.</p>

        POST /v1/billing/credit_grants

        Args:
            effective_at: The time when the billing credits become effective-when they're eligible for use. It defaults to the current timestamp if not specified.
            expand: Specifies which fields in the response should be expanded.
            expires_at: The time when the billing credits expire. If not specified, the billing credits don't expire.
            metadata: Set of key-value pairs that you can attach to an object. You can use this to store additional information about the object (for example, cost basis) in a structured format.
            name: A descriptive name shown in the Dashboard.
            priority: The desired priority for applying this credit grant. If not specified, it will be set to the default value of 50. The highest priority is 0 and the lowest is 100.
            amount: Amount of this credit grant.
            applicability_config: Configuration specifying what this credit grant applies to. We currently only support `metered` prices that have a [Billing Meter](https://docs.stripe.com/api/billing/meter) attached to them.
            category: The category of this credit grant.
            customer: ID of the customer to receive the billing credits.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.billing.credit_grant.create(
            amount={"type_": "monetary"},
            applicability_config={"scope": {}},
            category="paid",
            customer="string",
        )
        ```
        """
        models.BillingCreditGrant.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _data = to_form_urlencoded(
            item={
                "effective_at": effective_at,
                "expand": expand,
                "expires_at": expires_at,
                "metadata": metadata,
                "name": name,
                "priority": priority,
                "amount": amount,
                "applicability_config": applicability_config,
                "category": category,
                "customer": customer,
            },
            dump_with=params._SerializerBillingCreditGrantCreateBody,
            style={
                "amount": "deepObject",
                "applicability_config": "deepObject",
                "category": "form",
                "customer": "form",
                "effective_at": "form",
                "expand": "deepObject",
                "expires_at": "form",
                "metadata": "deepObject",
                "name": "form",
                "priority": "form",
            },
            explode={
                "amount": True,
                "applicability_config": True,
                "category": True,
                "customer": True,
                "effective_at": True,
                "expand": True,
                "expires_at": True,
                "metadata": True,
                "name": True,
                "priority": True,
            },
        )
        return self._base_client.request(
            method="POST",
            path="/v1/billing/credit_grants",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.BillingCreditGrant,
            request_options=request_options or default_request_options(),
        )

    def update(
        self,
        *,
        id: str,
        data: typing.Union[
            typing.Optional[params.BillingCreditGrantUpdateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.BillingCreditGrant:
        """
        Update a credit grant

        <p>Updates a credit grant.</p>

        POST /v1/billing/credit_grants/{id}

        Args:
            data: BillingCreditGrantUpdateBody
            id: Unique identifier for the object.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.billing.credit_grant.update(id="string")
        ```
        """
        models.BillingCreditGrant.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerBillingCreditGrantUpdateBody,
                style={
                    "expand": "deepObject",
                    "expires_at": "deepObject",
                    "metadata": "deepObject",
                },
                explode={"expand": True, "expires_at": True, "metadata": True},
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/billing/credit_grants/{id}",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.BillingCreditGrant,
            request_options=request_options or default_request_options(),
        )

    def expire(
        self,
        *,
        id: str,
        data: typing.Union[
            typing.Optional[params.BillingCreditGrantExpireBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.BillingCreditGrant:
        """
        Expire a credit grant

        <p>Expires a credit grant.</p>

        POST /v1/billing/credit_grants/{id}/expire

        Args:
            data: BillingCreditGrantExpireBody
            id: Unique identifier for the object.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.billing.credit_grant.expire(id="string")
        ```
        """
        models.BillingCreditGrant.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerBillingCreditGrantExpireBody,
                style={"expand": "deepObject"},
                explode={"expand": True},
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/billing/credit_grants/{id}/expire",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.BillingCreditGrant,
            request_options=request_options or default_request_options(),
        )

    def void(
        self,
        *,
        id: str,
        data: typing.Union[
            typing.Optional[params.BillingCreditGrantVoidBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.BillingCreditGrant:
        """
        Void a credit grant

        <p>Voids a credit grant.</p>

        POST /v1/billing/credit_grants/{id}/void

        Args:
            data: BillingCreditGrantVoidBody
            id: Unique identifier for the object.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.billing.credit_grant.void(id="string")
        ```
        """
        models.BillingCreditGrant.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerBillingCreditGrantVoidBody,
                style={"expand": "deepObject"},
                explode={"expand": True},
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/billing/credit_grants/{id}/void",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.BillingCreditGrant,
            request_options=request_options or default_request_options(),
        )


class AsyncCreditGrantClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def list(
        self,
        *,
        customer: typing.Union[
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
    ) -> models.BillingCreditGrantListResponse:
        """
        List credit grants

        <p>Retrieve a list of credit grants.</p>

        GET /v1/billing/credit_grants

        Args:
            customer: Only return credit grants for this customer.
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
        await client.billing.credit_grant.list()
        ```
        """
        models.BillingCreditGrantListResponse.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _query: QueryParams = {}
        if not isinstance(customer, type_utils.NotGiven):
            encode_query_param(
                _query,
                "customer",
                to_encodable(item=customer, dump_with=str),
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
            path="/v1/billing/credit_grants",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.BillingCreditGrantListResponse,
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
    ) -> models.BillingCreditGrant:
        """
        Retrieve a credit grant

        <p>Retrieves a credit grant.</p>

        GET /v1/billing/credit_grants/{id}

        Args:
            expand: Specifies which fields in the response should be expanded.
            id: Unique identifier for the object.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.billing.credit_grant.get(id="string")
        ```
        """
        models.BillingCreditGrant.model_rebuild(
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
            path=f"/v1/billing/credit_grants/{id}",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.BillingCreditGrant,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        amount: params.BillingCreditGrantCreateBodyAmount,
        applicability_config: params.BillingCreditGrantCreateBodyApplicabilityConfig,
        category: typing_extensions.Literal["paid", "promotional"],
        customer: str,
        effective_at: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        expires_at: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        metadata: typing.Union[
            typing.Optional[params.BillingCreditGrantCreateBodyMetadata],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        priority: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.BillingCreditGrant:
        """
        Create a credit grant

        <p>Creates a credit grant.</p>

        POST /v1/billing/credit_grants

        Args:
            effective_at: The time when the billing credits become effective-when they're eligible for use. It defaults to the current timestamp if not specified.
            expand: Specifies which fields in the response should be expanded.
            expires_at: The time when the billing credits expire. If not specified, the billing credits don't expire.
            metadata: Set of key-value pairs that you can attach to an object. You can use this to store additional information about the object (for example, cost basis) in a structured format.
            name: A descriptive name shown in the Dashboard.
            priority: The desired priority for applying this credit grant. If not specified, it will be set to the default value of 50. The highest priority is 0 and the lowest is 100.
            amount: Amount of this credit grant.
            applicability_config: Configuration specifying what this credit grant applies to. We currently only support `metered` prices that have a [Billing Meter](https://docs.stripe.com/api/billing/meter) attached to them.
            category: The category of this credit grant.
            customer: ID of the customer to receive the billing credits.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.billing.credit_grant.create(
            amount={"type_": "monetary"},
            applicability_config={"scope": {}},
            category="paid",
            customer="string",
        )
        ```
        """
        models.BillingCreditGrant.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _data = to_form_urlencoded(
            item={
                "effective_at": effective_at,
                "expand": expand,
                "expires_at": expires_at,
                "metadata": metadata,
                "name": name,
                "priority": priority,
                "amount": amount,
                "applicability_config": applicability_config,
                "category": category,
                "customer": customer,
            },
            dump_with=params._SerializerBillingCreditGrantCreateBody,
            style={
                "amount": "deepObject",
                "applicability_config": "deepObject",
                "category": "form",
                "customer": "form",
                "effective_at": "form",
                "expand": "deepObject",
                "expires_at": "form",
                "metadata": "deepObject",
                "name": "form",
                "priority": "form",
            },
            explode={
                "amount": True,
                "applicability_config": True,
                "category": True,
                "customer": True,
                "effective_at": True,
                "expand": True,
                "expires_at": True,
                "metadata": True,
                "name": True,
                "priority": True,
            },
        )
        return await self._base_client.request(
            method="POST",
            path="/v1/billing/credit_grants",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.BillingCreditGrant,
            request_options=request_options or default_request_options(),
        )

    async def update(
        self,
        *,
        id: str,
        data: typing.Union[
            typing.Optional[params.BillingCreditGrantUpdateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.BillingCreditGrant:
        """
        Update a credit grant

        <p>Updates a credit grant.</p>

        POST /v1/billing/credit_grants/{id}

        Args:
            data: BillingCreditGrantUpdateBody
            id: Unique identifier for the object.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.billing.credit_grant.update(id="string")
        ```
        """
        models.BillingCreditGrant.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerBillingCreditGrantUpdateBody,
                style={
                    "expand": "deepObject",
                    "expires_at": "deepObject",
                    "metadata": "deepObject",
                },
                explode={"expand": True, "expires_at": True, "metadata": True},
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/billing/credit_grants/{id}",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.BillingCreditGrant,
            request_options=request_options or default_request_options(),
        )

    async def expire(
        self,
        *,
        id: str,
        data: typing.Union[
            typing.Optional[params.BillingCreditGrantExpireBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.BillingCreditGrant:
        """
        Expire a credit grant

        <p>Expires a credit grant.</p>

        POST /v1/billing/credit_grants/{id}/expire

        Args:
            data: BillingCreditGrantExpireBody
            id: Unique identifier for the object.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.billing.credit_grant.expire(id="string")
        ```
        """
        models.BillingCreditGrant.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerBillingCreditGrantExpireBody,
                style={"expand": "deepObject"},
                explode={"expand": True},
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/billing/credit_grants/{id}/expire",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.BillingCreditGrant,
            request_options=request_options or default_request_options(),
        )

    async def void(
        self,
        *,
        id: str,
        data: typing.Union[
            typing.Optional[params.BillingCreditGrantVoidBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.BillingCreditGrant:
        """
        Void a credit grant

        <p>Voids a credit grant.</p>

        POST /v1/billing/credit_grants/{id}/void

        Args:
            data: BillingCreditGrantVoidBody
            id: Unique identifier for the object.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.billing.credit_grant.void(id="string")
        ```
        """
        models.BillingCreditGrant.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerBillingCreditGrantVoidBody,
                style={"expand": "deepObject"},
                explode={"expand": True},
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/billing/credit_grants/{id}/void",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.BillingCreditGrant,
            request_options=request_options or default_request_options(),
        )
