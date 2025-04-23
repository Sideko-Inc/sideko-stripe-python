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


class PaymentIntentClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def list(
        self,
        *,
        created: typing.Union[
            typing.Optional[typing.Union[params.PaymentIntentListCreatedObj0, int]],
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
        starting_after: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PaymentIntentListResponse:
        """
        List all PaymentIntents

        <p>Returns a list of PaymentIntents.</p>

        GET /v1/payment_intents

        Args:
            created: A filter on the list, based on the object `created` field. The value can be a string with an integer Unix timestamp or a dictionary with a number of different query options.
            customer: Only return PaymentIntents for the customer that this customer ID specifies.
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
        client.payment_intent.list()
        ```
        """
        models.PaymentIntentListResponse.model_rebuild(
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
                        params._SerializerPaymentIntentListCreatedObj0, int
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
            path="/v1/payment_intents",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.PaymentIntentListResponse,
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
    ) -> models.PaymentIntentSearchResponse:
        """
        Search PaymentIntents

        <p>Search for PaymentIntents you’ve previously created using Stripe’s <a href="/docs/search#search-query-language">Search Query Language</a>.
        Don’t use search in read-after-write flows where strict consistency is necessary. Under normal operating
        conditions, data is searchable in less than a minute. Occasionally, propagation of new or updated data can be up
        to an hour behind during outages. Search functionality is not available to merchants in India.</p>

        GET /v1/payment_intents/search

        Args:
            expand: Specifies which fields in the response should be expanded.
            limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            page: A cursor for pagination across multiple pages of results. Don't include this parameter on the first call. Use the next_page value returned in a previous response to request subsequent results.
            query: The search query string. See [search query language](https://stripe.com/docs/search#search-query-language) and the list of supported [query fields for payment intents](https://stripe.com/docs/search#query-fields-for-payment-intents).
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.payment_intent.search(query="string")
        ```
        """
        models.PaymentIntentSearchResponse.model_rebuild(
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
            path="/v1/payment_intents/search",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.PaymentIntentSearchResponse,
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
    ) -> models.PaymentIntent:
        """
        Retrieve a PaymentIntent

        <p>Retrieves the details of a PaymentIntent that has previously been created. </p>

        <p>You can retrieve a PaymentIntent client-side using a publishable key when the <code>client_secret</code> is in the query string. </p>

        <p>If you retrieve a PaymentIntent with a publishable key, it only returns a subset of properties. Refer to the <a href="#payment_intent_object">payment intent</a> object reference for more details.</p>

        GET /v1/payment_intents/{intent}

        Args:
            client_secret: The client secret of the PaymentIntent. We require it if you use a publishable key to retrieve the source.
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
        client.payment_intent.get(intent="string")
        ```
        """
        models.PaymentIntent.model_rebuild(_types_namespace=models._types_namespace)
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
            path=f"/v1/payment_intents/{intent}",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.PaymentIntent,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        amount: int,
        currency: str,
        application_fee_amount: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        automatic_payment_methods: typing.Union[
            typing.Optional[params.PaymentIntentCreateBodyAutomaticPaymentMethods],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        capture_method: typing.Union[
            typing.Optional[
                typing_extensions.Literal["automatic", "automatic_async", "manual"]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        confirm: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        confirmation_method: typing.Union[
            typing.Optional[typing_extensions.Literal["automatic", "manual"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        confirmation_token: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        customer: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        description: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        error_on_requires_action: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        mandate: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        mandate_data: typing.Union[
            typing.Optional[
                typing.Union[params.PaymentIntentCreateBodyMandateDataObj0, str]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        metadata: typing.Union[
            typing.Optional[params.PaymentIntentCreateBodyMetadata], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        off_session: typing.Union[
            typing.Optional[
                typing.Union[bool, typing_extensions.Literal["one_off", "recurring"]]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        on_behalf_of: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        payment_method: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        payment_method_configuration: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        payment_method_data: typing.Union[
            typing.Optional[params.PaymentIntentCreateBodyPaymentMethodData],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        payment_method_options: typing.Union[
            typing.Optional[params.PaymentIntentCreateBodyPaymentMethodOptions],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        payment_method_types: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        radar_options: typing.Union[
            typing.Optional[params.PaymentIntentCreateBodyRadarOptions],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        receipt_email: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        return_url: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        setup_future_usage: typing.Union[
            typing.Optional[typing_extensions.Literal["off_session", "on_session"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        shipping: typing.Union[
            typing.Optional[params.PaymentIntentCreateBodyShipping], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        statement_descriptor: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        statement_descriptor_suffix: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        transfer_data: typing.Union[
            typing.Optional[params.PaymentIntentCreateBodyTransferData],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        transfer_group: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        use_stripe_sdk: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PaymentIntent:
        """
        Create a PaymentIntent

        <p>Creates a PaymentIntent object.</p>

        <p>After the PaymentIntent is created, attach a payment method and <a href="/docs/api/payment_intents/confirm">confirm</a>
        to continue the payment. Learn more about <a href="/docs/payments/payment-intents">the available payment flows
        with the Payment Intents API</a>.</p>

        <p>When you use <code>confirm=true</code> during creation, it’s equivalent to creating
        and confirming the PaymentIntent in the same call. You can use any parameters
        available in the <a href="/docs/api/payment_intents/confirm">confirm API</a> when you supply
        <code>confirm=true</code>.</p>

        POST /v1/payment_intents

        Args:
            application_fee_amount: The amount of the application fee (if any) that will be requested to be applied to the payment and transferred to the application owner's Stripe account. The amount of the application fee collected will be capped at the total amount captured. For more information, see the PaymentIntents [use case for connected accounts](https://stripe.com/docs/payments/connected-accounts).
            automatic_payment_methods: When you enable this parameter, this PaymentIntent accepts payment methods that you enable in the Dashboard and that are compatible with this PaymentIntent's other parameters.
            capture_method: Controls when the funds will be captured from the customer's account.
            confirm: Set to `true` to attempt to [confirm this PaymentIntent](https://stripe.com/docs/api/payment_intents/confirm) immediately. This parameter defaults to `false`. When creating and confirming a PaymentIntent at the same time, you can also provide the parameters available in the [Confirm API](https://stripe.com/docs/api/payment_intents/confirm).
            confirmation_method: Describes whether we can confirm this PaymentIntent automatically, or if it requires customer action to confirm the payment.
            confirmation_token: ID of the ConfirmationToken used to confirm this PaymentIntent.

        If the provided ConfirmationToken contains properties that are also being provided in this request, such as `payment_method`, then the values in this request will take precedence.
            customer: ID of the Customer this PaymentIntent belongs to, if one exists.

        Payment methods attached to other Customers cannot be used with this PaymentIntent.

        If [setup_future_usage](https://stripe.com/docs/api#payment_intent_object-setup_future_usage) is set and this PaymentIntent's payment method is not `card_present`, then the payment method attaches to the Customer after the PaymentIntent has been confirmed and any required actions from the user are complete. If the payment method is `card_present` and isn't a digital wallet, then a [generated_card](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-card_present-generated_card) payment method representing the card is created and attached to the Customer instead.
            description: An arbitrary string attached to the object. Often useful for displaying to users.
            error_on_requires_action: Set to `true` to fail the payment attempt if the PaymentIntent transitions into `requires_action`. Use this parameter for simpler integrations that don't handle customer actions, such as [saving cards without authentication](https://stripe.com/docs/payments/save-card-without-authentication). This parameter can only be used with [`confirm=true`](https://stripe.com/docs/api/payment_intents/create#create_payment_intent-confirm).
            expand: Specifies which fields in the response should be expanded.
            mandate: ID of the mandate that's used for this payment. This parameter can only be used with [`confirm=true`](https://stripe.com/docs/api/payment_intents/create#create_payment_intent-confirm).
            mandate_data: This hash contains details about the Mandate to create. This parameter can only be used with [`confirm=true`](https://stripe.com/docs/api/payment_intents/create#create_payment_intent-confirm).
            metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
            off_session: Set to `true` to indicate that the customer isn't in your checkout flow during this payment attempt and can't authenticate. Use this parameter in scenarios where you collect card details and [charge them later](https://stripe.com/docs/payments/cards/charging-saved-cards). This parameter can only be used with [`confirm=true`](https://stripe.com/docs/api/payment_intents/create#create_payment_intent-confirm).
            on_behalf_of: The Stripe account ID that these funds are intended for. Learn more about the [use case for connected accounts](https://stripe.com/docs/payments/connected-accounts).
            payment_method: ID of the payment method (a PaymentMethod, Card, or [compatible Source](https://stripe.com/docs/payments/payment-methods/transitioning#compatibility) object) to attach to this PaymentIntent.

        If you omit this parameter with `confirm=true`, `customer.default_source` attaches as this PaymentIntent's payment instrument to improve migration for users of the Charges API. We recommend that you explicitly provide the `payment_method` moving forward.
            payment_method_configuration: The ID of the [payment method configuration](https://stripe.com/docs/api/payment_method_configurations) to use with this PaymentIntent.
            payment_method_data: If provided, this hash will be used to create a PaymentMethod. The new PaymentMethod will appear
        in the [payment_method](https://stripe.com/docs/api/payment_intents/object#payment_intent_object-payment_method)
        property on the PaymentIntent.
            payment_method_options: Payment method-specific configuration for this PaymentIntent.
            payment_method_types: The list of payment method types (for example, a card) that this PaymentIntent can use. If you don't provide this, Stripe will dynamically show relevant payment methods from your [payment method settings](https://dashboard.stripe.com/settings/payment_methods).
            radar_options: Options to configure Radar. Learn more about [Radar Sessions](https://stripe.com/docs/radar/radar-session).
            receipt_email: Email address to send the receipt to. If you specify `receipt_email` for a payment in live mode, you send a receipt regardless of your [email settings](https://dashboard.stripe.com/account/emails).
            return_url: The URL to redirect your customer back to after they authenticate or cancel their payment on the payment method's app or site. If you'd prefer to redirect to a mobile application, you can alternatively supply an application URI scheme. This parameter can only be used with [`confirm=true`](https://stripe.com/docs/api/payment_intents/create#create_payment_intent-confirm).
            setup_future_usage: Indicates that you intend to make future payments with this PaymentIntent's payment method.

        If you provide a Customer with the PaymentIntent, you can use this parameter to [attach the payment method](/payments/save-during-payment) to the Customer after the PaymentIntent is confirmed and the customer completes any required actions. If you don't provide a Customer, you can still [attach](/api/payment_methods/attach) the payment method to a Customer after the transaction completes.

        If the payment method is `card_present` and isn't a digital wallet, Stripe creates and attaches a [generated_card](/api/charges/object#charge_object-payment_method_details-card_present-generated_card) payment method representing the card to the Customer instead.

        When processing card payments, Stripe uses `setup_future_usage` to help you comply with regional legislation and network rules, such as [SCA](/strong-customer-authentication).
            shipping: Shipping information for this PaymentIntent.
            statement_descriptor: Text that appears on the customer's statement as the statement descriptor for a non-card charge. This value overrides the account's default statement descriptor. For information about requirements, including the 22-character limit, see [the Statement Descriptor docs](https://docs.stripe.com/get-started/account/statement-descriptors).

        Setting this value for a card charge returns an error. For card charges, set the [statement_descriptor_suffix](https://docs.stripe.com/get-started/account/statement-descriptors#dynamic) instead.
            statement_descriptor_suffix: Provides information about a card charge. Concatenated to the account's [statement descriptor prefix](https://docs.stripe.com/get-started/account/statement-descriptors#static) to form the complete statement descriptor that appears on the customer's statement.
            transfer_data: The parameters that you can use to automatically create a Transfer.
        Learn more about the [use case for connected accounts](https://stripe.com/docs/payments/connected-accounts).
            transfer_group: A string that identifies the resulting payment as part of a group. Learn more about the [use case for connected accounts](https://stripe.com/docs/connect/separate-charges-and-transfers).
            use_stripe_sdk: Set to `true` when confirming server-side and using Stripe.js, iOS, or Android client-side SDKs to handle the next actions.
            amount: Amount intended to be collected by this PaymentIntent. A positive integer representing how much to charge in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal) (e.g., 100 cents to charge $1.00 or 100 to charge ¥100, a zero-decimal currency). The minimum amount is $0.50 US or [equivalent in charge currency](https://stripe.com/docs/currencies#minimum-and-maximum-charge-amounts). The amount value supports up to eight digits (e.g., a value of 99999999 for a USD charge of $999,999.99).
            currency: Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.payment_intent.create(amount=123, currency="string")
        ```
        """
        models.PaymentIntent.model_rebuild(_types_namespace=models._types_namespace)
        _data = to_form_urlencoded(
            item={
                "application_fee_amount": application_fee_amount,
                "automatic_payment_methods": automatic_payment_methods,
                "capture_method": capture_method,
                "confirm": confirm,
                "confirmation_method": confirmation_method,
                "confirmation_token": confirmation_token,
                "customer": customer,
                "description": description,
                "error_on_requires_action": error_on_requires_action,
                "expand": expand,
                "mandate": mandate,
                "mandate_data": mandate_data,
                "metadata": metadata,
                "off_session": off_session,
                "on_behalf_of": on_behalf_of,
                "payment_method": payment_method,
                "payment_method_configuration": payment_method_configuration,
                "payment_method_data": payment_method_data,
                "payment_method_options": payment_method_options,
                "payment_method_types": payment_method_types,
                "radar_options": radar_options,
                "receipt_email": receipt_email,
                "return_url": return_url,
                "setup_future_usage": setup_future_usage,
                "shipping": shipping,
                "statement_descriptor": statement_descriptor,
                "statement_descriptor_suffix": statement_descriptor_suffix,
                "transfer_data": transfer_data,
                "transfer_group": transfer_group,
                "use_stripe_sdk": use_stripe_sdk,
                "amount": amount,
                "currency": currency,
            },
            dump_with=params._SerializerPaymentIntentCreateBody,
            style={
                "amount": "form",
                "application_fee_amount": "form",
                "automatic_payment_methods": "deepObject",
                "capture_method": "form",
                "confirm": "form",
                "confirmation_method": "form",
                "confirmation_token": "form",
                "currency": "form",
                "customer": "form",
                "description": "form",
                "error_on_requires_action": "form",
                "expand": "deepObject",
                "mandate": "form",
                "mandate_data": "deepObject",
                "metadata": "deepObject",
                "off_session": "deepObject",
                "on_behalf_of": "form",
                "payment_method": "form",
                "payment_method_configuration": "form",
                "payment_method_data": "deepObject",
                "payment_method_options": "deepObject",
                "payment_method_types": "deepObject",
                "radar_options": "deepObject",
                "receipt_email": "form",
                "return_url": "form",
                "setup_future_usage": "form",
                "shipping": "deepObject",
                "statement_descriptor": "form",
                "statement_descriptor_suffix": "form",
                "transfer_data": "deepObject",
                "transfer_group": "form",
                "use_stripe_sdk": "form",
            },
            explode={
                "amount": True,
                "application_fee_amount": True,
                "automatic_payment_methods": True,
                "capture_method": True,
                "confirm": True,
                "confirmation_method": True,
                "confirmation_token": True,
                "currency": True,
                "customer": True,
                "description": True,
                "error_on_requires_action": True,
                "expand": True,
                "mandate": True,
                "mandate_data": True,
                "metadata": True,
                "off_session": True,
                "on_behalf_of": True,
                "payment_method": True,
                "payment_method_configuration": True,
                "payment_method_data": True,
                "payment_method_options": True,
                "payment_method_types": True,
                "radar_options": True,
                "receipt_email": True,
                "return_url": True,
                "setup_future_usage": True,
                "shipping": True,
                "statement_descriptor": True,
                "statement_descriptor_suffix": True,
                "transfer_data": True,
                "transfer_group": True,
                "use_stripe_sdk": True,
            },
        )
        return self._base_client.request(
            method="POST",
            path="/v1/payment_intents",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.PaymentIntent,
            request_options=request_options or default_request_options(),
        )

    def update(
        self,
        *,
        intent: str,
        data: typing.Union[
            typing.Optional[params.PaymentIntentUpdateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PaymentIntent:
        """
        Update a PaymentIntent

        <p>Updates properties on a PaymentIntent object without confirming.</p>

        <p>Depending on which properties you update, you might need to confirm the
        PaymentIntent again. For example, updating the <code>payment_method</code>
        always requires you to confirm the PaymentIntent again. If you prefer to
        update and confirm at the same time, we recommend updating properties through
        the <a href="/docs/api/payment_intents/confirm">confirm API</a> instead.</p>

        POST /v1/payment_intents/{intent}

        Args:
            data: PaymentIntentUpdateBody
            intent: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.payment_intent.update(intent="string")
        ```
        """
        models.PaymentIntent.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerPaymentIntentUpdateBody,
                style={
                    "amount": "form",
                    "application_fee_amount": "deepObject",
                    "capture_method": "form",
                    "currency": "form",
                    "customer": "form",
                    "description": "form",
                    "expand": "deepObject",
                    "metadata": "deepObject",
                    "payment_method": "form",
                    "payment_method_configuration": "form",
                    "payment_method_data": "deepObject",
                    "payment_method_options": "deepObject",
                    "payment_method_types": "deepObject",
                    "receipt_email": "deepObject",
                    "setup_future_usage": "form",
                    "shipping": "deepObject",
                    "statement_descriptor": "form",
                    "statement_descriptor_suffix": "form",
                    "transfer_data": "deepObject",
                    "transfer_group": "form",
                },
                explode={
                    "amount": True,
                    "application_fee_amount": True,
                    "capture_method": True,
                    "currency": True,
                    "customer": True,
                    "description": True,
                    "expand": True,
                    "metadata": True,
                    "payment_method": True,
                    "payment_method_configuration": True,
                    "payment_method_data": True,
                    "payment_method_options": True,
                    "payment_method_types": True,
                    "receipt_email": True,
                    "setup_future_usage": True,
                    "shipping": True,
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
            path=f"/v1/payment_intents/{intent}",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.PaymentIntent,
            request_options=request_options or default_request_options(),
        )

    def apply_customer_balance(
        self,
        *,
        intent: str,
        data: typing.Union[
            typing.Optional[params.PaymentIntentApplyCustomerBalanceBody],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PaymentIntent:
        """
        Reconcile a customer_balance PaymentIntent

        <p>Manually reconcile the remaining amount for a <code>customer_balance</code> PaymentIntent.</p>

        POST /v1/payment_intents/{intent}/apply_customer_balance

        Args:
            data: PaymentIntentApplyCustomerBalanceBody
            intent: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.payment_intent.apply_customer_balance(intent="string")
        ```
        """
        models.PaymentIntent.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerPaymentIntentApplyCustomerBalanceBody,
                style={"amount": "form", "currency": "form", "expand": "deepObject"},
                explode={"amount": True, "currency": True, "expand": True},
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/payment_intents/{intent}/apply_customer_balance",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.PaymentIntent,
            request_options=request_options or default_request_options(),
        )

    def cancel(
        self,
        *,
        intent: str,
        data: typing.Union[
            typing.Optional[params.PaymentIntentCancelBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PaymentIntent:
        """
        Cancel a PaymentIntent

        <p>You can cancel a PaymentIntent object when it’s in one of these statuses: <code>requires_payment_method</code>, <code>requires_capture</code>, <code>requires_confirmation</code>, <code>requires_action</code> or, <a href="/docs/payments/intents">in rare cases</a>, <code>processing</code>. </p>

        <p>After it’s canceled, no additional charges are made by the PaymentIntent and any operations on the PaymentIntent fail with an error. For PaymentIntents with a <code>status</code> of <code>requires_capture</code>, the remaining <code>amount_capturable</code> is automatically refunded. </p>

        <p>You can’t cancel the PaymentIntent for a Checkout Session. <a href="/docs/api/checkout/sessions/expire">Expire the Checkout Session</a> instead.</p>

        POST /v1/payment_intents/{intent}/cancel

        Args:
            data: PaymentIntentCancelBody
            intent: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.payment_intent.cancel(intent="string")
        ```
        """
        models.PaymentIntent.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerPaymentIntentCancelBody,
                style={"cancellation_reason": "form", "expand": "deepObject"},
                explode={"cancellation_reason": True, "expand": True},
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/payment_intents/{intent}/cancel",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.PaymentIntent,
            request_options=request_options or default_request_options(),
        )

    def capture(
        self,
        *,
        intent: str,
        data: typing.Union[
            typing.Optional[params.PaymentIntentCaptureBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PaymentIntent:
        """
        Capture a PaymentIntent

        <p>Capture the funds of an existing uncaptured PaymentIntent when its status is <code>requires_capture</code>.</p>

        <p>Uncaptured PaymentIntents are cancelled a set number of days (7 by default) after their creation.</p>

        <p>Learn more about <a href="/docs/payments/capture-later">separate authorization and capture</a>.</p>

        POST /v1/payment_intents/{intent}/capture

        Args:
            data: PaymentIntentCaptureBody
            intent: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.payment_intent.capture(intent="string")
        ```
        """
        models.PaymentIntent.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerPaymentIntentCaptureBody,
                style={
                    "amount_to_capture": "form",
                    "application_fee_amount": "form",
                    "expand": "deepObject",
                    "final_capture": "form",
                    "metadata": "deepObject",
                    "statement_descriptor": "form",
                    "statement_descriptor_suffix": "form",
                    "transfer_data": "deepObject",
                },
                explode={
                    "amount_to_capture": True,
                    "application_fee_amount": True,
                    "expand": True,
                    "final_capture": True,
                    "metadata": True,
                    "statement_descriptor": True,
                    "statement_descriptor_suffix": True,
                    "transfer_data": True,
                },
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/payment_intents/{intent}/capture",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.PaymentIntent,
            request_options=request_options or default_request_options(),
        )

    def confirm(
        self,
        *,
        intent: str,
        data: typing.Union[
            typing.Optional[params.PaymentIntentConfirmBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PaymentIntent:
        """
        Confirm a PaymentIntent

        <p>Confirm that your customer intends to pay with current or provided
        payment method. Upon confirmation, the PaymentIntent will attempt to initiate
        a payment.
        If the selected payment method requires additional authentication steps, the
        PaymentIntent will transition to the <code>requires_action</code> status and
        suggest additional actions via <code>next_action</code>. If payment fails,
        the PaymentIntent transitions to the <code>requires_payment_method</code> status or the
        <code>canceled</code> status if the confirmation limit is reached. If
        payment succeeds, the PaymentIntent will transition to the <code>succeeded</code>
        status (or <code>requires_capture</code>, if <code>capture_method</code> is set to <code>manual</code>).
        If the <code>confirmation_method</code> is <code>automatic</code>, payment may be attempted
        using our <a href="/docs/stripe-js/reference#stripe-handle-card-payment">client SDKs</a>
        and the PaymentIntent’s <a href="#payment_intent_object-client_secret">client_secret</a>.
        After <code>next_action</code>s are handled by the client, no additional
        confirmation is required to complete the payment.
        If the <code>confirmation_method</code> is <code>manual</code>, all payment attempts must be
        initiated using a secret key.
        If any actions are required for the payment, the PaymentIntent will
        return to the <code>requires_confirmation</code> state
        after those actions are completed. Your server needs to then
        explicitly re-confirm the PaymentIntent to initiate the next payment
        attempt.
        There is a variable upper limit on how many times a PaymentIntent can be confirmed.
        After this limit is reached, any further calls to this endpoint will
        transition the PaymentIntent to the <code>canceled</code> state.</p>

        POST /v1/payment_intents/{intent}/confirm

        Args:
            data: PaymentIntentConfirmBody
            intent: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.payment_intent.confirm(intent="string")
        ```
        """
        models.PaymentIntent.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerPaymentIntentConfirmBody,
                style={
                    "capture_method": "form",
                    "client_secret": "form",
                    "confirmation_token": "form",
                    "error_on_requires_action": "form",
                    "expand": "deepObject",
                    "mandate": "form",
                    "mandate_data": "deepObject",
                    "off_session": "deepObject",
                    "payment_method": "form",
                    "payment_method_data": "deepObject",
                    "payment_method_options": "deepObject",
                    "payment_method_types": "deepObject",
                    "radar_options": "deepObject",
                    "receipt_email": "deepObject",
                    "return_url": "form",
                    "setup_future_usage": "form",
                    "shipping": "deepObject",
                    "use_stripe_sdk": "form",
                },
                explode={
                    "capture_method": True,
                    "client_secret": True,
                    "confirmation_token": True,
                    "error_on_requires_action": True,
                    "expand": True,
                    "mandate": True,
                    "mandate_data": True,
                    "off_session": True,
                    "payment_method": True,
                    "payment_method_data": True,
                    "payment_method_options": True,
                    "payment_method_types": True,
                    "radar_options": True,
                    "receipt_email": True,
                    "return_url": True,
                    "setup_future_usage": True,
                    "shipping": True,
                    "use_stripe_sdk": True,
                },
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/payment_intents/{intent}/confirm",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.PaymentIntent,
            request_options=request_options or default_request_options(),
        )

    def increment_authorization(
        self,
        *,
        amount: int,
        intent: str,
        application_fee_amount: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        description: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        metadata: typing.Union[
            typing.Optional[params.PaymentIntentIncrementAuthorizationBodyMetadata],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        statement_descriptor: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        transfer_data: typing.Union[
            typing.Optional[params.PaymentIntentIncrementAuthorizationBodyTransferData],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PaymentIntent:
        """
        Increment an authorization

        <p>Perform an incremental authorization on an eligible
        <a href="/docs/api/payment_intents/object">PaymentIntent</a>. To be eligible, the
        PaymentIntent’s status must be <code>requires_capture</code> and
        <a href="/docs/api/charges/object#charge_object-payment_method_details-card_present-incremental_authorization_supported">incremental_authorization_supported</a>
        must be <code>true</code>.</p>

        <p>Incremental authorizations attempt to increase the authorized amount on
        your customer’s card to the new, higher <code>amount</code> provided. Similar to the
        initial authorization, incremental authorizations can be declined. A
        single PaymentIntent can call this endpoint multiple times to further
        increase the authorized amount.</p>

        <p>If the incremental authorization succeeds, the PaymentIntent object
        returns with the updated
        <a href="/docs/api/payment_intents/object#payment_intent_object-amount">amount</a>.
        If the incremental authorization fails, a
        <a href="/docs/error-codes#card-declined">card_declined</a> error returns, and no other
        fields on the PaymentIntent or Charge update. The PaymentIntent
        object remains capturable for the previously authorized amount.</p>

        <p>Each PaymentIntent can have a maximum of 10 incremental authorization attempts, including declines.
        After it’s captured, a PaymentIntent can no longer be incremented.</p>

        <p>Learn more about <a href="/docs/terminal/features/incremental-authorizations">incremental authorizations</a>.</p>

        POST /v1/payment_intents/{intent}/increment_authorization

        Args:
            application_fee_amount: The amount of the application fee (if any) that will be requested to be applied to the payment and transferred to the application owner's Stripe account. The amount of the application fee collected will be capped at the total amount captured. For more information, see the PaymentIntents [use case for connected accounts](https://stripe.com/docs/payments/connected-accounts).
            description: An arbitrary string attached to the object. Often useful for displaying to users.
            expand: Specifies which fields in the response should be expanded.
            metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
            statement_descriptor: Text that appears on the customer's statement as the statement descriptor for a non-card or card charge. This value overrides the account's default statement descriptor. For information about requirements, including the 22-character limit, see [the Statement Descriptor docs](https://docs.stripe.com/get-started/account/statement-descriptors).
            transfer_data: The parameters used to automatically create a transfer after the payment is captured.
        Learn more about the [use case for connected accounts](https://stripe.com/docs/payments/connected-accounts).
            amount: The updated total amount that you intend to collect from the cardholder. This amount must be greater than the currently authorized amount.
            intent: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.payment_intent.increment_authorization(amount=123, intent="string")
        ```
        """
        models.PaymentIntent.model_rebuild(_types_namespace=models._types_namespace)
        _data = to_form_urlencoded(
            item={
                "application_fee_amount": application_fee_amount,
                "description": description,
                "expand": expand,
                "metadata": metadata,
                "statement_descriptor": statement_descriptor,
                "transfer_data": transfer_data,
                "amount": amount,
            },
            dump_with=params._SerializerPaymentIntentIncrementAuthorizationBody,
            style={
                "amount": "form",
                "application_fee_amount": "form",
                "description": "form",
                "expand": "deepObject",
                "metadata": "deepObject",
                "statement_descriptor": "form",
                "transfer_data": "deepObject",
            },
            explode={
                "amount": True,
                "application_fee_amount": True,
                "description": True,
                "expand": True,
                "metadata": True,
                "statement_descriptor": True,
                "transfer_data": True,
            },
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/payment_intents/{intent}/increment_authorization",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.PaymentIntent,
            request_options=request_options or default_request_options(),
        )

    def verify_microdeposits(
        self,
        *,
        intent: str,
        data: typing.Union[
            typing.Optional[params.PaymentIntentVerifyMicrodepositsBody],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PaymentIntent:
        """
        Verify microdeposits on a PaymentIntent

        <p>Verifies microdeposits on a PaymentIntent object.</p>

        POST /v1/payment_intents/{intent}/verify_microdeposits

        Args:
            data: PaymentIntentVerifyMicrodepositsBody
            intent: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.payment_intent.verify_microdeposits(intent="string")
        ```
        """
        models.PaymentIntent.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerPaymentIntentVerifyMicrodepositsBody,
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
            path=f"/v1/payment_intents/{intent}/verify_microdeposits",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.PaymentIntent,
            request_options=request_options or default_request_options(),
        )


class AsyncPaymentIntentClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def list(
        self,
        *,
        created: typing.Union[
            typing.Optional[typing.Union[params.PaymentIntentListCreatedObj0, int]],
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
        starting_after: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PaymentIntentListResponse:
        """
        List all PaymentIntents

        <p>Returns a list of PaymentIntents.</p>

        GET /v1/payment_intents

        Args:
            created: A filter on the list, based on the object `created` field. The value can be a string with an integer Unix timestamp or a dictionary with a number of different query options.
            customer: Only return PaymentIntents for the customer that this customer ID specifies.
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
        await client.payment_intent.list()
        ```
        """
        models.PaymentIntentListResponse.model_rebuild(
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
                        params._SerializerPaymentIntentListCreatedObj0, int
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
            path="/v1/payment_intents",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.PaymentIntentListResponse,
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
    ) -> models.PaymentIntentSearchResponse:
        """
        Search PaymentIntents

        <p>Search for PaymentIntents you’ve previously created using Stripe’s <a href="/docs/search#search-query-language">Search Query Language</a>.
        Don’t use search in read-after-write flows where strict consistency is necessary. Under normal operating
        conditions, data is searchable in less than a minute. Occasionally, propagation of new or updated data can be up
        to an hour behind during outages. Search functionality is not available to merchants in India.</p>

        GET /v1/payment_intents/search

        Args:
            expand: Specifies which fields in the response should be expanded.
            limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            page: A cursor for pagination across multiple pages of results. Don't include this parameter on the first call. Use the next_page value returned in a previous response to request subsequent results.
            query: The search query string. See [search query language](https://stripe.com/docs/search#search-query-language) and the list of supported [query fields for payment intents](https://stripe.com/docs/search#query-fields-for-payment-intents).
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.payment_intent.search(query="string")
        ```
        """
        models.PaymentIntentSearchResponse.model_rebuild(
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
            path="/v1/payment_intents/search",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.PaymentIntentSearchResponse,
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
    ) -> models.PaymentIntent:
        """
        Retrieve a PaymentIntent

        <p>Retrieves the details of a PaymentIntent that has previously been created. </p>

        <p>You can retrieve a PaymentIntent client-side using a publishable key when the <code>client_secret</code> is in the query string. </p>

        <p>If you retrieve a PaymentIntent with a publishable key, it only returns a subset of properties. Refer to the <a href="#payment_intent_object">payment intent</a> object reference for more details.</p>

        GET /v1/payment_intents/{intent}

        Args:
            client_secret: The client secret of the PaymentIntent. We require it if you use a publishable key to retrieve the source.
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
        await client.payment_intent.get(intent="string")
        ```
        """
        models.PaymentIntent.model_rebuild(_types_namespace=models._types_namespace)
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
            path=f"/v1/payment_intents/{intent}",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.PaymentIntent,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        amount: int,
        currency: str,
        application_fee_amount: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        automatic_payment_methods: typing.Union[
            typing.Optional[params.PaymentIntentCreateBodyAutomaticPaymentMethods],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        capture_method: typing.Union[
            typing.Optional[
                typing_extensions.Literal["automatic", "automatic_async", "manual"]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        confirm: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        confirmation_method: typing.Union[
            typing.Optional[typing_extensions.Literal["automatic", "manual"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        confirmation_token: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        customer: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        description: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        error_on_requires_action: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        mandate: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        mandate_data: typing.Union[
            typing.Optional[
                typing.Union[params.PaymentIntentCreateBodyMandateDataObj0, str]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        metadata: typing.Union[
            typing.Optional[params.PaymentIntentCreateBodyMetadata], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        off_session: typing.Union[
            typing.Optional[
                typing.Union[bool, typing_extensions.Literal["one_off", "recurring"]]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        on_behalf_of: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        payment_method: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        payment_method_configuration: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        payment_method_data: typing.Union[
            typing.Optional[params.PaymentIntentCreateBodyPaymentMethodData],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        payment_method_options: typing.Union[
            typing.Optional[params.PaymentIntentCreateBodyPaymentMethodOptions],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        payment_method_types: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        radar_options: typing.Union[
            typing.Optional[params.PaymentIntentCreateBodyRadarOptions],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        receipt_email: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        return_url: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        setup_future_usage: typing.Union[
            typing.Optional[typing_extensions.Literal["off_session", "on_session"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        shipping: typing.Union[
            typing.Optional[params.PaymentIntentCreateBodyShipping], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        statement_descriptor: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        statement_descriptor_suffix: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        transfer_data: typing.Union[
            typing.Optional[params.PaymentIntentCreateBodyTransferData],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        transfer_group: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        use_stripe_sdk: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PaymentIntent:
        """
        Create a PaymentIntent

        <p>Creates a PaymentIntent object.</p>

        <p>After the PaymentIntent is created, attach a payment method and <a href="/docs/api/payment_intents/confirm">confirm</a>
        to continue the payment. Learn more about <a href="/docs/payments/payment-intents">the available payment flows
        with the Payment Intents API</a>.</p>

        <p>When you use <code>confirm=true</code> during creation, it’s equivalent to creating
        and confirming the PaymentIntent in the same call. You can use any parameters
        available in the <a href="/docs/api/payment_intents/confirm">confirm API</a> when you supply
        <code>confirm=true</code>.</p>

        POST /v1/payment_intents

        Args:
            application_fee_amount: The amount of the application fee (if any) that will be requested to be applied to the payment and transferred to the application owner's Stripe account. The amount of the application fee collected will be capped at the total amount captured. For more information, see the PaymentIntents [use case for connected accounts](https://stripe.com/docs/payments/connected-accounts).
            automatic_payment_methods: When you enable this parameter, this PaymentIntent accepts payment methods that you enable in the Dashboard and that are compatible with this PaymentIntent's other parameters.
            capture_method: Controls when the funds will be captured from the customer's account.
            confirm: Set to `true` to attempt to [confirm this PaymentIntent](https://stripe.com/docs/api/payment_intents/confirm) immediately. This parameter defaults to `false`. When creating and confirming a PaymentIntent at the same time, you can also provide the parameters available in the [Confirm API](https://stripe.com/docs/api/payment_intents/confirm).
            confirmation_method: Describes whether we can confirm this PaymentIntent automatically, or if it requires customer action to confirm the payment.
            confirmation_token: ID of the ConfirmationToken used to confirm this PaymentIntent.

        If the provided ConfirmationToken contains properties that are also being provided in this request, such as `payment_method`, then the values in this request will take precedence.
            customer: ID of the Customer this PaymentIntent belongs to, if one exists.

        Payment methods attached to other Customers cannot be used with this PaymentIntent.

        If [setup_future_usage](https://stripe.com/docs/api#payment_intent_object-setup_future_usage) is set and this PaymentIntent's payment method is not `card_present`, then the payment method attaches to the Customer after the PaymentIntent has been confirmed and any required actions from the user are complete. If the payment method is `card_present` and isn't a digital wallet, then a [generated_card](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-card_present-generated_card) payment method representing the card is created and attached to the Customer instead.
            description: An arbitrary string attached to the object. Often useful for displaying to users.
            error_on_requires_action: Set to `true` to fail the payment attempt if the PaymentIntent transitions into `requires_action`. Use this parameter for simpler integrations that don't handle customer actions, such as [saving cards without authentication](https://stripe.com/docs/payments/save-card-without-authentication). This parameter can only be used with [`confirm=true`](https://stripe.com/docs/api/payment_intents/create#create_payment_intent-confirm).
            expand: Specifies which fields in the response should be expanded.
            mandate: ID of the mandate that's used for this payment. This parameter can only be used with [`confirm=true`](https://stripe.com/docs/api/payment_intents/create#create_payment_intent-confirm).
            mandate_data: This hash contains details about the Mandate to create. This parameter can only be used with [`confirm=true`](https://stripe.com/docs/api/payment_intents/create#create_payment_intent-confirm).
            metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
            off_session: Set to `true` to indicate that the customer isn't in your checkout flow during this payment attempt and can't authenticate. Use this parameter in scenarios where you collect card details and [charge them later](https://stripe.com/docs/payments/cards/charging-saved-cards). This parameter can only be used with [`confirm=true`](https://stripe.com/docs/api/payment_intents/create#create_payment_intent-confirm).
            on_behalf_of: The Stripe account ID that these funds are intended for. Learn more about the [use case for connected accounts](https://stripe.com/docs/payments/connected-accounts).
            payment_method: ID of the payment method (a PaymentMethod, Card, or [compatible Source](https://stripe.com/docs/payments/payment-methods/transitioning#compatibility) object) to attach to this PaymentIntent.

        If you omit this parameter with `confirm=true`, `customer.default_source` attaches as this PaymentIntent's payment instrument to improve migration for users of the Charges API. We recommend that you explicitly provide the `payment_method` moving forward.
            payment_method_configuration: The ID of the [payment method configuration](https://stripe.com/docs/api/payment_method_configurations) to use with this PaymentIntent.
            payment_method_data: If provided, this hash will be used to create a PaymentMethod. The new PaymentMethod will appear
        in the [payment_method](https://stripe.com/docs/api/payment_intents/object#payment_intent_object-payment_method)
        property on the PaymentIntent.
            payment_method_options: Payment method-specific configuration for this PaymentIntent.
            payment_method_types: The list of payment method types (for example, a card) that this PaymentIntent can use. If you don't provide this, Stripe will dynamically show relevant payment methods from your [payment method settings](https://dashboard.stripe.com/settings/payment_methods).
            radar_options: Options to configure Radar. Learn more about [Radar Sessions](https://stripe.com/docs/radar/radar-session).
            receipt_email: Email address to send the receipt to. If you specify `receipt_email` for a payment in live mode, you send a receipt regardless of your [email settings](https://dashboard.stripe.com/account/emails).
            return_url: The URL to redirect your customer back to after they authenticate or cancel their payment on the payment method's app or site. If you'd prefer to redirect to a mobile application, you can alternatively supply an application URI scheme. This parameter can only be used with [`confirm=true`](https://stripe.com/docs/api/payment_intents/create#create_payment_intent-confirm).
            setup_future_usage: Indicates that you intend to make future payments with this PaymentIntent's payment method.

        If you provide a Customer with the PaymentIntent, you can use this parameter to [attach the payment method](/payments/save-during-payment) to the Customer after the PaymentIntent is confirmed and the customer completes any required actions. If you don't provide a Customer, you can still [attach](/api/payment_methods/attach) the payment method to a Customer after the transaction completes.

        If the payment method is `card_present` and isn't a digital wallet, Stripe creates and attaches a [generated_card](/api/charges/object#charge_object-payment_method_details-card_present-generated_card) payment method representing the card to the Customer instead.

        When processing card payments, Stripe uses `setup_future_usage` to help you comply with regional legislation and network rules, such as [SCA](/strong-customer-authentication).
            shipping: Shipping information for this PaymentIntent.
            statement_descriptor: Text that appears on the customer's statement as the statement descriptor for a non-card charge. This value overrides the account's default statement descriptor. For information about requirements, including the 22-character limit, see [the Statement Descriptor docs](https://docs.stripe.com/get-started/account/statement-descriptors).

        Setting this value for a card charge returns an error. For card charges, set the [statement_descriptor_suffix](https://docs.stripe.com/get-started/account/statement-descriptors#dynamic) instead.
            statement_descriptor_suffix: Provides information about a card charge. Concatenated to the account's [statement descriptor prefix](https://docs.stripe.com/get-started/account/statement-descriptors#static) to form the complete statement descriptor that appears on the customer's statement.
            transfer_data: The parameters that you can use to automatically create a Transfer.
        Learn more about the [use case for connected accounts](https://stripe.com/docs/payments/connected-accounts).
            transfer_group: A string that identifies the resulting payment as part of a group. Learn more about the [use case for connected accounts](https://stripe.com/docs/connect/separate-charges-and-transfers).
            use_stripe_sdk: Set to `true` when confirming server-side and using Stripe.js, iOS, or Android client-side SDKs to handle the next actions.
            amount: Amount intended to be collected by this PaymentIntent. A positive integer representing how much to charge in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal) (e.g., 100 cents to charge $1.00 or 100 to charge ¥100, a zero-decimal currency). The minimum amount is $0.50 US or [equivalent in charge currency](https://stripe.com/docs/currencies#minimum-and-maximum-charge-amounts). The amount value supports up to eight digits (e.g., a value of 99999999 for a USD charge of $999,999.99).
            currency: Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.payment_intent.create(amount=123, currency="string")
        ```
        """
        models.PaymentIntent.model_rebuild(_types_namespace=models._types_namespace)
        _data = to_form_urlencoded(
            item={
                "application_fee_amount": application_fee_amount,
                "automatic_payment_methods": automatic_payment_methods,
                "capture_method": capture_method,
                "confirm": confirm,
                "confirmation_method": confirmation_method,
                "confirmation_token": confirmation_token,
                "customer": customer,
                "description": description,
                "error_on_requires_action": error_on_requires_action,
                "expand": expand,
                "mandate": mandate,
                "mandate_data": mandate_data,
                "metadata": metadata,
                "off_session": off_session,
                "on_behalf_of": on_behalf_of,
                "payment_method": payment_method,
                "payment_method_configuration": payment_method_configuration,
                "payment_method_data": payment_method_data,
                "payment_method_options": payment_method_options,
                "payment_method_types": payment_method_types,
                "radar_options": radar_options,
                "receipt_email": receipt_email,
                "return_url": return_url,
                "setup_future_usage": setup_future_usage,
                "shipping": shipping,
                "statement_descriptor": statement_descriptor,
                "statement_descriptor_suffix": statement_descriptor_suffix,
                "transfer_data": transfer_data,
                "transfer_group": transfer_group,
                "use_stripe_sdk": use_stripe_sdk,
                "amount": amount,
                "currency": currency,
            },
            dump_with=params._SerializerPaymentIntentCreateBody,
            style={
                "amount": "form",
                "application_fee_amount": "form",
                "automatic_payment_methods": "deepObject",
                "capture_method": "form",
                "confirm": "form",
                "confirmation_method": "form",
                "confirmation_token": "form",
                "currency": "form",
                "customer": "form",
                "description": "form",
                "error_on_requires_action": "form",
                "expand": "deepObject",
                "mandate": "form",
                "mandate_data": "deepObject",
                "metadata": "deepObject",
                "off_session": "deepObject",
                "on_behalf_of": "form",
                "payment_method": "form",
                "payment_method_configuration": "form",
                "payment_method_data": "deepObject",
                "payment_method_options": "deepObject",
                "payment_method_types": "deepObject",
                "radar_options": "deepObject",
                "receipt_email": "form",
                "return_url": "form",
                "setup_future_usage": "form",
                "shipping": "deepObject",
                "statement_descriptor": "form",
                "statement_descriptor_suffix": "form",
                "transfer_data": "deepObject",
                "transfer_group": "form",
                "use_stripe_sdk": "form",
            },
            explode={
                "amount": True,
                "application_fee_amount": True,
                "automatic_payment_methods": True,
                "capture_method": True,
                "confirm": True,
                "confirmation_method": True,
                "confirmation_token": True,
                "currency": True,
                "customer": True,
                "description": True,
                "error_on_requires_action": True,
                "expand": True,
                "mandate": True,
                "mandate_data": True,
                "metadata": True,
                "off_session": True,
                "on_behalf_of": True,
                "payment_method": True,
                "payment_method_configuration": True,
                "payment_method_data": True,
                "payment_method_options": True,
                "payment_method_types": True,
                "radar_options": True,
                "receipt_email": True,
                "return_url": True,
                "setup_future_usage": True,
                "shipping": True,
                "statement_descriptor": True,
                "statement_descriptor_suffix": True,
                "transfer_data": True,
                "transfer_group": True,
                "use_stripe_sdk": True,
            },
        )
        return await self._base_client.request(
            method="POST",
            path="/v1/payment_intents",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.PaymentIntent,
            request_options=request_options or default_request_options(),
        )

    async def update(
        self,
        *,
        intent: str,
        data: typing.Union[
            typing.Optional[params.PaymentIntentUpdateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PaymentIntent:
        """
        Update a PaymentIntent

        <p>Updates properties on a PaymentIntent object without confirming.</p>

        <p>Depending on which properties you update, you might need to confirm the
        PaymentIntent again. For example, updating the <code>payment_method</code>
        always requires you to confirm the PaymentIntent again. If you prefer to
        update and confirm at the same time, we recommend updating properties through
        the <a href="/docs/api/payment_intents/confirm">confirm API</a> instead.</p>

        POST /v1/payment_intents/{intent}

        Args:
            data: PaymentIntentUpdateBody
            intent: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.payment_intent.update(intent="string")
        ```
        """
        models.PaymentIntent.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerPaymentIntentUpdateBody,
                style={
                    "amount": "form",
                    "application_fee_amount": "deepObject",
                    "capture_method": "form",
                    "currency": "form",
                    "customer": "form",
                    "description": "form",
                    "expand": "deepObject",
                    "metadata": "deepObject",
                    "payment_method": "form",
                    "payment_method_configuration": "form",
                    "payment_method_data": "deepObject",
                    "payment_method_options": "deepObject",
                    "payment_method_types": "deepObject",
                    "receipt_email": "deepObject",
                    "setup_future_usage": "form",
                    "shipping": "deepObject",
                    "statement_descriptor": "form",
                    "statement_descriptor_suffix": "form",
                    "transfer_data": "deepObject",
                    "transfer_group": "form",
                },
                explode={
                    "amount": True,
                    "application_fee_amount": True,
                    "capture_method": True,
                    "currency": True,
                    "customer": True,
                    "description": True,
                    "expand": True,
                    "metadata": True,
                    "payment_method": True,
                    "payment_method_configuration": True,
                    "payment_method_data": True,
                    "payment_method_options": True,
                    "payment_method_types": True,
                    "receipt_email": True,
                    "setup_future_usage": True,
                    "shipping": True,
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
            path=f"/v1/payment_intents/{intent}",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.PaymentIntent,
            request_options=request_options or default_request_options(),
        )

    async def apply_customer_balance(
        self,
        *,
        intent: str,
        data: typing.Union[
            typing.Optional[params.PaymentIntentApplyCustomerBalanceBody],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PaymentIntent:
        """
        Reconcile a customer_balance PaymentIntent

        <p>Manually reconcile the remaining amount for a <code>customer_balance</code> PaymentIntent.</p>

        POST /v1/payment_intents/{intent}/apply_customer_balance

        Args:
            data: PaymentIntentApplyCustomerBalanceBody
            intent: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.payment_intent.apply_customer_balance(intent="string")
        ```
        """
        models.PaymentIntent.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerPaymentIntentApplyCustomerBalanceBody,
                style={"amount": "form", "currency": "form", "expand": "deepObject"},
                explode={"amount": True, "currency": True, "expand": True},
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/payment_intents/{intent}/apply_customer_balance",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.PaymentIntent,
            request_options=request_options or default_request_options(),
        )

    async def cancel(
        self,
        *,
        intent: str,
        data: typing.Union[
            typing.Optional[params.PaymentIntentCancelBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PaymentIntent:
        """
        Cancel a PaymentIntent

        <p>You can cancel a PaymentIntent object when it’s in one of these statuses: <code>requires_payment_method</code>, <code>requires_capture</code>, <code>requires_confirmation</code>, <code>requires_action</code> or, <a href="/docs/payments/intents">in rare cases</a>, <code>processing</code>. </p>

        <p>After it’s canceled, no additional charges are made by the PaymentIntent and any operations on the PaymentIntent fail with an error. For PaymentIntents with a <code>status</code> of <code>requires_capture</code>, the remaining <code>amount_capturable</code> is automatically refunded. </p>

        <p>You can’t cancel the PaymentIntent for a Checkout Session. <a href="/docs/api/checkout/sessions/expire">Expire the Checkout Session</a> instead.</p>

        POST /v1/payment_intents/{intent}/cancel

        Args:
            data: PaymentIntentCancelBody
            intent: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.payment_intent.cancel(intent="string")
        ```
        """
        models.PaymentIntent.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerPaymentIntentCancelBody,
                style={"cancellation_reason": "form", "expand": "deepObject"},
                explode={"cancellation_reason": True, "expand": True},
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/payment_intents/{intent}/cancel",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.PaymentIntent,
            request_options=request_options or default_request_options(),
        )

    async def capture(
        self,
        *,
        intent: str,
        data: typing.Union[
            typing.Optional[params.PaymentIntentCaptureBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PaymentIntent:
        """
        Capture a PaymentIntent

        <p>Capture the funds of an existing uncaptured PaymentIntent when its status is <code>requires_capture</code>.</p>

        <p>Uncaptured PaymentIntents are cancelled a set number of days (7 by default) after their creation.</p>

        <p>Learn more about <a href="/docs/payments/capture-later">separate authorization and capture</a>.</p>

        POST /v1/payment_intents/{intent}/capture

        Args:
            data: PaymentIntentCaptureBody
            intent: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.payment_intent.capture(intent="string")
        ```
        """
        models.PaymentIntent.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerPaymentIntentCaptureBody,
                style={
                    "amount_to_capture": "form",
                    "application_fee_amount": "form",
                    "expand": "deepObject",
                    "final_capture": "form",
                    "metadata": "deepObject",
                    "statement_descriptor": "form",
                    "statement_descriptor_suffix": "form",
                    "transfer_data": "deepObject",
                },
                explode={
                    "amount_to_capture": True,
                    "application_fee_amount": True,
                    "expand": True,
                    "final_capture": True,
                    "metadata": True,
                    "statement_descriptor": True,
                    "statement_descriptor_suffix": True,
                    "transfer_data": True,
                },
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/payment_intents/{intent}/capture",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.PaymentIntent,
            request_options=request_options or default_request_options(),
        )

    async def confirm(
        self,
        *,
        intent: str,
        data: typing.Union[
            typing.Optional[params.PaymentIntentConfirmBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PaymentIntent:
        """
        Confirm a PaymentIntent

        <p>Confirm that your customer intends to pay with current or provided
        payment method. Upon confirmation, the PaymentIntent will attempt to initiate
        a payment.
        If the selected payment method requires additional authentication steps, the
        PaymentIntent will transition to the <code>requires_action</code> status and
        suggest additional actions via <code>next_action</code>. If payment fails,
        the PaymentIntent transitions to the <code>requires_payment_method</code> status or the
        <code>canceled</code> status if the confirmation limit is reached. If
        payment succeeds, the PaymentIntent will transition to the <code>succeeded</code>
        status (or <code>requires_capture</code>, if <code>capture_method</code> is set to <code>manual</code>).
        If the <code>confirmation_method</code> is <code>automatic</code>, payment may be attempted
        using our <a href="/docs/stripe-js/reference#stripe-handle-card-payment">client SDKs</a>
        and the PaymentIntent’s <a href="#payment_intent_object-client_secret">client_secret</a>.
        After <code>next_action</code>s are handled by the client, no additional
        confirmation is required to complete the payment.
        If the <code>confirmation_method</code> is <code>manual</code>, all payment attempts must be
        initiated using a secret key.
        If any actions are required for the payment, the PaymentIntent will
        return to the <code>requires_confirmation</code> state
        after those actions are completed. Your server needs to then
        explicitly re-confirm the PaymentIntent to initiate the next payment
        attempt.
        There is a variable upper limit on how many times a PaymentIntent can be confirmed.
        After this limit is reached, any further calls to this endpoint will
        transition the PaymentIntent to the <code>canceled</code> state.</p>

        POST /v1/payment_intents/{intent}/confirm

        Args:
            data: PaymentIntentConfirmBody
            intent: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.payment_intent.confirm(intent="string")
        ```
        """
        models.PaymentIntent.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerPaymentIntentConfirmBody,
                style={
                    "capture_method": "form",
                    "client_secret": "form",
                    "confirmation_token": "form",
                    "error_on_requires_action": "form",
                    "expand": "deepObject",
                    "mandate": "form",
                    "mandate_data": "deepObject",
                    "off_session": "deepObject",
                    "payment_method": "form",
                    "payment_method_data": "deepObject",
                    "payment_method_options": "deepObject",
                    "payment_method_types": "deepObject",
                    "radar_options": "deepObject",
                    "receipt_email": "deepObject",
                    "return_url": "form",
                    "setup_future_usage": "form",
                    "shipping": "deepObject",
                    "use_stripe_sdk": "form",
                },
                explode={
                    "capture_method": True,
                    "client_secret": True,
                    "confirmation_token": True,
                    "error_on_requires_action": True,
                    "expand": True,
                    "mandate": True,
                    "mandate_data": True,
                    "off_session": True,
                    "payment_method": True,
                    "payment_method_data": True,
                    "payment_method_options": True,
                    "payment_method_types": True,
                    "radar_options": True,
                    "receipt_email": True,
                    "return_url": True,
                    "setup_future_usage": True,
                    "shipping": True,
                    "use_stripe_sdk": True,
                },
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/payment_intents/{intent}/confirm",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.PaymentIntent,
            request_options=request_options or default_request_options(),
        )

    async def increment_authorization(
        self,
        *,
        amount: int,
        intent: str,
        application_fee_amount: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        description: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        metadata: typing.Union[
            typing.Optional[params.PaymentIntentIncrementAuthorizationBodyMetadata],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        statement_descriptor: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        transfer_data: typing.Union[
            typing.Optional[params.PaymentIntentIncrementAuthorizationBodyTransferData],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PaymentIntent:
        """
        Increment an authorization

        <p>Perform an incremental authorization on an eligible
        <a href="/docs/api/payment_intents/object">PaymentIntent</a>. To be eligible, the
        PaymentIntent’s status must be <code>requires_capture</code> and
        <a href="/docs/api/charges/object#charge_object-payment_method_details-card_present-incremental_authorization_supported">incremental_authorization_supported</a>
        must be <code>true</code>.</p>

        <p>Incremental authorizations attempt to increase the authorized amount on
        your customer’s card to the new, higher <code>amount</code> provided. Similar to the
        initial authorization, incremental authorizations can be declined. A
        single PaymentIntent can call this endpoint multiple times to further
        increase the authorized amount.</p>

        <p>If the incremental authorization succeeds, the PaymentIntent object
        returns with the updated
        <a href="/docs/api/payment_intents/object#payment_intent_object-amount">amount</a>.
        If the incremental authorization fails, a
        <a href="/docs/error-codes#card-declined">card_declined</a> error returns, and no other
        fields on the PaymentIntent or Charge update. The PaymentIntent
        object remains capturable for the previously authorized amount.</p>

        <p>Each PaymentIntent can have a maximum of 10 incremental authorization attempts, including declines.
        After it’s captured, a PaymentIntent can no longer be incremented.</p>

        <p>Learn more about <a href="/docs/terminal/features/incremental-authorizations">incremental authorizations</a>.</p>

        POST /v1/payment_intents/{intent}/increment_authorization

        Args:
            application_fee_amount: The amount of the application fee (if any) that will be requested to be applied to the payment and transferred to the application owner's Stripe account. The amount of the application fee collected will be capped at the total amount captured. For more information, see the PaymentIntents [use case for connected accounts](https://stripe.com/docs/payments/connected-accounts).
            description: An arbitrary string attached to the object. Often useful for displaying to users.
            expand: Specifies which fields in the response should be expanded.
            metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
            statement_descriptor: Text that appears on the customer's statement as the statement descriptor for a non-card or card charge. This value overrides the account's default statement descriptor. For information about requirements, including the 22-character limit, see [the Statement Descriptor docs](https://docs.stripe.com/get-started/account/statement-descriptors).
            transfer_data: The parameters used to automatically create a transfer after the payment is captured.
        Learn more about the [use case for connected accounts](https://stripe.com/docs/payments/connected-accounts).
            amount: The updated total amount that you intend to collect from the cardholder. This amount must be greater than the currently authorized amount.
            intent: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.payment_intent.increment_authorization(amount=123, intent="string")
        ```
        """
        models.PaymentIntent.model_rebuild(_types_namespace=models._types_namespace)
        _data = to_form_urlencoded(
            item={
                "application_fee_amount": application_fee_amount,
                "description": description,
                "expand": expand,
                "metadata": metadata,
                "statement_descriptor": statement_descriptor,
                "transfer_data": transfer_data,
                "amount": amount,
            },
            dump_with=params._SerializerPaymentIntentIncrementAuthorizationBody,
            style={
                "amount": "form",
                "application_fee_amount": "form",
                "description": "form",
                "expand": "deepObject",
                "metadata": "deepObject",
                "statement_descriptor": "form",
                "transfer_data": "deepObject",
            },
            explode={
                "amount": True,
                "application_fee_amount": True,
                "description": True,
                "expand": True,
                "metadata": True,
                "statement_descriptor": True,
                "transfer_data": True,
            },
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/payment_intents/{intent}/increment_authorization",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.PaymentIntent,
            request_options=request_options or default_request_options(),
        )

    async def verify_microdeposits(
        self,
        *,
        intent: str,
        data: typing.Union[
            typing.Optional[params.PaymentIntentVerifyMicrodepositsBody],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PaymentIntent:
        """
        Verify microdeposits on a PaymentIntent

        <p>Verifies microdeposits on a PaymentIntent object.</p>

        POST /v1/payment_intents/{intent}/verify_microdeposits

        Args:
            data: PaymentIntentVerifyMicrodepositsBody
            intent: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.payment_intent.verify_microdeposits(intent="string")
        ```
        """
        models.PaymentIntent.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerPaymentIntentVerifyMicrodepositsBody,
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
            path=f"/v1/payment_intents/{intent}/verify_microdeposits",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.PaymentIntent,
            request_options=request_options or default_request_options(),
        )
