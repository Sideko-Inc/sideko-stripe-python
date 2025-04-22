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


class SetupIntentClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def list(
        self,
        *,
        attach_to_self: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        created: typing.Union[
            typing.Optional[typing.Union[params.SetupIntentListCreatedObj0, int]],
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
        payment_method: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        starting_after: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.SetupIntentListResponse:
        """
        List all SetupIntents

        <p>Returns a list of SetupIntents.</p>

        GET /v1/setup_intents

        Args:
            attach_to_self: If present, the SetupIntent's payment method will be attached to the in-context Stripe Account.

        It can only be used for this Stripe Account’s own money movement flows like InboundTransfer and OutboundTransfers. It cannot be set to true when setting up a PaymentMethod for a Customer, and defaults to false when attaching a PaymentMethod to a Customer.
            created: A filter on the list, based on the object `created` field. The value can be a string with an integer Unix timestamp, or it can be a dictionary with a number of different query options.
            customer: Only return SetupIntents for the customer specified by this customer ID.
            ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            expand: Specifies which fields in the response should be expanded.
            limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            payment_method: Only return SetupIntents that associate with the specified payment method.
            starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.setup_intent.list()
        ```
        """
        models.SetupIntentListResponse.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _query: QueryParams = {}
        if not isinstance(attach_to_self, type_utils.NotGiven):
            encode_query_param(
                _query,
                "attach_to_self",
                to_encodable(item=attach_to_self, dump_with=bool),
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
                        params._SerializerSetupIntentListCreatedObj0, int
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
        if not isinstance(payment_method, type_utils.NotGiven):
            encode_query_param(
                _query,
                "payment_method",
                to_encodable(item=payment_method, dump_with=str),
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
            path="/v1/setup_intents",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.SetupIntentListResponse,
            request_options=request_options or default_request_options(),
        )

    def get(
        self,
        *,
        intent: str,
        client_secret: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.SetupIntent:
        """
        Retrieve a SetupIntent

        <p>Retrieves the details of a SetupIntent that has previously been created. </p>

        <p>Client-side retrieval using a publishable key is allowed when the <code>client_secret</code> is provided in the query string. </p>

        <p>When retrieved with a publishable key, only a subset of properties will be returned. Please refer to the <a href="#setup_intent_object">SetupIntent</a> object reference for more details.</p>

        GET /v1/setup_intents/{intent}

        Args:
            client_secret: The client secret of the SetupIntent. We require this string if you use a publishable key to retrieve the SetupIntent.
            expand: Specifies which fields in the response should be expanded.
            intent: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.setup_intent.get(intent="string")
        ```
        """
        models.SetupIntent.model_rebuild(_types_namespace=models._types_namespace)
        _query: QueryParams = {}
        if not isinstance(client_secret, type_utils.NotGiven):
            encode_query_param(
                _query,
                "client_secret",
                to_encodable(item=client_secret, dump_with=str),
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
        return self._base_client.request(
            method="GET",
            path=f"/v1/setup_intents/{intent}",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.SetupIntent,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        data: typing.Union[
            typing.Optional[params.SetupIntentCreateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.SetupIntent:
        """
        Create a SetupIntent

        <p>Creates a SetupIntent object.</p>

        <p>After you create the SetupIntent, attach a payment method and <a href="/docs/api/setup_intents/confirm">confirm</a>
        it to collect any required permissions to charge the payment method later.</p>

        POST /v1/setup_intents

        Args:
            data: SetupIntentCreateBody
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.setup_intent.create()
        ```
        """
        models.SetupIntent.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerSetupIntentCreateBody,
                style={
                    "attach_to_self": "form",
                    "automatic_payment_methods": "deepObject",
                    "confirm": "form",
                    "confirmation_token": "form",
                    "customer": "form",
                    "description": "form",
                    "expand": "deepObject",
                    "flow_directions": "deepObject",
                    "mandate_data": "deepObject",
                    "metadata": "deepObject",
                    "on_behalf_of": "form",
                    "payment_method": "form",
                    "payment_method_configuration": "form",
                    "payment_method_data": "deepObject",
                    "payment_method_options": "deepObject",
                    "payment_method_types": "deepObject",
                    "return_url": "form",
                    "single_use": "deepObject",
                    "usage": "form",
                    "use_stripe_sdk": "form",
                },
                explode={
                    "attach_to_self": True,
                    "automatic_payment_methods": True,
                    "confirm": True,
                    "confirmation_token": True,
                    "customer": True,
                    "description": True,
                    "expand": True,
                    "flow_directions": True,
                    "mandate_data": True,
                    "metadata": True,
                    "on_behalf_of": True,
                    "payment_method": True,
                    "payment_method_configuration": True,
                    "payment_method_data": True,
                    "payment_method_options": True,
                    "payment_method_types": True,
                    "return_url": True,
                    "single_use": True,
                    "usage": True,
                    "use_stripe_sdk": True,
                },
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path="/v1/setup_intents",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.SetupIntent,
            request_options=request_options or default_request_options(),
        )

    def update(
        self,
        *,
        intent: str,
        data: typing.Union[
            typing.Optional[params.SetupIntentUpdateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.SetupIntent:
        """
        Update a SetupIntent

        <p>Updates a SetupIntent object.</p>

        POST /v1/setup_intents/{intent}

        Args:
            data: SetupIntentUpdateBody
            intent: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.setup_intent.update(intent="string")
        ```
        """
        models.SetupIntent.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerSetupIntentUpdateBody,
                style={
                    "attach_to_self": "form",
                    "customer": "form",
                    "description": "form",
                    "expand": "deepObject",
                    "flow_directions": "deepObject",
                    "metadata": "deepObject",
                    "payment_method": "form",
                    "payment_method_configuration": "form",
                    "payment_method_data": "deepObject",
                    "payment_method_options": "deepObject",
                    "payment_method_types": "deepObject",
                },
                explode={
                    "attach_to_self": True,
                    "customer": True,
                    "description": True,
                    "expand": True,
                    "flow_directions": True,
                    "metadata": True,
                    "payment_method": True,
                    "payment_method_configuration": True,
                    "payment_method_data": True,
                    "payment_method_options": True,
                    "payment_method_types": True,
                },
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/setup_intents/{intent}",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.SetupIntent,
            request_options=request_options or default_request_options(),
        )

    def cancel(
        self,
        *,
        intent: str,
        data: typing.Union[
            typing.Optional[params.SetupIntentCancelBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.SetupIntent:
        """
        Cancel a SetupIntent

        <p>You can cancel a SetupIntent object when it’s in one of these statuses: <code>requires_payment_method</code>, <code>requires_confirmation</code>, or <code>requires_action</code>. </p>

        <p>After you cancel it, setup is abandoned and any operations on the SetupIntent fail with an error. You can’t cancel the SetupIntent for a Checkout Session. <a href="/docs/api/checkout/sessions/expire">Expire the Checkout Session</a> instead.</p>

        POST /v1/setup_intents/{intent}/cancel

        Args:
            data: SetupIntentCancelBody
            intent: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.setup_intent.cancel(intent="string")
        ```
        """
        models.SetupIntent.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerSetupIntentCancelBody,
                style={"cancellation_reason": "form", "expand": "deepObject"},
                explode={"cancellation_reason": True, "expand": True},
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/setup_intents/{intent}/cancel",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.SetupIntent,
            request_options=request_options or default_request_options(),
        )

    def confirm(
        self,
        *,
        intent: str,
        data: typing.Union[
            typing.Optional[params.SetupIntentConfirmBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.SetupIntent:
        """
        Confirm a SetupIntent

        <p>Confirm that your customer intends to set up the current or
        provided payment method. For example, you would confirm a SetupIntent
        when a customer hits the “Save” button on a payment method management
        page on your website.</p>

        <p>If the selected payment method does not require any additional
        steps from the customer, the SetupIntent will transition to the
        <code>succeeded</code> status.</p>

        <p>Otherwise, it will transition to the <code>requires_action</code> status and
        suggest additional actions via <code>next_action</code>. If setup fails,
        the SetupIntent will transition to the
        <code>requires_payment_method</code> status or the <code>canceled</code> status if the
        confirmation limit is reached.</p>

        POST /v1/setup_intents/{intent}/confirm

        Args:
            data: SetupIntentConfirmBody
            intent: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.setup_intent.confirm(intent="string")
        ```
        """
        models.SetupIntent.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerSetupIntentConfirmBody,
                style={
                    "client_secret": "form",
                    "confirmation_token": "form",
                    "expand": "deepObject",
                    "mandate_data": "deepObject",
                    "payment_method": "form",
                    "payment_method_data": "deepObject",
                    "payment_method_options": "deepObject",
                    "return_url": "form",
                    "use_stripe_sdk": "form",
                },
                explode={
                    "client_secret": True,
                    "confirmation_token": True,
                    "expand": True,
                    "mandate_data": True,
                    "payment_method": True,
                    "payment_method_data": True,
                    "payment_method_options": True,
                    "return_url": True,
                    "use_stripe_sdk": True,
                },
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/setup_intents/{intent}/confirm",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.SetupIntent,
            request_options=request_options or default_request_options(),
        )

    def verify_microdeposits(
        self,
        *,
        intent: str,
        data: typing.Union[
            typing.Optional[params.SetupIntentVerifyMicrodepositsBody],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.SetupIntent:
        """
        Verify microdeposits on a SetupIntent

        <p>Verifies microdeposits on a SetupIntent object.</p>

        POST /v1/setup_intents/{intent}/verify_microdeposits

        Args:
            data: SetupIntentVerifyMicrodepositsBody
            intent: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.setup_intent.verify_microdeposits(intent="string")
        ```
        """
        models.SetupIntent.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerSetupIntentVerifyMicrodepositsBody,
                style={
                    "amounts": "deepObject",
                    "client_secret": "form",
                    "descriptor_code": "form",
                    "expand": "deepObject",
                },
                explode={
                    "amounts": True,
                    "client_secret": True,
                    "descriptor_code": True,
                    "expand": True,
                },
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/setup_intents/{intent}/verify_microdeposits",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.SetupIntent,
            request_options=request_options or default_request_options(),
        )


class AsyncSetupIntentClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def list(
        self,
        *,
        attach_to_self: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        created: typing.Union[
            typing.Optional[typing.Union[params.SetupIntentListCreatedObj0, int]],
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
        payment_method: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        starting_after: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.SetupIntentListResponse:
        """
        List all SetupIntents

        <p>Returns a list of SetupIntents.</p>

        GET /v1/setup_intents

        Args:
            attach_to_self: If present, the SetupIntent's payment method will be attached to the in-context Stripe Account.

        It can only be used for this Stripe Account’s own money movement flows like InboundTransfer and OutboundTransfers. It cannot be set to true when setting up a PaymentMethod for a Customer, and defaults to false when attaching a PaymentMethod to a Customer.
            created: A filter on the list, based on the object `created` field. The value can be a string with an integer Unix timestamp, or it can be a dictionary with a number of different query options.
            customer: Only return SetupIntents for the customer specified by this customer ID.
            ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            expand: Specifies which fields in the response should be expanded.
            limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            payment_method: Only return SetupIntents that associate with the specified payment method.
            starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.setup_intent.list()
        ```
        """
        models.SetupIntentListResponse.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _query: QueryParams = {}
        if not isinstance(attach_to_self, type_utils.NotGiven):
            encode_query_param(
                _query,
                "attach_to_self",
                to_encodable(item=attach_to_self, dump_with=bool),
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
                        params._SerializerSetupIntentListCreatedObj0, int
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
        if not isinstance(payment_method, type_utils.NotGiven):
            encode_query_param(
                _query,
                "payment_method",
                to_encodable(item=payment_method, dump_with=str),
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
            path="/v1/setup_intents",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.SetupIntentListResponse,
            request_options=request_options or default_request_options(),
        )

    async def get(
        self,
        *,
        intent: str,
        client_secret: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.SetupIntent:
        """
        Retrieve a SetupIntent

        <p>Retrieves the details of a SetupIntent that has previously been created. </p>

        <p>Client-side retrieval using a publishable key is allowed when the <code>client_secret</code> is provided in the query string. </p>

        <p>When retrieved with a publishable key, only a subset of properties will be returned. Please refer to the <a href="#setup_intent_object">SetupIntent</a> object reference for more details.</p>

        GET /v1/setup_intents/{intent}

        Args:
            client_secret: The client secret of the SetupIntent. We require this string if you use a publishable key to retrieve the SetupIntent.
            expand: Specifies which fields in the response should be expanded.
            intent: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.setup_intent.get(intent="string")
        ```
        """
        models.SetupIntent.model_rebuild(_types_namespace=models._types_namespace)
        _query: QueryParams = {}
        if not isinstance(client_secret, type_utils.NotGiven):
            encode_query_param(
                _query,
                "client_secret",
                to_encodable(item=client_secret, dump_with=str),
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
        return await self._base_client.request(
            method="GET",
            path=f"/v1/setup_intents/{intent}",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.SetupIntent,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        data: typing.Union[
            typing.Optional[params.SetupIntentCreateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.SetupIntent:
        """
        Create a SetupIntent

        <p>Creates a SetupIntent object.</p>

        <p>After you create the SetupIntent, attach a payment method and <a href="/docs/api/setup_intents/confirm">confirm</a>
        it to collect any required permissions to charge the payment method later.</p>

        POST /v1/setup_intents

        Args:
            data: SetupIntentCreateBody
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.setup_intent.create()
        ```
        """
        models.SetupIntent.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerSetupIntentCreateBody,
                style={
                    "attach_to_self": "form",
                    "automatic_payment_methods": "deepObject",
                    "confirm": "form",
                    "confirmation_token": "form",
                    "customer": "form",
                    "description": "form",
                    "expand": "deepObject",
                    "flow_directions": "deepObject",
                    "mandate_data": "deepObject",
                    "metadata": "deepObject",
                    "on_behalf_of": "form",
                    "payment_method": "form",
                    "payment_method_configuration": "form",
                    "payment_method_data": "deepObject",
                    "payment_method_options": "deepObject",
                    "payment_method_types": "deepObject",
                    "return_url": "form",
                    "single_use": "deepObject",
                    "usage": "form",
                    "use_stripe_sdk": "form",
                },
                explode={
                    "attach_to_self": True,
                    "automatic_payment_methods": True,
                    "confirm": True,
                    "confirmation_token": True,
                    "customer": True,
                    "description": True,
                    "expand": True,
                    "flow_directions": True,
                    "mandate_data": True,
                    "metadata": True,
                    "on_behalf_of": True,
                    "payment_method": True,
                    "payment_method_configuration": True,
                    "payment_method_data": True,
                    "payment_method_options": True,
                    "payment_method_types": True,
                    "return_url": True,
                    "single_use": True,
                    "usage": True,
                    "use_stripe_sdk": True,
                },
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path="/v1/setup_intents",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.SetupIntent,
            request_options=request_options or default_request_options(),
        )

    async def update(
        self,
        *,
        intent: str,
        data: typing.Union[
            typing.Optional[params.SetupIntentUpdateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.SetupIntent:
        """
        Update a SetupIntent

        <p>Updates a SetupIntent object.</p>

        POST /v1/setup_intents/{intent}

        Args:
            data: SetupIntentUpdateBody
            intent: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.setup_intent.update(intent="string")
        ```
        """
        models.SetupIntent.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerSetupIntentUpdateBody,
                style={
                    "attach_to_self": "form",
                    "customer": "form",
                    "description": "form",
                    "expand": "deepObject",
                    "flow_directions": "deepObject",
                    "metadata": "deepObject",
                    "payment_method": "form",
                    "payment_method_configuration": "form",
                    "payment_method_data": "deepObject",
                    "payment_method_options": "deepObject",
                    "payment_method_types": "deepObject",
                },
                explode={
                    "attach_to_self": True,
                    "customer": True,
                    "description": True,
                    "expand": True,
                    "flow_directions": True,
                    "metadata": True,
                    "payment_method": True,
                    "payment_method_configuration": True,
                    "payment_method_data": True,
                    "payment_method_options": True,
                    "payment_method_types": True,
                },
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/setup_intents/{intent}",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.SetupIntent,
            request_options=request_options or default_request_options(),
        )

    async def cancel(
        self,
        *,
        intent: str,
        data: typing.Union[
            typing.Optional[params.SetupIntentCancelBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.SetupIntent:
        """
        Cancel a SetupIntent

        <p>You can cancel a SetupIntent object when it’s in one of these statuses: <code>requires_payment_method</code>, <code>requires_confirmation</code>, or <code>requires_action</code>. </p>

        <p>After you cancel it, setup is abandoned and any operations on the SetupIntent fail with an error. You can’t cancel the SetupIntent for a Checkout Session. <a href="/docs/api/checkout/sessions/expire">Expire the Checkout Session</a> instead.</p>

        POST /v1/setup_intents/{intent}/cancel

        Args:
            data: SetupIntentCancelBody
            intent: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.setup_intent.cancel(intent="string")
        ```
        """
        models.SetupIntent.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerSetupIntentCancelBody,
                style={"cancellation_reason": "form", "expand": "deepObject"},
                explode={"cancellation_reason": True, "expand": True},
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/setup_intents/{intent}/cancel",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.SetupIntent,
            request_options=request_options or default_request_options(),
        )

    async def confirm(
        self,
        *,
        intent: str,
        data: typing.Union[
            typing.Optional[params.SetupIntentConfirmBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.SetupIntent:
        """
        Confirm a SetupIntent

        <p>Confirm that your customer intends to set up the current or
        provided payment method. For example, you would confirm a SetupIntent
        when a customer hits the “Save” button on a payment method management
        page on your website.</p>

        <p>If the selected payment method does not require any additional
        steps from the customer, the SetupIntent will transition to the
        <code>succeeded</code> status.</p>

        <p>Otherwise, it will transition to the <code>requires_action</code> status and
        suggest additional actions via <code>next_action</code>. If setup fails,
        the SetupIntent will transition to the
        <code>requires_payment_method</code> status or the <code>canceled</code> status if the
        confirmation limit is reached.</p>

        POST /v1/setup_intents/{intent}/confirm

        Args:
            data: SetupIntentConfirmBody
            intent: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.setup_intent.confirm(intent="string")
        ```
        """
        models.SetupIntent.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerSetupIntentConfirmBody,
                style={
                    "client_secret": "form",
                    "confirmation_token": "form",
                    "expand": "deepObject",
                    "mandate_data": "deepObject",
                    "payment_method": "form",
                    "payment_method_data": "deepObject",
                    "payment_method_options": "deepObject",
                    "return_url": "form",
                    "use_stripe_sdk": "form",
                },
                explode={
                    "client_secret": True,
                    "confirmation_token": True,
                    "expand": True,
                    "mandate_data": True,
                    "payment_method": True,
                    "payment_method_data": True,
                    "payment_method_options": True,
                    "return_url": True,
                    "use_stripe_sdk": True,
                },
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/setup_intents/{intent}/confirm",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.SetupIntent,
            request_options=request_options or default_request_options(),
        )

    async def verify_microdeposits(
        self,
        *,
        intent: str,
        data: typing.Union[
            typing.Optional[params.SetupIntentVerifyMicrodepositsBody],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.SetupIntent:
        """
        Verify microdeposits on a SetupIntent

        <p>Verifies microdeposits on a SetupIntent object.</p>

        POST /v1/setup_intents/{intent}/verify_microdeposits

        Args:
            data: SetupIntentVerifyMicrodepositsBody
            intent: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.setup_intent.verify_microdeposits(intent="string")
        ```
        """
        models.SetupIntent.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerSetupIntentVerifyMicrodepositsBody,
                style={
                    "amounts": "deepObject",
                    "client_secret": "form",
                    "descriptor_code": "form",
                    "expand": "deepObject",
                },
                explode={
                    "amounts": True,
                    "client_secret": True,
                    "descriptor_code": True,
                    "expand": True,
                },
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/setup_intents/{intent}/verify_microdeposits",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.SetupIntent,
            request_options=request_options or default_request_options(),
        )
