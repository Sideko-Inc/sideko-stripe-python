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


class PaymentMethodDomainClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def list(
        self,
        *,
        domain_name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        enabled: typing.Union[
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
    ) -> models.PaymentMethodDomainListResponse:
        """
        List payment method domains

        <p>Lists the details of existing payment method domains.</p>

        GET /v1/payment_method_domains

        Args:
            domain_name: The domain name that this payment method domain object represents.
            enabled: Whether this payment method domain is enabled. If the domain is not enabled, payment methods will not appear in Elements or Embedded Checkout
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
        client.payment_method_domain.list()
        ```
        """
        _query: QueryParams = {}
        if not isinstance(domain_name, type_utils.NotGiven):
            encode_query_param(
                _query,
                "domain_name",
                to_encodable(item=domain_name, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(enabled, type_utils.NotGiven):
            encode_query_param(
                _query,
                "enabled",
                to_encodable(item=enabled, dump_with=bool),
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
            path="/v1/payment_method_domains",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.PaymentMethodDomainListResponse,
            request_options=request_options or default_request_options(),
        )

    def get(
        self,
        *,
        payment_method_domain: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PaymentMethodDomain:
        """
        Retrieve a payment method domain

        <p>Retrieves the details of an existing payment method domain.</p>

        GET /v1/payment_method_domains/{payment_method_domain}

        Args:
            expand: Specifies which fields in the response should be expanded.
            payment_method_domain: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.payment_method_domain.get(payment_method_domain="string")
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
            path=f"/v1/payment_method_domains/{payment_method_domain}",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.PaymentMethodDomain,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        domain_name: str,
        enabled: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PaymentMethodDomain:
        """
        Create a payment method domain

        <p>Creates a payment method domain.</p>

        POST /v1/payment_method_domains

        Args:
            enabled: Whether this payment method domain is enabled. If the domain is not enabled, payment methods that require a payment method domain will not appear in Elements or Embedded Checkout.
            expand: Specifies which fields in the response should be expanded.
            domain_name: The domain name that this payment method domain object represents.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.payment_method_domain.create(domain_name="string")
        ```
        """
        _data = to_form_urlencoded(
            item={"enabled": enabled, "expand": expand, "domain_name": domain_name},
            dump_with=params._SerializerPaymentMethodDomainCreateBody,
            style={"domain_name": "form", "enabled": "form", "expand": "deepObject"},
            explode={"domain_name": True, "enabled": True, "expand": True},
        )
        return self._base_client.request(
            method="POST",
            path="/v1/payment_method_domains",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.PaymentMethodDomain,
            request_options=request_options or default_request_options(),
        )

    def update(
        self,
        *,
        payment_method_domain: str,
        data: typing.Union[
            typing.Optional[params.PaymentMethodDomainUpdateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PaymentMethodDomain:
        """
        Update a payment method domain

        <p>Updates an existing payment method domain.</p>

        POST /v1/payment_method_domains/{payment_method_domain}

        Args:
            data: PaymentMethodDomainUpdateBody
            payment_method_domain: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.payment_method_domain.update(payment_method_domain="string")
        ```
        """
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerPaymentMethodDomainUpdateBody,
                style={"enabled": "form", "expand": "deepObject"},
                explode={"enabled": True, "expand": True},
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/payment_method_domains/{payment_method_domain}",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.PaymentMethodDomain,
            request_options=request_options or default_request_options(),
        )

    def validate(
        self,
        *,
        payment_method_domain: str,
        data: typing.Union[
            typing.Optional[params.PaymentMethodDomainValidateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PaymentMethodDomain:
        """
        Validate an existing payment method domain

        <p>Some payment methods might require additional steps to register a domain. If the requirements weren’t satisfied when the domain was created, the payment method will be inactive on the domain.
        The payment method doesn’t appear in Elements or Embedded Checkout for this domain until it is active.</p>

        <p>To activate a payment method on an existing payment method domain, complete the required registration steps specific to the payment method, and then validate the payment method domain with this endpoint.</p>

        <p>Related guides: <a href="/docs/payments/payment-methods/pmd-registration">Payment method domains</a>.</p>

        POST /v1/payment_method_domains/{payment_method_domain}/validate

        Args:
            data: PaymentMethodDomainValidateBody
            payment_method_domain: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.payment_method_domain.validate(payment_method_domain="string")
        ```
        """
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerPaymentMethodDomainValidateBody,
                style={"expand": "deepObject"},
                explode={"expand": True},
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path=f"/v1/payment_method_domains/{payment_method_domain}/validate",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.PaymentMethodDomain,
            request_options=request_options or default_request_options(),
        )


class AsyncPaymentMethodDomainClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def list(
        self,
        *,
        domain_name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        enabled: typing.Union[
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
    ) -> models.PaymentMethodDomainListResponse:
        """
        List payment method domains

        <p>Lists the details of existing payment method domains.</p>

        GET /v1/payment_method_domains

        Args:
            domain_name: The domain name that this payment method domain object represents.
            enabled: Whether this payment method domain is enabled. If the domain is not enabled, payment methods will not appear in Elements or Embedded Checkout
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
        await client.payment_method_domain.list()
        ```
        """
        _query: QueryParams = {}
        if not isinstance(domain_name, type_utils.NotGiven):
            encode_query_param(
                _query,
                "domain_name",
                to_encodable(item=domain_name, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(enabled, type_utils.NotGiven):
            encode_query_param(
                _query,
                "enabled",
                to_encodable(item=enabled, dump_with=bool),
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
            path="/v1/payment_method_domains",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.PaymentMethodDomainListResponse,
            request_options=request_options or default_request_options(),
        )

    async def get(
        self,
        *,
        payment_method_domain: str,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PaymentMethodDomain:
        """
        Retrieve a payment method domain

        <p>Retrieves the details of an existing payment method domain.</p>

        GET /v1/payment_method_domains/{payment_method_domain}

        Args:
            expand: Specifies which fields in the response should be expanded.
            payment_method_domain: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.payment_method_domain.get(payment_method_domain="string")
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
            path=f"/v1/payment_method_domains/{payment_method_domain}",
            auth_names=["basicAuth", "bearerAuth"],
            query_params=_query,
            cast_to=models.PaymentMethodDomain,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        domain_name: str,
        enabled: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        expand: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PaymentMethodDomain:
        """
        Create a payment method domain

        <p>Creates a payment method domain.</p>

        POST /v1/payment_method_domains

        Args:
            enabled: Whether this payment method domain is enabled. If the domain is not enabled, payment methods that require a payment method domain will not appear in Elements or Embedded Checkout.
            expand: Specifies which fields in the response should be expanded.
            domain_name: The domain name that this payment method domain object represents.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.payment_method_domain.create(domain_name="string")
        ```
        """
        _data = to_form_urlencoded(
            item={"enabled": enabled, "expand": expand, "domain_name": domain_name},
            dump_with=params._SerializerPaymentMethodDomainCreateBody,
            style={"domain_name": "form", "enabled": "form", "expand": "deepObject"},
            explode={"domain_name": True, "enabled": True, "expand": True},
        )
        return await self._base_client.request(
            method="POST",
            path="/v1/payment_method_domains",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.PaymentMethodDomain,
            request_options=request_options or default_request_options(),
        )

    async def update(
        self,
        *,
        payment_method_domain: str,
        data: typing.Union[
            typing.Optional[params.PaymentMethodDomainUpdateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PaymentMethodDomain:
        """
        Update a payment method domain

        <p>Updates an existing payment method domain.</p>

        POST /v1/payment_method_domains/{payment_method_domain}

        Args:
            data: PaymentMethodDomainUpdateBody
            payment_method_domain: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.payment_method_domain.update(payment_method_domain="string")
        ```
        """
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerPaymentMethodDomainUpdateBody,
                style={"enabled": "form", "expand": "deepObject"},
                explode={"enabled": True, "expand": True},
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/payment_method_domains/{payment_method_domain}",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.PaymentMethodDomain,
            request_options=request_options or default_request_options(),
        )

    async def validate(
        self,
        *,
        payment_method_domain: str,
        data: typing.Union[
            typing.Optional[params.PaymentMethodDomainValidateBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PaymentMethodDomain:
        """
        Validate an existing payment method domain

        <p>Some payment methods might require additional steps to register a domain. If the requirements weren’t satisfied when the domain was created, the payment method will be inactive on the domain.
        The payment method doesn’t appear in Elements or Embedded Checkout for this domain until it is active.</p>

        <p>To activate a payment method on an existing payment method domain, complete the required registration steps specific to the payment method, and then validate the payment method domain with this endpoint.</p>

        <p>Related guides: <a href="/docs/payments/payment-methods/pmd-registration">Payment method domains</a>.</p>

        POST /v1/payment_method_domains/{payment_method_domain}/validate

        Args:
            data: PaymentMethodDomainValidateBody
            payment_method_domain: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful response.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.payment_method_domain.validate(payment_method_domain="string")
        ```
        """
        _data = (
            to_form_urlencoded(
                item=data,
                dump_with=params._SerializerPaymentMethodDomainValidateBody,
                style={"expand": "deepObject"},
                explode={"expand": True},
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path=f"/v1/payment_method_domains/{payment_method_domain}/validate",
            auth_names=["basicAuth", "bearerAuth"],
            data=_data,
            cast_to=models.PaymentMethodDomain,
            request_options=request_options or default_request_options(),
        )
