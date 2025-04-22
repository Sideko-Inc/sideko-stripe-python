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
    type_utils,
)
from sideko_stripe.types import models


class PaymentMethodClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def list(
        self,
        *,
        customer: str,
        allow_redisplay: typing.Union[
            typing.Optional[
                typing_extensions.Literal["always", "limited", "unspecified"]
            ],
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
    ) -> models.CustomerPaymentMethodListResponse:
        """
        List a Customer's PaymentMethods

        <p>Returns a list of PaymentMethods for a given Customer</p>

        GET /v1/customers/{customer}/payment_methods

        Args:
            allow_redisplay: This field indicates whether this payment method can be shown again to its customer in a checkout flow. Stripe products such as Checkout and Elements use this field to determine whether a payment method can be shown as a saved payment method in a checkout flow. The field defaults to `unspecified`.
            ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            expand: Specifies which fields in the response should be expanded.
            limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
            type: An optional filter on the list, based on the object `type` field. Without the filter, the list includes all current and future payment method types. If your integration expects only one type of payment method in the response, make sure to provide a type value in the request.
            customer: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.customer.payment_method.list(customer="string")
        ```
        """
        models.CustomerPaymentMethodListResponse.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _query: QueryParams = {}
        if not isinstance(allow_redisplay, type_utils.NotGiven):
            encode_query_param(
                _query,
                "allow_redisplay",
                to_encodable(
                    item=allow_redisplay,
                    dump_with=typing_extensions.Literal[
                        "always", "limited", "unspecified"
                    ],
                ),
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
            path=f"/v1/customers/{customer}/payment_methods",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.CustomerPaymentMethodListResponse,
            request_options=request_options or default_request_options(),
        )

    def get(
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
        Retrieve a Customer's PaymentMethod

        <p>Retrieves a PaymentMethod object for a given Customer.</p>

        GET /v1/customers/{customer}/payment_methods/{payment_method}

        Args:
            expand: Specifies which fields in the response should be expanded.
            customer: str
            payment_method: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.customer.payment_method.get(customer="string", payment_method="string")
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
            path=f"/v1/customers/{customer}/payment_methods/{payment_method}",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.PaymentMethod,
            request_options=request_options or default_request_options(),
        )


class AsyncPaymentMethodClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def list(
        self,
        *,
        customer: str,
        allow_redisplay: typing.Union[
            typing.Optional[
                typing_extensions.Literal["always", "limited", "unspecified"]
            ],
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
    ) -> models.CustomerPaymentMethodListResponse:
        """
        List a Customer's PaymentMethods

        <p>Returns a list of PaymentMethods for a given Customer</p>

        GET /v1/customers/{customer}/payment_methods

        Args:
            allow_redisplay: This field indicates whether this payment method can be shown again to its customer in a checkout flow. Stripe products such as Checkout and Elements use this field to determine whether a payment method can be shown as a saved payment method in a checkout flow. The field defaults to `unspecified`.
            ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            expand: Specifies which fields in the response should be expanded.
            limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
            type: An optional filter on the list, based on the object `type` field. Without the filter, the list includes all current and future payment method types. If your integration expects only one type of payment method in the response, make sure to provide a type value in the request.
            customer: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.customer.payment_method.list(customer="string")
        ```
        """
        models.CustomerPaymentMethodListResponse.model_rebuild(
            _types_namespace=models._types_namespace
        )
        _query: QueryParams = {}
        if not isinstance(allow_redisplay, type_utils.NotGiven):
            encode_query_param(
                _query,
                "allow_redisplay",
                to_encodable(
                    item=allow_redisplay,
                    dump_with=typing_extensions.Literal[
                        "always", "limited", "unspecified"
                    ],
                ),
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
            path=f"/v1/customers/{customer}/payment_methods",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.CustomerPaymentMethodListResponse,
            request_options=request_options or default_request_options(),
        )

    async def get(
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
        Retrieve a Customer's PaymentMethod

        <p>Retrieves a PaymentMethod object for a given Customer.</p>

        GET /v1/customers/{customer}/payment_methods/{payment_method}

        Args:
            expand: Specifies which fields in the response should be expanded.
            customer: str
            payment_method: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.customer.payment_method.get(
            customer="string", payment_method="string"
        )
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
            path=f"/v1/customers/{customer}/payment_methods/{payment_method}",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.PaymentMethod,
            request_options=request_options or default_request_options(),
        )
