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


class PaymentMethodConfigurationClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def list(
        self,
        *,
        application: typing.Union[
            typing.Optional[typing.Union[str, str]], type_utils.NotGiven
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
    ) -> models.PaymentMethodConfigurationListResponse:
        """
        List payment method configurations

        <p>List payment method configurations</p>

        GET /v1/payment_method_configurations

        Args:
            application: The Connect application to filter by.
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
        client.payment_method_configuration.list()
        ```
        """
        _query: QueryParams = {}
        if not isinstance(application, type_utils.NotGiven):
            encode_query_param(
                _query,
                "application",
                to_encodable(item=application, dump_with=typing.Union[str, str]),
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
            path="/v1/payment_method_configurations",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.PaymentMethodConfigurationListResponse,
            request_options=request_options or default_request_options(),
        )

    def get(
        self,
        *,
        configuration: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PaymentMethodConfiguration:
        """
        Retrieve payment method configuration

        <p>Retrieve payment method configuration</p>

        GET /v1/payment_method_configurations/{configuration}

        Args:
            expand: Specifies which fields in the response should be expanded.
            configuration: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.payment_method_configuration.get(configuration="string")
        ```
        """
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
            path=f"/v1/payment_method_configurations/{configuration}",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.PaymentMethodConfiguration,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        data: typing.Union[
            typing.Optional[params.PaymentMethodConfigurationCreateBody],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PaymentMethodConfiguration:
        """
        Create a payment method configuration

        <p>Creates a payment method configuration</p>

        POST /v1/payment_method_configurations

        Args:
            data: PaymentMethodConfigurationCreateBody
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.payment_method_configuration.create()
        ```
        """
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerPaymentMethodConfigurationCreateBody,
                style={
                    "acss_debit": "deepObject",
                    "affirm": "deepObject",
                    "afterpay_clearpay": "deepObject",
                    "alipay": "deepObject",
                    "alma": "deepObject",
                    "amazon_pay": "deepObject",
                    "apple_pay": "deepObject",
                    "apple_pay_later": "deepObject",
                    "au_becs_debit": "deepObject",
                    "bacs_debit": "deepObject",
                    "bancontact": "deepObject",
                    "billie": "deepObject",
                    "blik": "deepObject",
                    "boleto": "deepObject",
                    "card": "deepObject",
                    "cartes_bancaires": "deepObject",
                    "cashapp": "deepObject",
                    "customer_balance": "deepObject",
                    "eps": "deepObject",
                    "expand": "deepObject",
                    "fpx": "deepObject",
                    "giropay": "deepObject",
                    "google_pay": "deepObject",
                    "grabpay": "deepObject",
                    "ideal": "deepObject",
                    "jcb": "deepObject",
                    "klarna": "deepObject",
                    "konbini": "deepObject",
                    "link": "deepObject",
                    "mobilepay": "deepObject",
                    "multibanco": "deepObject",
                    "name": "form",
                    "nz_bank_account": "deepObject",
                    "oxxo": "deepObject",
                    "p24": "deepObject",
                    "parent": "form",
                    "pay_by_bank": "deepObject",
                    "paynow": "deepObject",
                    "paypal": "deepObject",
                    "promptpay": "deepObject",
                    "revolut_pay": "deepObject",
                    "satispay": "deepObject",
                    "sepa_debit": "deepObject",
                    "sofort": "deepObject",
                    "swish": "deepObject",
                    "twint": "deepObject",
                    "us_bank_account": "deepObject",
                    "wechat_pay": "deepObject",
                    "zip": "deepObject",
                },
                explode={
                    "acss_debit": True,
                    "affirm": True,
                    "afterpay_clearpay": True,
                    "alipay": True,
                    "alma": True,
                    "amazon_pay": True,
                    "apple_pay": True,
                    "apple_pay_later": True,
                    "au_becs_debit": True,
                    "bacs_debit": True,
                    "bancontact": True,
                    "billie": True,
                    "blik": True,
                    "boleto": True,
                    "card": True,
                    "cartes_bancaires": True,
                    "cashapp": True,
                    "customer_balance": True,
                    "eps": True,
                    "expand": True,
                    "fpx": True,
                    "giropay": True,
                    "google_pay": True,
                    "grabpay": True,
                    "ideal": True,
                    "jcb": True,
                    "klarna": True,
                    "konbini": True,
                    "link": True,
                    "mobilepay": True,
                    "multibanco": True,
                    "name": True,
                    "nz_bank_account": True,
                    "oxxo": True,
                    "p24": True,
                    "parent": True,
                    "pay_by_bank": True,
                    "paynow": True,
                    "paypal": True,
                    "promptpay": True,
                    "revolut_pay": True,
                    "satispay": True,
                    "sepa_debit": True,
                    "sofort": True,
                    "swish": True,
                    "twint": True,
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
            path="/v1/payment_method_configurations",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.PaymentMethodConfiguration,
            request_options=request_options or default_request_options(),
        )

    def update(
        self,
        *,
        configuration: str,
        data: typing.Union[
            typing.Optional[params.PaymentMethodConfigurationUpdateBody],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PaymentMethodConfiguration:
        """
        Update payment method configuration

        <p>Update payment method configuration</p>

        POST /v1/payment_method_configurations/{configuration}

        Args:
            data: PaymentMethodConfigurationUpdateBody
            configuration: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.payment_method_configuration.update(configuration="string")
        ```
        """
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerPaymentMethodConfigurationUpdateBody,
                style={
                    "acss_debit": "deepObject",
                    "active": "form",
                    "affirm": "deepObject",
                    "afterpay_clearpay": "deepObject",
                    "alipay": "deepObject",
                    "alma": "deepObject",
                    "amazon_pay": "deepObject",
                    "apple_pay": "deepObject",
                    "apple_pay_later": "deepObject",
                    "au_becs_debit": "deepObject",
                    "bacs_debit": "deepObject",
                    "bancontact": "deepObject",
                    "billie": "deepObject",
                    "blik": "deepObject",
                    "boleto": "deepObject",
                    "card": "deepObject",
                    "cartes_bancaires": "deepObject",
                    "cashapp": "deepObject",
                    "customer_balance": "deepObject",
                    "eps": "deepObject",
                    "expand": "deepObject",
                    "fpx": "deepObject",
                    "giropay": "deepObject",
                    "google_pay": "deepObject",
                    "grabpay": "deepObject",
                    "ideal": "deepObject",
                    "jcb": "deepObject",
                    "klarna": "deepObject",
                    "konbini": "deepObject",
                    "link": "deepObject",
                    "mobilepay": "deepObject",
                    "multibanco": "deepObject",
                    "name": "form",
                    "nz_bank_account": "deepObject",
                    "oxxo": "deepObject",
                    "p24": "deepObject",
                    "pay_by_bank": "deepObject",
                    "paynow": "deepObject",
                    "paypal": "deepObject",
                    "promptpay": "deepObject",
                    "revolut_pay": "deepObject",
                    "satispay": "deepObject",
                    "sepa_debit": "deepObject",
                    "sofort": "deepObject",
                    "swish": "deepObject",
                    "twint": "deepObject",
                    "us_bank_account": "deepObject",
                    "wechat_pay": "deepObject",
                    "zip": "deepObject",
                },
                explode={
                    "acss_debit": True,
                    "active": True,
                    "affirm": True,
                    "afterpay_clearpay": True,
                    "alipay": True,
                    "alma": True,
                    "amazon_pay": True,
                    "apple_pay": True,
                    "apple_pay_later": True,
                    "au_becs_debit": True,
                    "bacs_debit": True,
                    "bancontact": True,
                    "billie": True,
                    "blik": True,
                    "boleto": True,
                    "card": True,
                    "cartes_bancaires": True,
                    "cashapp": True,
                    "customer_balance": True,
                    "eps": True,
                    "expand": True,
                    "fpx": True,
                    "giropay": True,
                    "google_pay": True,
                    "grabpay": True,
                    "ideal": True,
                    "jcb": True,
                    "klarna": True,
                    "konbini": True,
                    "link": True,
                    "mobilepay": True,
                    "multibanco": True,
                    "name": True,
                    "nz_bank_account": True,
                    "oxxo": True,
                    "p24": True,
                    "pay_by_bank": True,
                    "paynow": True,
                    "paypal": True,
                    "promptpay": True,
                    "revolut_pay": True,
                    "satispay": True,
                    "sepa_debit": True,
                    "sofort": True,
                    "swish": True,
                    "twint": True,
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
            path=f"/v1/payment_method_configurations/{configuration}",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.PaymentMethodConfiguration,
            request_options=request_options or default_request_options(),
        )


class AsyncPaymentMethodConfigurationClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def list(
        self,
        *,
        application: typing.Union[
            typing.Optional[typing.Union[str, str]], type_utils.NotGiven
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
    ) -> models.PaymentMethodConfigurationListResponse:
        """
        List payment method configurations

        <p>List payment method configurations</p>

        GET /v1/payment_method_configurations

        Args:
            application: The Connect application to filter by.
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
        await client.payment_method_configuration.list()
        ```
        """
        _query: QueryParams = {}
        if not isinstance(application, type_utils.NotGiven):
            encode_query_param(
                _query,
                "application",
                to_encodable(item=application, dump_with=typing.Union[str, str]),
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
            path="/v1/payment_method_configurations",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.PaymentMethodConfigurationListResponse,
            request_options=request_options or default_request_options(),
        )

    async def get(
        self,
        *,
        configuration: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PaymentMethodConfiguration:
        """
        Retrieve payment method configuration

        <p>Retrieve payment method configuration</p>

        GET /v1/payment_method_configurations/{configuration}

        Args:
            expand: Specifies which fields in the response should be expanded.
            configuration: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.payment_method_configuration.get(configuration="string")
        ```
        """
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
            path=f"/v1/payment_method_configurations/{configuration}",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.PaymentMethodConfiguration,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        data: typing.Union[
            typing.Optional[params.PaymentMethodConfigurationCreateBody],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PaymentMethodConfiguration:
        """
        Create a payment method configuration

        <p>Creates a payment method configuration</p>

        POST /v1/payment_method_configurations

        Args:
            data: PaymentMethodConfigurationCreateBody
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.payment_method_configuration.create()
        ```
        """
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerPaymentMethodConfigurationCreateBody,
                style={
                    "acss_debit": "deepObject",
                    "affirm": "deepObject",
                    "afterpay_clearpay": "deepObject",
                    "alipay": "deepObject",
                    "alma": "deepObject",
                    "amazon_pay": "deepObject",
                    "apple_pay": "deepObject",
                    "apple_pay_later": "deepObject",
                    "au_becs_debit": "deepObject",
                    "bacs_debit": "deepObject",
                    "bancontact": "deepObject",
                    "billie": "deepObject",
                    "blik": "deepObject",
                    "boleto": "deepObject",
                    "card": "deepObject",
                    "cartes_bancaires": "deepObject",
                    "cashapp": "deepObject",
                    "customer_balance": "deepObject",
                    "eps": "deepObject",
                    "expand": "deepObject",
                    "fpx": "deepObject",
                    "giropay": "deepObject",
                    "google_pay": "deepObject",
                    "grabpay": "deepObject",
                    "ideal": "deepObject",
                    "jcb": "deepObject",
                    "klarna": "deepObject",
                    "konbini": "deepObject",
                    "link": "deepObject",
                    "mobilepay": "deepObject",
                    "multibanco": "deepObject",
                    "name": "form",
                    "nz_bank_account": "deepObject",
                    "oxxo": "deepObject",
                    "p24": "deepObject",
                    "parent": "form",
                    "pay_by_bank": "deepObject",
                    "paynow": "deepObject",
                    "paypal": "deepObject",
                    "promptpay": "deepObject",
                    "revolut_pay": "deepObject",
                    "satispay": "deepObject",
                    "sepa_debit": "deepObject",
                    "sofort": "deepObject",
                    "swish": "deepObject",
                    "twint": "deepObject",
                    "us_bank_account": "deepObject",
                    "wechat_pay": "deepObject",
                    "zip": "deepObject",
                },
                explode={
                    "acss_debit": True,
                    "affirm": True,
                    "afterpay_clearpay": True,
                    "alipay": True,
                    "alma": True,
                    "amazon_pay": True,
                    "apple_pay": True,
                    "apple_pay_later": True,
                    "au_becs_debit": True,
                    "bacs_debit": True,
                    "bancontact": True,
                    "billie": True,
                    "blik": True,
                    "boleto": True,
                    "card": True,
                    "cartes_bancaires": True,
                    "cashapp": True,
                    "customer_balance": True,
                    "eps": True,
                    "expand": True,
                    "fpx": True,
                    "giropay": True,
                    "google_pay": True,
                    "grabpay": True,
                    "ideal": True,
                    "jcb": True,
                    "klarna": True,
                    "konbini": True,
                    "link": True,
                    "mobilepay": True,
                    "multibanco": True,
                    "name": True,
                    "nz_bank_account": True,
                    "oxxo": True,
                    "p24": True,
                    "parent": True,
                    "pay_by_bank": True,
                    "paynow": True,
                    "paypal": True,
                    "promptpay": True,
                    "revolut_pay": True,
                    "satispay": True,
                    "sepa_debit": True,
                    "sofort": True,
                    "swish": True,
                    "twint": True,
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
            path="/v1/payment_method_configurations",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.PaymentMethodConfiguration,
            request_options=request_options or default_request_options(),
        )

    async def update(
        self,
        *,
        configuration: str,
        data: typing.Union[
            typing.Optional[params.PaymentMethodConfigurationUpdateBody],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PaymentMethodConfiguration:
        """
        Update payment method configuration

        <p>Update payment method configuration</p>

        POST /v1/payment_method_configurations/{configuration}

        Args:
            data: PaymentMethodConfigurationUpdateBody
            configuration: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.payment_method_configuration.update(configuration="string")
        ```
        """
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerPaymentMethodConfigurationUpdateBody,
                style={
                    "acss_debit": "deepObject",
                    "active": "form",
                    "affirm": "deepObject",
                    "afterpay_clearpay": "deepObject",
                    "alipay": "deepObject",
                    "alma": "deepObject",
                    "amazon_pay": "deepObject",
                    "apple_pay": "deepObject",
                    "apple_pay_later": "deepObject",
                    "au_becs_debit": "deepObject",
                    "bacs_debit": "deepObject",
                    "bancontact": "deepObject",
                    "billie": "deepObject",
                    "blik": "deepObject",
                    "boleto": "deepObject",
                    "card": "deepObject",
                    "cartes_bancaires": "deepObject",
                    "cashapp": "deepObject",
                    "customer_balance": "deepObject",
                    "eps": "deepObject",
                    "expand": "deepObject",
                    "fpx": "deepObject",
                    "giropay": "deepObject",
                    "google_pay": "deepObject",
                    "grabpay": "deepObject",
                    "ideal": "deepObject",
                    "jcb": "deepObject",
                    "klarna": "deepObject",
                    "konbini": "deepObject",
                    "link": "deepObject",
                    "mobilepay": "deepObject",
                    "multibanco": "deepObject",
                    "name": "form",
                    "nz_bank_account": "deepObject",
                    "oxxo": "deepObject",
                    "p24": "deepObject",
                    "pay_by_bank": "deepObject",
                    "paynow": "deepObject",
                    "paypal": "deepObject",
                    "promptpay": "deepObject",
                    "revolut_pay": "deepObject",
                    "satispay": "deepObject",
                    "sepa_debit": "deepObject",
                    "sofort": "deepObject",
                    "swish": "deepObject",
                    "twint": "deepObject",
                    "us_bank_account": "deepObject",
                    "wechat_pay": "deepObject",
                    "zip": "deepObject",
                },
                explode={
                    "acss_debit": True,
                    "active": True,
                    "affirm": True,
                    "afterpay_clearpay": True,
                    "alipay": True,
                    "alma": True,
                    "amazon_pay": True,
                    "apple_pay": True,
                    "apple_pay_later": True,
                    "au_becs_debit": True,
                    "bacs_debit": True,
                    "bancontact": True,
                    "billie": True,
                    "blik": True,
                    "boleto": True,
                    "card": True,
                    "cartes_bancaires": True,
                    "cashapp": True,
                    "customer_balance": True,
                    "eps": True,
                    "expand": True,
                    "fpx": True,
                    "giropay": True,
                    "google_pay": True,
                    "grabpay": True,
                    "ideal": True,
                    "jcb": True,
                    "klarna": True,
                    "konbini": True,
                    "link": True,
                    "mobilepay": True,
                    "multibanco": True,
                    "name": True,
                    "nz_bank_account": True,
                    "oxxo": True,
                    "p24": True,
                    "pay_by_bank": True,
                    "paynow": True,
                    "paypal": True,
                    "promptpay": True,
                    "revolut_pay": True,
                    "satispay": True,
                    "sepa_debit": True,
                    "sofort": True,
                    "swish": True,
                    "twint": True,
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
            path=f"/v1/payment_method_configurations/{configuration}",
            auth_names=["bearerAuth"],
            data=_data,
            cast_to=models.PaymentMethodConfiguration,
            request_options=request_options or default_request_options(),
        )
