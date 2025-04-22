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
from sideko_stripe.resources.checkout.session.line_items import (
    AsyncLineItemsClient,
    LineItemsClient,
)
from sideko_stripe.types import models, params


class SessionClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        self.line_items = LineItemsClient(base_client=self._base_client)

    def list(
        self,
        *,
        created: typing.Union[
            typing.Optional[typing.Union[params.CheckoutSessionListCreatedObj0, int]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        customer: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        customer_details: typing.Union[
            typing.Optional[params.CheckoutSessionListCustomerDetails],
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
        payment_link: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        starting_after: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        status: typing.Union[
            typing.Optional[typing_extensions.Literal["complete", "expired", "open"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        subscription: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.CheckoutSessionListResponse:
        """
        List all Checkout Sessions

        <p>Returns a list of Checkout Sessions.</p>

        GET /v1/checkout/sessions

        Args:
            created: Only return Checkout Sessions that were created during the given date interval.
            customer: Only return the Checkout Sessions for the Customer specified.
            customer_details: Only return the Checkout Sessions for the Customer details specified.
            ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            expand: Specifies which fields in the response should be expanded.
            limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            payment_intent: Only return the Checkout Session for the PaymentIntent specified.
            payment_link: Only return the Checkout Sessions for the Payment Link specified.
            starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
            status: Only return the Checkout Sessions matching the given status.
            subscription: Only return the Checkout Session for the subscription specified.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.checkout.session.list()
        ```
        """
        models.CheckoutSessionListResponse.model_rebuild(
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
                        params._SerializerCheckoutSessionListCreatedObj0, int
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
        if not isinstance(customer_details, type_utils.NotGiven):
            encode_query_param(
                _query,
                "customer_details",
                to_encodable(
                    item=customer_details,
                    dump_with=params._SerializerCheckoutSessionListCustomerDetails,
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
        if not isinstance(payment_link, type_utils.NotGiven):
            encode_query_param(
                _query,
                "payment_link",
                to_encodable(item=payment_link, dump_with=str),
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
                    dump_with=typing_extensions.Literal["complete", "expired", "open"],
                ),
                style="form",
                explode=True,
            )
        if not isinstance(subscription, type_utils.NotGiven):
            encode_query_param(
                _query,
                "subscription",
                to_encodable(item=subscription, dump_with=str),
                style="form",
                explode=True,
            )
        return self._base_client.request(
            method="GET",
            path="/v1/checkout/sessions",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.CheckoutSessionListResponse,
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
    ) -> models.CheckoutSession:
        """
        Retrieve a Checkout Session

        <p>Retrieves a Checkout Session object.</p>

        GET /v1/checkout/sessions/{session}

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
        client.checkout.session.get(session="string")
        ```
        """
        models.CheckoutSession.model_rebuild(_types_namespace=models._types_namespace)
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
            path=f"/v1/checkout/sessions/{session}",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.CheckoutSession,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        data: typing.Union[
            typing.Optional[params.CheckoutSessionCreateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.CheckoutSession:
        """
        Create a Checkout Session

        <p>Creates a Checkout Session object.</p>

        POST /v1/checkout/sessions

        Args:
            data: CheckoutSessionCreateBody
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.checkout.session.create()
        ```
        """
        models.CheckoutSession.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerCheckoutSessionCreateBody,
                style={
                    "adaptive_pricing": "deepObject",
                    "after_expiration": "deepObject",
                    "allow_promotion_codes": "form",
                    "automatic_tax": "deepObject",
                    "billing_address_collection": "form",
                    "cancel_url": "form",
                    "client_reference_id": "form",
                    "consent_collection": "deepObject",
                    "currency": "form",
                    "custom_fields": "deepObject",
                    "custom_text": "deepObject",
                    "customer": "form",
                    "customer_creation": "form",
                    "customer_email": "form",
                    "customer_update": "deepObject",
                    "discounts": "deepObject",
                    "expand": "deepObject",
                    "expires_at": "form",
                    "invoice_creation": "deepObject",
                    "line_items": "deepObject",
                    "locale": "form",
                    "metadata": "deepObject",
                    "mode": "form",
                    "optional_items": "deepObject",
                    "payment_intent_data": "deepObject",
                    "payment_method_collection": "form",
                    "payment_method_configuration": "form",
                    "payment_method_data": "deepObject",
                    "payment_method_options": "deepObject",
                    "payment_method_types": "deepObject",
                    "permissions": "deepObject",
                    "phone_number_collection": "deepObject",
                    "redirect_on_completion": "form",
                    "return_url": "form",
                    "saved_payment_method_options": "deepObject",
                    "setup_intent_data": "deepObject",
                    "shipping_address_collection": "deepObject",
                    "shipping_options": "deepObject",
                    "submit_type": "form",
                    "subscription_data": "deepObject",
                    "success_url": "form",
                    "tax_id_collection": "deepObject",
                    "ui_mode": "form",
                },
                explode={
                    "adaptive_pricing": True,
                    "after_expiration": True,
                    "allow_promotion_codes": True,
                    "automatic_tax": True,
                    "billing_address_collection": True,
                    "cancel_url": True,
                    "client_reference_id": True,
                    "consent_collection": True,
                    "currency": True,
                    "custom_fields": True,
                    "custom_text": True,
                    "customer": True,
                    "customer_creation": True,
                    "customer_email": True,
                    "customer_update": True,
                    "discounts": True,
                    "expand": True,
                    "expires_at": True,
                    "invoice_creation": True,
                    "line_items": True,
                    "locale": True,
                    "metadata": True,
                    "mode": True,
                    "optional_items": True,
                    "payment_intent_data": True,
                    "payment_method_collection": True,
                    "payment_method_configuration": True,
                    "payment_method_data": True,
                    "payment_method_options": True,
                    "payment_method_types": True,
                    "permissions": True,
                    "phone_number_collection": True,
                    "redirect_on_completion": True,
                    "return_url": True,
                    "saved_payment_method_options": True,
                    "setup_intent_data": True,
                    "shipping_address_collection": True,
                    "shipping_options": True,
                    "submit_type": True,
                    "subscription_data": True,
                    "success_url": True,
                    "tax_id_collection": True,
                    "ui_mode": True,
                },
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path="/v1/checkout/sessions",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.CheckoutSession,
            request_options=request_options or default_request_options(),
        )

    def update(
        self,
        *,
        session: str,
        data: typing.Union[
            typing.Optional[params.CheckoutSessionUpdateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.CheckoutSession:
        """
        Update a Checkout Session

        <p>Updates a Checkout Session object.</p>

        POST /v1/checkout/sessions/{session}

        Args:
            data: CheckoutSessionUpdateBody
            session: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.checkout.session.update(session="string")
        ```
        """
        models.CheckoutSession.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerCheckoutSessionUpdateBody,
                style={
                    "collected_information": "deepObject",
                    "expand": "deepObject",
                    "metadata": "deepObject",
                    "shipping_options": "deepObject",
                },
                explode={
                    "collected_information": True,
                    "expand": True,
                    "metadata": True,
                    "shipping_options": True,
                },
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/checkout/sessions/{session}",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.CheckoutSession,
            request_options=request_options or default_request_options(),
        )

    def expire(
        self,
        *,
        session: str,
        data: typing.Union[
            typing.Optional[params.CheckoutSessionExpireBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.CheckoutSession:
        """
        Expire a Checkout Session

        <p>A Checkout Session can be expired when it is in one of these statuses: <code>open</code> </p>

        <p>After it expires, a customer can’t complete a Checkout Session and customers loading the Checkout Session see a message saying the Checkout Session is expired.</p>

        POST /v1/checkout/sessions/{session}/expire

        Args:
            data: CheckoutSessionExpireBody
            session: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.checkout.session.expire(session="string")
        ```
        """
        models.CheckoutSession.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerCheckoutSessionExpireBody,
                style={"expand": "deepObject"},
                explode={"expand": True},
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/checkout/sessions/{session}/expire",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.CheckoutSession,
            request_options=request_options or default_request_options(),
        )


class AsyncSessionClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        self.line_items = AsyncLineItemsClient(base_client=self._base_client)

    async def list(
        self,
        *,
        created: typing.Union[
            typing.Optional[typing.Union[params.CheckoutSessionListCreatedObj0, int]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        customer: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        customer_details: typing.Union[
            typing.Optional[params.CheckoutSessionListCustomerDetails],
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
        payment_link: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        starting_after: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        status: typing.Union[
            typing.Optional[typing_extensions.Literal["complete", "expired", "open"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        subscription: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.CheckoutSessionListResponse:
        """
        List all Checkout Sessions

        <p>Returns a list of Checkout Sessions.</p>

        GET /v1/checkout/sessions

        Args:
            created: Only return Checkout Sessions that were created during the given date interval.
            customer: Only return the Checkout Sessions for the Customer specified.
            customer_details: Only return the Checkout Sessions for the Customer details specified.
            ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            expand: Specifies which fields in the response should be expanded.
            limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            payment_intent: Only return the Checkout Session for the PaymentIntent specified.
            payment_link: Only return the Checkout Sessions for the Payment Link specified.
            starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
            status: Only return the Checkout Sessions matching the given status.
            subscription: Only return the Checkout Session for the subscription specified.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.checkout.session.list()
        ```
        """
        models.CheckoutSessionListResponse.model_rebuild(
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
                        params._SerializerCheckoutSessionListCreatedObj0, int
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
        if not isinstance(customer_details, type_utils.NotGiven):
            encode_query_param(
                _query,
                "customer_details",
                to_encodable(
                    item=customer_details,
                    dump_with=params._SerializerCheckoutSessionListCustomerDetails,
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
        if not isinstance(payment_link, type_utils.NotGiven):
            encode_query_param(
                _query,
                "payment_link",
                to_encodable(item=payment_link, dump_with=str),
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
                    dump_with=typing_extensions.Literal["complete", "expired", "open"],
                ),
                style="form",
                explode=True,
            )
        if not isinstance(subscription, type_utils.NotGiven):
            encode_query_param(
                _query,
                "subscription",
                to_encodable(item=subscription, dump_with=str),
                style="form",
                explode=True,
            )
        return await self._base_client.request(
            method="GET",
            path="/v1/checkout/sessions",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.CheckoutSessionListResponse,
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
    ) -> models.CheckoutSession:
        """
        Retrieve a Checkout Session

        <p>Retrieves a Checkout Session object.</p>

        GET /v1/checkout/sessions/{session}

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
        await client.checkout.session.get(session="string")
        ```
        """
        models.CheckoutSession.model_rebuild(_types_namespace=models._types_namespace)
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
            path=f"/v1/checkout/sessions/{session}",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.CheckoutSession,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        data: typing.Union[
            typing.Optional[params.CheckoutSessionCreateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.CheckoutSession:
        """
        Create a Checkout Session

        <p>Creates a Checkout Session object.</p>

        POST /v1/checkout/sessions

        Args:
            data: CheckoutSessionCreateBody
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.checkout.session.create()
        ```
        """
        models.CheckoutSession.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerCheckoutSessionCreateBody,
                style={
                    "adaptive_pricing": "deepObject",
                    "after_expiration": "deepObject",
                    "allow_promotion_codes": "form",
                    "automatic_tax": "deepObject",
                    "billing_address_collection": "form",
                    "cancel_url": "form",
                    "client_reference_id": "form",
                    "consent_collection": "deepObject",
                    "currency": "form",
                    "custom_fields": "deepObject",
                    "custom_text": "deepObject",
                    "customer": "form",
                    "customer_creation": "form",
                    "customer_email": "form",
                    "customer_update": "deepObject",
                    "discounts": "deepObject",
                    "expand": "deepObject",
                    "expires_at": "form",
                    "invoice_creation": "deepObject",
                    "line_items": "deepObject",
                    "locale": "form",
                    "metadata": "deepObject",
                    "mode": "form",
                    "optional_items": "deepObject",
                    "payment_intent_data": "deepObject",
                    "payment_method_collection": "form",
                    "payment_method_configuration": "form",
                    "payment_method_data": "deepObject",
                    "payment_method_options": "deepObject",
                    "payment_method_types": "deepObject",
                    "permissions": "deepObject",
                    "phone_number_collection": "deepObject",
                    "redirect_on_completion": "form",
                    "return_url": "form",
                    "saved_payment_method_options": "deepObject",
                    "setup_intent_data": "deepObject",
                    "shipping_address_collection": "deepObject",
                    "shipping_options": "deepObject",
                    "submit_type": "form",
                    "subscription_data": "deepObject",
                    "success_url": "form",
                    "tax_id_collection": "deepObject",
                    "ui_mode": "form",
                },
                explode={
                    "adaptive_pricing": True,
                    "after_expiration": True,
                    "allow_promotion_codes": True,
                    "automatic_tax": True,
                    "billing_address_collection": True,
                    "cancel_url": True,
                    "client_reference_id": True,
                    "consent_collection": True,
                    "currency": True,
                    "custom_fields": True,
                    "custom_text": True,
                    "customer": True,
                    "customer_creation": True,
                    "customer_email": True,
                    "customer_update": True,
                    "discounts": True,
                    "expand": True,
                    "expires_at": True,
                    "invoice_creation": True,
                    "line_items": True,
                    "locale": True,
                    "metadata": True,
                    "mode": True,
                    "optional_items": True,
                    "payment_intent_data": True,
                    "payment_method_collection": True,
                    "payment_method_configuration": True,
                    "payment_method_data": True,
                    "payment_method_options": True,
                    "payment_method_types": True,
                    "permissions": True,
                    "phone_number_collection": True,
                    "redirect_on_completion": True,
                    "return_url": True,
                    "saved_payment_method_options": True,
                    "setup_intent_data": True,
                    "shipping_address_collection": True,
                    "shipping_options": True,
                    "submit_type": True,
                    "subscription_data": True,
                    "success_url": True,
                    "tax_id_collection": True,
                    "ui_mode": True,
                },
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path="/v1/checkout/sessions",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.CheckoutSession,
            request_options=request_options or default_request_options(),
        )

    async def update(
        self,
        *,
        session: str,
        data: typing.Union[
            typing.Optional[params.CheckoutSessionUpdateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.CheckoutSession:
        """
        Update a Checkout Session

        <p>Updates a Checkout Session object.</p>

        POST /v1/checkout/sessions/{session}

        Args:
            data: CheckoutSessionUpdateBody
            session: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.checkout.session.update(session="string")
        ```
        """
        models.CheckoutSession.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerCheckoutSessionUpdateBody,
                style={
                    "collected_information": "deepObject",
                    "expand": "deepObject",
                    "metadata": "deepObject",
                    "shipping_options": "deepObject",
                },
                explode={
                    "collected_information": True,
                    "expand": True,
                    "metadata": True,
                    "shipping_options": True,
                },
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/checkout/sessions/{session}",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.CheckoutSession,
            request_options=request_options or default_request_options(),
        )

    async def expire(
        self,
        *,
        session: str,
        data: typing.Union[
            typing.Optional[params.CheckoutSessionExpireBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.CheckoutSession:
        """
        Expire a Checkout Session

        <p>A Checkout Session can be expired when it is in one of these statuses: <code>open</code> </p>

        <p>After it expires, a customer can’t complete a Checkout Session and customers loading the Checkout Session see a message saying the Checkout Session is expired.</p>

        POST /v1/checkout/sessions/{session}/expire

        Args:
            data: CheckoutSessionExpireBody
            session: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.checkout.session.expire(session="string")
        ```
        """
        models.CheckoutSession.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerCheckoutSessionExpireBody,
                style={"expand": "deepObject"},
                explode={"expand": True},
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/checkout/sessions/{session}/expire",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.CheckoutSession,
            request_options=request_options or default_request_options(),
        )
