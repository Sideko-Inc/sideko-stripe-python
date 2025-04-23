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


class PaymentMethodClient:
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
        type_: typing.Union[
            typing.Optional[
                typing_extensions.Literal[
                    "acss_debit",
                    "affirm",
                    "afterpay_clearpay",
                    "alipay",
                    "alma",
                    "amazon_pay",
                    "au_becs_debit",
                    "bacs_debit",
                    "bancontact",
                    "billie",
                    "blik",
                    "boleto",
                    "card",
                    "cashapp",
                    "customer_balance",
                    "eps",
                    "fpx",
                    "giropay",
                    "grabpay",
                    "ideal",
                    "kakao_pay",
                    "klarna",
                    "konbini",
                    "kr_card",
                    "link",
                    "mobilepay",
                    "multibanco",
                    "naver_pay",
                    "nz_bank_account",
                    "oxxo",
                    "p24",
                    "pay_by_bank",
                    "payco",
                    "paynow",
                    "paypal",
                    "pix",
                    "promptpay",
                    "revolut_pay",
                    "samsung_pay",
                    "satispay",
                    "sepa_debit",
                    "sofort",
                    "swish",
                    "twint",
                    "us_bank_account",
                    "wechat_pay",
                    "zip",
                ]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PaymentMethodListResponse:
        """
        List PaymentMethods

        <p>Returns a list of PaymentMethods for Treasury flows. If you want to list the PaymentMethods attached to a Customer for payments, you should use the <a href="/docs/api/payment_methods/customer_list">List a Customer’s PaymentMethods</a> API instead.</p>

        GET /v1/payment_methods

        Args:
            customer: The ID of the customer whose PaymentMethods will be retrieved.
            ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            expand: Specifies which fields in the response should be expanded.
            limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
            type: An optional filter on the list, based on the object `type` field. Without the filter, the list includes all current and future payment method types. If your integration expects only one type of payment method in the response, make sure to provide a type value in the request.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.payment_method.list()
        ```
        """
        models.PaymentMethodListResponse.model_rebuild(
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
        if not isinstance(type_, type_utils.NotGiven):
            encode_query_param(
                _query,
                "type",
                to_encodable(
                    item=type_,
                    dump_with=typing_extensions.Literal[
                        "acss_debit",
                        "affirm",
                        "afterpay_clearpay",
                        "alipay",
                        "alma",
                        "amazon_pay",
                        "au_becs_debit",
                        "bacs_debit",
                        "bancontact",
                        "billie",
                        "blik",
                        "boleto",
                        "card",
                        "cashapp",
                        "customer_balance",
                        "eps",
                        "fpx",
                        "giropay",
                        "grabpay",
                        "ideal",
                        "kakao_pay",
                        "klarna",
                        "konbini",
                        "kr_card",
                        "link",
                        "mobilepay",
                        "multibanco",
                        "naver_pay",
                        "nz_bank_account",
                        "oxxo",
                        "p24",
                        "pay_by_bank",
                        "payco",
                        "paynow",
                        "paypal",
                        "pix",
                        "promptpay",
                        "revolut_pay",
                        "samsung_pay",
                        "satispay",
                        "sepa_debit",
                        "sofort",
                        "swish",
                        "twint",
                        "us_bank_account",
                        "wechat_pay",
                        "zip",
                    ],
                ),
                style="form",
                explode=True,
            )
        return self._base_client.request(
            method="GET",
            path="/v1/payment_methods",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.PaymentMethodListResponse,
            request_options=request_options or default_request_options(),
        )

    def get(
        self,
        *,
        payment_method: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PaymentMethod:
        """
        Retrieve a PaymentMethod

        <p>Retrieves a PaymentMethod object attached to the StripeAccount. To retrieve a payment method attached to a Customer, you should use <a href="/docs/api/payment_methods/customer">Retrieve a Customer’s PaymentMethods</a></p>

        GET /v1/payment_methods/{payment_method}

        Args:
            expand: Specifies which fields in the response should be expanded.
            payment_method: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.payment_method.get(payment_method="string")
        ```
        """
        models.PaymentMethod.model_rebuild(_types_namespace=models._types_namespace)
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
            path=f"/v1/payment_methods/{payment_method}",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.PaymentMethod,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        data: typing.Union[
            typing.Optional[params.PaymentMethodCreateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PaymentMethod:
        """
        Shares a PaymentMethod

        <p>Creates a PaymentMethod object. Read the <a href="/docs/stripe-js/reference#stripe-create-payment-method">Stripe.js reference</a> to learn how to create PaymentMethods via Stripe.js.</p>

        <p>Instead of creating a PaymentMethod directly, we recommend using the <a href="/docs/payments/accept-a-payment">PaymentIntents</a> API to accept a payment immediately or the <a href="/docs/payments/save-and-reuse">SetupIntent</a> API to collect payment method details ahead of a future payment.</p>

        POST /v1/payment_methods

        Args:
            data: PaymentMethodCreateBody
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.payment_method.create()
        ```
        """
        models.PaymentMethod.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerPaymentMethodCreateBody,
                style={
                    "acss_debit": "deepObject",
                    "affirm": "deepObject",
                    "afterpay_clearpay": "deepObject",
                    "alipay": "deepObject",
                    "allow_redisplay": "form",
                    "alma": "deepObject",
                    "amazon_pay": "deepObject",
                    "au_becs_debit": "deepObject",
                    "bacs_debit": "deepObject",
                    "bancontact": "deepObject",
                    "billie": "deepObject",
                    "billing_details": "deepObject",
                    "blik": "deepObject",
                    "boleto": "deepObject",
                    "card": "deepObject",
                    "cashapp": "deepObject",
                    "customer": "form",
                    "customer_balance": "deepObject",
                    "eps": "deepObject",
                    "expand": "deepObject",
                    "fpx": "deepObject",
                    "giropay": "deepObject",
                    "grabpay": "deepObject",
                    "ideal": "deepObject",
                    "interac_present": "deepObject",
                    "kakao_pay": "deepObject",
                    "klarna": "deepObject",
                    "konbini": "deepObject",
                    "kr_card": "deepObject",
                    "link": "deepObject",
                    "metadata": "deepObject",
                    "mobilepay": "deepObject",
                    "multibanco": "deepObject",
                    "naver_pay": "deepObject",
                    "nz_bank_account": "deepObject",
                    "oxxo": "deepObject",
                    "p24": "deepObject",
                    "pay_by_bank": "deepObject",
                    "payco": "deepObject",
                    "payment_method": "form",
                    "paynow": "deepObject",
                    "paypal": "deepObject",
                    "pix": "deepObject",
                    "promptpay": "deepObject",
                    "radar_options": "deepObject",
                    "revolut_pay": "deepObject",
                    "samsung_pay": "deepObject",
                    "satispay": "deepObject",
                    "sepa_debit": "deepObject",
                    "sofort": "deepObject",
                    "swish": "deepObject",
                    "twint": "deepObject",
                    "type": "form",
                    "us_bank_account": "deepObject",
                    "wechat_pay": "deepObject",
                    "zip": "deepObject",
                },
                explode={
                    "acss_debit": True,
                    "affirm": True,
                    "afterpay_clearpay": True,
                    "alipay": True,
                    "allow_redisplay": True,
                    "alma": True,
                    "amazon_pay": True,
                    "au_becs_debit": True,
                    "bacs_debit": True,
                    "bancontact": True,
                    "billie": True,
                    "billing_details": True,
                    "blik": True,
                    "boleto": True,
                    "card": True,
                    "cashapp": True,
                    "customer": True,
                    "customer_balance": True,
                    "eps": True,
                    "expand": True,
                    "fpx": True,
                    "giropay": True,
                    "grabpay": True,
                    "ideal": True,
                    "interac_present": True,
                    "kakao_pay": True,
                    "klarna": True,
                    "konbini": True,
                    "kr_card": True,
                    "link": True,
                    "metadata": True,
                    "mobilepay": True,
                    "multibanco": True,
                    "naver_pay": True,
                    "nz_bank_account": True,
                    "oxxo": True,
                    "p24": True,
                    "pay_by_bank": True,
                    "payco": True,
                    "payment_method": True,
                    "paynow": True,
                    "paypal": True,
                    "pix": True,
                    "promptpay": True,
                    "radar_options": True,
                    "revolut_pay": True,
                    "samsung_pay": True,
                    "satispay": True,
                    "sepa_debit": True,
                    "sofort": True,
                    "swish": True,
                    "twint": True,
                    "type": True,
                    "us_bank_account": True,
                    "wechat_pay": True,
                    "zip": True,
                },
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path="/v1/payment_methods",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.PaymentMethod,
            request_options=request_options or default_request_options(),
        )

    def update(
        self,
        *,
        payment_method: str,
        data: typing.Union[
            typing.Optional[params.PaymentMethodUpdateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PaymentMethod:
        """
        Update a PaymentMethod

        <p>Updates a PaymentMethod object. A PaymentMethod must be attached a customer to be updated.</p>

        POST /v1/payment_methods/{payment_method}

        Args:
            data: PaymentMethodUpdateBody
            payment_method: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.payment_method.update(payment_method="string")
        ```
        """
        models.PaymentMethod.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerPaymentMethodUpdateBody,
                style={
                    "allow_redisplay": "form",
                    "billing_details": "deepObject",
                    "card": "deepObject",
                    "expand": "deepObject",
                    "link": "deepObject",
                    "metadata": "deepObject",
                    "pay_by_bank": "deepObject",
                    "us_bank_account": "deepObject",
                },
                explode={
                    "allow_redisplay": True,
                    "billing_details": True,
                    "card": True,
                    "expand": True,
                    "link": True,
                    "metadata": True,
                    "pay_by_bank": True,
                    "us_bank_account": True,
                },
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/payment_methods/{payment_method}",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.PaymentMethod,
            request_options=request_options or default_request_options(),
        )

    def attach(
        self,
        *,
        customer: str,
        payment_method: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PaymentMethod:
        """
        Attach a PaymentMethod to a Customer

        <p>Attaches a PaymentMethod object to a Customer.</p>

        <p>To attach a new PaymentMethod to a customer for future payments, we recommend you use a <a href="/docs/api/setup_intents">SetupIntent</a>
        or a PaymentIntent with <a href="/docs/api/payment_intents/create#create_payment_intent-setup_future_usage">setup_future_usage</a>.
        These approaches will perform any necessary steps to set up the PaymentMethod for future payments. Using the <code>/v1/payment_methods/:id/attach</code>
        endpoint without first using a SetupIntent or PaymentIntent with <code>setup_future_usage</code> does not optimize the PaymentMethod for
        future use, which makes later declines and payment friction more likely.
        See <a href="/docs/payments/payment-intents#future-usage">Optimizing cards for future payments</a> for more information about setting up
        future payments.</p>

        <p>To use this PaymentMethod as the default for invoice or subscription payments,
        set <a href="/docs/api/customers/update#update_customer-invoice_settings-default_payment_method"><code>invoice_settings.default_payment_method</code></a>,
        on the Customer to the PaymentMethod’s ID.</p>

        POST /v1/payment_methods/{payment_method}/attach

        Args:
            expand: Specifies which fields in the response should be expanded.
            customer: The ID of the customer to which to attach the PaymentMethod.
            payment_method: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.payment_method.attach(customer="string", payment_method="string")
        ```
        """
        models.PaymentMethod.model_rebuild(_types_namespace=models._types_namespace)
        _data = to_form_urlencoded(
            item={"expand": expand, "customer": customer},
            dump_with=params._SerializerPaymentMethodAttachBody,
            style={"customer": "form", "expand": "deepObject"},
            explode={"customer": True, "expand": True},
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/payment_methods/{payment_method}/attach",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.PaymentMethod,
            request_options=request_options or default_request_options(),
        )

    def detach(
        self,
        *,
        payment_method: str,
        data: typing.Union[
            typing.Optional[params.PaymentMethodDetachBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PaymentMethod:
        """
        Detach a PaymentMethod from a Customer

        <p>Detaches a PaymentMethod object from a Customer. After a PaymentMethod is detached, it can no longer be used for a payment or re-attached to a Customer.</p>

        POST /v1/payment_methods/{payment_method}/detach

        Args:
            data: PaymentMethodDetachBody
            payment_method: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.payment_method.detach(payment_method="string")
        ```
        """
        models.PaymentMethod.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerPaymentMethodDetachBody,
                style={"expand": "deepObject"},
                explode={"expand": True},
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/payment_methods/{payment_method}/detach",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.PaymentMethod,
            request_options=request_options or default_request_options(),
        )


class AsyncPaymentMethodClient:
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
        type_: typing.Union[
            typing.Optional[
                typing_extensions.Literal[
                    "acss_debit",
                    "affirm",
                    "afterpay_clearpay",
                    "alipay",
                    "alma",
                    "amazon_pay",
                    "au_becs_debit",
                    "bacs_debit",
                    "bancontact",
                    "billie",
                    "blik",
                    "boleto",
                    "card",
                    "cashapp",
                    "customer_balance",
                    "eps",
                    "fpx",
                    "giropay",
                    "grabpay",
                    "ideal",
                    "kakao_pay",
                    "klarna",
                    "konbini",
                    "kr_card",
                    "link",
                    "mobilepay",
                    "multibanco",
                    "naver_pay",
                    "nz_bank_account",
                    "oxxo",
                    "p24",
                    "pay_by_bank",
                    "payco",
                    "paynow",
                    "paypal",
                    "pix",
                    "promptpay",
                    "revolut_pay",
                    "samsung_pay",
                    "satispay",
                    "sepa_debit",
                    "sofort",
                    "swish",
                    "twint",
                    "us_bank_account",
                    "wechat_pay",
                    "zip",
                ]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PaymentMethodListResponse:
        """
        List PaymentMethods

        <p>Returns a list of PaymentMethods for Treasury flows. If you want to list the PaymentMethods attached to a Customer for payments, you should use the <a href="/docs/api/payment_methods/customer_list">List a Customer’s PaymentMethods</a> API instead.</p>

        GET /v1/payment_methods

        Args:
            customer: The ID of the customer whose PaymentMethods will be retrieved.
            ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            expand: Specifies which fields in the response should be expanded.
            limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
            type: An optional filter on the list, based on the object `type` field. Without the filter, the list includes all current and future payment method types. If your integration expects only one type of payment method in the response, make sure to provide a type value in the request.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.payment_method.list()
        ```
        """
        models.PaymentMethodListResponse.model_rebuild(
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
        if not isinstance(type_, type_utils.NotGiven):
            encode_query_param(
                _query,
                "type",
                to_encodable(
                    item=type_,
                    dump_with=typing_extensions.Literal[
                        "acss_debit",
                        "affirm",
                        "afterpay_clearpay",
                        "alipay",
                        "alma",
                        "amazon_pay",
                        "au_becs_debit",
                        "bacs_debit",
                        "bancontact",
                        "billie",
                        "blik",
                        "boleto",
                        "card",
                        "cashapp",
                        "customer_balance",
                        "eps",
                        "fpx",
                        "giropay",
                        "grabpay",
                        "ideal",
                        "kakao_pay",
                        "klarna",
                        "konbini",
                        "kr_card",
                        "link",
                        "mobilepay",
                        "multibanco",
                        "naver_pay",
                        "nz_bank_account",
                        "oxxo",
                        "p24",
                        "pay_by_bank",
                        "payco",
                        "paynow",
                        "paypal",
                        "pix",
                        "promptpay",
                        "revolut_pay",
                        "samsung_pay",
                        "satispay",
                        "sepa_debit",
                        "sofort",
                        "swish",
                        "twint",
                        "us_bank_account",
                        "wechat_pay",
                        "zip",
                    ],
                ),
                style="form",
                explode=True,
            )
        return await self._base_client.request(
            method="GET",
            path="/v1/payment_methods",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.PaymentMethodListResponse,
            request_options=request_options or default_request_options(),
        )

    async def get(
        self,
        *,
        payment_method: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PaymentMethod:
        """
        Retrieve a PaymentMethod

        <p>Retrieves a PaymentMethod object attached to the StripeAccount. To retrieve a payment method attached to a Customer, you should use <a href="/docs/api/payment_methods/customer">Retrieve a Customer’s PaymentMethods</a></p>

        GET /v1/payment_methods/{payment_method}

        Args:
            expand: Specifies which fields in the response should be expanded.
            payment_method: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.payment_method.get(payment_method="string")
        ```
        """
        models.PaymentMethod.model_rebuild(_types_namespace=models._types_namespace)
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
            path=f"/v1/payment_methods/{payment_method}",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.PaymentMethod,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        data: typing.Union[
            typing.Optional[params.PaymentMethodCreateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PaymentMethod:
        """
        Shares a PaymentMethod

        <p>Creates a PaymentMethod object. Read the <a href="/docs/stripe-js/reference#stripe-create-payment-method">Stripe.js reference</a> to learn how to create PaymentMethods via Stripe.js.</p>

        <p>Instead of creating a PaymentMethod directly, we recommend using the <a href="/docs/payments/accept-a-payment">PaymentIntents</a> API to accept a payment immediately or the <a href="/docs/payments/save-and-reuse">SetupIntent</a> API to collect payment method details ahead of a future payment.</p>

        POST /v1/payment_methods

        Args:
            data: PaymentMethodCreateBody
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.payment_method.create()
        ```
        """
        models.PaymentMethod.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerPaymentMethodCreateBody,
                style={
                    "acss_debit": "deepObject",
                    "affirm": "deepObject",
                    "afterpay_clearpay": "deepObject",
                    "alipay": "deepObject",
                    "allow_redisplay": "form",
                    "alma": "deepObject",
                    "amazon_pay": "deepObject",
                    "au_becs_debit": "deepObject",
                    "bacs_debit": "deepObject",
                    "bancontact": "deepObject",
                    "billie": "deepObject",
                    "billing_details": "deepObject",
                    "blik": "deepObject",
                    "boleto": "deepObject",
                    "card": "deepObject",
                    "cashapp": "deepObject",
                    "customer": "form",
                    "customer_balance": "deepObject",
                    "eps": "deepObject",
                    "expand": "deepObject",
                    "fpx": "deepObject",
                    "giropay": "deepObject",
                    "grabpay": "deepObject",
                    "ideal": "deepObject",
                    "interac_present": "deepObject",
                    "kakao_pay": "deepObject",
                    "klarna": "deepObject",
                    "konbini": "deepObject",
                    "kr_card": "deepObject",
                    "link": "deepObject",
                    "metadata": "deepObject",
                    "mobilepay": "deepObject",
                    "multibanco": "deepObject",
                    "naver_pay": "deepObject",
                    "nz_bank_account": "deepObject",
                    "oxxo": "deepObject",
                    "p24": "deepObject",
                    "pay_by_bank": "deepObject",
                    "payco": "deepObject",
                    "payment_method": "form",
                    "paynow": "deepObject",
                    "paypal": "deepObject",
                    "pix": "deepObject",
                    "promptpay": "deepObject",
                    "radar_options": "deepObject",
                    "revolut_pay": "deepObject",
                    "samsung_pay": "deepObject",
                    "satispay": "deepObject",
                    "sepa_debit": "deepObject",
                    "sofort": "deepObject",
                    "swish": "deepObject",
                    "twint": "deepObject",
                    "type": "form",
                    "us_bank_account": "deepObject",
                    "wechat_pay": "deepObject",
                    "zip": "deepObject",
                },
                explode={
                    "acss_debit": True,
                    "affirm": True,
                    "afterpay_clearpay": True,
                    "alipay": True,
                    "allow_redisplay": True,
                    "alma": True,
                    "amazon_pay": True,
                    "au_becs_debit": True,
                    "bacs_debit": True,
                    "bancontact": True,
                    "billie": True,
                    "billing_details": True,
                    "blik": True,
                    "boleto": True,
                    "card": True,
                    "cashapp": True,
                    "customer": True,
                    "customer_balance": True,
                    "eps": True,
                    "expand": True,
                    "fpx": True,
                    "giropay": True,
                    "grabpay": True,
                    "ideal": True,
                    "interac_present": True,
                    "kakao_pay": True,
                    "klarna": True,
                    "konbini": True,
                    "kr_card": True,
                    "link": True,
                    "metadata": True,
                    "mobilepay": True,
                    "multibanco": True,
                    "naver_pay": True,
                    "nz_bank_account": True,
                    "oxxo": True,
                    "p24": True,
                    "pay_by_bank": True,
                    "payco": True,
                    "payment_method": True,
                    "paynow": True,
                    "paypal": True,
                    "pix": True,
                    "promptpay": True,
                    "radar_options": True,
                    "revolut_pay": True,
                    "samsung_pay": True,
                    "satispay": True,
                    "sepa_debit": True,
                    "sofort": True,
                    "swish": True,
                    "twint": True,
                    "type": True,
                    "us_bank_account": True,
                    "wechat_pay": True,
                    "zip": True,
                },
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path="/v1/payment_methods",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.PaymentMethod,
            request_options=request_options or default_request_options(),
        )

    async def update(
        self,
        *,
        payment_method: str,
        data: typing.Union[
            typing.Optional[params.PaymentMethodUpdateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PaymentMethod:
        """
        Update a PaymentMethod

        <p>Updates a PaymentMethod object. A PaymentMethod must be attached a customer to be updated.</p>

        POST /v1/payment_methods/{payment_method}

        Args:
            data: PaymentMethodUpdateBody
            payment_method: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.payment_method.update(payment_method="string")
        ```
        """
        models.PaymentMethod.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerPaymentMethodUpdateBody,
                style={
                    "allow_redisplay": "form",
                    "billing_details": "deepObject",
                    "card": "deepObject",
                    "expand": "deepObject",
                    "link": "deepObject",
                    "metadata": "deepObject",
                    "pay_by_bank": "deepObject",
                    "us_bank_account": "deepObject",
                },
                explode={
                    "allow_redisplay": True,
                    "billing_details": True,
                    "card": True,
                    "expand": True,
                    "link": True,
                    "metadata": True,
                    "pay_by_bank": True,
                    "us_bank_account": True,
                },
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/payment_methods/{payment_method}",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.PaymentMethod,
            request_options=request_options or default_request_options(),
        )

    async def attach(
        self,
        *,
        customer: str,
        payment_method: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PaymentMethod:
        """
        Attach a PaymentMethod to a Customer

        <p>Attaches a PaymentMethod object to a Customer.</p>

        <p>To attach a new PaymentMethod to a customer for future payments, we recommend you use a <a href="/docs/api/setup_intents">SetupIntent</a>
        or a PaymentIntent with <a href="/docs/api/payment_intents/create#create_payment_intent-setup_future_usage">setup_future_usage</a>.
        These approaches will perform any necessary steps to set up the PaymentMethod for future payments. Using the <code>/v1/payment_methods/:id/attach</code>
        endpoint without first using a SetupIntent or PaymentIntent with <code>setup_future_usage</code> does not optimize the PaymentMethod for
        future use, which makes later declines and payment friction more likely.
        See <a href="/docs/payments/payment-intents#future-usage">Optimizing cards for future payments</a> for more information about setting up
        future payments.</p>

        <p>To use this PaymentMethod as the default for invoice or subscription payments,
        set <a href="/docs/api/customers/update#update_customer-invoice_settings-default_payment_method"><code>invoice_settings.default_payment_method</code></a>,
        on the Customer to the PaymentMethod’s ID.</p>

        POST /v1/payment_methods/{payment_method}/attach

        Args:
            expand: Specifies which fields in the response should be expanded.
            customer: The ID of the customer to which to attach the PaymentMethod.
            payment_method: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.payment_method.attach(customer="string", payment_method="string")
        ```
        """
        models.PaymentMethod.model_rebuild(_types_namespace=models._types_namespace)
        _data = to_form_urlencoded(
            item={"expand": expand, "customer": customer},
            dump_with=params._SerializerPaymentMethodAttachBody,
            style={"customer": "form", "expand": "deepObject"},
            explode={"customer": True, "expand": True},
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/payment_methods/{payment_method}/attach",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.PaymentMethod,
            request_options=request_options or default_request_options(),
        )

    async def detach(
        self,
        *,
        payment_method: str,
        data: typing.Union[
            typing.Optional[params.PaymentMethodDetachBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PaymentMethod:
        """
        Detach a PaymentMethod from a Customer

        <p>Detaches a PaymentMethod object from a Customer. After a PaymentMethod is detached, it can no longer be used for a payment or re-attached to a Customer.</p>

        POST /v1/payment_methods/{payment_method}/detach

        Args:
            data: PaymentMethodDetachBody
            payment_method: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.payment_method.detach(payment_method="string")
        ```
        """
        models.PaymentMethod.model_rebuild(_types_namespace=models._types_namespace)
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerPaymentMethodDetachBody,
                style={"expand": "deepObject"},
                explode={"expand": True},
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/payment_methods/{payment_method}/detach",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.PaymentMethod,
            request_options=request_options or default_request_options(),
        )
