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


class SubscriptionClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def delete(
        self,
        *,
        subscription_exposed_id: str,
        data: typing.Union[
            typing.Optional[params.SubscriptionDeleteBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Subscription:
        """
        Cancel a subscription

        <p>Cancels a customer’s subscription immediately. The customer won’t be charged again for the subscription. After it’s canceled, you can no longer update the subscription or its <a href="/metadata">metadata</a>.</p>

        <p>Any pending invoice items that you’ve created are still charged at the end of the period, unless manually <a href="#delete_invoiceitem">deleted</a>. If you’ve set the subscription to cancel at the end of the period, any pending prorations are also left in place and collected at the end of the period. But if the subscription is set to cancel immediately, pending prorations are removed.</p>

        <p>By default, upon subscription cancellation, Stripe stops automatic collection of all finalized invoices for the customer. This is intended to prevent unexpected payment attempts after the customer has canceled a subscription. However, you can resume automatic collection of the invoices manually after subscription cancellation to have us proceed. Or, you could check for unpaid invoices before allowing the customer to cancel the subscription at all.</p>

        DELETE /v1/subscriptions/{subscription_exposed_id}

        Args:
            data: SubscriptionDeleteBody
            subscription_exposed_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.subscription.delete(subscription_exposed_id="string")
        ```
        """
        models.Subscription.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerSubscriptionDeleteBody,
                style={
                    "cancellation_details": "deepObject",
                    "expand": "deepObject",
                    "invoice_now": "form",
                    "prorate": "form",
                },
                explode={
                    "cancellation_details": True,
                    "expand": True,
                    "invoice_now": True,
                    "prorate": True,
                },
            )
            if data
            else None
        )
        return self._base_client.request(
            method="DELETE",
            path=f"/v1/subscriptions/{subscription_exposed_id}",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.Subscription,
            request_options=request_options or default_request_options(),
        )

    def list(
        self,
        *,
        automatic_tax: typing.Union[
            typing.Optional[params.SubscriptionListAutomaticTax], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        collection_method: typing.Union[
            typing.Optional[
                typing_extensions.Literal["charge_automatically", "send_invoice"]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        created: typing.Union[
            typing.Optional[typing.Union[params.SubscriptionListCreatedObj0, int]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        current_period_end: typing.Union[
            typing.Optional[
                typing.Union[params.SubscriptionListCurrentPeriodEndObj0, int]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        current_period_start: typing.Union[
            typing.Optional[
                typing.Union[params.SubscriptionListCurrentPeriodStartObj0, int]
            ],
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
        price: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        starting_after: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        status: typing.Union[
            typing.Optional[
                typing_extensions.Literal[
                    "active",
                    "all",
                    "canceled",
                    "ended",
                    "incomplete",
                    "incomplete_expired",
                    "past_due",
                    "paused",
                    "trialing",
                    "unpaid",
                ]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        test_clock: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.SubscriptionListResponse:
        """
        List subscriptions

        <p>By default, returns a list of subscriptions that have not been canceled. In order to list canceled subscriptions, specify <code>status=canceled</code>.</p>

        GET /v1/subscriptions

        Args:
            automatic_tax: Filter subscriptions by their automatic tax settings.
            collection_method: The collection method of the subscriptions to retrieve. Either `charge_automatically` or `send_invoice`.
            created: Only return subscriptions that were created during the given date interval.
            current_period_end: Only return subscriptions whose current_period_end falls within the given date interval.
            current_period_start: Only return subscriptions whose current_period_start falls within the given date interval.
            customer: The ID of the customer whose subscriptions will be retrieved.
            ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            expand: Specifies which fields in the response should be expanded.
            limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            price: Filter for subscriptions that contain this recurring price ID.
            starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
            status: The status of the subscriptions to retrieve. Passing in a value of `canceled` will return all canceled subscriptions, including those belonging to deleted customers. Pass `ended` to find subscriptions that are canceled and subscriptions that are expired due to [incomplete payment](https://stripe.com/docs/billing/subscriptions/overview#subscription-statuses). Passing in a value of `all` will return subscriptions of all statuses. If no value is supplied, all subscriptions that have not been canceled are returned.
            test_clock: Filter for subscriptions that are associated with the specified test clock. The response will not include subscriptions with test clocks if this and the customer parameter is not set.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.subscription.list()
        ```
        """
        models.SubscriptionListResponse.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _query: QueryParams = {}
        if not isinstance(automatic_tax, type_utils.NotGiven):
            encode_query_param(
                _query,
                "automatic_tax",
                to_encodable(
                    item=automatic_tax,
                    dump_with=params._SerializerSubscriptionListAutomaticTax,
                ),
                style="deepObject",
                explode=True,
            )
        if not isinstance(collection_method, type_utils.NotGiven):
            encode_query_param(
                _query,
                "collection_method",
                to_encodable(
                    item=collection_method,
                    dump_with=typing_extensions.Literal[
                        "charge_automatically", "send_invoice"
                    ],
                ),
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
                        params._SerializerSubscriptionListCreatedObj0, int
                    ],
                ),
                style="deepObject",
                explode=True,
            )
        if not isinstance(current_period_end, type_utils.NotGiven):
            encode_query_param(
                _query,
                "current_period_end",
                to_encodable(
                    item=current_period_end,
                    dump_with=typing.Union[
                        params._SerializerSubscriptionListCurrentPeriodEndObj0, int
                    ],
                ),
                style="deepObject",
                explode=True,
            )
        if not isinstance(current_period_start, type_utils.NotGiven):
            encode_query_param(
                _query,
                "current_period_start",
                to_encodable(
                    item=current_period_start,
                    dump_with=typing.Union[
                        params._SerializerSubscriptionListCurrentPeriodStartObj0, int
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
        if not isinstance(price, type_utils.NotGiven):
            encode_query_param(
                _query,
                "price",
                to_encodable(item=price, dump_with=str),
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
                        "active",
                        "all",
                        "canceled",
                        "ended",
                        "incomplete",
                        "incomplete_expired",
                        "past_due",
                        "paused",
                        "trialing",
                        "unpaid",
                    ],
                ),
                style="form",
                explode=True,
            )
        if not isinstance(test_clock, type_utils.NotGiven):
            encode_query_param(
                _query,
                "test_clock",
                to_encodable(item=test_clock, dump_with=str),
                style="form",
                explode=True,
            )
        return self._base_client.request(
            method="GET",
            path="/v1/subscriptions",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.SubscriptionListResponse,
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
    ) -> models.SubscriptionSearchResponse:
        """
        Search subscriptions

        <p>Search for subscriptions you’ve previously created using Stripe’s <a href="/docs/search#search-query-language">Search Query Language</a>.
        Don’t use search in read-after-write flows where strict consistency is necessary. Under normal operating
        conditions, data is searchable in less than a minute. Occasionally, propagation of new or updated data can be up
        to an hour behind during outages. Search functionality is not available to merchants in India.</p>

        GET /v1/subscriptions/search

        Args:
            expand: Specifies which fields in the response should be expanded.
            limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            page: A cursor for pagination across multiple pages of results. Don't include this parameter on the first call. Use the next_page value returned in a previous response to request subsequent results.
            query: The search query string. See [search query language](https://stripe.com/docs/search#search-query-language) and the list of supported [query fields for subscriptions](https://stripe.com/docs/search#query-fields-for-subscriptions).
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.subscription.search(query="string")
        ```
        """
        models.SubscriptionSearchResponse.model_rebuild(
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
            path="/v1/subscriptions/search",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.SubscriptionSearchResponse,
            request_options=request_options or default_request_options(),
        )

    def get(
        self,
        *,
        subscription_exposed_id: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Subscription:
        """
        Retrieve a subscription

        <p>Retrieves the subscription with the given ID.</p>

        GET /v1/subscriptions/{subscription_exposed_id}

        Args:
            expand: Specifies which fields in the response should be expanded.
            subscription_exposed_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.subscription.get(subscription_exposed_id="string")
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
            path=f"/v1/subscriptions/{subscription_exposed_id}",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.Subscription,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        customer: str,
        add_invoice_items: typing.Union[
            typing.Optional[
                typing.List[params.SubscriptionCreateBodyAddInvoiceItemsItem]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        application_fee_percent: typing.Union[
            typing.Optional[typing.Union[float, str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        automatic_tax: typing.Union[
            typing.Optional[params.SubscriptionCreateBodyAutomaticTax],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        backdate_start_date: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        billing_cycle_anchor: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        billing_cycle_anchor_config: typing.Union[
            typing.Optional[params.SubscriptionCreateBodyBillingCycleAnchorConfig],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        cancel_at: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        cancel_at_period_end: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        collection_method: typing.Union[
            typing.Optional[
                typing_extensions.Literal["charge_automatically", "send_invoice"]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        currency: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        days_until_due: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        default_payment_method: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        default_source: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        default_tax_rates: typing.Union[
            typing.Optional[typing.Union[typing.List[str], str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        description: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        discounts: typing.Union[
            typing.Optional[
                typing.Union[
                    typing.List[params.SubscriptionCreateBodyDiscountsArr0Item], str
                ]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        invoice_settings: typing.Union[
            typing.Optional[params.SubscriptionCreateBodyInvoiceSettings],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        items: typing.Union[
            typing.Optional[typing.List[params.SubscriptionCreateBodyItemsItem]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        metadata: typing.Union[
            typing.Optional[
                typing.Union[params.SubscriptionCreateBodyMetadataObj0, str]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        off_session: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        on_behalf_of: typing.Union[
            typing.Optional[typing.Union[str, str]], type_utils.NotGiven
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
        payment_settings: typing.Union[
            typing.Optional[params.SubscriptionCreateBodyPaymentSettings],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        pending_invoice_item_interval: typing.Union[
            typing.Optional[
                typing.Union[
                    params.SubscriptionCreateBodyPendingInvoiceItemIntervalObj0, str
                ]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        proration_behavior: typing.Union[
            typing.Optional[
                typing_extensions.Literal["always_invoice", "create_prorations", "none"]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        transfer_data: typing.Union[
            typing.Optional[params.SubscriptionCreateBodyTransferData],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        trial_end: typing.Union[
            typing.Optional[typing.Union[typing_extensions.Literal["now"], int]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        trial_from_plan: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        trial_period_days: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        trial_settings: typing.Union[
            typing.Optional[params.SubscriptionCreateBodyTrialSettings],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Subscription:
        """
        Create a subscription

        <p>Creates a new subscription on an existing customer. Each customer can have up to 500 active or scheduled subscriptions.</p>

        <p>When you create a subscription with <code>collection_method=charge_automatically</code>, the first invoice is finalized as part of the request.
        The <code>payment_behavior</code> parameter determines the exact behavior of the initial payment.</p>

        <p>To start subscriptions where the first invoice always begins in a <code>draft</code> status, use <a href="/docs/billing/subscriptions/subscription-schedules#managing">subscription schedules</a> instead.
        Schedules provide the flexibility to model more complex billing configurations that change over time.</p>

        POST /v1/subscriptions

        Args:
            add_invoice_items: A list of prices and quantities that will generate invoice items appended to the next invoice for this subscription. You may pass up to 20 items.
            application_fee_percent: A non-negative decimal between 0 and 100, with at most two decimal places. This represents the percentage of the subscription invoice total that will be transferred to the application owner's Stripe account. The request must be made by a platform account on a connected account in order to set an application fee percentage. For more information, see the application fees [documentation](https://stripe.com/docs/connect/subscriptions#collecting-fees-on-subscriptions).
            automatic_tax: Automatic tax settings for this subscription. We recommend you only include this parameter when the existing value is being changed.
            backdate_start_date: For new subscriptions, a past timestamp to backdate the subscription's start date to. If set, the first invoice will contain a proration for the timespan between the start date and the current time. Can be combined with trials and the billing cycle anchor.
            billing_cycle_anchor: A future timestamp in UTC format to anchor the subscription's [billing cycle](https://stripe.com/docs/subscriptions/billing-cycle). The anchor is the reference point that aligns future billing cycle dates. It sets the day of week for `week` intervals, the day of month for `month` and `year` intervals, and the month of year for `year` intervals.
            billing_cycle_anchor_config: Mutually exclusive with billing_cycle_anchor and only valid with monthly and yearly price intervals. When provided, the billing_cycle_anchor is set to the next occurence of the day_of_month at the hour, minute, and second UTC.
            cancel_at: A timestamp at which the subscription should cancel. If set to a date before the current period ends, this will cause a proration if prorations have been enabled using `proration_behavior`. If set during a future period, this will always cause a proration for that period.
            cancel_at_period_end: Indicate whether this subscription should cancel at the end of the current period (`current_period_end`). Defaults to `false`.
            collection_method: Either `charge_automatically`, or `send_invoice`. When charging automatically, Stripe will attempt to pay this subscription at the end of the cycle using the default source attached to the customer. When sending an invoice, Stripe will email your customer an invoice with payment instructions and mark the subscription as `active`. Defaults to `charge_automatically`.
            currency: Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
            days_until_due: Number of days a customer has to pay invoices generated by this subscription. Valid only for subscriptions where `collection_method` is set to `send_invoice`.
            default_payment_method: ID of the default payment method for the subscription. It must belong to the customer associated with the subscription. This takes precedence over `default_source`. If neither are set, invoices will use the customer's [invoice_settings.default_payment_method](https://stripe.com/docs/api/customers/object#customer_object-invoice_settings-default_payment_method) or [default_source](https://stripe.com/docs/api/customers/object#customer_object-default_source).
            default_source: ID of the default payment source for the subscription. It must belong to the customer associated with the subscription and be in a chargeable state. If `default_payment_method` is also set, `default_payment_method` will take precedence. If neither are set, invoices will use the customer's [invoice_settings.default_payment_method](https://stripe.com/docs/api/customers/object#customer_object-invoice_settings-default_payment_method) or [default_source](https://stripe.com/docs/api/customers/object#customer_object-default_source).
            default_tax_rates: The tax rates that will apply to any subscription item that does not have `tax_rates` set. Invoices created will have their `default_tax_rates` populated from the subscription.
            description: The subscription's description, meant to be displayable to the customer. Use this field to optionally store an explanation of the subscription for rendering in Stripe surfaces and certain local payment methods UIs.
            discounts: The coupons to redeem into discounts for the subscription. If not specified or empty, inherits the discount from the subscription's customer.
            expand: Specifies which fields in the response should be expanded.
            invoice_settings: All invoices will be billed using the specified settings.
            items: A list of up to 20 subscription items, each with an attached price.
            metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
            off_session: Indicates if a customer is on or off-session while an invoice payment is attempted. Defaults to `false` (on-session).
            on_behalf_of: The account on behalf of which to charge, for each of the subscription's invoices.
            payment_behavior: Only applies to subscriptions with `collection_method=charge_automatically`.

        Use `allow_incomplete` to create Subscriptions with `status=incomplete` if the first invoice can't be paid. Creating Subscriptions with this status allows you to manage scenarios where additional customer actions are needed to pay a subscription's invoice. For example, SCA regulation may require 3DS authentication to complete payment. See the [SCA Migration Guide](https://stripe.com/docs/billing/migration/strong-customer-authentication) for Billing to learn more. This is the default behavior.

        Use `default_incomplete` to create Subscriptions with `status=incomplete` when the first invoice requires payment, otherwise start as active. Subscriptions transition to `status=active` when successfully confirming the PaymentIntent on the first invoice. This allows simpler management of scenarios where additional customer actions are needed to pay a subscription’s invoice, such as failed payments, [SCA regulation](https://stripe.com/docs/billing/migration/strong-customer-authentication), or collecting a mandate for a bank debit payment method. If the PaymentIntent is not confirmed within 23 hours Subscriptions transition to `status=incomplete_expired`, which is a terminal state.

        Use `error_if_incomplete` if you want Stripe to return an HTTP 402 status code if a subscription's first invoice can't be paid. For example, if a payment method requires 3DS authentication due to SCA regulation and further customer action is needed, this parameter doesn't create a Subscription and returns an error instead. This was the default behavior for API versions prior to 2019-03-14. See the [changelog](https://stripe.com/docs/upgrades#2019-03-14) to learn more.

        `pending_if_incomplete` is only used with updates and cannot be passed when creating a Subscription.

        Subscriptions with `collection_method=send_invoice` are automatically activated regardless of the first Invoice status.
            payment_settings: Payment settings to pass to invoices created by the subscription.
            pending_invoice_item_interval: Specifies an interval for how often to bill for any pending invoice items. It is analogous to calling [Create an invoice](https://stripe.com/docs/api#create_invoice) for the given subscription at the specified interval.
            proration_behavior: Determines how to handle [prorations](https://stripe.com/docs/billing/subscriptions/prorations) resulting from the `billing_cycle_anchor`. If no value is passed, the default is `create_prorations`.
            transfer_data: If specified, the funds from the subscription's invoices will be transferred to the destination and the ID of the resulting transfers will be found on the resulting charges.
            trial_end: Unix timestamp representing the end of the trial period the customer will get before being charged for the first time. If set, trial_end will override the default trial period of the plan the customer is being subscribed to. The special value `now` can be provided to end the customer's trial immediately. Can be at most two years from `billing_cycle_anchor`. See [Using trial periods on subscriptions](https://stripe.com/docs/billing/subscriptions/trials) to learn more.
            trial_from_plan: Indicates if a plan's `trial_period_days` should be applied to the subscription. Setting `trial_end` per subscription is preferred, and this defaults to `false`. Setting this flag to `true` together with `trial_end` is not allowed. See [Using trial periods on subscriptions](https://stripe.com/docs/billing/subscriptions/trials) to learn more.
            trial_period_days: Integer representing the number of trial period days before the customer is charged for the first time. This will always overwrite any trials that might apply via a subscribed plan. See [Using trial periods on subscriptions](https://stripe.com/docs/billing/subscriptions/trials) to learn more.
            trial_settings: Settings related to subscription trials.
            customer: The identifier of the customer to subscribe.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.subscription.create(customer="string")
        ```
        """
        models.Subscription.model_rebuild(_types_namespace=models._types_namespace)
        _data = to_form_urlencoded(
            item={
                "add_invoice_items": add_invoice_items,
                "application_fee_percent": application_fee_percent,
                "automatic_tax": automatic_tax,
                "backdate_start_date": backdate_start_date,
                "billing_cycle_anchor": billing_cycle_anchor,
                "billing_cycle_anchor_config": billing_cycle_anchor_config,
                "cancel_at": cancel_at,
                "cancel_at_period_end": cancel_at_period_end,
                "collection_method": collection_method,
                "currency": currency,
                "days_until_due": days_until_due,
                "default_payment_method": default_payment_method,
                "default_source": default_source,
                "default_tax_rates": default_tax_rates,
                "description": description,
                "discounts": discounts,
                "expand": expand,
                "invoice_settings": invoice_settings,
                "items": items,
                "metadata": metadata,
                "off_session": off_session,
                "on_behalf_of": on_behalf_of,
                "payment_behavior": payment_behavior,
                "payment_settings": payment_settings,
                "pending_invoice_item_interval": pending_invoice_item_interval,
                "proration_behavior": proration_behavior,
                "transfer_data": transfer_data,
                "trial_end": trial_end,
                "trial_from_plan": trial_from_plan,
                "trial_period_days": trial_period_days,
                "trial_settings": trial_settings,
                "customer": customer,
            },
            dump_with=params._SerializerSubscriptionCreateBody,
            style={
                "add_invoice_items": "deepObject",
                "application_fee_percent": "deepObject",
                "automatic_tax": "deepObject",
                "backdate_start_date": "form",
                "billing_cycle_anchor": "form",
                "billing_cycle_anchor_config": "deepObject",
                "cancel_at": "form",
                "cancel_at_period_end": "form",
                "collection_method": "form",
                "currency": "form",
                "customer": "form",
                "days_until_due": "form",
                "default_payment_method": "form",
                "default_source": "form",
                "default_tax_rates": "deepObject",
                "description": "form",
                "discounts": "deepObject",
                "expand": "deepObject",
                "invoice_settings": "deepObject",
                "items": "deepObject",
                "metadata": "deepObject",
                "off_session": "form",
                "on_behalf_of": "deepObject",
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
                "billing_cycle_anchor_config": True,
                "cancel_at": True,
                "cancel_at_period_end": True,
                "collection_method": True,
                "currency": True,
                "customer": True,
                "days_until_due": True,
                "default_payment_method": True,
                "default_source": True,
                "default_tax_rates": True,
                "description": True,
                "discounts": True,
                "expand": True,
                "invoice_settings": True,
                "items": True,
                "metadata": True,
                "off_session": True,
                "on_behalf_of": True,
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
        return self._base_client.request(
            method="POST",
            path="/v1/subscriptions",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.Subscription,
            request_options=request_options or default_request_options(),
        )

    def update(
        self,
        *,
        subscription_exposed_id: str,
        data: typing.Union[
            typing.Optional[params.SubscriptionUpdateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Subscription:
        """
        Update a subscription

        <p>Updates an existing subscription to match the specified parameters.
        When changing prices or quantities, we optionally prorate the price we charge next month to make up for any price changes.
        To preview how the proration is calculated, use the <a href="/docs/api/invoices/create_preview">create preview</a> endpoint.</p>

        <p>By default, we prorate subscription changes. For example, if a customer signs up on May 1 for a <currency>100</currency> price, they’ll be billed <currency>100</currency> immediately. If on May 15 they switch to a <currency>200</currency> price, then on June 1 they’ll be billed <currency>250</currency> (<currency>200</currency> for a renewal of her subscription, plus a <currency>50</currency> prorating adjustment for half of the previous month’s <currency>100</currency> difference). Similarly, a downgrade generates a credit that is applied to the next invoice. We also prorate when you make quantity changes.</p>

        <p>Switching prices does not normally change the billing date or generate an immediate charge unless:</p>

        <ul>
        <li>The billing interval is changed (for example, from monthly to yearly).</li>
        <li>The subscription moves from free to paid.</li>
        <li>A trial starts or ends.</li>
        </ul>

        <p>In these cases, we apply a credit for the unused time on the previous price, immediately charge the customer using the new price, and reset the billing date. Learn about how <a href="/docs/billing/subscriptions/upgrade-downgrade#immediate-payment">Stripe immediately attempts payment for subscription changes</a>.</p>

        <p>If you want to charge for an upgrade immediately, pass <code>proration_behavior</code> as <code>always_invoice</code> to create prorations, automatically invoice the customer for those proration adjustments, and attempt to collect payment. If you pass <code>create_prorations</code>, the prorations are created but not automatically invoiced. If you want to bill the customer for the prorations before the subscription’s renewal date, you need to manually <a href="/docs/api/invoices/create">invoice the customer</a>.</p>

        <p>If you don’t want to prorate, set the <code>proration_behavior</code> option to <code>none</code>. With this option, the customer is billed <currency>100</currency> on May 1 and <currency>200</currency> on June 1. Similarly, if you set <code>proration_behavior</code> to <code>none</code> when switching between different billing intervals (for example, from monthly to yearly), we don’t generate any credits for the old subscription’s unused time. We still reset the billing date and bill immediately for the new subscription.</p>

        <p>Updating the quantity on a subscription many times in an hour may result in <a href="/docs/rate-limits">rate limiting</a>. If you need to bill for a frequently changing quantity, consider integrating <a href="/docs/billing/subscriptions/usage-based">usage-based billing</a> instead.</p>

        POST /v1/subscriptions/{subscription_exposed_id}

        Args:
            data: SubscriptionUpdateBody
            subscription_exposed_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.subscription.update(subscription_exposed_id="string")
        ```
        """
        models.Subscription.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerSubscriptionUpdateBody,
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
                    "description": "deepObject",
                    "discounts": "deepObject",
                    "expand": "deepObject",
                    "invoice_settings": "deepObject",
                    "items": "deepObject",
                    "metadata": "deepObject",
                    "off_session": "form",
                    "on_behalf_of": "deepObject",
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
                    "description": True,
                    "discounts": True,
                    "expand": True,
                    "invoice_settings": True,
                    "items": True,
                    "metadata": True,
                    "off_session": True,
                    "on_behalf_of": True,
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
            path=f"/v1/subscriptions/{subscription_exposed_id}",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.Subscription,
            request_options=request_options or default_request_options(),
        )

    def resume(
        self,
        *,
        subscription: str,
        data: typing.Union[
            typing.Optional[params.SubscriptionResumeBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Subscription:
        """
        Resume a subscription

        <p>Initiates resumption of a paused subscription, optionally resetting the billing cycle anchor and creating prorations. If a resumption invoice is generated, it must be paid or marked uncollectible before the subscription will be unpaused. If payment succeeds the subscription will become <code>active</code>, and if payment fails the subscription will be <code>past_due</code>. The resumption invoice will void automatically if not paid by the expiration date.</p>

        POST /v1/subscriptions/{subscription}/resume

        Args:
            data: SubscriptionResumeBody
            subscription: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.subscription.resume(subscription="string")
        ```
        """
        models.Subscription.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerSubscriptionResumeBody,
                style={
                    "billing_cycle_anchor": "form",
                    "expand": "deepObject",
                    "proration_behavior": "form",
                    "proration_date": "form",
                },
                explode={
                    "billing_cycle_anchor": True,
                    "expand": True,
                    "proration_behavior": True,
                    "proration_date": True,
                },
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/subscriptions/{subscription}/resume",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.Subscription,
            request_options=request_options or default_request_options(),
        )


class AsyncSubscriptionClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def delete(
        self,
        *,
        subscription_exposed_id: str,
        data: typing.Union[
            typing.Optional[params.SubscriptionDeleteBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Subscription:
        """
        Cancel a subscription

        <p>Cancels a customer’s subscription immediately. The customer won’t be charged again for the subscription. After it’s canceled, you can no longer update the subscription or its <a href="/metadata">metadata</a>.</p>

        <p>Any pending invoice items that you’ve created are still charged at the end of the period, unless manually <a href="#delete_invoiceitem">deleted</a>. If you’ve set the subscription to cancel at the end of the period, any pending prorations are also left in place and collected at the end of the period. But if the subscription is set to cancel immediately, pending prorations are removed.</p>

        <p>By default, upon subscription cancellation, Stripe stops automatic collection of all finalized invoices for the customer. This is intended to prevent unexpected payment attempts after the customer has canceled a subscription. However, you can resume automatic collection of the invoices manually after subscription cancellation to have us proceed. Or, you could check for unpaid invoices before allowing the customer to cancel the subscription at all.</p>

        DELETE /v1/subscriptions/{subscription_exposed_id}

        Args:
            data: SubscriptionDeleteBody
            subscription_exposed_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.subscription.delete(subscription_exposed_id="string")
        ```
        """
        models.Subscription.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerSubscriptionDeleteBody,
                style={
                    "cancellation_details": "deepObject",
                    "expand": "deepObject",
                    "invoice_now": "form",
                    "prorate": "form",
                },
                explode={
                    "cancellation_details": True,
                    "expand": True,
                    "invoice_now": True,
                    "prorate": True,
                },
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="DELETE",
            path=f"/v1/subscriptions/{subscription_exposed_id}",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.Subscription,
            request_options=request_options or default_request_options(),
        )

    async def list(
        self,
        *,
        automatic_tax: typing.Union[
            typing.Optional[params.SubscriptionListAutomaticTax], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        collection_method: typing.Union[
            typing.Optional[
                typing_extensions.Literal["charge_automatically", "send_invoice"]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        created: typing.Union[
            typing.Optional[typing.Union[params.SubscriptionListCreatedObj0, int]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        current_period_end: typing.Union[
            typing.Optional[
                typing.Union[params.SubscriptionListCurrentPeriodEndObj0, int]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        current_period_start: typing.Union[
            typing.Optional[
                typing.Union[params.SubscriptionListCurrentPeriodStartObj0, int]
            ],
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
        price: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        starting_after: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        status: typing.Union[
            typing.Optional[
                typing_extensions.Literal[
                    "active",
                    "all",
                    "canceled",
                    "ended",
                    "incomplete",
                    "incomplete_expired",
                    "past_due",
                    "paused",
                    "trialing",
                    "unpaid",
                ]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        test_clock: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.SubscriptionListResponse:
        """
        List subscriptions

        <p>By default, returns a list of subscriptions that have not been canceled. In order to list canceled subscriptions, specify <code>status=canceled</code>.</p>

        GET /v1/subscriptions

        Args:
            automatic_tax: Filter subscriptions by their automatic tax settings.
            collection_method: The collection method of the subscriptions to retrieve. Either `charge_automatically` or `send_invoice`.
            created: Only return subscriptions that were created during the given date interval.
            current_period_end: Only return subscriptions whose current_period_end falls within the given date interval.
            current_period_start: Only return subscriptions whose current_period_start falls within the given date interval.
            customer: The ID of the customer whose subscriptions will be retrieved.
            ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            expand: Specifies which fields in the response should be expanded.
            limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            price: Filter for subscriptions that contain this recurring price ID.
            starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
            status: The status of the subscriptions to retrieve. Passing in a value of `canceled` will return all canceled subscriptions, including those belonging to deleted customers. Pass `ended` to find subscriptions that are canceled and subscriptions that are expired due to [incomplete payment](https://stripe.com/docs/billing/subscriptions/overview#subscription-statuses). Passing in a value of `all` will return subscriptions of all statuses. If no value is supplied, all subscriptions that have not been canceled are returned.
            test_clock: Filter for subscriptions that are associated with the specified test clock. The response will not include subscriptions with test clocks if this and the customer parameter is not set.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.subscription.list()
        ```
        """
        models.SubscriptionListResponse.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _query: QueryParams = {}
        if not isinstance(automatic_tax, type_utils.NotGiven):
            encode_query_param(
                _query,
                "automatic_tax",
                to_encodable(
                    item=automatic_tax,
                    dump_with=params._SerializerSubscriptionListAutomaticTax,
                ),
                style="deepObject",
                explode=True,
            )
        if not isinstance(collection_method, type_utils.NotGiven):
            encode_query_param(
                _query,
                "collection_method",
                to_encodable(
                    item=collection_method,
                    dump_with=typing_extensions.Literal[
                        "charge_automatically", "send_invoice"
                    ],
                ),
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
                        params._SerializerSubscriptionListCreatedObj0, int
                    ],
                ),
                style="deepObject",
                explode=True,
            )
        if not isinstance(current_period_end, type_utils.NotGiven):
            encode_query_param(
                _query,
                "current_period_end",
                to_encodable(
                    item=current_period_end,
                    dump_with=typing.Union[
                        params._SerializerSubscriptionListCurrentPeriodEndObj0, int
                    ],
                ),
                style="deepObject",
                explode=True,
            )
        if not isinstance(current_period_start, type_utils.NotGiven):
            encode_query_param(
                _query,
                "current_period_start",
                to_encodable(
                    item=current_period_start,
                    dump_with=typing.Union[
                        params._SerializerSubscriptionListCurrentPeriodStartObj0, int
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
        if not isinstance(price, type_utils.NotGiven):
            encode_query_param(
                _query,
                "price",
                to_encodable(item=price, dump_with=str),
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
                        "active",
                        "all",
                        "canceled",
                        "ended",
                        "incomplete",
                        "incomplete_expired",
                        "past_due",
                        "paused",
                        "trialing",
                        "unpaid",
                    ],
                ),
                style="form",
                explode=True,
            )
        if not isinstance(test_clock, type_utils.NotGiven):
            encode_query_param(
                _query,
                "test_clock",
                to_encodable(item=test_clock, dump_with=str),
                style="form",
                explode=True,
            )
        return await self._base_client.request(
            method="GET",
            path="/v1/subscriptions",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.SubscriptionListResponse,
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
    ) -> models.SubscriptionSearchResponse:
        """
        Search subscriptions

        <p>Search for subscriptions you’ve previously created using Stripe’s <a href="/docs/search#search-query-language">Search Query Language</a>.
        Don’t use search in read-after-write flows where strict consistency is necessary. Under normal operating
        conditions, data is searchable in less than a minute. Occasionally, propagation of new or updated data can be up
        to an hour behind during outages. Search functionality is not available to merchants in India.</p>

        GET /v1/subscriptions/search

        Args:
            expand: Specifies which fields in the response should be expanded.
            limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            page: A cursor for pagination across multiple pages of results. Don't include this parameter on the first call. Use the next_page value returned in a previous response to request subsequent results.
            query: The search query string. See [search query language](https://stripe.com/docs/search#search-query-language) and the list of supported [query fields for subscriptions](https://stripe.com/docs/search#query-fields-for-subscriptions).
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.subscription.search(query="string")
        ```
        """
        models.SubscriptionSearchResponse.model_rebuild(
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
            path="/v1/subscriptions/search",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.SubscriptionSearchResponse,
            request_options=request_options or default_request_options(),
        )

    async def get(
        self,
        *,
        subscription_exposed_id: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Subscription:
        """
        Retrieve a subscription

        <p>Retrieves the subscription with the given ID.</p>

        GET /v1/subscriptions/{subscription_exposed_id}

        Args:
            expand: Specifies which fields in the response should be expanded.
            subscription_exposed_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.subscription.get(subscription_exposed_id="string")
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
            path=f"/v1/subscriptions/{subscription_exposed_id}",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.Subscription,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        customer: str,
        add_invoice_items: typing.Union[
            typing.Optional[
                typing.List[params.SubscriptionCreateBodyAddInvoiceItemsItem]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        application_fee_percent: typing.Union[
            typing.Optional[typing.Union[float, str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        automatic_tax: typing.Union[
            typing.Optional[params.SubscriptionCreateBodyAutomaticTax],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        backdate_start_date: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        billing_cycle_anchor: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        billing_cycle_anchor_config: typing.Union[
            typing.Optional[params.SubscriptionCreateBodyBillingCycleAnchorConfig],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        cancel_at: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        cancel_at_period_end: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        collection_method: typing.Union[
            typing.Optional[
                typing_extensions.Literal["charge_automatically", "send_invoice"]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        currency: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        days_until_due: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        default_payment_method: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        default_source: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        default_tax_rates: typing.Union[
            typing.Optional[typing.Union[typing.List[str], str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        description: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        discounts: typing.Union[
            typing.Optional[
                typing.Union[
                    typing.List[params.SubscriptionCreateBodyDiscountsArr0Item], str
                ]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        invoice_settings: typing.Union[
            typing.Optional[params.SubscriptionCreateBodyInvoiceSettings],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        items: typing.Union[
            typing.Optional[typing.List[params.SubscriptionCreateBodyItemsItem]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        metadata: typing.Union[
            typing.Optional[
                typing.Union[params.SubscriptionCreateBodyMetadataObj0, str]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        off_session: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        on_behalf_of: typing.Union[
            typing.Optional[typing.Union[str, str]], type_utils.NotGiven
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
        payment_settings: typing.Union[
            typing.Optional[params.SubscriptionCreateBodyPaymentSettings],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        pending_invoice_item_interval: typing.Union[
            typing.Optional[
                typing.Union[
                    params.SubscriptionCreateBodyPendingInvoiceItemIntervalObj0, str
                ]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        proration_behavior: typing.Union[
            typing.Optional[
                typing_extensions.Literal["always_invoice", "create_prorations", "none"]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        transfer_data: typing.Union[
            typing.Optional[params.SubscriptionCreateBodyTransferData],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        trial_end: typing.Union[
            typing.Optional[typing.Union[typing_extensions.Literal["now"], int]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        trial_from_plan: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        trial_period_days: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        trial_settings: typing.Union[
            typing.Optional[params.SubscriptionCreateBodyTrialSettings],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Subscription:
        """
        Create a subscription

        <p>Creates a new subscription on an existing customer. Each customer can have up to 500 active or scheduled subscriptions.</p>

        <p>When you create a subscription with <code>collection_method=charge_automatically</code>, the first invoice is finalized as part of the request.
        The <code>payment_behavior</code> parameter determines the exact behavior of the initial payment.</p>

        <p>To start subscriptions where the first invoice always begins in a <code>draft</code> status, use <a href="/docs/billing/subscriptions/subscription-schedules#managing">subscription schedules</a> instead.
        Schedules provide the flexibility to model more complex billing configurations that change over time.</p>

        POST /v1/subscriptions

        Args:
            add_invoice_items: A list of prices and quantities that will generate invoice items appended to the next invoice for this subscription. You may pass up to 20 items.
            application_fee_percent: A non-negative decimal between 0 and 100, with at most two decimal places. This represents the percentage of the subscription invoice total that will be transferred to the application owner's Stripe account. The request must be made by a platform account on a connected account in order to set an application fee percentage. For more information, see the application fees [documentation](https://stripe.com/docs/connect/subscriptions#collecting-fees-on-subscriptions).
            automatic_tax: Automatic tax settings for this subscription. We recommend you only include this parameter when the existing value is being changed.
            backdate_start_date: For new subscriptions, a past timestamp to backdate the subscription's start date to. If set, the first invoice will contain a proration for the timespan between the start date and the current time. Can be combined with trials and the billing cycle anchor.
            billing_cycle_anchor: A future timestamp in UTC format to anchor the subscription's [billing cycle](https://stripe.com/docs/subscriptions/billing-cycle). The anchor is the reference point that aligns future billing cycle dates. It sets the day of week for `week` intervals, the day of month for `month` and `year` intervals, and the month of year for `year` intervals.
            billing_cycle_anchor_config: Mutually exclusive with billing_cycle_anchor and only valid with monthly and yearly price intervals. When provided, the billing_cycle_anchor is set to the next occurence of the day_of_month at the hour, minute, and second UTC.
            cancel_at: A timestamp at which the subscription should cancel. If set to a date before the current period ends, this will cause a proration if prorations have been enabled using `proration_behavior`. If set during a future period, this will always cause a proration for that period.
            cancel_at_period_end: Indicate whether this subscription should cancel at the end of the current period (`current_period_end`). Defaults to `false`.
            collection_method: Either `charge_automatically`, or `send_invoice`. When charging automatically, Stripe will attempt to pay this subscription at the end of the cycle using the default source attached to the customer. When sending an invoice, Stripe will email your customer an invoice with payment instructions and mark the subscription as `active`. Defaults to `charge_automatically`.
            currency: Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
            days_until_due: Number of days a customer has to pay invoices generated by this subscription. Valid only for subscriptions where `collection_method` is set to `send_invoice`.
            default_payment_method: ID of the default payment method for the subscription. It must belong to the customer associated with the subscription. This takes precedence over `default_source`. If neither are set, invoices will use the customer's [invoice_settings.default_payment_method](https://stripe.com/docs/api/customers/object#customer_object-invoice_settings-default_payment_method) or [default_source](https://stripe.com/docs/api/customers/object#customer_object-default_source).
            default_source: ID of the default payment source for the subscription. It must belong to the customer associated with the subscription and be in a chargeable state. If `default_payment_method` is also set, `default_payment_method` will take precedence. If neither are set, invoices will use the customer's [invoice_settings.default_payment_method](https://stripe.com/docs/api/customers/object#customer_object-invoice_settings-default_payment_method) or [default_source](https://stripe.com/docs/api/customers/object#customer_object-default_source).
            default_tax_rates: The tax rates that will apply to any subscription item that does not have `tax_rates` set. Invoices created will have their `default_tax_rates` populated from the subscription.
            description: The subscription's description, meant to be displayable to the customer. Use this field to optionally store an explanation of the subscription for rendering in Stripe surfaces and certain local payment methods UIs.
            discounts: The coupons to redeem into discounts for the subscription. If not specified or empty, inherits the discount from the subscription's customer.
            expand: Specifies which fields in the response should be expanded.
            invoice_settings: All invoices will be billed using the specified settings.
            items: A list of up to 20 subscription items, each with an attached price.
            metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
            off_session: Indicates if a customer is on or off-session while an invoice payment is attempted. Defaults to `false` (on-session).
            on_behalf_of: The account on behalf of which to charge, for each of the subscription's invoices.
            payment_behavior: Only applies to subscriptions with `collection_method=charge_automatically`.

        Use `allow_incomplete` to create Subscriptions with `status=incomplete` if the first invoice can't be paid. Creating Subscriptions with this status allows you to manage scenarios where additional customer actions are needed to pay a subscription's invoice. For example, SCA regulation may require 3DS authentication to complete payment. See the [SCA Migration Guide](https://stripe.com/docs/billing/migration/strong-customer-authentication) for Billing to learn more. This is the default behavior.

        Use `default_incomplete` to create Subscriptions with `status=incomplete` when the first invoice requires payment, otherwise start as active. Subscriptions transition to `status=active` when successfully confirming the PaymentIntent on the first invoice. This allows simpler management of scenarios where additional customer actions are needed to pay a subscription’s invoice, such as failed payments, [SCA regulation](https://stripe.com/docs/billing/migration/strong-customer-authentication), or collecting a mandate for a bank debit payment method. If the PaymentIntent is not confirmed within 23 hours Subscriptions transition to `status=incomplete_expired`, which is a terminal state.

        Use `error_if_incomplete` if you want Stripe to return an HTTP 402 status code if a subscription's first invoice can't be paid. For example, if a payment method requires 3DS authentication due to SCA regulation and further customer action is needed, this parameter doesn't create a Subscription and returns an error instead. This was the default behavior for API versions prior to 2019-03-14. See the [changelog](https://stripe.com/docs/upgrades#2019-03-14) to learn more.

        `pending_if_incomplete` is only used with updates and cannot be passed when creating a Subscription.

        Subscriptions with `collection_method=send_invoice` are automatically activated regardless of the first Invoice status.
            payment_settings: Payment settings to pass to invoices created by the subscription.
            pending_invoice_item_interval: Specifies an interval for how often to bill for any pending invoice items. It is analogous to calling [Create an invoice](https://stripe.com/docs/api#create_invoice) for the given subscription at the specified interval.
            proration_behavior: Determines how to handle [prorations](https://stripe.com/docs/billing/subscriptions/prorations) resulting from the `billing_cycle_anchor`. If no value is passed, the default is `create_prorations`.
            transfer_data: If specified, the funds from the subscription's invoices will be transferred to the destination and the ID of the resulting transfers will be found on the resulting charges.
            trial_end: Unix timestamp representing the end of the trial period the customer will get before being charged for the first time. If set, trial_end will override the default trial period of the plan the customer is being subscribed to. The special value `now` can be provided to end the customer's trial immediately. Can be at most two years from `billing_cycle_anchor`. See [Using trial periods on subscriptions](https://stripe.com/docs/billing/subscriptions/trials) to learn more.
            trial_from_plan: Indicates if a plan's `trial_period_days` should be applied to the subscription. Setting `trial_end` per subscription is preferred, and this defaults to `false`. Setting this flag to `true` together with `trial_end` is not allowed. See [Using trial periods on subscriptions](https://stripe.com/docs/billing/subscriptions/trials) to learn more.
            trial_period_days: Integer representing the number of trial period days before the customer is charged for the first time. This will always overwrite any trials that might apply via a subscribed plan. See [Using trial periods on subscriptions](https://stripe.com/docs/billing/subscriptions/trials) to learn more.
            trial_settings: Settings related to subscription trials.
            customer: The identifier of the customer to subscribe.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.subscription.create(customer="string")
        ```
        """
        models.Subscription.model_rebuild(_types_namespace=models._types_namespace)
        _data = to_form_urlencoded(
            item={
                "add_invoice_items": add_invoice_items,
                "application_fee_percent": application_fee_percent,
                "automatic_tax": automatic_tax,
                "backdate_start_date": backdate_start_date,
                "billing_cycle_anchor": billing_cycle_anchor,
                "billing_cycle_anchor_config": billing_cycle_anchor_config,
                "cancel_at": cancel_at,
                "cancel_at_period_end": cancel_at_period_end,
                "collection_method": collection_method,
                "currency": currency,
                "days_until_due": days_until_due,
                "default_payment_method": default_payment_method,
                "default_source": default_source,
                "default_tax_rates": default_tax_rates,
                "description": description,
                "discounts": discounts,
                "expand": expand,
                "invoice_settings": invoice_settings,
                "items": items,
                "metadata": metadata,
                "off_session": off_session,
                "on_behalf_of": on_behalf_of,
                "payment_behavior": payment_behavior,
                "payment_settings": payment_settings,
                "pending_invoice_item_interval": pending_invoice_item_interval,
                "proration_behavior": proration_behavior,
                "transfer_data": transfer_data,
                "trial_end": trial_end,
                "trial_from_plan": trial_from_plan,
                "trial_period_days": trial_period_days,
                "trial_settings": trial_settings,
                "customer": customer,
            },
            dump_with=params._SerializerSubscriptionCreateBody,
            style={
                "add_invoice_items": "deepObject",
                "application_fee_percent": "deepObject",
                "automatic_tax": "deepObject",
                "backdate_start_date": "form",
                "billing_cycle_anchor": "form",
                "billing_cycle_anchor_config": "deepObject",
                "cancel_at": "form",
                "cancel_at_period_end": "form",
                "collection_method": "form",
                "currency": "form",
                "customer": "form",
                "days_until_due": "form",
                "default_payment_method": "form",
                "default_source": "form",
                "default_tax_rates": "deepObject",
                "description": "form",
                "discounts": "deepObject",
                "expand": "deepObject",
                "invoice_settings": "deepObject",
                "items": "deepObject",
                "metadata": "deepObject",
                "off_session": "form",
                "on_behalf_of": "deepObject",
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
                "billing_cycle_anchor_config": True,
                "cancel_at": True,
                "cancel_at_period_end": True,
                "collection_method": True,
                "currency": True,
                "customer": True,
                "days_until_due": True,
                "default_payment_method": True,
                "default_source": True,
                "default_tax_rates": True,
                "description": True,
                "discounts": True,
                "expand": True,
                "invoice_settings": True,
                "items": True,
                "metadata": True,
                "off_session": True,
                "on_behalf_of": True,
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
        return await self._base_client.request(
            method="POST",
            path="/v1/subscriptions",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.Subscription,
            request_options=request_options or default_request_options(),
        )

    async def update(
        self,
        *,
        subscription_exposed_id: str,
        data: typing.Union[
            typing.Optional[params.SubscriptionUpdateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Subscription:
        """
        Update a subscription

        <p>Updates an existing subscription to match the specified parameters.
        When changing prices or quantities, we optionally prorate the price we charge next month to make up for any price changes.
        To preview how the proration is calculated, use the <a href="/docs/api/invoices/create_preview">create preview</a> endpoint.</p>

        <p>By default, we prorate subscription changes. For example, if a customer signs up on May 1 for a <currency>100</currency> price, they’ll be billed <currency>100</currency> immediately. If on May 15 they switch to a <currency>200</currency> price, then on June 1 they’ll be billed <currency>250</currency> (<currency>200</currency> for a renewal of her subscription, plus a <currency>50</currency> prorating adjustment for half of the previous month’s <currency>100</currency> difference). Similarly, a downgrade generates a credit that is applied to the next invoice. We also prorate when you make quantity changes.</p>

        <p>Switching prices does not normally change the billing date or generate an immediate charge unless:</p>

        <ul>
        <li>The billing interval is changed (for example, from monthly to yearly).</li>
        <li>The subscription moves from free to paid.</li>
        <li>A trial starts or ends.</li>
        </ul>

        <p>In these cases, we apply a credit for the unused time on the previous price, immediately charge the customer using the new price, and reset the billing date. Learn about how <a href="/docs/billing/subscriptions/upgrade-downgrade#immediate-payment">Stripe immediately attempts payment for subscription changes</a>.</p>

        <p>If you want to charge for an upgrade immediately, pass <code>proration_behavior</code> as <code>always_invoice</code> to create prorations, automatically invoice the customer for those proration adjustments, and attempt to collect payment. If you pass <code>create_prorations</code>, the prorations are created but not automatically invoiced. If you want to bill the customer for the prorations before the subscription’s renewal date, you need to manually <a href="/docs/api/invoices/create">invoice the customer</a>.</p>

        <p>If you don’t want to prorate, set the <code>proration_behavior</code> option to <code>none</code>. With this option, the customer is billed <currency>100</currency> on May 1 and <currency>200</currency> on June 1. Similarly, if you set <code>proration_behavior</code> to <code>none</code> when switching between different billing intervals (for example, from monthly to yearly), we don’t generate any credits for the old subscription’s unused time. We still reset the billing date and bill immediately for the new subscription.</p>

        <p>Updating the quantity on a subscription many times in an hour may result in <a href="/docs/rate-limits">rate limiting</a>. If you need to bill for a frequently changing quantity, consider integrating <a href="/docs/billing/subscriptions/usage-based">usage-based billing</a> instead.</p>

        POST /v1/subscriptions/{subscription_exposed_id}

        Args:
            data: SubscriptionUpdateBody
            subscription_exposed_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.subscription.update(subscription_exposed_id="string")
        ```
        """
        models.Subscription.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerSubscriptionUpdateBody,
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
                    "description": "deepObject",
                    "discounts": "deepObject",
                    "expand": "deepObject",
                    "invoice_settings": "deepObject",
                    "items": "deepObject",
                    "metadata": "deepObject",
                    "off_session": "form",
                    "on_behalf_of": "deepObject",
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
                    "description": True,
                    "discounts": True,
                    "expand": True,
                    "invoice_settings": True,
                    "items": True,
                    "metadata": True,
                    "off_session": True,
                    "on_behalf_of": True,
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
            path=f"/v1/subscriptions/{subscription_exposed_id}",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.Subscription,
            request_options=request_options or default_request_options(),
        )

    async def resume(
        self,
        *,
        subscription: str,
        data: typing.Union[
            typing.Optional[params.SubscriptionResumeBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Subscription:
        """
        Resume a subscription

        <p>Initiates resumption of a paused subscription, optionally resetting the billing cycle anchor and creating prorations. If a resumption invoice is generated, it must be paid or marked uncollectible before the subscription will be unpaused. If payment succeeds the subscription will become <code>active</code>, and if payment fails the subscription will be <code>past_due</code>. The resumption invoice will void automatically if not paid by the expiration date.</p>

        POST /v1/subscriptions/{subscription}/resume

        Args:
            data: SubscriptionResumeBody
            subscription: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.subscription.resume(subscription="string")
        ```
        """
        models.Subscription.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerSubscriptionResumeBody,
                style={
                    "billing_cycle_anchor": "form",
                    "expand": "deepObject",
                    "proration_behavior": "form",
                    "proration_date": "form",
                },
                explode={
                    "billing_cycle_anchor": True,
                    "expand": True,
                    "proration_behavior": True,
                    "proration_date": True,
                },
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/subscriptions/{subscription}/resume",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.Subscription,
            request_options=request_options or default_request_options(),
        )
