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
from sideko_stripe.resources.customer.subscription.discount import (
    AsyncDiscountClient,
    DiscountClient,
)
from sideko_stripe.types import models, params


class SubscriptionClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        self.discount = DiscountClient(base_client=self._base_client)

    def delete(
        self,
        *,
        customer: str,
        subscription_exposed_id: str,
        data: typing.Union[
            typing.Optional[params.CustomerSubscriptionDeleteBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Subscription:
        """
        Cancel a subscription

        <p>Cancels a customer’s subscription. If you set the <code>at_period_end</code> parameter to <code>true</code>, the subscription will remain active until the end of the period, at which point it will be canceled and not renewed. Otherwise, with the default <code>false</code> value, the subscription is terminated immediately. In either case, the customer will not be charged again for the subscription.</p>

        <p>Note, however, that any pending invoice items that you’ve created will still be charged for at the end of the period, unless manually <a href="#delete_invoiceitem">deleted</a>. If you’ve set the subscription to cancel at the end of the period, any pending prorations will also be left in place and collected at the end of the period. But if the subscription is set to cancel immediately, pending prorations will be removed.</p>

        <p>By default, upon subscription cancellation, Stripe will stop automatic collection of all finalized invoices for the customer. This is intended to prevent unexpected payment attempts after the customer has canceled a subscription. However, you can resume automatic collection of the invoices manually after subscription cancellation to have us proceed. Or, you could check for unpaid invoices before allowing the customer to cancel the subscription at all.</p>

        DELETE /v1/customers/{customer}/subscriptions/{subscription_exposed_id}

        Args:
            data: CustomerSubscriptionDeleteBody
            customer: str
            subscription_exposed_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.customer.subscription.delete(
            customer="string", subscription_exposed_id="string"
        )
        ```
        """
        models.Subscription.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerCustomerSubscriptionDeleteBody,
                style={
                    "expand": "deepObject",
                    "invoice_now": "form",
                    "prorate": "form",
                },
                explode={"expand": True, "invoice_now": True, "prorate": True},
            )
            if data
            else None
        )
        return self._base_client.request(
            method="DELETE",
            path=f"/v1/customers/{customer}/subscriptions/{subscription_exposed_id}",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.Subscription,
            request_options=request_options or default_request_options(),
        )

    def list(
        self,
        *,
        customer: str,
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
    ) -> models.CustomerSubscriptionListResponse:
        """
        List active subscriptions

        <p>You can see a list of the customer’s active subscriptions. Note that the 10 most recent active subscriptions are always available by default on the customer object. If you need more than those 10, you can use the limit and starting_after parameters to page through additional subscriptions.</p>

        GET /v1/customers/{customer}/subscriptions

        Args:
            ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            expand: Specifies which fields in the response should be expanded.
            limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
            customer: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.customer.subscription.list(customer="string")
        ```
        """
        models.CustomerSubscriptionListResponse.model_rebuild(
            _types_namespace=models._types_namespace
        )
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
        return self._base_client.request(
            method="GET",
            path=f"/v1/customers/{customer}/subscriptions",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.CustomerSubscriptionListResponse,
            request_options=request_options or default_request_options(),
        )

    def get(
        self,
        *,
        customer: str,
        subscription_exposed_id: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Subscription:
        """
        Retrieve a subscription

        <p>Retrieves the subscription with the given ID.</p>

        GET /v1/customers/{customer}/subscriptions/{subscription_exposed_id}

        Args:
            expand: Specifies which fields in the response should be expanded.
            customer: str
            subscription_exposed_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.customer.subscription.get(
            customer="string", subscription_exposed_id="string"
        )
        ```
        """
        models.Subscription.model_rebuild(_types_namespace=models._types_namespace)
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
            path=f"/v1/customers/{customer}/subscriptions/{subscription_exposed_id}",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.Subscription,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        customer: str,
        data: typing.Union[
            typing.Optional[params.CustomerSubscriptionCreateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Subscription:
        """
        Create a subscription

        <p>Creates a new subscription on an existing customer.</p>

        POST /v1/customers/{customer}/subscriptions

        Args:
            data: CustomerSubscriptionCreateBody
            customer: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.customer.subscription.create(customer="string")
        ```
        """
        models.Subscription.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerCustomerSubscriptionCreateBody,
                style={
                    "add_invoice_items": "deepObject",
                    "application_fee_percent": "deepObject",
                    "automatic_tax": "deepObject",
                    "backdate_start_date": "form",
                    "billing_cycle_anchor": "form",
                    "cancel_at": "form",
                    "cancel_at_period_end": "form",
                    "collection_method": "form",
                    "currency": "form",
                    "days_until_due": "form",
                    "default_payment_method": "form",
                    "default_source": "form",
                    "default_tax_rates": "deepObject",
                    "discounts": "deepObject",
                    "expand": "deepObject",
                    "invoice_settings": "deepObject",
                    "items": "deepObject",
                    "metadata": "deepObject",
                    "off_session": "form",
                    "payment_behavior": "form",
                    "payment_settings": "deepObject",
                    "pending_invoice_item_interval": "deepObject",
                    "proration_behavior": "form",
                    "transfer_data": "deepObject",
                    "trial_end": "deepObject",
                    "trial_from_plan": "form",
                    "trial_period_days": "form",
                    "trial_settings": "deepObject",
                },
                explode={
                    "add_invoice_items": True,
                    "application_fee_percent": True,
                    "automatic_tax": True,
                    "backdate_start_date": True,
                    "billing_cycle_anchor": True,
                    "cancel_at": True,
                    "cancel_at_period_end": True,
                    "collection_method": True,
                    "currency": True,
                    "days_until_due": True,
                    "default_payment_method": True,
                    "default_source": True,
                    "default_tax_rates": True,
                    "discounts": True,
                    "expand": True,
                    "invoice_settings": True,
                    "items": True,
                    "metadata": True,
                    "off_session": True,
                    "payment_behavior": True,
                    "payment_settings": True,
                    "pending_invoice_item_interval": True,
                    "proration_behavior": True,
                    "transfer_data": True,
                    "trial_end": True,
                    "trial_from_plan": True,
                    "trial_period_days": True,
                    "trial_settings": True,
                },
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/customers/{customer}/subscriptions",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.Subscription,
            request_options=request_options or default_request_options(),
        )

    def modify(
        self,
        *,
        customer: str,
        subscription_exposed_id: str,
        data: typing.Union[
            typing.Optional[params.CustomerSubscriptionModifyBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Subscription:
        """
        Update a subscription on a customer

        <p>Updates an existing subscription on a customer to match the specified parameters. When changing plans or quantities, we will optionally prorate the price we charge next month to make up for any price changes. To preview how the proration will be calculated, use the <a href="#upcoming_invoice">upcoming invoice</a> endpoint.</p>

        POST /v1/customers/{customer}/subscriptions/{subscription_exposed_id}

        Args:
            data: CustomerSubscriptionModifyBody
            customer: str
            subscription_exposed_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.customer.subscription.modify(
            customer="string", subscription_exposed_id="string"
        )
        ```
        """
        models.Subscription.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerCustomerSubscriptionModifyBody,
                style={
                    "add_invoice_items": "deepObject",
                    "application_fee_percent": "deepObject",
                    "automatic_tax": "deepObject",
                    "billing_cycle_anchor": "form",
                    "cancel_at": "deepObject",
                    "cancel_at_period_end": "form",
                    "cancellation_details": "deepObject",
                    "collection_method": "form",
                    "days_until_due": "form",
                    "default_payment_method": "form",
                    "default_source": "deepObject",
                    "default_tax_rates": "deepObject",
                    "discounts": "deepObject",
                    "expand": "deepObject",
                    "invoice_settings": "deepObject",
                    "items": "deepObject",
                    "metadata": "deepObject",
                    "off_session": "form",
                    "pause_collection": "deepObject",
                    "payment_behavior": "form",
                    "payment_settings": "deepObject",
                    "pending_invoice_item_interval": "deepObject",
                    "proration_behavior": "form",
                    "proration_date": "form",
                    "transfer_data": "deepObject",
                    "trial_end": "deepObject",
                    "trial_from_plan": "form",
                    "trial_settings": "deepObject",
                },
                explode={
                    "add_invoice_items": True,
                    "application_fee_percent": True,
                    "automatic_tax": True,
                    "billing_cycle_anchor": True,
                    "cancel_at": True,
                    "cancel_at_period_end": True,
                    "cancellation_details": True,
                    "collection_method": True,
                    "days_until_due": True,
                    "default_payment_method": True,
                    "default_source": True,
                    "default_tax_rates": True,
                    "discounts": True,
                    "expand": True,
                    "invoice_settings": True,
                    "items": True,
                    "metadata": True,
                    "off_session": True,
                    "pause_collection": True,
                    "payment_behavior": True,
                    "payment_settings": True,
                    "pending_invoice_item_interval": True,
                    "proration_behavior": True,
                    "proration_date": True,
                    "transfer_data": True,
                    "trial_end": True,
                    "trial_from_plan": True,
                    "trial_settings": True,
                },
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/customers/{customer}/subscriptions/{subscription_exposed_id}",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.Subscription,
            request_options=request_options or default_request_options(),
        )


class AsyncSubscriptionClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        self.discount = AsyncDiscountClient(base_client=self._base_client)

    async def delete(
        self,
        *,
        customer: str,
        subscription_exposed_id: str,
        data: typing.Union[
            typing.Optional[params.CustomerSubscriptionDeleteBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Subscription:
        """
        Cancel a subscription

        <p>Cancels a customer’s subscription. If you set the <code>at_period_end</code> parameter to <code>true</code>, the subscription will remain active until the end of the period, at which point it will be canceled and not renewed. Otherwise, with the default <code>false</code> value, the subscription is terminated immediately. In either case, the customer will not be charged again for the subscription.</p>

        <p>Note, however, that any pending invoice items that you’ve created will still be charged for at the end of the period, unless manually <a href="#delete_invoiceitem">deleted</a>. If you’ve set the subscription to cancel at the end of the period, any pending prorations will also be left in place and collected at the end of the period. But if the subscription is set to cancel immediately, pending prorations will be removed.</p>

        <p>By default, upon subscription cancellation, Stripe will stop automatic collection of all finalized invoices for the customer. This is intended to prevent unexpected payment attempts after the customer has canceled a subscription. However, you can resume automatic collection of the invoices manually after subscription cancellation to have us proceed. Or, you could check for unpaid invoices before allowing the customer to cancel the subscription at all.</p>

        DELETE /v1/customers/{customer}/subscriptions/{subscription_exposed_id}

        Args:
            data: CustomerSubscriptionDeleteBody
            customer: str
            subscription_exposed_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.customer.subscription.delete(
            customer="string", subscription_exposed_id="string"
        )
        ```
        """
        models.Subscription.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerCustomerSubscriptionDeleteBody,
                style={
                    "expand": "deepObject",
                    "invoice_now": "form",
                    "prorate": "form",
                },
                explode={"expand": True, "invoice_now": True, "prorate": True},
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="DELETE",
            path=f"/v1/customers/{customer}/subscriptions/{subscription_exposed_id}",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.Subscription,
            request_options=request_options or default_request_options(),
        )

    async def list(
        self,
        *,
        customer: str,
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
    ) -> models.CustomerSubscriptionListResponse:
        """
        List active subscriptions

        <p>You can see a list of the customer’s active subscriptions. Note that the 10 most recent active subscriptions are always available by default on the customer object. If you need more than those 10, you can use the limit and starting_after parameters to page through additional subscriptions.</p>

        GET /v1/customers/{customer}/subscriptions

        Args:
            ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            expand: Specifies which fields in the response should be expanded.
            limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
            customer: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.customer.subscription.list(customer="string")
        ```
        """
        models.CustomerSubscriptionListResponse.model_rebuild(
            _types_namespace=models._types_namespace
        )
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
        return await self._base_client.request(
            method="GET",
            path=f"/v1/customers/{customer}/subscriptions",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.CustomerSubscriptionListResponse,
            request_options=request_options or default_request_options(),
        )

    async def get(
        self,
        *,
        customer: str,
        subscription_exposed_id: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Subscription:
        """
        Retrieve a subscription

        <p>Retrieves the subscription with the given ID.</p>

        GET /v1/customers/{customer}/subscriptions/{subscription_exposed_id}

        Args:
            expand: Specifies which fields in the response should be expanded.
            customer: str
            subscription_exposed_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.customer.subscription.get(
            customer="string", subscription_exposed_id="string"
        )
        ```
        """
        models.Subscription.model_rebuild(_types_namespace=models._types_namespace)
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
            path=f"/v1/customers/{customer}/subscriptions/{subscription_exposed_id}",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.Subscription,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        customer: str,
        data: typing.Union[
            typing.Optional[params.CustomerSubscriptionCreateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Subscription:
        """
        Create a subscription

        <p>Creates a new subscription on an existing customer.</p>

        POST /v1/customers/{customer}/subscriptions

        Args:
            data: CustomerSubscriptionCreateBody
            customer: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.customer.subscription.create(customer="string")
        ```
        """
        models.Subscription.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerCustomerSubscriptionCreateBody,
                style={
                    "add_invoice_items": "deepObject",
                    "application_fee_percent": "deepObject",
                    "automatic_tax": "deepObject",
                    "backdate_start_date": "form",
                    "billing_cycle_anchor": "form",
                    "cancel_at": "form",
                    "cancel_at_period_end": "form",
                    "collection_method": "form",
                    "currency": "form",
                    "days_until_due": "form",
                    "default_payment_method": "form",
                    "default_source": "form",
                    "default_tax_rates": "deepObject",
                    "discounts": "deepObject",
                    "expand": "deepObject",
                    "invoice_settings": "deepObject",
                    "items": "deepObject",
                    "metadata": "deepObject",
                    "off_session": "form",
                    "payment_behavior": "form",
                    "payment_settings": "deepObject",
                    "pending_invoice_item_interval": "deepObject",
                    "proration_behavior": "form",
                    "transfer_data": "deepObject",
                    "trial_end": "deepObject",
                    "trial_from_plan": "form",
                    "trial_period_days": "form",
                    "trial_settings": "deepObject",
                },
                explode={
                    "add_invoice_items": True,
                    "application_fee_percent": True,
                    "automatic_tax": True,
                    "backdate_start_date": True,
                    "billing_cycle_anchor": True,
                    "cancel_at": True,
                    "cancel_at_period_end": True,
                    "collection_method": True,
                    "currency": True,
                    "days_until_due": True,
                    "default_payment_method": True,
                    "default_source": True,
                    "default_tax_rates": True,
                    "discounts": True,
                    "expand": True,
                    "invoice_settings": True,
                    "items": True,
                    "metadata": True,
                    "off_session": True,
                    "payment_behavior": True,
                    "payment_settings": True,
                    "pending_invoice_item_interval": True,
                    "proration_behavior": True,
                    "transfer_data": True,
                    "trial_end": True,
                    "trial_from_plan": True,
                    "trial_period_days": True,
                    "trial_settings": True,
                },
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/customers/{customer}/subscriptions",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.Subscription,
            request_options=request_options or default_request_options(),
        )

    async def modify(
        self,
        *,
        customer: str,
        subscription_exposed_id: str,
        data: typing.Union[
            typing.Optional[params.CustomerSubscriptionModifyBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Subscription:
        """
        Update a subscription on a customer

        <p>Updates an existing subscription on a customer to match the specified parameters. When changing plans or quantities, we will optionally prorate the price we charge next month to make up for any price changes. To preview how the proration will be calculated, use the <a href="#upcoming_invoice">upcoming invoice</a> endpoint.</p>

        POST /v1/customers/{customer}/subscriptions/{subscription_exposed_id}

        Args:
            data: CustomerSubscriptionModifyBody
            customer: str
            subscription_exposed_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.customer.subscription.modify(
            customer="string", subscription_exposed_id="string"
        )
        ```
        """
        models.Subscription.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerCustomerSubscriptionModifyBody,
                style={
                    "add_invoice_items": "deepObject",
                    "application_fee_percent": "deepObject",
                    "automatic_tax": "deepObject",
                    "billing_cycle_anchor": "form",
                    "cancel_at": "deepObject",
                    "cancel_at_period_end": "form",
                    "cancellation_details": "deepObject",
                    "collection_method": "form",
                    "days_until_due": "form",
                    "default_payment_method": "form",
                    "default_source": "deepObject",
                    "default_tax_rates": "deepObject",
                    "discounts": "deepObject",
                    "expand": "deepObject",
                    "invoice_settings": "deepObject",
                    "items": "deepObject",
                    "metadata": "deepObject",
                    "off_session": "form",
                    "pause_collection": "deepObject",
                    "payment_behavior": "form",
                    "payment_settings": "deepObject",
                    "pending_invoice_item_interval": "deepObject",
                    "proration_behavior": "form",
                    "proration_date": "form",
                    "transfer_data": "deepObject",
                    "trial_end": "deepObject",
                    "trial_from_plan": "form",
                    "trial_settings": "deepObject",
                },
                explode={
                    "add_invoice_items": True,
                    "application_fee_percent": True,
                    "automatic_tax": True,
                    "billing_cycle_anchor": True,
                    "cancel_at": True,
                    "cancel_at_period_end": True,
                    "cancellation_details": True,
                    "collection_method": True,
                    "days_until_due": True,
                    "default_payment_method": True,
                    "default_source": True,
                    "default_tax_rates": True,
                    "discounts": True,
                    "expand": True,
                    "invoice_settings": True,
                    "items": True,
                    "metadata": True,
                    "off_session": True,
                    "pause_collection": True,
                    "payment_behavior": True,
                    "payment_settings": True,
                    "pending_invoice_item_interval": True,
                    "proration_behavior": True,
                    "proration_date": True,
                    "transfer_data": True,
                    "trial_end": True,
                    "trial_from_plan": True,
                    "trial_settings": True,
                },
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/customers/{customer}/subscriptions/{subscription_exposed_id}",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.Subscription,
            request_options=request_options or default_request_options(),
        )
