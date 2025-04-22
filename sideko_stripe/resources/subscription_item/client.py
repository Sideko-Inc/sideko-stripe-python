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


class SubscriptionItemClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def delete(
        self,
        *,
        item: str,
        data: typing.Union[
            typing.Optional[params.SubscriptionItemDeleteBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.DeletedSubscriptionItem:
        """
        Delete a subscription item

        <p>Deletes an item from the subscription. Removing a subscription item from a subscription will not cancel the subscription.</p>

        DELETE /v1/subscription_items/{item}

        Args:
            data: SubscriptionItemDeleteBody
            item: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.subscription_item.delete(item="string")
        ```
        """
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerSubscriptionItemDeleteBody,
                style={
                    "clear_usage": "form",
                    "proration_behavior": "form",
                    "proration_date": "form",
                },
                explode={
                    "clear_usage": True,
                    "proration_behavior": True,
                    "proration_date": True,
                },
            )
            if data
            else None
        )
        return self._base_client.request(
            method="DELETE",
            path=f"/v1/subscription_items/{item}",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.DeletedSubscriptionItem,
            request_options=request_options or default_request_options(),
        )

    def list(
        self,
        *,
        subscription: str,
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
    ) -> models.SubscriptionItemListResponse:
        """
        List all subscription items

        <p>Returns a list of your subscription items for a given subscription.</p>

        GET /v1/subscription_items

        Args:
            ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            expand: Specifies which fields in the response should be expanded.
            limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
            subscription: The ID of the subscription whose items will be retrieved.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.subscription_item.list(subscription="string")
        ```
        """
        models.SubscriptionItemListResponse.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _query: QueryParams = {}
        encode_query_param(
            _query,
            "subscription",
            to_encodable(item=subscription, dump_with=str),
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
            path="/v1/subscription_items",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.SubscriptionItemListResponse,
            request_options=request_options or default_request_options(),
        )

    def get(
        self,
        *,
        item: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.SubscriptionItem:
        """
        Retrieve a subscription item

        <p>Retrieves the subscription item with the given ID.</p>

        GET /v1/subscription_items/{item}

        Args:
            expand: Specifies which fields in the response should be expanded.
            item: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.subscription_item.get(item="string")
        ```
        """
        models.SubscriptionItem.model_rebuild(_types_namespace=models._types_namespace)
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
            path=f"/v1/subscription_items/{item}",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.SubscriptionItem,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        subscription: str,
        discounts: typing.Union[
            typing.Optional[
                typing.Union[
                    typing.List[params.SubscriptionItemCreateBodyDiscountsArr0Item], str
                ]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        metadata: typing.Union[
            typing.Optional[params.SubscriptionItemCreateBodyMetadata],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        payment_behavior: typing.Union[
            typing.Optional[
                typing_extensions.Literal[
                    "allow_incomplete",
                    "default_incomplete",
                    "error_if_incomplete",
                    "pending_if_incomplete",
                ]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        price: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        price_data: typing.Union[
            typing.Optional[params.SubscriptionItemCreateBodyPriceData],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        proration_behavior: typing.Union[
            typing.Optional[
                typing_extensions.Literal["always_invoice", "create_prorations", "none"]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        proration_date: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        quantity: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        tax_rates: typing.Union[
            typing.Optional[typing.Union[typing.List[str], str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.SubscriptionItem:
        """
        Create a subscription item

        <p>Adds a new item to an existing subscription. No existing items will be changed or replaced.</p>

        POST /v1/subscription_items

        Args:
            discounts: The coupons to redeem into discounts for the subscription item.
            expand: Specifies which fields in the response should be expanded.
            metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
            payment_behavior: Use `allow_incomplete` to transition the subscription to `status=past_due` if a payment is required but cannot be paid. This allows you to manage scenarios where additional user actions are needed to pay a subscription's invoice. For example, SCA regulation may require 3DS authentication to complete payment. See the [SCA Migration Guide](https://stripe.com/docs/billing/migration/strong-customer-authentication) for Billing to learn more. This is the default behavior.

        Use `default_incomplete` to transition the subscription to `status=past_due` when payment is required and await explicit confirmation of the invoice's payment intent. This allows simpler management of scenarios where additional user actions are needed to pay a subscription’s invoice. Such as failed payments, [SCA regulation](https://stripe.com/docs/billing/migration/strong-customer-authentication), or collecting a mandate for a bank debit payment method.

        Use `pending_if_incomplete` to update the subscription using [pending updates](https://stripe.com/docs/billing/subscriptions/pending-updates). When you use `pending_if_incomplete` you can only pass the parameters [supported by pending updates](https://stripe.com/docs/billing/pending-updates-reference#supported-attributes).

        Use `error_if_incomplete` if you want Stripe to return an HTTP 402 status code if a subscription's invoice cannot be paid. For example, if a payment method requires 3DS authentication due to SCA regulation and further user action is needed, this parameter does not update the subscription and returns an error instead. This was the default behavior for API versions prior to 2019-03-14. See the [changelog](https://stripe.com/docs/upgrades#2019-03-14) to learn more.
            price: The ID of the price object.
            price_data: Data used to generate a new [Price](https://stripe.com/docs/api/prices) object inline.
            proration_behavior: Determines how to handle [prorations](https://stripe.com/docs/billing/subscriptions/prorations) when the billing cycle changes (e.g., when switching plans, resetting `billing_cycle_anchor=now`, or starting a trial), or if an item's `quantity` changes. The default value is `create_prorations`.
            proration_date: If set, the proration will be calculated as though the subscription was updated at the given time. This can be used to apply the same proration that was previewed with the [upcoming invoice](https://stripe.com/docs/api#retrieve_customer_invoice) endpoint.
            quantity: The quantity you'd like to apply to the subscription item you're creating.
            tax_rates: A list of [Tax Rate](https://stripe.com/docs/api/tax_rates) ids. These Tax Rates will override the [`default_tax_rates`](https://stripe.com/docs/api/subscriptions/create#create_subscription-default_tax_rates) on the Subscription. When updating, pass an empty string to remove previously-defined tax rates.
            subscription: The identifier of the subscription to modify.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.subscription_item.create(subscription="string")
        ```
        """
        models.SubscriptionItem.model_rebuild(_types_namespace=models._types_namespace)
        _data = to_form_urlencoded(
            item={
                "discounts": discounts,
                "expand": expand,
                "metadata": metadata,
                "payment_behavior": payment_behavior,
                "price": price,
                "price_data": price_data,
                "proration_behavior": proration_behavior,
                "proration_date": proration_date,
                "quantity": quantity,
                "tax_rates": tax_rates,
                "subscription": subscription,
            },
            dump_with=params._SerializerSubscriptionItemCreateBody,
            style={
                "discounts": "deepObject",
                "expand": "deepObject",
                "metadata": "deepObject",
                "payment_behavior": "form",
                "price": "form",
                "price_data": "deepObject",
                "proration_behavior": "form",
                "proration_date": "form",
                "quantity": "form",
                "subscription": "form",
                "tax_rates": "deepObject",
            },
            explode={
                "discounts": True,
                "expand": True,
                "metadata": True,
                "payment_behavior": True,
                "price": True,
                "price_data": True,
                "proration_behavior": True,
                "proration_date": True,
                "quantity": True,
                "subscription": True,
                "tax_rates": True,
            },
        )
        return self._base_client.request(
            method="POST",
            path="/v1/subscription_items",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.SubscriptionItem,
            request_options=request_options or default_request_options(),
        )

    def update(
        self,
        *,
        item: str,
        data: typing.Union[
            typing.Optional[params.SubscriptionItemUpdateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.SubscriptionItem:
        """
        Update a subscription item

        <p>Updates the plan or quantity of an item on a current subscription.</p>

        POST /v1/subscription_items/{item}

        Args:
            data: SubscriptionItemUpdateBody
            item: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.subscription_item.update(item="string")
        ```
        """
        models.SubscriptionItem.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerSubscriptionItemUpdateBody,
                style={
                    "discounts": "deepObject",
                    "expand": "deepObject",
                    "metadata": "deepObject",
                    "off_session": "form",
                    "payment_behavior": "form",
                    "price": "form",
                    "price_data": "deepObject",
                    "proration_behavior": "form",
                    "proration_date": "form",
                    "quantity": "form",
                    "tax_rates": "deepObject",
                },
                explode={
                    "discounts": True,
                    "expand": True,
                    "metadata": True,
                    "off_session": True,
                    "payment_behavior": True,
                    "price": True,
                    "price_data": True,
                    "proration_behavior": True,
                    "proration_date": True,
                    "quantity": True,
                    "tax_rates": True,
                },
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/subscription_items/{item}",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.SubscriptionItem,
            request_options=request_options or default_request_options(),
        )


class AsyncSubscriptionItemClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def delete(
        self,
        *,
        item: str,
        data: typing.Union[
            typing.Optional[params.SubscriptionItemDeleteBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.DeletedSubscriptionItem:
        """
        Delete a subscription item

        <p>Deletes an item from the subscription. Removing a subscription item from a subscription will not cancel the subscription.</p>

        DELETE /v1/subscription_items/{item}

        Args:
            data: SubscriptionItemDeleteBody
            item: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.subscription_item.delete(item="string")
        ```
        """
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerSubscriptionItemDeleteBody,
                style={
                    "clear_usage": "form",
                    "proration_behavior": "form",
                    "proration_date": "form",
                },
                explode={
                    "clear_usage": True,
                    "proration_behavior": True,
                    "proration_date": True,
                },
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="DELETE",
            path=f"/v1/subscription_items/{item}",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.DeletedSubscriptionItem,
            request_options=request_options or default_request_options(),
        )

    async def list(
        self,
        *,
        subscription: str,
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
    ) -> models.SubscriptionItemListResponse:
        """
        List all subscription items

        <p>Returns a list of your subscription items for a given subscription.</p>

        GET /v1/subscription_items

        Args:
            ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            expand: Specifies which fields in the response should be expanded.
            limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
            subscription: The ID of the subscription whose items will be retrieved.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.subscription_item.list(subscription="string")
        ```
        """
        models.SubscriptionItemListResponse.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _query: QueryParams = {}
        encode_query_param(
            _query,
            "subscription",
            to_encodable(item=subscription, dump_with=str),
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
            path="/v1/subscription_items",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.SubscriptionItemListResponse,
            request_options=request_options or default_request_options(),
        )

    async def get(
        self,
        *,
        item: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.SubscriptionItem:
        """
        Retrieve a subscription item

        <p>Retrieves the subscription item with the given ID.</p>

        GET /v1/subscription_items/{item}

        Args:
            expand: Specifies which fields in the response should be expanded.
            item: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.subscription_item.get(item="string")
        ```
        """
        models.SubscriptionItem.model_rebuild(_types_namespace=models._types_namespace)
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
            path=f"/v1/subscription_items/{item}",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.SubscriptionItem,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        subscription: str,
        discounts: typing.Union[
            typing.Optional[
                typing.Union[
                    typing.List[params.SubscriptionItemCreateBodyDiscountsArr0Item], str
                ]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        metadata: typing.Union[
            typing.Optional[params.SubscriptionItemCreateBodyMetadata],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        payment_behavior: typing.Union[
            typing.Optional[
                typing_extensions.Literal[
                    "allow_incomplete",
                    "default_incomplete",
                    "error_if_incomplete",
                    "pending_if_incomplete",
                ]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        price: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        price_data: typing.Union[
            typing.Optional[params.SubscriptionItemCreateBodyPriceData],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        proration_behavior: typing.Union[
            typing.Optional[
                typing_extensions.Literal["always_invoice", "create_prorations", "none"]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        proration_date: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        quantity: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        tax_rates: typing.Union[
            typing.Optional[typing.Union[typing.List[str], str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.SubscriptionItem:
        """
        Create a subscription item

        <p>Adds a new item to an existing subscription. No existing items will be changed or replaced.</p>

        POST /v1/subscription_items

        Args:
            discounts: The coupons to redeem into discounts for the subscription item.
            expand: Specifies which fields in the response should be expanded.
            metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
            payment_behavior: Use `allow_incomplete` to transition the subscription to `status=past_due` if a payment is required but cannot be paid. This allows you to manage scenarios where additional user actions are needed to pay a subscription's invoice. For example, SCA regulation may require 3DS authentication to complete payment. See the [SCA Migration Guide](https://stripe.com/docs/billing/migration/strong-customer-authentication) for Billing to learn more. This is the default behavior.

        Use `default_incomplete` to transition the subscription to `status=past_due` when payment is required and await explicit confirmation of the invoice's payment intent. This allows simpler management of scenarios where additional user actions are needed to pay a subscription’s invoice. Such as failed payments, [SCA regulation](https://stripe.com/docs/billing/migration/strong-customer-authentication), or collecting a mandate for a bank debit payment method.

        Use `pending_if_incomplete` to update the subscription using [pending updates](https://stripe.com/docs/billing/subscriptions/pending-updates). When you use `pending_if_incomplete` you can only pass the parameters [supported by pending updates](https://stripe.com/docs/billing/pending-updates-reference#supported-attributes).

        Use `error_if_incomplete` if you want Stripe to return an HTTP 402 status code if a subscription's invoice cannot be paid. For example, if a payment method requires 3DS authentication due to SCA regulation and further user action is needed, this parameter does not update the subscription and returns an error instead. This was the default behavior for API versions prior to 2019-03-14. See the [changelog](https://stripe.com/docs/upgrades#2019-03-14) to learn more.
            price: The ID of the price object.
            price_data: Data used to generate a new [Price](https://stripe.com/docs/api/prices) object inline.
            proration_behavior: Determines how to handle [prorations](https://stripe.com/docs/billing/subscriptions/prorations) when the billing cycle changes (e.g., when switching plans, resetting `billing_cycle_anchor=now`, or starting a trial), or if an item's `quantity` changes. The default value is `create_prorations`.
            proration_date: If set, the proration will be calculated as though the subscription was updated at the given time. This can be used to apply the same proration that was previewed with the [upcoming invoice](https://stripe.com/docs/api#retrieve_customer_invoice) endpoint.
            quantity: The quantity you'd like to apply to the subscription item you're creating.
            tax_rates: A list of [Tax Rate](https://stripe.com/docs/api/tax_rates) ids. These Tax Rates will override the [`default_tax_rates`](https://stripe.com/docs/api/subscriptions/create#create_subscription-default_tax_rates) on the Subscription. When updating, pass an empty string to remove previously-defined tax rates.
            subscription: The identifier of the subscription to modify.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.subscription_item.create(subscription="string")
        ```
        """
        models.SubscriptionItem.model_rebuild(_types_namespace=models._types_namespace)
        _data = to_form_urlencoded(
            item={
                "discounts": discounts,
                "expand": expand,
                "metadata": metadata,
                "payment_behavior": payment_behavior,
                "price": price,
                "price_data": price_data,
                "proration_behavior": proration_behavior,
                "proration_date": proration_date,
                "quantity": quantity,
                "tax_rates": tax_rates,
                "subscription": subscription,
            },
            dump_with=params._SerializerSubscriptionItemCreateBody,
            style={
                "discounts": "deepObject",
                "expand": "deepObject",
                "metadata": "deepObject",
                "payment_behavior": "form",
                "price": "form",
                "price_data": "deepObject",
                "proration_behavior": "form",
                "proration_date": "form",
                "quantity": "form",
                "subscription": "form",
                "tax_rates": "deepObject",
            },
            explode={
                "discounts": True,
                "expand": True,
                "metadata": True,
                "payment_behavior": True,
                "price": True,
                "price_data": True,
                "proration_behavior": True,
                "proration_date": True,
                "quantity": True,
                "subscription": True,
                "tax_rates": True,
            },
        )
        return await self._base_client.request(
            method="POST",
            path="/v1/subscription_items",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.SubscriptionItem,
            request_options=request_options or default_request_options(),
        )

    async def update(
        self,
        *,
        item: str,
        data: typing.Union[
            typing.Optional[params.SubscriptionItemUpdateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.SubscriptionItem:
        """
        Update a subscription item

        <p>Updates the plan or quantity of an item on a current subscription.</p>

        POST /v1/subscription_items/{item}

        Args:
            data: SubscriptionItemUpdateBody
            item: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.subscription_item.update(item="string")
        ```
        """
        models.SubscriptionItem.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerSubscriptionItemUpdateBody,
                style={
                    "discounts": "deepObject",
                    "expand": "deepObject",
                    "metadata": "deepObject",
                    "off_session": "form",
                    "payment_behavior": "form",
                    "price": "form",
                    "price_data": "deepObject",
                    "proration_behavior": "form",
                    "proration_date": "form",
                    "quantity": "form",
                    "tax_rates": "deepObject",
                },
                explode={
                    "discounts": True,
                    "expand": True,
                    "metadata": True,
                    "off_session": True,
                    "payment_behavior": True,
                    "price": True,
                    "price_data": True,
                    "proration_behavior": True,
                    "proration_date": True,
                    "quantity": True,
                    "tax_rates": True,
                },
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/subscription_items/{item}",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.SubscriptionItem,
            request_options=request_options or default_request_options(),
        )
