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
from sideko_stripe.resources.charge.dispute import AsyncDisputeClient, DisputeClient
from sideko_stripe.resources.charge.refund import AsyncRefundClient, RefundClient
from sideko_stripe.types import models, params


class ChargeClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        self.dispute = DisputeClient(base_client=self._base_client)
        self.refund = RefundClient(base_client=self._base_client)

    def list(
        self,
        *,
        created: typing.Union[
            typing.Optional[typing.Union[params.ChargeListCreatedObj0, int]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
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
        payment_intent: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        starting_after: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        transfer_group: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ChargeListResponse:
        """
        List all charges

        <p>Returns a list of charges you’ve previously created. The charges are returned in sorted order, with the most recent charges appearing first.</p>

        GET /v1/charges

        Args:
            created: Only return charges that were created during the given date interval.
            customer: Only return charges for the customer specified by this customer ID.
            ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            expand: Specifies which fields in the response should be expanded.
            limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            payment_intent: Only return charges that were created by the PaymentIntent specified by this PaymentIntent ID.
            starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
            transfer_group: Only return charges for this transfer group, limited to 100.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.charge.list()
        ```
        """
        models.ChargeListResponse.model_rebuild(
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
                        params._SerializerChargeListCreatedObj0, int
                    ],
                ),
                style="deepObject",
                explode=True,
            )
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
        if not isinstance(transfer_group, type_utils.NotGiven):
            encode_query_param(
                _query,
                "transfer_group",
                to_encodable(item=transfer_group, dump_with=str),
                style="form",
                explode=True,
            )
        return self._base_client.request(
            method="GET",
            path="/v1/charges",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.ChargeListResponse,
            request_options=request_options or default_request_options(),
        )

    def search(
        self,
        *,
        query: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        limit: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        page: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ChargeSearchResponse:
        """
        Search charges

        <p>Search for charges you’ve previously created using Stripe’s <a href="/docs/search#search-query-language">Search Query Language</a>.
        Don’t use search in read-after-write flows where strict consistency is necessary. Under normal operating
        conditions, data is searchable in less than a minute. Occasionally, propagation of new or updated data can be up
        to an hour behind during outages. Search functionality is not available to merchants in India.</p>

        GET /v1/charges/search

        Args:
            expand: Specifies which fields in the response should be expanded.
            limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            page: A cursor for pagination across multiple pages of results. Don't include this parameter on the first call. Use the next_page value returned in a previous response to request subsequent results.
            query: The search query string. See [search query language](https://stripe.com/docs/search#search-query-language) and the list of supported [query fields for charges](https://stripe.com/docs/search#query-fields-for-charges).
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.charge.search(query="string")
        ```
        """
        models.ChargeSearchResponse.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _query: QueryParams = {}
        encode_query_param(
            _query,
            "query",
            to_encodable(item=query, dump_with=str),
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
        if not isinstance(page, type_utils.NotGiven):
            encode_query_param(
                _query,
                "page",
                to_encodable(item=page, dump_with=str),
                style="form",
                explode=True,
            )
        return self._base_client.request(
            method="GET",
            path="/v1/charges/search",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.ChargeSearchResponse,
            request_options=request_options or default_request_options(),
        )

    def get(
        self,
        *,
        charge: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Charge:
        """
        Retrieve a charge

        <p>Retrieves the details of a charge that has previously been created. Supply the unique charge ID that was returned from your previous request, and Stripe will return the corresponding charge information. The same information is returned when creating or refunding the charge.</p>

        GET /v1/charges/{charge}

        Args:
            expand: Specifies which fields in the response should be expanded.
            charge: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.charge.get(charge="string")
        ```
        """
        models.Charge.model_rebuild(_types_namespace=models._types_namespace)
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
            path=f"/v1/charges/{charge}",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.Charge,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        data: typing.Union[
            typing.Optional[params.ChargeCreateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Charge:
        """
        <p>This method is no longer recommended—use the <a href="/docs/api/payment_intents">Payment Intents API</a>
        to initiate a new payment instead. Confirmation of the PaymentIntent creates the <code>Charge</code>
        object used to request payment.</p>

        POST /v1/charges

        Args:
            data: ChargeCreateBody
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.charge.create()
        ```
        """
        models.Charge.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerChargeCreateBody,
                style={
                    "amount": "form",
                    "application_fee": "form",
                    "application_fee_amount": "form",
                    "capture": "form",
                    "card": "deepObject",
                    "currency": "form",
                    "customer": "form",
                    "description": "form",
                    "destination": "deepObject",
                    "expand": "deepObject",
                    "metadata": "deepObject",
                    "on_behalf_of": "form",
                    "radar_options": "deepObject",
                    "receipt_email": "form",
                    "shipping": "deepObject",
                    "source": "form",
                    "statement_descriptor": "form",
                    "statement_descriptor_suffix": "form",
                    "transfer_data": "deepObject",
                    "transfer_group": "form",
                },
                explode={
                    "amount": True,
                    "application_fee": True,
                    "application_fee_amount": True,
                    "capture": True,
                    "card": True,
                    "currency": True,
                    "customer": True,
                    "description": True,
                    "destination": True,
                    "expand": True,
                    "metadata": True,
                    "on_behalf_of": True,
                    "radar_options": True,
                    "receipt_email": True,
                    "shipping": True,
                    "source": True,
                    "statement_descriptor": True,
                    "statement_descriptor_suffix": True,
                    "transfer_data": True,
                    "transfer_group": True,
                },
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path="/v1/charges",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.Charge,
            request_options=request_options or default_request_options(),
        )

    def update(
        self,
        *,
        charge: str,
        data: typing.Union[
            typing.Optional[params.ChargeUpdateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Charge:
        """
        Update a charge

        <p>Updates the specified charge by setting the values of the parameters passed. Any parameters not provided will be left unchanged.</p>

        POST /v1/charges/{charge}

        Args:
            data: ChargeUpdateBody
            charge: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.charge.update(charge="string")
        ```
        """
        models.Charge.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerChargeUpdateBody,
                style={
                    "customer": "form",
                    "description": "form",
                    "expand": "deepObject",
                    "fraud_details": "deepObject",
                    "metadata": "deepObject",
                    "receipt_email": "form",
                    "shipping": "deepObject",
                    "transfer_group": "form",
                },
                explode={
                    "customer": True,
                    "description": True,
                    "expand": True,
                    "fraud_details": True,
                    "metadata": True,
                    "receipt_email": True,
                    "shipping": True,
                    "transfer_group": True,
                },
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/charges/{charge}",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.Charge,
            request_options=request_options or default_request_options(),
        )

    def capture(
        self,
        *,
        charge: str,
        data: typing.Union[
            typing.Optional[params.ChargeCaptureBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Charge:
        """
        Capture a payment

        <p>Capture the payment of an existing, uncaptured charge that was created with the <code>capture</code> option set to false.</p>

        <p>Uncaptured payments expire a set number of days after they are created (<a href="/docs/charges/placing-a-hold">7 by default</a>), after which they are marked as refunded and capture attempts will fail.</p>

        <p>Don’t use this method to capture a PaymentIntent-initiated charge. Use <a href="/docs/api/payment_intents/capture">Capture a PaymentIntent</a>.</p>

        POST /v1/charges/{charge}/capture

        Args:
            data: ChargeCaptureBody
            charge: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.charge.capture(charge="string")
        ```
        """
        models.Charge.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerChargeCaptureBody,
                style={
                    "amount": "form",
                    "application_fee": "form",
                    "application_fee_amount": "form",
                    "expand": "deepObject",
                    "receipt_email": "form",
                    "statement_descriptor": "form",
                    "statement_descriptor_suffix": "form",
                    "transfer_data": "deepObject",
                    "transfer_group": "form",
                },
                explode={
                    "amount": True,
                    "application_fee": True,
                    "application_fee_amount": True,
                    "expand": True,
                    "receipt_email": True,
                    "statement_descriptor": True,
                    "statement_descriptor_suffix": True,
                    "transfer_data": True,
                    "transfer_group": True,
                },
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/charges/{charge}/capture",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.Charge,
            request_options=request_options or default_request_options(),
        )


class AsyncChargeClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        self.dispute = AsyncDisputeClient(base_client=self._base_client)
        self.refund = AsyncRefundClient(base_client=self._base_client)

    async def list(
        self,
        *,
        created: typing.Union[
            typing.Optional[typing.Union[params.ChargeListCreatedObj0, int]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
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
        payment_intent: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        starting_after: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        transfer_group: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ChargeListResponse:
        """
        List all charges

        <p>Returns a list of charges you’ve previously created. The charges are returned in sorted order, with the most recent charges appearing first.</p>

        GET /v1/charges

        Args:
            created: Only return charges that were created during the given date interval.
            customer: Only return charges for the customer specified by this customer ID.
            ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            expand: Specifies which fields in the response should be expanded.
            limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            payment_intent: Only return charges that were created by the PaymentIntent specified by this PaymentIntent ID.
            starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
            transfer_group: Only return charges for this transfer group, limited to 100.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.charge.list()
        ```
        """
        models.ChargeListResponse.model_rebuild(
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
                        params._SerializerChargeListCreatedObj0, int
                    ],
                ),
                style="deepObject",
                explode=True,
            )
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
        if not isinstance(transfer_group, type_utils.NotGiven):
            encode_query_param(
                _query,
                "transfer_group",
                to_encodable(item=transfer_group, dump_with=str),
                style="form",
                explode=True,
            )
        return await self._base_client.request(
            method="GET",
            path="/v1/charges",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.ChargeListResponse,
            request_options=request_options or default_request_options(),
        )

    async def search(
        self,
        *,
        query: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        limit: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        page: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ChargeSearchResponse:
        """
        Search charges

        <p>Search for charges you’ve previously created using Stripe’s <a href="/docs/search#search-query-language">Search Query Language</a>.
        Don’t use search in read-after-write flows where strict consistency is necessary. Under normal operating
        conditions, data is searchable in less than a minute. Occasionally, propagation of new or updated data can be up
        to an hour behind during outages. Search functionality is not available to merchants in India.</p>

        GET /v1/charges/search

        Args:
            expand: Specifies which fields in the response should be expanded.
            limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            page: A cursor for pagination across multiple pages of results. Don't include this parameter on the first call. Use the next_page value returned in a previous response to request subsequent results.
            query: The search query string. See [search query language](https://stripe.com/docs/search#search-query-language) and the list of supported [query fields for charges](https://stripe.com/docs/search#query-fields-for-charges).
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.charge.search(query="string")
        ```
        """
        models.ChargeSearchResponse.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _query: QueryParams = {}
        encode_query_param(
            _query,
            "query",
            to_encodable(item=query, dump_with=str),
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
        if not isinstance(page, type_utils.NotGiven):
            encode_query_param(
                _query,
                "page",
                to_encodable(item=page, dump_with=str),
                style="form",
                explode=True,
            )
        return await self._base_client.request(
            method="GET",
            path="/v1/charges/search",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.ChargeSearchResponse,
            request_options=request_options or default_request_options(),
        )

    async def get(
        self,
        *,
        charge: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Charge:
        """
        Retrieve a charge

        <p>Retrieves the details of a charge that has previously been created. Supply the unique charge ID that was returned from your previous request, and Stripe will return the corresponding charge information. The same information is returned when creating or refunding the charge.</p>

        GET /v1/charges/{charge}

        Args:
            expand: Specifies which fields in the response should be expanded.
            charge: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.charge.get(charge="string")
        ```
        """
        models.Charge.model_rebuild(_types_namespace=models._types_namespace)
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
            path=f"/v1/charges/{charge}",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.Charge,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        data: typing.Union[
            typing.Optional[params.ChargeCreateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Charge:
        """
        <p>This method is no longer recommended—use the <a href="/docs/api/payment_intents">Payment Intents API</a>
        to initiate a new payment instead. Confirmation of the PaymentIntent creates the <code>Charge</code>
        object used to request payment.</p>

        POST /v1/charges

        Args:
            data: ChargeCreateBody
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.charge.create()
        ```
        """
        models.Charge.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerChargeCreateBody,
                style={
                    "amount": "form",
                    "application_fee": "form",
                    "application_fee_amount": "form",
                    "capture": "form",
                    "card": "deepObject",
                    "currency": "form",
                    "customer": "form",
                    "description": "form",
                    "destination": "deepObject",
                    "expand": "deepObject",
                    "metadata": "deepObject",
                    "on_behalf_of": "form",
                    "radar_options": "deepObject",
                    "receipt_email": "form",
                    "shipping": "deepObject",
                    "source": "form",
                    "statement_descriptor": "form",
                    "statement_descriptor_suffix": "form",
                    "transfer_data": "deepObject",
                    "transfer_group": "form",
                },
                explode={
                    "amount": True,
                    "application_fee": True,
                    "application_fee_amount": True,
                    "capture": True,
                    "card": True,
                    "currency": True,
                    "customer": True,
                    "description": True,
                    "destination": True,
                    "expand": True,
                    "metadata": True,
                    "on_behalf_of": True,
                    "radar_options": True,
                    "receipt_email": True,
                    "shipping": True,
                    "source": True,
                    "statement_descriptor": True,
                    "statement_descriptor_suffix": True,
                    "transfer_data": True,
                    "transfer_group": True,
                },
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path="/v1/charges",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.Charge,
            request_options=request_options or default_request_options(),
        )

    async def update(
        self,
        *,
        charge: str,
        data: typing.Union[
            typing.Optional[params.ChargeUpdateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Charge:
        """
        Update a charge

        <p>Updates the specified charge by setting the values of the parameters passed. Any parameters not provided will be left unchanged.</p>

        POST /v1/charges/{charge}

        Args:
            data: ChargeUpdateBody
            charge: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.charge.update(charge="string")
        ```
        """
        models.Charge.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerChargeUpdateBody,
                style={
                    "customer": "form",
                    "description": "form",
                    "expand": "deepObject",
                    "fraud_details": "deepObject",
                    "metadata": "deepObject",
                    "receipt_email": "form",
                    "shipping": "deepObject",
                    "transfer_group": "form",
                },
                explode={
                    "customer": True,
                    "description": True,
                    "expand": True,
                    "fraud_details": True,
                    "metadata": True,
                    "receipt_email": True,
                    "shipping": True,
                    "transfer_group": True,
                },
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/charges/{charge}",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.Charge,
            request_options=request_options or default_request_options(),
        )

    async def capture(
        self,
        *,
        charge: str,
        data: typing.Union[
            typing.Optional[params.ChargeCaptureBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Charge:
        """
        Capture a payment

        <p>Capture the payment of an existing, uncaptured charge that was created with the <code>capture</code> option set to false.</p>

        <p>Uncaptured payments expire a set number of days after they are created (<a href="/docs/charges/placing-a-hold">7 by default</a>), after which they are marked as refunded and capture attempts will fail.</p>

        <p>Don’t use this method to capture a PaymentIntent-initiated charge. Use <a href="/docs/api/payment_intents/capture">Capture a PaymentIntent</a>.</p>

        POST /v1/charges/{charge}/capture

        Args:
            data: ChargeCaptureBody
            charge: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.charge.capture(charge="string")
        ```
        """
        models.Charge.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerChargeCaptureBody,
                style={
                    "amount": "form",
                    "application_fee": "form",
                    "application_fee_amount": "form",
                    "expand": "deepObject",
                    "receipt_email": "form",
                    "statement_descriptor": "form",
                    "statement_descriptor_suffix": "form",
                    "transfer_data": "deepObject",
                    "transfer_group": "form",
                },
                explode={
                    "amount": True,
                    "application_fee": True,
                    "application_fee_amount": True,
                    "expand": True,
                    "receipt_email": True,
                    "statement_descriptor": True,
                    "statement_descriptor_suffix": True,
                    "transfer_data": True,
                    "transfer_group": True,
                },
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/charges/{charge}/capture",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.Charge,
            request_options=request_options or default_request_options(),
        )
