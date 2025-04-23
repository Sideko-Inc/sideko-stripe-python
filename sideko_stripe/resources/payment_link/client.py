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


class PaymentLinkClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def list(
        self,
        *,
        active: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
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
    ) -> models.PaymentLinkListResponse:
        """
        List all payment links

        <p>Returns a list of your payment links.</p>

        GET /v1/payment_links

        Args:
            active: Only return payment links that are active or inactive (e.g., pass `false` to list all inactive payment links).
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
        client.payment_link.list()
        ```
        """
        models.PaymentLinkListResponse.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _query: QueryParams = {}
        if not isinstance(active, type_utils.NotGiven):
            encode_query_param(
                _query,
                "active",
                to_encodable(item=active, dump_with=bool),
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
            path="/v1/payment_links",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.PaymentLinkListResponse,
            request_options=request_options or default_request_options(),
        )

    def get(
        self,
        *,
        payment_link: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PaymentLink:
        """
        Retrieve payment link

        <p>Retrieve a payment link.</p>

        GET /v1/payment_links/{payment_link}

        Args:
            expand: Specifies which fields in the response should be expanded.
            payment_link: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.payment_link.get(payment_link="string")
        ```
        """
        models.PaymentLink.model_rebuild(_types_namespace=models._types_namespace)
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
            path=f"/v1/payment_links/{payment_link}",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.PaymentLink,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        line_items: typing.List[params.PaymentLinkCreateBodyLineItemsItem],
        after_completion: typing.Union[
            typing.Optional[params.PaymentLinkCreateBodyAfterCompletion],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        allow_promotion_codes: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        application_fee_amount: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        application_fee_percent: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        automatic_tax: typing.Union[
            typing.Optional[params.PaymentLinkCreateBodyAutomaticTax],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        billing_address_collection: typing.Union[
            typing.Optional[typing_extensions.Literal["auto", "required"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        consent_collection: typing.Union[
            typing.Optional[params.PaymentLinkCreateBodyConsentCollection],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        currency: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        custom_fields: typing.Union[
            typing.Optional[typing.List[params.PaymentLinkCreateBodyCustomFieldsItem]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        custom_text: typing.Union[
            typing.Optional[params.PaymentLinkCreateBodyCustomText], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        customer_creation: typing.Union[
            typing.Optional[typing_extensions.Literal["always", "if_required"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        inactive_message: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        invoice_creation: typing.Union[
            typing.Optional[params.PaymentLinkCreateBodyInvoiceCreation],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        metadata: typing.Union[
            typing.Optional[params.PaymentLinkCreateBodyMetadata], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        on_behalf_of: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        optional_items: typing.Union[
            typing.Optional[typing.List[params.PaymentLinkCreateBodyOptionalItemsItem]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        payment_intent_data: typing.Union[
            typing.Optional[params.PaymentLinkCreateBodyPaymentIntentData],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        payment_method_collection: typing.Union[
            typing.Optional[typing_extensions.Literal["always", "if_required"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        payment_method_types: typing.Union[
            typing.Optional[
                typing.List[
                    typing_extensions.Literal[
                        "affirm",
                        "afterpay_clearpay",
                        "alipay",
                        "alma",
                        "au_becs_debit",
                        "bacs_debit",
                        "bancontact",
                        "billie",
                        "blik",
                        "boleto",
                        "card",
                        "cashapp",
                        "eps",
                        "fpx",
                        "giropay",
                        "grabpay",
                        "ideal",
                        "klarna",
                        "konbini",
                        "link",
                        "mobilepay",
                        "multibanco",
                        "oxxo",
                        "p24",
                        "pay_by_bank",
                        "paynow",
                        "paypal",
                        "pix",
                        "promptpay",
                        "satispay",
                        "sepa_debit",
                        "sofort",
                        "swish",
                        "twint",
                        "us_bank_account",
                        "wechat_pay",
                        "zip",
                    ]
                ]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        phone_number_collection: typing.Union[
            typing.Optional[params.PaymentLinkCreateBodyPhoneNumberCollection],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        restrictions: typing.Union[
            typing.Optional[params.PaymentLinkCreateBodyRestrictions],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        shipping_address_collection: typing.Union[
            typing.Optional[params.PaymentLinkCreateBodyShippingAddressCollection],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        shipping_options: typing.Union[
            typing.Optional[
                typing.List[params.PaymentLinkCreateBodyShippingOptionsItem]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        submit_type: typing.Union[
            typing.Optional[
                typing_extensions.Literal["auto", "book", "donate", "pay", "subscribe"]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        subscription_data: typing.Union[
            typing.Optional[params.PaymentLinkCreateBodySubscriptionData],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        tax_id_collection: typing.Union[
            typing.Optional[params.PaymentLinkCreateBodyTaxIdCollection],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        transfer_data: typing.Union[
            typing.Optional[params.PaymentLinkCreateBodyTransferData],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PaymentLink:
        """
        Create a payment link

        <p>Creates a payment link.</p>

        POST /v1/payment_links

        Args:
            after_completion: Behavior after the purchase is complete.
            allow_promotion_codes: Enables user redeemable promotion codes.
            application_fee_amount: The amount of the application fee (if any) that will be requested to be applied to the payment and transferred to the application owner's Stripe account. Can only be applied when there are no line items with recurring prices.
            application_fee_percent: A non-negative decimal between 0 and 100, with at most two decimal places. This represents the percentage of the subscription invoice total that will be transferred to the application owner's Stripe account. There must be at least 1 line item with a recurring price to use this field.
            automatic_tax: Configuration for automatic tax collection.
            billing_address_collection: Configuration for collecting the customer's billing address. Defaults to `auto`.
            consent_collection: Configure fields to gather active consent from customers.
            currency: Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies) and supported by each line item's price.
            custom_fields: Collect additional information from your customer using custom fields. Up to 3 fields are supported.
            custom_text: Display additional text for your customers using custom text.
            customer_creation: Configures whether [checkout sessions](https://stripe.com/docs/api/checkout/sessions) created by this payment link create a [Customer](https://stripe.com/docs/api/customers).
            expand: Specifies which fields in the response should be expanded.
            inactive_message: The custom message to be displayed to a customer when a payment link is no longer active.
            invoice_creation: Generate a post-purchase Invoice for one-time payments.
            metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`. Metadata associated with this Payment Link will automatically be copied to [checkout sessions](https://stripe.com/docs/api/checkout/sessions) created by this payment link.
            on_behalf_of: The account on behalf of which to charge.
            optional_items: A list of optional items the customer can add to their order at checkout. Use this parameter to pass one-time or recurring [Prices](https://stripe.com/docs/api/prices).
        There is a maximum of 10 optional items allowed on a payment link, and the existing limits on the number of line items allowed on a payment link apply to the combined number of line items and optional items.
        There is a maximum of 20 combined line items and optional items.
            payment_intent_data: A subset of parameters to be passed to PaymentIntent creation for Checkout Sessions in `payment` mode.
            payment_method_collection: Specify whether Checkout should collect a payment method. When set to `if_required`, Checkout will not collect a payment method when the total due for the session is 0.This may occur if the Checkout Session includes a free trial or a discount.

        Can only be set in `subscription` mode. Defaults to `always`.

        If you'd like information on how to collect a payment method outside of Checkout, read the guide on [configuring subscriptions with a free trial](https://stripe.com/docs/payments/checkout/free-trials).
            payment_method_types: The list of payment method types that customers can use. If no value is passed, Stripe will dynamically show relevant payment methods from your [payment method settings](https://dashboard.stripe.com/settings/payment_methods) (20+ payment methods [supported](https://stripe.com/docs/payments/payment-methods/integration-options#payment-method-product-support)).
            phone_number_collection: Controls phone number collection settings during checkout.

        We recommend that you review your privacy policy and check with your legal contacts.
            restrictions: Settings that restrict the usage of a payment link.
            shipping_address_collection: Configuration for collecting the customer's shipping address.
            shipping_options: The shipping rate options to apply to [checkout sessions](https://stripe.com/docs/api/checkout/sessions) created by this payment link.
            submit_type: Describes the type of transaction being performed in order to customize relevant text on the page, such as the submit button. Changing this value will also affect the hostname in the [url](https://stripe.com/docs/api/payment_links/payment_links/object#url) property (example: `donate.stripe.com`).
            subscription_data: When creating a subscription, the specified configuration data will be used. There must be at least one line item with a recurring price to use `subscription_data`.
            tax_id_collection: Controls tax ID collection during checkout.
            transfer_data: The account (if any) the payments will be attributed to for tax reporting, and where funds from each payment will be transferred to.
            line_items: The line items representing what is being sold. Each line item represents an item being sold. Up to 20 line items are supported.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.payment_link.create(line_items=[{"price": "string", "quantity": 123}])
        ```
        """
        models.PaymentLink.model_rebuild(_types_namespace=models._types_namespace)
        _data = to_form_urlencoded(
            item={
                "after_completion": after_completion,
                "allow_promotion_codes": allow_promotion_codes,
                "application_fee_amount": application_fee_amount,
                "application_fee_percent": application_fee_percent,
                "automatic_tax": automatic_tax,
                "billing_address_collection": billing_address_collection,
                "consent_collection": consent_collection,
                "currency": currency,
                "custom_fields": custom_fields,
                "custom_text": custom_text,
                "customer_creation": customer_creation,
                "expand": expand,
                "inactive_message": inactive_message,
                "invoice_creation": invoice_creation,
                "metadata": metadata,
                "on_behalf_of": on_behalf_of,
                "optional_items": optional_items,
                "payment_intent_data": payment_intent_data,
                "payment_method_collection": payment_method_collection,
                "payment_method_types": payment_method_types,
                "phone_number_collection": phone_number_collection,
                "restrictions": restrictions,
                "shipping_address_collection": shipping_address_collection,
                "shipping_options": shipping_options,
                "submit_type": submit_type,
                "subscription_data": subscription_data,
                "tax_id_collection": tax_id_collection,
                "transfer_data": transfer_data,
                "line_items": line_items,
            },
            dump_with=params._SerializerPaymentLinkCreateBody,
            style={
                "after_completion": "deepObject",
                "allow_promotion_codes": "form",
                "application_fee_amount": "form",
                "application_fee_percent": "form",
                "automatic_tax": "deepObject",
                "billing_address_collection": "form",
                "consent_collection": "deepObject",
                "currency": "form",
                "custom_fields": "deepObject",
                "custom_text": "deepObject",
                "customer_creation": "form",
                "expand": "deepObject",
                "inactive_message": "form",
                "invoice_creation": "deepObject",
                "line_items": "deepObject",
                "metadata": "deepObject",
                "on_behalf_of": "form",
                "optional_items": "deepObject",
                "payment_intent_data": "deepObject",
                "payment_method_collection": "form",
                "payment_method_types": "deepObject",
                "phone_number_collection": "deepObject",
                "restrictions": "deepObject",
                "shipping_address_collection": "deepObject",
                "shipping_options": "deepObject",
                "submit_type": "form",
                "subscription_data": "deepObject",
                "tax_id_collection": "deepObject",
                "transfer_data": "deepObject",
            },
            explode={
                "after_completion": True,
                "allow_promotion_codes": True,
                "application_fee_amount": True,
                "application_fee_percent": True,
                "automatic_tax": True,
                "billing_address_collection": True,
                "consent_collection": True,
                "currency": True,
                "custom_fields": True,
                "custom_text": True,
                "customer_creation": True,
                "expand": True,
                "inactive_message": True,
                "invoice_creation": True,
                "line_items": True,
                "metadata": True,
                "on_behalf_of": True,
                "optional_items": True,
                "payment_intent_data": True,
                "payment_method_collection": True,
                "payment_method_types": True,
                "phone_number_collection": True,
                "restrictions": True,
                "shipping_address_collection": True,
                "shipping_options": True,
                "submit_type": True,
                "subscription_data": True,
                "tax_id_collection": True,
                "transfer_data": True,
            },
        )
        return self._base_client.request(
            method="POST",
            path="/v1/payment_links",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.PaymentLink,
            request_options=request_options or default_request_options(),
        )

    def update(
        self,
        *,
        payment_link: str,
        data: typing.Union[
            typing.Optional[params.PaymentLinkUpdateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PaymentLink:
        """
        Update a payment link

        <p>Updates a payment link.</p>

        POST /v1/payment_links/{payment_link}

        Args:
            data: PaymentLinkUpdateBody
            payment_link: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.payment_link.update(payment_link="string")
        ```
        """
        models.PaymentLink.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerPaymentLinkUpdateBody,
                style={
                    "active": "form",
                    "after_completion": "deepObject",
                    "allow_promotion_codes": "form",
                    "automatic_tax": "deepObject",
                    "billing_address_collection": "form",
                    "custom_fields": "deepObject",
                    "custom_text": "deepObject",
                    "customer_creation": "form",
                    "expand": "deepObject",
                    "inactive_message": "deepObject",
                    "invoice_creation": "deepObject",
                    "line_items": "deepObject",
                    "metadata": "deepObject",
                    "payment_intent_data": "deepObject",
                    "payment_method_collection": "form",
                    "payment_method_types": "deepObject",
                    "phone_number_collection": "deepObject",
                    "restrictions": "deepObject",
                    "shipping_address_collection": "deepObject",
                    "submit_type": "form",
                    "subscription_data": "deepObject",
                    "tax_id_collection": "deepObject",
                },
                explode={
                    "active": True,
                    "after_completion": True,
                    "allow_promotion_codes": True,
                    "automatic_tax": True,
                    "billing_address_collection": True,
                    "custom_fields": True,
                    "custom_text": True,
                    "customer_creation": True,
                    "expand": True,
                    "inactive_message": True,
                    "invoice_creation": True,
                    "line_items": True,
                    "metadata": True,
                    "payment_intent_data": True,
                    "payment_method_collection": True,
                    "payment_method_types": True,
                    "phone_number_collection": True,
                    "restrictions": True,
                    "shipping_address_collection": True,
                    "submit_type": True,
                    "subscription_data": True,
                    "tax_id_collection": True,
                },
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/payment_links/{payment_link}",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.PaymentLink,
            request_options=request_options or default_request_options(),
        )


class AsyncPaymentLinkClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def list(
        self,
        *,
        active: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
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
    ) -> models.PaymentLinkListResponse:
        """
        List all payment links

        <p>Returns a list of your payment links.</p>

        GET /v1/payment_links

        Args:
            active: Only return payment links that are active or inactive (e.g., pass `false` to list all inactive payment links).
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
        await client.payment_link.list()
        ```
        """
        models.PaymentLinkListResponse.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _query: QueryParams = {}
        if not isinstance(active, type_utils.NotGiven):
            encode_query_param(
                _query,
                "active",
                to_encodable(item=active, dump_with=bool),
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
            path="/v1/payment_links",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.PaymentLinkListResponse,
            request_options=request_options or default_request_options(),
        )

    async def get(
        self,
        *,
        payment_link: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PaymentLink:
        """
        Retrieve payment link

        <p>Retrieve a payment link.</p>

        GET /v1/payment_links/{payment_link}

        Args:
            expand: Specifies which fields in the response should be expanded.
            payment_link: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.payment_link.get(payment_link="string")
        ```
        """
        models.PaymentLink.model_rebuild(_types_namespace=models._types_namespace)
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
            path=f"/v1/payment_links/{payment_link}",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.PaymentLink,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        line_items: typing.List[params.PaymentLinkCreateBodyLineItemsItem],
        after_completion: typing.Union[
            typing.Optional[params.PaymentLinkCreateBodyAfterCompletion],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        allow_promotion_codes: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        application_fee_amount: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        application_fee_percent: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        automatic_tax: typing.Union[
            typing.Optional[params.PaymentLinkCreateBodyAutomaticTax],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        billing_address_collection: typing.Union[
            typing.Optional[typing_extensions.Literal["auto", "required"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        consent_collection: typing.Union[
            typing.Optional[params.PaymentLinkCreateBodyConsentCollection],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        currency: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        custom_fields: typing.Union[
            typing.Optional[typing.List[params.PaymentLinkCreateBodyCustomFieldsItem]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        custom_text: typing.Union[
            typing.Optional[params.PaymentLinkCreateBodyCustomText], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        customer_creation: typing.Union[
            typing.Optional[typing_extensions.Literal["always", "if_required"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        inactive_message: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        invoice_creation: typing.Union[
            typing.Optional[params.PaymentLinkCreateBodyInvoiceCreation],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        metadata: typing.Union[
            typing.Optional[params.PaymentLinkCreateBodyMetadata], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        on_behalf_of: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        optional_items: typing.Union[
            typing.Optional[typing.List[params.PaymentLinkCreateBodyOptionalItemsItem]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        payment_intent_data: typing.Union[
            typing.Optional[params.PaymentLinkCreateBodyPaymentIntentData],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        payment_method_collection: typing.Union[
            typing.Optional[typing_extensions.Literal["always", "if_required"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        payment_method_types: typing.Union[
            typing.Optional[
                typing.List[
                    typing_extensions.Literal[
                        "affirm",
                        "afterpay_clearpay",
                        "alipay",
                        "alma",
                        "au_becs_debit",
                        "bacs_debit",
                        "bancontact",
                        "billie",
                        "blik",
                        "boleto",
                        "card",
                        "cashapp",
                        "eps",
                        "fpx",
                        "giropay",
                        "grabpay",
                        "ideal",
                        "klarna",
                        "konbini",
                        "link",
                        "mobilepay",
                        "multibanco",
                        "oxxo",
                        "p24",
                        "pay_by_bank",
                        "paynow",
                        "paypal",
                        "pix",
                        "promptpay",
                        "satispay",
                        "sepa_debit",
                        "sofort",
                        "swish",
                        "twint",
                        "us_bank_account",
                        "wechat_pay",
                        "zip",
                    ]
                ]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        phone_number_collection: typing.Union[
            typing.Optional[params.PaymentLinkCreateBodyPhoneNumberCollection],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        restrictions: typing.Union[
            typing.Optional[params.PaymentLinkCreateBodyRestrictions],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        shipping_address_collection: typing.Union[
            typing.Optional[params.PaymentLinkCreateBodyShippingAddressCollection],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        shipping_options: typing.Union[
            typing.Optional[
                typing.List[params.PaymentLinkCreateBodyShippingOptionsItem]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        submit_type: typing.Union[
            typing.Optional[
                typing_extensions.Literal["auto", "book", "donate", "pay", "subscribe"]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        subscription_data: typing.Union[
            typing.Optional[params.PaymentLinkCreateBodySubscriptionData],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        tax_id_collection: typing.Union[
            typing.Optional[params.PaymentLinkCreateBodyTaxIdCollection],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        transfer_data: typing.Union[
            typing.Optional[params.PaymentLinkCreateBodyTransferData],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PaymentLink:
        """
        Create a payment link

        <p>Creates a payment link.</p>

        POST /v1/payment_links

        Args:
            after_completion: Behavior after the purchase is complete.
            allow_promotion_codes: Enables user redeemable promotion codes.
            application_fee_amount: The amount of the application fee (if any) that will be requested to be applied to the payment and transferred to the application owner's Stripe account. Can only be applied when there are no line items with recurring prices.
            application_fee_percent: A non-negative decimal between 0 and 100, with at most two decimal places. This represents the percentage of the subscription invoice total that will be transferred to the application owner's Stripe account. There must be at least 1 line item with a recurring price to use this field.
            automatic_tax: Configuration for automatic tax collection.
            billing_address_collection: Configuration for collecting the customer's billing address. Defaults to `auto`.
            consent_collection: Configure fields to gather active consent from customers.
            currency: Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies) and supported by each line item's price.
            custom_fields: Collect additional information from your customer using custom fields. Up to 3 fields are supported.
            custom_text: Display additional text for your customers using custom text.
            customer_creation: Configures whether [checkout sessions](https://stripe.com/docs/api/checkout/sessions) created by this payment link create a [Customer](https://stripe.com/docs/api/customers).
            expand: Specifies which fields in the response should be expanded.
            inactive_message: The custom message to be displayed to a customer when a payment link is no longer active.
            invoice_creation: Generate a post-purchase Invoice for one-time payments.
            metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`. Metadata associated with this Payment Link will automatically be copied to [checkout sessions](https://stripe.com/docs/api/checkout/sessions) created by this payment link.
            on_behalf_of: The account on behalf of which to charge.
            optional_items: A list of optional items the customer can add to their order at checkout. Use this parameter to pass one-time or recurring [Prices](https://stripe.com/docs/api/prices).
        There is a maximum of 10 optional items allowed on a payment link, and the existing limits on the number of line items allowed on a payment link apply to the combined number of line items and optional items.
        There is a maximum of 20 combined line items and optional items.
            payment_intent_data: A subset of parameters to be passed to PaymentIntent creation for Checkout Sessions in `payment` mode.
            payment_method_collection: Specify whether Checkout should collect a payment method. When set to `if_required`, Checkout will not collect a payment method when the total due for the session is 0.This may occur if the Checkout Session includes a free trial or a discount.

        Can only be set in `subscription` mode. Defaults to `always`.

        If you'd like information on how to collect a payment method outside of Checkout, read the guide on [configuring subscriptions with a free trial](https://stripe.com/docs/payments/checkout/free-trials).
            payment_method_types: The list of payment method types that customers can use. If no value is passed, Stripe will dynamically show relevant payment methods from your [payment method settings](https://dashboard.stripe.com/settings/payment_methods) (20+ payment methods [supported](https://stripe.com/docs/payments/payment-methods/integration-options#payment-method-product-support)).
            phone_number_collection: Controls phone number collection settings during checkout.

        We recommend that you review your privacy policy and check with your legal contacts.
            restrictions: Settings that restrict the usage of a payment link.
            shipping_address_collection: Configuration for collecting the customer's shipping address.
            shipping_options: The shipping rate options to apply to [checkout sessions](https://stripe.com/docs/api/checkout/sessions) created by this payment link.
            submit_type: Describes the type of transaction being performed in order to customize relevant text on the page, such as the submit button. Changing this value will also affect the hostname in the [url](https://stripe.com/docs/api/payment_links/payment_links/object#url) property (example: `donate.stripe.com`).
            subscription_data: When creating a subscription, the specified configuration data will be used. There must be at least one line item with a recurring price to use `subscription_data`.
            tax_id_collection: Controls tax ID collection during checkout.
            transfer_data: The account (if any) the payments will be attributed to for tax reporting, and where funds from each payment will be transferred to.
            line_items: The line items representing what is being sold. Each line item represents an item being sold. Up to 20 line items are supported.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.payment_link.create(
            line_items=[{"price": "string", "quantity": 123}]
        )
        ```
        """
        models.PaymentLink.model_rebuild(_types_namespace=models._types_namespace)
        _data = to_form_urlencoded(
            item={
                "after_completion": after_completion,
                "allow_promotion_codes": allow_promotion_codes,
                "application_fee_amount": application_fee_amount,
                "application_fee_percent": application_fee_percent,
                "automatic_tax": automatic_tax,
                "billing_address_collection": billing_address_collection,
                "consent_collection": consent_collection,
                "currency": currency,
                "custom_fields": custom_fields,
                "custom_text": custom_text,
                "customer_creation": customer_creation,
                "expand": expand,
                "inactive_message": inactive_message,
                "invoice_creation": invoice_creation,
                "metadata": metadata,
                "on_behalf_of": on_behalf_of,
                "optional_items": optional_items,
                "payment_intent_data": payment_intent_data,
                "payment_method_collection": payment_method_collection,
                "payment_method_types": payment_method_types,
                "phone_number_collection": phone_number_collection,
                "restrictions": restrictions,
                "shipping_address_collection": shipping_address_collection,
                "shipping_options": shipping_options,
                "submit_type": submit_type,
                "subscription_data": subscription_data,
                "tax_id_collection": tax_id_collection,
                "transfer_data": transfer_data,
                "line_items": line_items,
            },
            dump_with=params._SerializerPaymentLinkCreateBody,
            style={
                "after_completion": "deepObject",
                "allow_promotion_codes": "form",
                "application_fee_amount": "form",
                "application_fee_percent": "form",
                "automatic_tax": "deepObject",
                "billing_address_collection": "form",
                "consent_collection": "deepObject",
                "currency": "form",
                "custom_fields": "deepObject",
                "custom_text": "deepObject",
                "customer_creation": "form",
                "expand": "deepObject",
                "inactive_message": "form",
                "invoice_creation": "deepObject",
                "line_items": "deepObject",
                "metadata": "deepObject",
                "on_behalf_of": "form",
                "optional_items": "deepObject",
                "payment_intent_data": "deepObject",
                "payment_method_collection": "form",
                "payment_method_types": "deepObject",
                "phone_number_collection": "deepObject",
                "restrictions": "deepObject",
                "shipping_address_collection": "deepObject",
                "shipping_options": "deepObject",
                "submit_type": "form",
                "subscription_data": "deepObject",
                "tax_id_collection": "deepObject",
                "transfer_data": "deepObject",
            },
            explode={
                "after_completion": True,
                "allow_promotion_codes": True,
                "application_fee_amount": True,
                "application_fee_percent": True,
                "automatic_tax": True,
                "billing_address_collection": True,
                "consent_collection": True,
                "currency": True,
                "custom_fields": True,
                "custom_text": True,
                "customer_creation": True,
                "expand": True,
                "inactive_message": True,
                "invoice_creation": True,
                "line_items": True,
                "metadata": True,
                "on_behalf_of": True,
                "optional_items": True,
                "payment_intent_data": True,
                "payment_method_collection": True,
                "payment_method_types": True,
                "phone_number_collection": True,
                "restrictions": True,
                "shipping_address_collection": True,
                "shipping_options": True,
                "submit_type": True,
                "subscription_data": True,
                "tax_id_collection": True,
                "transfer_data": True,
            },
        )
        return await self._base_client.request(
            method="POST",
            path="/v1/payment_links",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.PaymentLink,
            request_options=request_options or default_request_options(),
        )

    async def update(
        self,
        *,
        payment_link: str,
        data: typing.Union[
            typing.Optional[params.PaymentLinkUpdateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PaymentLink:
        """
        Update a payment link

        <p>Updates a payment link.</p>

        POST /v1/payment_links/{payment_link}

        Args:
            data: PaymentLinkUpdateBody
            payment_link: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.payment_link.update(payment_link="string")
        ```
        """
        models.PaymentLink.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerPaymentLinkUpdateBody,
                style={
                    "active": "form",
                    "after_completion": "deepObject",
                    "allow_promotion_codes": "form",
                    "automatic_tax": "deepObject",
                    "billing_address_collection": "form",
                    "custom_fields": "deepObject",
                    "custom_text": "deepObject",
                    "customer_creation": "form",
                    "expand": "deepObject",
                    "inactive_message": "deepObject",
                    "invoice_creation": "deepObject",
                    "line_items": "deepObject",
                    "metadata": "deepObject",
                    "payment_intent_data": "deepObject",
                    "payment_method_collection": "form",
                    "payment_method_types": "deepObject",
                    "phone_number_collection": "deepObject",
                    "restrictions": "deepObject",
                    "shipping_address_collection": "deepObject",
                    "submit_type": "form",
                    "subscription_data": "deepObject",
                    "tax_id_collection": "deepObject",
                },
                explode={
                    "active": True,
                    "after_completion": True,
                    "allow_promotion_codes": True,
                    "automatic_tax": True,
                    "billing_address_collection": True,
                    "custom_fields": True,
                    "custom_text": True,
                    "customer_creation": True,
                    "expand": True,
                    "inactive_message": True,
                    "invoice_creation": True,
                    "line_items": True,
                    "metadata": True,
                    "payment_intent_data": True,
                    "payment_method_collection": True,
                    "payment_method_types": True,
                    "phone_number_collection": True,
                    "restrictions": True,
                    "shipping_address_collection": True,
                    "submit_type": True,
                    "subscription_data": True,
                    "tax_id_collection": True,
                },
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/payment_links/{payment_link}",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.PaymentLink,
            request_options=request_options or default_request_options(),
        )
